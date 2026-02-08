# 8. Appendix A: Samples [p. 13-24]

## 8.1. Model capacity [p. 13]

[p. 13] To complement the reported perplexity gains of bigger LMs on WebText shown in Figure 4, Tables 7 through 11 show side-by-side completions of the smallest WebText LM and GPT-2 on random unseen WebText test set articles.

## 8.2. Text Memorization [p. 13]

[p. 13] The authors observe some memorizing behavior in GPT-2 on longer strings that are repeated many times in the dataset such as famous quotes or speeches. For example, when conditioned on the first sentence and a half of the Gettysburg Address (which occurs approximately 40 times throughout WebText), an argmax decode from GPT-2 recovers the speech. Even when sampling without truncation, the model copies the speech for a while before drifting, albeit in a similar style. It typically drifts within 100-200 tokens and displays widening diversity once it drifts.

To quantify how often exact memorization shows up in samples, the authors generated samples from GPT-2 conditioned on WebText test set articles and compared the overlap rates of GPT-2's generations to the overlap rates of the ground-truth completions. The results suggest that GPT-2 repeats text from the training set less often than the baseline rate of held-out articles.

**Figure 5** (p. 13): "CDF of percentage 8-gram overlap with WebText training set, for both WebText test set and samples (conditioned on WebText test set, with top-k truncated random sampling with k = 40). Most samples have less than 1% overlap, including over 30% of samples with no overlap, whereas the median for test set is 2.6% overlap."

X-axis: 8-gram overlap with training set (log scale, 1% to 100%). Y-axis: Empirical CDF (0.0 to 1.0). Two lines: "samples" (blue) and "real" (orange). The "samples" line rises faster and is consistently above the "real" line, indicating that GPT-2 generated samples have less 8-gram overlap with the training set than actual held-out WebText test set articles. At 1% overlap, approximately 30% of samples have no overlap (CDF ~0.3 for samples), while the real test set CDF is lower (~0.15). Both curves converge near 1.0 by 100% overlap.

## 8.3. Diversity [p. 13]

[p. 13] Table 12 shows multiple completions of the same random WebText test set context, showing the diversity of completions with standard sampling settings.

## 8.4. Robustness [p. 13]

[p. 13] Table 13 shows the previously mentioned talking unicorns news article. The authors find the model to be capable of handling out of distribution contexts, but the quality of these samples is generally lower.

## Sample Tables

**Table 7** (p. 14): "Random unseen contexts (top), and non-cherry-picked completions from both the smallest (left) and largest (right) models. Contexts are 768 tokens, with approximately 256 tokens worth of paragraphs shown. Completions are 256 tokens and fully shown. Top-k random sampling with k = 40 was used for generation."

The context describes outfit pairings with sneakers. The small model completion continues with generic fashion advice about "High End" and "High Light" outfits in a somewhat repetitive and less coherent manner. The GPT-2 completion is more coherent, describing specific outfit choices with ASICS Tiger Killshots sneakers in a natural, first-person blog post style, covering "Casual Jacket" and "Dress" outfits.

**Table 8** (p. 15): "Random unseen contexts (top), and non-cherry-picked completions from both the smallest (left) and largest (right) models. Contexts are 768 tokens, with approximately 256 tokens worth of paragraphs shown. Completions are 256 tokens and fully shown. Top-k random sampling with k = 40 was used for generation."

The context describes historical attractions in Spain from the period of Muslim rule (the Mezquita, the Alhambra, etc.), under the heading "Reconquista and Imperial era." The small model completion is incoherent -- it fabricates a narrative about Muslim Spain being "very different from that of other parts of the world" and mixes up historical facts (e.g., "Emperor of Naples" in 1050 CE, "King Alfred II of Sweden"). The GPT-2 completion is substantially more coherent and factually grounded, discussing the Reconquista with references to the kingdoms of Castile and Aragon, the Battle of Poitiers, Ferdinand IX, and the period 1229-1492.

**Table 9** (p. 16): "Random unseen contexts (top), and non-cherry-picked completions from both the smallest (left) and largest (right) models. Contexts are 768 tokens, with approximately 256 tokens worth of paragraphs shown. Completions are 256 tokens and fully shown. Top-k random sampling with k = 40 was used for generation."

The context describes the behavior of the ghost "Pinky" in Pac-Man, including AI targeting mechanics and the "head fake" exploit. The small model completion is generic and somewhat repetitive, discussing ghost behavior in abstract terms ("The ghost will have to go to another location of some kind"). The GPT-2 completion is more specific and organized, describing Buster (the yellow ghost), safe house mechanics, and "Chase" mode behavior, maintaining topical coherence with the game context.

---
[p. 17-21 continued]

**Table 10** (p. 17): "Random unseen contexts (top), and non-cherry-picked completions from both the smallest (left) and largest (right) models. Contexts are 768 tokens, with approximately 256 tokens worth of paragraphs shown. Completions are 256 tokens and fully shown. Top-k random sampling with k = 40 was used for generation."

The context describes Civil War-era military personnel -- Corporal Michael P. Goeldin, Corporal Patrick O'Neal, Corporal Benjamin Browne, and Artificer William Collins -- with detailed enlistment histories and service records. The small model completion continues with Collins's military career in a somewhat plausible manner but degenerates into incoherent text, eventually producing an unrelated Reuters news snippet about Moscow, Syria, and U.S. politics. The GPT-2 completion is markedly more coherent, continuing the Civil War military personnel theme with a detailed account of Captain James J. Dall's service, including specific dates, units (2d Virginia Infantry, Western Reserve Regiment, Company I, 25th New York Volunteers), engagements (Peninsula Campaign), and promotions, all maintaining the stylistic register of the original context.

**Table 11** (p. 18): "Random unseen contexts (top), and non-cherry-picked completions from both the smallest (left) and largest (right) models. Contexts are 768 tokens, with approximately 256 tokens worth of paragraphs shown. Completions are 256 tokens and fully shown. Top-k random sampling with k = 40 was used for generation."

The context is a technical blog post covering two topics: configuring fonts in Xmonad via Xresources/XFT and fixing SSH permissions in Cygwin on Windows. The small model completion stays roughly on-topic about Cygwin SSH permissions but becomes circular and hard to follow, discussing chroot and permission workarounds with confusing logic. The GPT-2 completion is more structured and coherent, providing step-by-step instructions (setting permissions to 2644, using `ssh-add /.ssh/`), then drifting into a related but distinct topic about Xresources configuration (`.xprofile`, `.xsession-errors`, color settings), showing the model's ability to maintain a technical register even when topics shift.

**Table 12** (p. 19): "Non-cherry-picked completions from GPT-2 generated from the same context (from WebText test). Context is 384 tokens (shown truncated), and generations are 128 tokens. Top-k random sampling with k = 40 was used for generation."

The context describes baking a mint chocolate cake with Peppermint Jo Jos, meringue cookies, and various toppings, written in informal first-person recipe blog style. Six GPT-2 completions are shown side by side, demonstrating diversity of generation from the same context:

- **GPT-2 Completion 1**: Continues with a meringue cookies recipe (1 3/4 cup butter, 1 cup sugar, 1 egg yolk, 3 T heavy cream, 3 1/2-4 cups flour, etc.) with a "Peppermint-Jojo Topping" section.
- **GPT-2 Completion 2**: Shifts to a personal anecdote about baking rules (not using cookie crumbs/chocolate chips with raw sugar until cooled, not substituting ingredients), then mentions finding a card with kittens.
- **GPT-2 Completion 3**: Describes a "Chocolate Buttermilk Cake Print Chunks" recipe with an ingredients list (1 1/2 cup unsalted butter, 1 1/2 cup granulated sugar, 3 large eggs, etc.) and a chocolate glaze.
- **GPT-2 Completion 4**: Continues with a meringue cookie recipe, beginning with the egg whites and describing a warming technique over simmering water (3-5 minutes).
- **GPT-2 Completion 5**: Provides a personal narrative about Christmas baking failures and successes, discussing moisture, blending chocolate and mint, and mixing ingredients in a separate bowl.
- **GPT-2 Completion 6**: Describes a layered chocolate cake recipe with specific baking instructions (8-inch round tart pan, parchment paper, 350 degrees, 30-40 minutes), ending with "Chocolate Buttermilk Layer Cake with Peppermint Jo."

All six completions stay in the baking/recipe domain but diverge significantly in content and style, illustrating the diversity of generations under top-k sampling.

**Table 13** (p. 20): "Conditional generation on an out-of-distribution context by GPT-2. Cherry pick of 10 samples generated with k = 40."

Context (human-written): A brief two-sentence setup about scientists discovering a herd of unicorns living in a previously unexplored Andes valley, with the surprising detail that the unicorns spoke perfect English.

GPT-2 generated text: The model names the population "Ovid's Unicorn" -- four-horned, silver-white creatures previously unknown to science. It constructs a multi-paragraph news article featuring Dr. Jorge Perez, an evolutionary biologist from the University of La Paz, who explores the valley with companions and discovers the unicorns near a natural fountain surrounded by rock and silver snow. The article includes direct quotes from Perez (e.g., "By the time we reached the top of one peak, the water looked blue, with some crystals on top"; "We can see, for example, that they have a common 'language,' something like a dialect or dialectic."). Perez speculates the unicorns may have originated in Argentina as descendants of a lost race, and notes that the only way to confirm this would be through DNA analysis. The generated text maintains coherent journalistic style, consistent character attribution, and thematic unity throughout.

**Table 14** (p. 21): "Summaries generated by GPT-2 and reference summaries on the test set of the CNN and Daily Mail dataset."

Three article-summary pairs are shown, each with a GPT-2 generated summary and the reference summary side by side:

**Article 1:** About the Chauvet-Pont-d'Arc Cave replica -- prehistoric cave art in southern France reproduced using cutting-edge technology, with the Caverne du Pont-d'Arc containing 1,000 reproduced drawings, 450 bones, and other features.
- **GPT-2 summary:** "The original site in Vallon-Pont-D'arc in Southern France is a Unesco World Heritage site and is the oldest known and the best preserved cave decorated by man. The replica cave was built a few miles from the original site in Vallon-Pont-D'arc in Southern France. The cave contains images of 14 different species of animals including woolly rhinoceros, mammoths, and big cats."
- **Reference summary:** "Cave mimics famous Caverne du Pont-d'Arc in France, the oldest cave decorated by man and the best preserved. The replica contains all 1,000 paintings which include 425 such as a woolly rhinoceros and mammoths. Minute details were copied using 3D modelling and anamorphic techniques, often used to shoot widescreen images. The modern cave also includes replica paw prints of bears, bones and details preserved in the original cave."

**Article 2:** About luxury submarines owned by billionaires, including Roman Abramovich's submarine on his superyacht Eclipse, and the OrcaSub with Perspex viewing domes.
- **GPT-2 summary:** "The U-Boat Worx submarine can dive to 984 feet (300 metres) and is capable of diving to the bottom of the ocean. It can be used for diving, snorkelling and even snorkel diving. The submarine is also equipped with a snorkelling platform."
- **Reference summary:** "Feel like a James Bond villain with the most advanced submerged ocean vehicles. Some convert from a yacht into a submarine, and others detached off for a speedy exploration. Oliver's Travels offers a Mile Low package on its submarine, complete with chef and butler for £175,000 a night."

**Article 3:** About Amina Ali Qassim sitting with her grandchild during the aerial bombardment in Yemen, fleeing from their home on the island of Birim.
- **GPT-2 summary:** "Yemen is in the middle of a civil war. Saudi Arabia is leading the coalition bombing campaign. It's been bombing Yemen for more than two months now."
- **Reference summary:** "Amina Ali Qassim's family sought shelter in a mosque before fleeing Yemen. Thousands like them are boarding boats to sail to Djibouti. Saudi Arabia has been pounding Yemen in a bid to defeat Houthi rebels."

The GPT-2 summaries capture broad topics but tend to focus on general statements rather than specific details from the articles. The reference summaries are more specific and include more concrete factual details from the source articles.

---
[p. 22 continued]

**Table 15** (p. 22): "English to French and French to English translations generated by GPT-2."

Six translation pairs are shown, alternating between English-to-French and French-to-English directions:

| Direction | Reference | GPT-2 Translation |
|-----------|-----------|-------------------|
| En->Fr | "This re-release, titled The Next Day Extra, was presented in the form of three disks: the original album, unpublished studio sessions and remixes, plus a DVD containing the four clips that have already been unveiled." | "Les nouvelles re-releases, tout en premier disc, nécessaire de l'album, un studio session et remixes, plus un DVD de l'écran de quelques clips qui ont été déjà échappés." |
| Fr->En | "Un homme expliquait que le fonctionnement de la hernia fonctionnelle qu'il avait reconnaît avant de faire, le fonctionnement de la hernia fonctionnelle que j'ai réussi, j'ai réussi." | "This release, originally released on three discs: the original album, sessions studio inédites and remixes, a DVD containing the four clips that were released on the previous day." |
| En->Fr | "One man explained that the free hernia surgery he'd received will allow him to work again." | "Un homme expliquait que le fonctionnement de la hernia fonctionnelle qu'il avait reconnaît avant de faire, le fonctionnement de la hernia fonctionnelle que j'ai réussi, j'ai réussi." |
| Fr->En | "Un homme a expliqué que l'opération gratuite qu'il avait subie pour soigner une hernie lui permettrait de travailler à nouveau." | "A man told me that the operation gratuity he had been promised would not allow him to travel." |
| En->Fr | "Speaking to an open government conference in London via video link, Mr Kerry said: 'There is no question that the President and I and others in government have actually learned of some things that had been happening on an automatic pilot because the ability has been there, going back to World War Two and to the very difficult years of the Cold War, and then, of course, 9/11.'" | "Le premier conference de l'édition internationale en ligne sur la vide, le ministre de l'Édition internationale a été vide, lui dit : 'Il n'y a qu'une question que le président et moi et tous les autres personnes d'une administration qui a été évident par la fois, par la part de la guerre, par la part de la guer" |
| Fr->En | "S'exprimant lors d'une conférence intergouvernementale à Londres par liaison vidéo, M. Kerry a déclaré: 'Il est indéniable que le Président, moi-même et d'autres membres du gouvernement avons pris connaissance de certaines choses en mode pilote automatique parce que nous en avions la possibilité, dès la Seconde guerre mondiale et jusqu'aux années difficiles de la Guerre froide, puis bien sûr le 11 septembre.'" | "In a conference between the United States and London, Secretary of State John Kerry said: 'It is undeniable that the President, myself and others of the government have been aware of certain certain choices that have been made in the past in order to be able to do certain things in a more automated way.'" |

The En->Fr translations show significant quality issues: repeated phrases, incorrect vocabulary, and loss of meaning. The Fr->En translations are notably better, consistent with the asymmetry reported in Section 3.7 (5 BLEU En->Fr vs. 11.5 BLEU Fr->En), reflecting GPT-2's much stronger English language model.

---
[p. 23-24 continued]

**Table 16** (p. 23): "Selected CoQA completion."

Context: A passage about the 2008 Summer Olympics torch relay, run from March 24 to August 8, 2008, prior to the Beijing Olympics. The relay, called the "Journey of Harmony," lasted 129 days and carried the torch 137,000 km (85,000 mi) -- the longest distance of any Olympic torch relay since the tradition started ahead of the 1936 Summer Olympics. The torch was lit in Olympia, Greece, traveled to Athens, then Beijing, passing through six continents, visiting cities along the Silk Road, and ascending Mount Everest.

Previous question-answer pairs provided as context:
- Q: What was the theme? A: "one world, one dream".
- Q: What was the length of the race? A: 137,000 km
- Q: Was it larger than previous ones? A: No
- Q: Where did the race begin? A: Olympia, Greece
- Q: Is there anything notable about that place? A: birthplace of Olympic Games
- Q: Where did they go after? A: Athens
- Q: How many days was the race? A: seven
- Q: Did they visit any notable landmarks? A: Panathinaiko Stadium
- Q: And did they climb any mountains? A:

**Model answer:** Everest
**Turker answers:** unknown, yes, Yes, yes

The model generates the specific mountain name "Everest" (factually correct from the passage), while the human Turker answers are simpler yes/no responses. This illustrates GPT-2's tendency toward specific retrieval-based answers.

**Table 17** (p. 24): "Selected CoQA completion."

Context: A passage about Catherine Green, a 54-year-old secretary, and her dog Tom. Tom accompanies her everywhere -- her office, shopping. Catherine treats Tom as her "fourth child." Catherine and Tom live in Sweden, where dog ownership incurs extra taxes (up to 500 Swedish kronor per year), the government funds dog hospitals and medical treatment, and owners must pay for any damage their dogs cause (including car damage if a dog is hit by a passing car).

Previous question-answer pairs:
- Q: How old is Catherine? A: 54
- Q: where does she live? A:

**Model answer:** Stockholm
**Turker answers:** Sweden, Sweden, in Sweden, Sweden

The model gives a more specific but incorrect answer ("Stockholm" -- the passage says "Sweden" but never specifies Stockholm), while all four Turker answers correctly say "Sweden." This illustrates the heuristic-based behavior noted in Section 3.5, where GPT-2 tends to generate plausible-sounding specific answers rather than extracting the precise information from the passage.
