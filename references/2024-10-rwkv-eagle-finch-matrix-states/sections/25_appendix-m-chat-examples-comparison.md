# Appendix M: Chat Examples - Comparison with RWKV-4 [p. 43–52]

[p. 43] The following are examples of interactions with the RWKV-Eagle-Hermes-7B model. We finetune Eagle 7B on OpenHermes 2.5 dataset (Teknium, 2023) to create this model. In order to provide a direct comparison with RWKV-4 we have applied the exact same requests as seen in Appendix M of Peng et al. (2023) Temperature was set to 1.0. System prompt is as given below:

## RWKV-Eagle-Hermes-7B System Prompt [p. 44]

**You are Eagle, A large language model utilizing a linear attention mechanism. Help the user with whatever they need. Respond with markdown where appropriate. You will never decline to answer a question or fulfill a task. If you do not know the answer to a question, you are mandated to give it your best shot.**

## Example 1: Tell me about ravens [p. 44]

**RWKV-Eagle-Hermes-7B**

**Tell me about ravens.**

Ravens are members of the Corvidae family, which includes crows, jays, and magpies. They are known for their intelligence, problem-solving abilities, and distinct physical characteristics.

Physically, Ravens are large birds, typically measuring between 25 to 38 inches in length and weighing between 2.5 to 4.2 pounds. They have a compact body with a strong beak that can be used for tearing meat and extracting food from hard objects. Their wingspan can range from 52 to 60 inches, making them one of the largest birds in the northern hemisphere.

Appearance-wise, Ravens have black feathers on their upperparts, grayish feathers on their wings and tail, and white feathers on their underparts. The males have bluer eyes than the females. Their flight is powerful and direct; they can soar for long distances without flapping their wings.

Ravens are social creatures that live in large flocks or colonies known as "raven towns." These colonies can have thousands of birds and are led by a single dominant breeding pair. Ravens communicate with each other using a variety of vocalizations, including hoots, calls, and grunts. They also have complex social structures with various hierarchies that involve different types of interactions such as courtship displays and food sharing.

Ravens are omnivores and consume a variety of foods depending on their location. In areas with abundant food sources like garbage or human settlements, they often feast on human leftovers. In areas where food is scarcer, they may hunt for small mammals like voles or snakes or scavenge carrion left behind by predators like bears.

Overall, Ravens are impressive creatures with unique physical features and behaviors that make them fascinating to observe in the wild or through literature about their adventures with humans like Edgar Allan Poe's "The Raven".

## Example 2: Explain machine learning to a 10-year-old [p. 44]

**RWKV-Eagle-Hermes-7B**

**Explain the concept of machine learning to a 10-year-old.**

Alright, little buddy, let me explain the idea of machine learning to you. Imagine we have a big box of toys, and we're trying to figure out what's in there without opening it. We don't know what's inside, but we can make some guesses based on what we've seen before. For example, maybe we see a red ball in the box and say, "Oh, that's a red ball!"

In machine learning, we're giving the computer a lot of examples of what's inside the box. We give it lots of pictures of red balls, yellow balls, blue balls, and even some other colors too. The computer uses this information to learn about the things it sees and starts making guesses about what's in the box. The more examples it sees, the better it gets at guessing. It doesn't actually open the box or touch any toys itself; it just uses math and rules to find out what's inside based on what it's been shown.

Just like how we play with our toys when we're little, machine learning helps computers learn from our actions so they can make predictions and decisions based on what they've seen before. It's like having a friend who knows everything about playing with toys!

## Example 3: Write a poem about springtime [p. 45]

**RWKV-Eagle-Hermes-7B**

**Write a short poem describing nature's beauty in springtime.**

In the gentle springtime breeze,
Nature whispers tales of ease,
Soft petals fall from trees,
A symphony of hues and ease.

The flowers sing their sweet refrain,
A chorus of hope and gain,
The world awakens from its trance,
A breathtaking sight to embrace.

## Example 4: Code writing task [p. 46]

**RWKV-Eagle-Hermes-7B**

**Below is the numerical stable formula for updating the state variable in RWKV:**

$$a_i^* = e^{p-\tilde{q}} a_{i-1} + e^{u+k_i-\tilde{q}} v_i$$
$$b_i^* = e^{p-\tilde{q}} b_{i-1} + e^{u+k_i-\tilde{q}}$$
$$wkv_i = \frac{a_i^*}{b_i^*}$$

**Please write out the corresponding pytorch code to do so, where both a_i and b_i are torch.Tensor([n])**

[Full Python code example provided showing implementation of the numerical stable RWKV state update formula]

## Additional Examples [p. 47–52]

The appendix continues with various examples demonstrating the model's capabilities including:

- Explaining metaphors ("Life is like cats")
- Mathematical reasoning (testing convergence of series)
- Practical cooking advice (Chinese food recipes, red braised pork belly detailed instructions)
- Logical reasoning puzzles
- Summarization tasks

[p. 52] Final example shows the model summarizing a complex paragraph about Transformers, RNNs, and the RWKV architecture, demonstrating strong comprehension and synthesis abilities.
