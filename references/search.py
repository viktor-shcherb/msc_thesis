#!/usr/bin/env python3
"""
Search tool for the references/ directory.

Reads per-paper metadata from YAML front matter in each analysis.md file
and the shared ontology from metadata.yaml.

Usage:
    ./references/search.py category <category-id>
    ./references/search.py benchmark <benchmark-id>
    ./references/search.py model <model-id>
    ./references/search.py lineage <dir-name>
    ./references/search.py contradictions
    ./references/search.py claims [contested|supported|unvalidated]
    ./references/search.py open-questions [--unresolved]
    ./references/search.py text "<query>"
    ./references/search.py info <dir-name>
    ./references/search.py related <dir-name>
"""

import os
import sys
import re
import yaml
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
METADATA_PATH = SCRIPT_DIR / "metadata.yaml"


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def parse_frontmatter(filepath):
    """Extract YAML front matter from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---\n"):
        return None, content
    end = content.index("\n---\n", 4)
    yaml_str = content[4:end]
    body = content[end + 5:]
    return yaml.safe_load(yaml_str), body


def load_all_references():
    """Load metadata from all analysis.md files."""
    refs = {}
    for entry in sorted(SCRIPT_DIR.iterdir()):
        if not entry.is_dir() or entry.name.startswith("_"):
            continue
        analysis = entry / "analysis.md"
        if not analysis.exists():
            continue
        meta, _ = parse_frontmatter(analysis)
        if meta:
            refs[entry.name] = meta
    return refs


def load_ontology():
    """Load the ontology from metadata.yaml."""
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("ontology", {})


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def short_title(meta):
    title = meta.get("title", "?")
    if len(title) > 70:
        return title[:67] + "..."
    return title


def fmt_paper(dir_name, meta):
    year = meta.get("year", "?")
    venue = meta.get("venue", "")
    return f"  {dir_name}\n    {short_title(meta)} ({year}, {venue})"


def fmt_claim(dir_name, claim):
    return (
        f"  [{claim.get('status', '?').upper()}] {dir_name}\n"
        f"    {claim.get('id', '?')}: {claim.get('claim', '?')}\n"
        f"    Evidence: {claim.get('evidence', '?')}"
    )


def fmt_xref(xref, refs):
    target = xref.get("target", "?")
    rel = xref.get("type", "?")
    detail = xref.get("detail", "")
    target_title = short_title(refs[target]) if target in refs else target
    return f"  [{rel}] {target}\n    {target_title}\n    {detail}"


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_category(refs, cat_id):
    """List papers in a given category."""
    results = []
    for name, meta in sorted(refs.items()):
        cats = meta.get("categories", [])
        if cat_id in cats:
            results.append((name, meta))
    if not results:
        print(f"No papers found in category '{cat_id}'.")
        return
    print(f"Papers in category '{cat_id}' ({len(results)}):\n")
    for name, meta in results:
        print(fmt_paper(name, meta))
    print()


def cmd_benchmark(refs, bench_id):
    """List papers using a given benchmark."""
    results = []
    for name, meta in sorted(refs.items()):
        benches = meta.get("benchmarks_used", [])
        if bench_id in benches:
            results.append((name, meta))
    if not results:
        print(f"No papers found using benchmark '{bench_id}'.")
        return
    print(f"Papers using benchmark '{bench_id}' ({len(results)}):\n")
    for name, meta in results:
        print(fmt_paper(name, meta))
    print()


def cmd_model(refs, model_id):
    """List papers introducing or evaluating a given model."""
    introduced = []
    evaluated = []
    for name, meta in sorted(refs.items()):
        if model_id in meta.get("models_introduced", []):
            introduced.append((name, meta))
        if model_id in meta.get("models_evaluated", []):
            evaluated.append((name, meta))
    if not introduced and not evaluated:
        print(f"No papers found for model '{model_id}'.")
        return
    if introduced:
        print(f"Papers introducing '{model_id}':\n")
        for name, meta in introduced:
            print(fmt_paper(name, meta))
        print()
    if evaluated:
        print(f"Papers evaluating '{model_id}' ({len(evaluated)}):\n")
        for name, meta in evaluated:
            print(fmt_paper(name, meta))
        print()


def cmd_lineage(refs, start):
    """Trace extends/extended-by chains from a starting paper."""
    if start not in refs:
        print(f"Paper '{start}' not found.")
        return

    visited = set()
    chain = []

    def trace(name, direction, depth=0):
        if name in visited:
            return
        visited.add(name)
        meta = refs.get(name)
        if not meta:
            return
        chain.append((depth, direction, name, meta))
        for xref in meta.get("cross_references", []):
            rel = xref.get("type", "")
            target = xref.get("target", "")
            if rel == "extends" and direction in ("root", "ancestors"):
                trace(target, "ancestors", depth + 1)
            elif rel == "extended-by" and direction in ("root", "descendants"):
                trace(target, "descendants", depth + 1)

    # Trace ancestors (papers this one extends)
    trace(start, "root")

    # Re-trace descendants explicitly
    visited_ancestors = visited.copy()
    for xref in refs[start].get("cross_references", []):
        if xref.get("type") == "extended-by":
            target = xref.get("target", "")
            if target not in visited:
                trace(target, "descendants")

    print(f"Lineage for {start}:\n")
    print(f"  {short_title(refs[start])}\n")

    ancestors = [(d, n, m) for d, dir_, n, m in chain if dir_ == "ancestors"]
    descendants = [(d, n, m) for d, dir_, n, m in chain if dir_ == "descendants"]

    if ancestors:
        print("  Ancestors (this paper extends):")
        for depth, name, meta in ancestors:
            indent = "    " + "  " * depth
            print(f"{indent}-> {name}: {short_title(meta)}")
        print()

    if descendants:
        print("  Descendants (extended by):")
        for depth, name, meta in descendants:
            indent = "    " + "  " * depth
            print(f"{indent}<- {name}: {short_title(meta)}")
        print()


def cmd_contradictions(refs):
    """Find all contradiction relationships."""
    results = []
    seen = set()
    for name, meta in sorted(refs.items()):
        for xref in meta.get("cross_references", []):
            if xref.get("type") == "contradicts":
                target = xref.get("target", "")
                pair = tuple(sorted([name, target]))
                if pair not in seen:
                    seen.add(pair)
                    results.append((name, target, xref.get("detail", "")))
    if not results:
        print("No contradictions found.")
        return
    print(f"Contradictions ({len(results)}):\n")
    for a, b, detail in results:
        print(f"  {a}")
        print(f"    vs. {b}")
        print(f"    {detail}")
        print()


def cmd_claims(refs, status_filter=None):
    """List key claims, optionally filtered by status."""
    results = []
    for name, meta in sorted(refs.items()):
        for claim in meta.get("key_claims", []):
            s = claim.get("status", "")
            if status_filter is None or s == status_filter:
                results.append((name, claim))
    if not results:
        print(f"No claims found{' with status ' + status_filter if status_filter else ''}.")
        return
    label = f" ({status_filter})" if status_filter else ""
    print(f"Key claims{label} ({len(results)}):\n")
    for name, claim in results:
        print(fmt_claim(name, claim))
        if claim.get("contested_by"):
            print(f"    Contested by: {claim['contested_by']}")
        print()


def cmd_open_questions(refs, unresolved_only=False):
    """List open questions across all papers."""
    results = []
    for name, meta in sorted(refs.items()):
        for q in meta.get("open_questions", []):
            addr = q.get("addressed_by")
            if unresolved_only and addr:
                continue
            results.append((name, q))
    if not results:
        label = " (unresolved)" if unresolved_only else ""
        print(f"No open questions found{label}.")
        return
    label = " (unresolved only)" if unresolved_only else ""
    print(f"Open questions{label} ({len(results)}):\n")
    for name, q in results:
        addr = q.get("addressed_by")
        status = f"  -> Addressed by: {addr}" if addr else "  -> UNRESOLVED"
        print(f"  [{name}]")
        print(f"    {q.get('question', '?')}")
        print(status)
        print()


def cmd_text(refs, query):
    """Full-text search across titles, claims, and cross-reference details."""
    query_lower = query.lower()
    results = []
    for name, meta in sorted(refs.items()):
        matches = []
        # Search title
        if query_lower in meta.get("title", "").lower():
            matches.append("title")
        # Search claims
        for claim in meta.get("key_claims", []):
            if query_lower in claim.get("claim", "").lower():
                matches.append(f"claim {claim.get('id', '?')}")
        # Search cross-reference details
        for xref in meta.get("cross_references", []):
            if query_lower in xref.get("detail", "").lower():
                matches.append(f"xref -> {xref.get('target', '?')}")
        # Search scope
        for s in meta.get("scope", []):
            if query_lower in s.lower():
                matches.append("scope")
                break
        # Search open questions
        for q in meta.get("open_questions", []):
            if query_lower in q.get("question", "").lower():
                matches.append("open question")
        if matches:
            results.append((name, meta, matches))
    if not results:
        print(f"No results for '{query}'.")
        return
    print(f"Text search for '{query}' ({len(results)} papers):\n")
    for name, meta, matches in results:
        print(f"  {name}: {short_title(meta)}")
        print(f"    Matches in: {', '.join(matches)}")
        print()


def cmd_info(refs, dir_name):
    """Show full metadata for a single paper."""
    if dir_name not in refs:
        print(f"Paper '{dir_name}' not found.")
        return
    meta = refs[dir_name]
    print(f"{'=' * 78}")
    print(f"  {meta.get('title', '?')}")
    print(f"  {meta.get('authors', '?')}")
    print(f"  {meta.get('year', '?')} | {meta.get('venue', '?')} | {meta.get('paper_type', '?')}")
    print(f"{'=' * 78}")
    print(f"\n  Categories: {', '.join(meta.get('categories', []))}")
    print(f"  Scope: {', '.join(meta.get('scope', []))}")
    benches = meta.get("benchmarks_used", [])
    if benches:
        print(f"  Benchmarks: {', '.join(benches)}")
    intro = meta.get("models_introduced", [])
    if intro:
        print(f"  Models introduced: {', '.join(intro)}")
    evald = meta.get("models_evaluated", [])
    if evald:
        print(f"  Models evaluated: {', '.join(evald)}")
    claims = meta.get("key_claims", [])
    if claims:
        print(f"\n  Key Claims ({len(claims)}):")
        for c in claims:
            print(f"    {c.get('id', '?')} [{c.get('status', '?')}]: {c.get('claim', '?')}")
            print(f"      Evidence: {c.get('evidence', '?')}")
            if c.get("contested_by"):
                print(f"      Contested by: {c['contested_by']}")
    xrefs = meta.get("cross_references", [])
    if xrefs:
        print(f"\n  Cross-references ({len(xrefs)}):")
        for x in xrefs:
            print(f"    [{x.get('type', '?')}] -> {x.get('target', '?')}")
            print(f"      {x.get('detail', '')}")
    oqs = meta.get("open_questions", [])
    if oqs:
        print(f"\n  Open questions ({len(oqs)}):")
        for q in oqs:
            addr = q.get("addressed_by")
            status = f"Addressed by {addr}" if addr else "UNRESOLVED"
            print(f"    - {q.get('question', '?')} [{status}]")
    print()


def cmd_related(refs, dir_name):
    """Show all cross-references for a given paper (both directions)."""
    if dir_name not in refs:
        print(f"Paper '{dir_name}' not found.")
        return
    meta = refs[dir_name]
    print(f"Related papers for {dir_name}:\n  {short_title(meta)}\n")

    # Outgoing references
    outgoing = meta.get("cross_references", [])
    if outgoing:
        print(f"  Outgoing ({len(outgoing)}):")
        for xref in outgoing:
            print(f"    [{xref.get('type', '?')}] -> {xref.get('target', '?')}")
            if xref.get("target") in refs:
                print(f"      {short_title(refs[xref['target']])}")
            print(f"      {xref.get('detail', '')}")
        print()

    # Incoming references (other papers referencing this one)
    incoming = []
    for other_name, other_meta in sorted(refs.items()):
        if other_name == dir_name:
            continue
        for xref in other_meta.get("cross_references", []):
            if xref.get("target") == dir_name:
                incoming.append((other_name, xref))
    if incoming:
        print(f"  Incoming ({len(incoming)}):")
        for other_name, xref in incoming:
            print(f"    [{xref.get('type', '?')}] <- {other_name}")
            print(f"      {short_title(refs[other_name])}")
            print(f"      {xref.get('detail', '')}")
        print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def usage():
    print(__doc__.strip())
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        usage()

    command = sys.argv[1]
    refs = load_all_references()

    if command == "category" and len(sys.argv) == 3:
        cmd_category(refs, sys.argv[2])
    elif command == "benchmark" and len(sys.argv) == 3:
        cmd_benchmark(refs, sys.argv[2])
    elif command == "model" and len(sys.argv) == 3:
        cmd_model(refs, sys.argv[2])
    elif command == "lineage" and len(sys.argv) == 3:
        cmd_lineage(refs, sys.argv[2])
    elif command == "contradictions":
        cmd_contradictions(refs)
    elif command == "claims":
        status = sys.argv[2] if len(sys.argv) == 3 else None
        cmd_claims(refs, status)
    elif command == "open-questions":
        unresolved = "--unresolved" in sys.argv
        cmd_open_questions(refs, unresolved)
    elif command == "text" and len(sys.argv) == 3:
        cmd_text(refs, sys.argv[2])
    elif command == "info" and len(sys.argv) == 3:
        cmd_info(refs, sys.argv[2])
    elif command == "related" and len(sys.argv) == 3:
        cmd_related(refs, sys.argv[2])
    else:
        usage()


if __name__ == "__main__":
    main()
