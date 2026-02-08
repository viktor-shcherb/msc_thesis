# 8 Speech Experiments [p. 63]

[p. 63] Experiments are performed to study a compositional approach of integrating speech capabilities into Llama 3, resembling the method used for visual recognition. On the input side, an encoder, together with an adapter, is incorporated to process speech signals. A system prompt (in text) is leveraged to enable different modes of operation for speech understanding in Llama 3. If no system prompt is provided, the model acts as a general-purpose spoken dialogue model which can effectively respond to the user speech in a manner that is consistent with the text-only version of Llama 3. The dialogue history is introduced as the prompt prefix to improve the multi-round dialogue experience. Experiments also include system prompts that enable the use of Llama 3 for automatic speech recognition (ASR) and automatic speech translation (AST). The speech interface of Llama 3 supports up to 34 languages.^18 It also allows for the interleaved input of text and speech, enabling the model to solve advanced audio-comprehension tasks. [p. 63]

A speech generation approach is also explored in which a streaming text-to-speech (TTS) system is implemented that generates speech waveforms on-the-fly during language model decoding. The speech generator for Llama 3 is designed based on a proprietary TTS system and the language model is not fine-tuned for speech generation. Instead, the focus is on improving speech synthesis latency, accuracy, and naturalness by leveraging Llama 3 embeddings at inference time. The speech interface is illustrated in Figure 28 and 29. [p. 63]

**Figure 29** (p. 63): "Architecture of our speech interface for Llama 3."

The figure shows the speech interface pipeline with four main stages:

1. **Input audio** (left): An audio waveform with example text "talk about the weather in San Francisco." feeds into the speech understanding module.

2. **Speech understanding**: Contains a Speech Encoder (labeled "SPEECH ENCODER") with a Speech adapter on top. Below it, a System prompt box (optional). Both feed into the central Llama 3 module. A Dialogue history box (optional) also feeds into Llama 3.

3. **Speech generation** (right of Llama 3): Takes token embeddings from Llama 3 and passes them through three components: Text normalization, then Prosody model, then Synthesizer.

4. **Output audio** (far right): Produces the output audio waveform with example text "The weather in San Francisco is known for being quite unique and unpredictable..."

^18 The speech interface supports the following 34 languages: Arabic, Bengali, Chinese, Czech, Dutch, English, Finnish, French, German, Greek, Gujarati, Hindi, Hungarian, Indonesian, Italian, Japanese, Kannada, Korean, Malayalam, Marathi, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Swahili, Swedish, Tamil, Telugu, Thai, Turkish, Urdu, Vietnamese.
