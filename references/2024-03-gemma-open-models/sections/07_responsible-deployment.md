# Responsible Deployment [p. 8-10]

In line with previous releases of Google's AI technologies (Gemini Team, 2023; Kavukcuoglu et al., 2022), a structured approach to responsible development and deployment of the models is followed, in order to identify, measure, and manage foreseeable downstream societal impacts. As with the recent Gemini release, these are informed by prior academic literature on language model risks (Weidinger et al., 2021), findings from similar prior exercises conducted across the industry (Anil et al., 2023), ongoing engagement with experts internally and externally, and unstructured attempts to discover new model vulnerabilities. [p. 8]

## Benefits

The authors believe that openness in AI science and technology can bring significant benefits. Open-sourcing is a significant driver of science and innovation, and a responsible practice in most circumstances. But this needs to be balanced against the risk of providing actors with the tools to cause harm now or in the future. [p. 8]

Google has long committed to providing broader access to successful research innovations (GraphCast, Transformer, BERT, T5, Word2Vec), and the authors believe that releasing Gemma into the AI development ecosystem will enable downstream developers to create a host of beneficial applications, in areas such as science, education and the arts. The instruction-tuned offerings should encourage a range of developers to leverage Gemma's chat and code capabilities to support their own beneficial applications, while allowing for custom fine-tuning to specialize the model's capabilities for specific use cases. To ensure Gemma supports a wide range of developer needs, two model sizes are released to optimally support different environments, and the models are made available across a number of platforms (see Kaggle for details). Providing broad access to Gemma should reduce the economic and technical barriers that newer ventures or independent developers face when incorporating these technologies into their workstreams. [p. 8-9]

As well as serving developers with instruction-tuned models, access to corresponding base pretrained models is also provided. By doing so, the intention is to encourage further AI safety research and community innovation, providing a wider pool of models available to developers to build on various methods of transparency and interpretability research that the community has already benefited from (Pacchiardi et al., 2023; Zou et al., 2023). [p. 9]

## Risks

The authors are aware that malicious uses of LLMs, such as the creation of deepfake imagery, AI-generated disinformation, and illegal and disturbing material can cause harm on both an individual and institutional levels (Weidinger et al., 2021). Providing access to model weights, rather than releasing models behind an API, also raises new challenges for responsible deployment. [p. 9]

First, bad actors cannot be prevented from fine-tuning Gemma for malicious intent, despite use being subject to Terms of Use that prohibit the use of Gemma models in ways that contravene the Gemma Prohibited Use Policy. However, further work is required to build more robust mitigation strategies against intentional misuse of open models, which Google DeepMind will continue to explore both internally and in collaboration with the AI community. [p. 9]

The second challenge is protecting developers and downstream users against the unintended behaviours of open models, including generation of toxic language or perpetuation of discriminatory social harms, model hallucinations and leakage of personally identifiable information. When deploying models behind an API, these risks can be reduced via various filtering methods. [p. 9]

## Mitigations

Without the API layer of defense for the Gemma family of models, the authors have endeavoured to safeguard against these risks by filtering and measuring biases in pre-training data in line with the Gemini approach, assessing safety through standardized AI safety benchmarks, internal red teaming to better understand the risks associated with external use of Gemma, and subjecting the models to rigorous ethics and safety evaluations, the results of which can be seen in Table 8. [p. 9]

While significantly investing in improving the model, the authors recognize its limitations. To ensure transparency for downstream users, a detailed model card has been published to provide researchers with a more comprehensive understanding of Gemma. [p. 9]

A Generative AI Responsible Toolkit has also been released to support developers to build AI responsibly. This encompasses a series of assets to help developers design and implement responsible AI best practices and keep their users safe. [p. 9]

The relative novelty of releasing open weights models means new uses, and misuses, of these models are still being discovered, which is why Google DeepMind is committed to the continuous research and development of robust mitigation strategies alongside future model development. [p. 9]

## Assessment

> "Ultimately, given the capabilities of larger systems accessible within the existing ecosystem, we believe the release of Gemma will have a negligible effect on the overall AI risk portfolio." [p. 9]

In light of this, and given the utility of these models for research, auditing and downstream product development, the authors are confident that the benefit of Gemma to the AI community outweighs the risks described. [p. 9]

## Going Forward

As a guiding principle, Google DeepMind strives to adopt assessments and safety mitigations proportionate to the potential risks from their models. [p. 9]

Although the authors are confident that Gemma models will provide a net benefit to the community, the emphasis on safety stems from the irreversible nature of this release. As the harms resulting from open models are not yet well defined, nor does an established evaluation framework for such models exist, Google DeepMind will continue to follow this precedent and take a measured and cautionary approach to open model development. As capabilities advance, extended testing, staggered releases or alternative access mechanisms may be explored to ensure responsible AI development. [p. 10]

As the ecosystem evolves, the authors urge the wider AI community to move beyond simplistic 'open vs. closed' debates, and avoid either exaggerating or minimising potential harms, as a nuanced, collaborative approach to risks and benefits is believed to be essential. At Google DeepMind they are committed to developing high-quality evaluations and invite the community to join in this effort for a deeper understanding of AI systems. [p. 10]
