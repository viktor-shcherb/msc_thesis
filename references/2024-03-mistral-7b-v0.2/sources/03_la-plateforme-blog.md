# Mistral AI Blog — La Plateforme (December 11, 2023)

**URL:** https://mistral.ai/news/la-plateforme
**Type:** blog-post
**Fetched:** 2026-02-15
**Priority:** primary

## Release Date

**December 11, 2023** — Mistral AI announced beta access to their first platform services.

## La Plateforme Service

Mistral introduced "la plateforme," their initial API offering featuring:
- Three chat endpoints for text generation
- One embedding endpoint
- Different performance/cost tradeoffs across endpoints

## Mistral-7B-Instruct-v0.2 Announcement

The blog post describes the most affordable endpoint, mistral-tiny, which serves:

> **"Mistral 7B Instruct v0.2, a new minor release"** of their base model.

### Model Specifications

- **Language support**: English only
- **Performance metric**: 7.6 on MT-Bench
- **Availability**: The instructed version is downloadable via Hugging Face

## Technical Context

The blog post notes that Mistral created these models through:

> "efficient fine-tuning, direct preference optimisation"

The platform follows "the popular chat interface initially proposed by our dearest competitor" and provides Python and JavaScript client libraries.

## Additional Endpoints

Two higher-tier options were simultaneously released:
- **mistral-small**: Serving Mixtral 8x7B, scoring 8.3 on MT-Bench
- **mistral-medium**: A prototype achieving 8.6 on MT-Bench

## Context for v0.2 Release

This blog post represents the first public announcement of the Mistral-7B-Instruct-v0.2 model. Notably, this was an instruction-tuned variant released through the API platform, with the base model weights not being made publicly available until March 2024 (three months later).
