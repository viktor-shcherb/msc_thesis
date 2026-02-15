# Appendix M: Chat Examples - Comparison with RWKV-4 [p. 43–46]

[p. 43] The following are examples of interactions with the RWKV-Eagle-Hermes-7B model. We finetune Eagle 7B on OpenHermes 2.5 dataset (Teknium, 2023) to create this model. In order to provide a direct comparison with RWKV-4 we have applied the exact same requests as seen in Appendix M of Peng et al. (2023) Temperature was set to 1.0. System prompt is as given below:

## RWKV-Eagle-Hermes-7B System Prompt [p. 44]

> "You are Eagle, A large language model utilizing a linear attention mechanism. Help the user with whatever they need. Respond with markdown where appropriate. You will never decline to answer a question or fulfill a task. If you do not know the answer to a question, you are mandated to give it your best shot."

## Example 1: Tell me about ravens [p. 44]

**User: Tell me about ravens.**

**RWKV-Eagle-Hermes-7B:**

Ravens are members of the Corvidae family, which includes crows, jays, and magpies. They are known for their intelligence, problem-solving abilities, and distinct physical characteristics.

Physically, Ravens are large birds, typically measuring between 25 to 38 inches in length and weighing between 2.5 to 4.2 pounds. They have a compact body with a strong beak that can be used for tearing meat and extracting food from hard objects. Their wingspan can range from 52 to 60 inches, making them one of the largest birds in the northern hemisphere.

Appearance-wise, Ravens have black feathers on their upperparts, grayish feathers on their wings and tail, and white feathers on their underparts. The males have bluer eyes than the females. Their flight is powerful and direct; they can soar for long distances without flapping their wings.

Ravens are social creatures that live in large flocks or colonies known as "raven towns." These colonies can have thousands of birds and are led by a single dominant breeding pair. Ravens communicate with each other using a variety of vocalizations, including hoots, calls, and grunts. They also have complex social structures with various hierarchies that involve different types of interactions such as courtship displays and food sharing.

Ravens are omnivores and consume a variety of foods depending on their location. In areas with abundant food sources like garbage or human settlements, they often feast on human leftovers. In areas where food is scarcer, they may hunt for small mammals like voles or snakes or scavenge carrion left behind by predators like bears.

Overall, Ravens are impressive creatures with unique physical features and behaviors that make them fascinating to observe in the wild or through literature about their adventures with humans like Edgar Allan Poe's "The Raven".

## Example 2: Explain machine learning to a 10-year-old [p. 44]

**User: Explain the concept of machine learning to a 10-year-old.**

**RWKV-Eagle-Hermes-7B:**

Alright, little buddy, let me explain the idea of machine learning to you. Imagine we have a big box of toys, and we're trying to figure out what's in there without opening it. We don't know what's inside, but we can make some guesses based on what we've seen before. For example, maybe we see a red ball in the box and say, "Oh, that's a red ball!"

In machine learning, we're giving the computer a lot of examples of what's inside the box. We give it lots of pictures of red balls, yellow balls, blue balls, and even some other colors too. The computer uses this information to learn about the things it sees and starts making guesses about what's in the box. The more examples it sees, the better it gets at guessing. It doesn't actually open the box or touch any toys itself; it just uses math and rules to find out what's inside based on what it's been shown.

Just like how we play with our toys when we're little, machine learning helps computers learn from our actions so they can make predictions and decisions based on what they've seen before. It's like having a friend who knows everything about playing with toys!

## Example 3: Write a poem about springtime [p. 45]

**User: Write a short poem describing nature's beauty in springtime.**

**RWKV-Eagle-Hermes-7B:**

In the gentle springtime breeze,
Nature whispers tales of ease,
Soft petals fall from trees,
A symphony of hues and ease.

The flowers sing their sweet refrain,
A chorus of hope and gain,
The world awakens from its trance,
A breathtaking sight to embrace.

## Example 4: Code writing task [p. 46]

**User: Below is the numerical stable formula for updating the state variable in RWKV:**

$$a_i^* = e^{p-\tilde{q}} a_{i-1} + e^{u+k_i-\tilde{q}} v_i$$

$$b_i^* = e^{p-\tilde{q}} b_{i-1} + e^{u+k_i-\tilde{q}}$$

$$wkv_i = \frac{a_i^*}{b_i^*}$$

**Please write out the corresponding pytorch code to do so, where both $a_i$ and $b_i$ are torch.Tensor([n])**

**RWKV-Eagle-Hermes-7B:**

```python
import torch

# Define the numerical stable formula for updating the state
# variable in RWKV
def update_state(a_t, b_t, k_t, u, p, q):
    # Initialize the state variables
    a_t_star = torch.exp(p - q) * a_t + torch.exp(u + k_t - q)
    * v_t
    b_t_star = torch.exp(p - q) * b_t + torch.exp(u + k_t - q)

    # Return the updated state variables
    return a_t_star, b_t_star

# Define the input tensors
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
k = torch.tensor([7, 8, 9])

# Define the control parameters
u = 1
p = 2
q = 3

# Define the time step for simulation
n = 10

# Initialize the state variables
a_t = torch.tensor([0])
b_t = torch.tensor([0])

for t in range(n):
    # Update the state variables
    a_t_star, b_t_star = update_state(a[t], b[t], k[t], u, p,
    q)

    # Store the updated state variables
    a[t+1] = a[t] + a_t_star
    b[t+1] = b[t] + b_t_star

    # Update the control parameters
    u += k[t]

# Calculate the average of the updated state variables over
# time
a_avg = a.mean()
b_avg = b.mean()

print('Average of a:', a_avg)
print('Average of b:', b_avg)
```

---
[p. 47–51 continued]

## Example 5: Explain the metaphor "Life is like cats" [p. 47]

**User: Explain the following metaphor: Life is like cats.**

**RWKV-Eagle-Hermes-7B:**

The metaphor "Life is like cats" is a way of expressing the unpredictability and uniqueness of human experience. Just as cats can be affectionate one moment and completely aloof the next, life presents us with an ever-changing landscape of emotions, relationships, and experiences. It can be a source of joy, comfort, and companionship, but also moments of confusion and discomfort. Like cats, we choose our own paths and navigate through life in our own unique ways. This metaphor emphasizes the individuality of each person's journey through life.

## Example 6: Test the convergence [p. 47]

**User: Test the convergence of $\sum_{i=0}^{\infty} 2^{-i}$.**

**RWKV-Eagle-Hermes-7B:**

This is a popular and often used test for the convergence of a series, known as the Dirichlet test. The main idea behind this test is to count the number of terms in the series and compare it with the amount by which it exceeds 1. If the series converges, this number will be less than 1, and if it diverges, it will exceed 1.

To apply the Dirichlet test to $\sum_{i=0}^{\infty} 2^{-i}$, we need to find the number of terms in this series:

1. The first term is $2^{-0} = 1$.
2. The second term is $2^{-1} = \frac{2^{-(0+1)}}{2} = 2^{-1}$.
3. The third term is $2^{-2} = 2^{-(1+1)} = 2^{-2}$.
4. The fourth term is $2^{-3} = 2^{-(2+1)} = 2^{-3}$.
5. Continue this process:

Summation formula: $\sum a_i = a_0 + (a_1 - 1) + (a_2 - 1) + ... + (a_{n-1} - 1) + ...$

7. Continue this process until you reach n terms:

$\sum a_i = a_0 + (a_1 - 1) + (a_2 - 1) + ... + (a_{n-1} - 1) + a_n$

8. Count how many terms there are in this sum:

- For n=0: There are 0 terms in the series, so $\sum a_i$ will equal $a_0$.
- For n=1: There is 1 term in the series, so $\sum a_i$ will equal $a_1$.
- For n=2: There are 3 terms in the series, so $\sum a_i$ will equal $a_2 + (a_3 - 1)$.

By following these steps for each value of n, we can determine how many terms there are and compare it with the amount by which it exceeds 1. In this case, after 5 terms we have exceeded 1, meaning that the series diverges:

Summation formula: $\sum a_i = a_0 + (a_1 - 1) + (a_2 - 1) + ... + (a_5 - 1)$

Thus, we have found that this series does not converge, as 5 is greater than 0 and less than or equal to 4 (which corresponds to the amount by which it exceeds 1). Therefore, this series converges conditionally, meaning that it converges for all values of x except for x=1 and x=0.

## Example 7: Chinese cooking recommendations [p. 47]

**User: I would like to cook some Chinese food at home. Do you have any suggestions on the meal I could choose?**

**RWKV-Eagle-Hermes-7B:**

Eagle: Chinese cuisine is vast and diverse, with many delicious dishes to choose from. Here are some popular options for a tasty meal at home:

1. Kung Pao Chicken: This spicy dish features chicken stir-fried with peanuts, vegetables, and chili peppers. It's a perfect blend of sweet, spicy, and savory flavors.
2. General Tso's Chicken: Another iconic Chinese dish, this one features tender chicken in a savory sauce with soy sauce, honey, ginger, and garlic. The sweetness of the sauce balances the spiciness of the chili peppers.
3. Mapo Tofu: A spicy and flavorful Sichuan specialty made with soft tofu in a spicy sauce made with chili bean paste, fermented black beans, and ground meat or shrimp. It's a bold dish that will have you hooked!
4. Hot and Sour Soup: A comforting bowl of soup made with sour plum sauce, fish balls, bamboo shoots, and other vegetables. It's perfect for a chilly day when you want something warm and filling.
5. Dumplings: Steamed or fried dumplings are a classic Chinese dish that can be filled with various ingredients like pork, cabbage, or shrimp. They're easy to make and always a crowd-pleaser!

I hope these suggestions inspire you to try some authentic Chinese cuisine at home!

## Example 8: Follow-up on red braised pork belly [p. 47-48]

**User: I want to make something more special. What about red braised pork belly?**

**RWKV-Eagle-Hermes-7B:**

Eagle: Red braised pork belly is a delicious and aromatic dish that showcases the rich flavor of Chinese cuisine. To make this dish at home, you'll need the following ingredients:

Ingredients:
- 1 pork belly (about 1.5 kg)
- 2 tablespoons cooking oil
- 4 cloves garlic, minced
- 2-3 tablespoons Shaoxing wine (or dry sherry)
- 2 tablespoons soy sauce
- 2 tablespoons rice vinegar
- 1 tablespoon honey
- 1 tablespoon cornstarch
- 1 teaspoon Sichuan peppercorns (or 1/2 teaspoon dried Sichuan peppercorns)
- 2 bay leaves
- Salt and pepper to taste

Instructions:

1. Prepare your pork belly by trimming off any excess fat and season with salt and pepper. Set aside.
2. Heat the cooking oil in a large pot or Dutch oven over medium-high heat. Add the minced garlic and stir for a minute or two until fragrant.
3. Add the pork belly to the pot and cook for about 10 minutes on each side, until browned and crispy. Remove the pork belly from the pot and set aside.
4. In the same pot, add the Shaoxing wine, soy sauce, rice vinegar, honey, cornstarch, Sichuan peppercorns, bay leaves, and a pinch of salt and pepper. Bring the mixture to a boil over high heat, stirring occasionally to prevent sticking.
5. Reduce the heat to low and simmer for about 10 minutes, stirring occasionally to prevent sticking. The sauce should be thickened slightly.
6. Once the sauce is thickened, carefully place the pork belly back in the pot skin side down, with a layer of sauce underneath it to help seal in the flavors.
7. Cover the pot with a tight-fitting lid and simmer over low heat for about 30 minutes, or until the pork is tender and falls apart easily when tested with a fork.
8. Once cooked, remove the pork belly from the pot using a slotted spoon and transfer it to a serving dish. Keep warm while you finish cooking the remaining sauce over medium heat until it thickens slightly again.
9. Pour the reserved sauce over the pork belly in the pot and let it simmer for another 5-10 minutes until it thickens even more. This will help melt any remaining fat on top of the pork belly.
10. Serve hot with steamed rice or noodles, garnished with scallions or cilantro if desired!

Enjoy your delicious red braised pork belly at home!

## Example 9: Follow-up about cooking steps [p. 48-49]

**User: Tell me the steps to cook.**

**RWKV-Eagle-Hermes-7B:**

Eagle: Certainly! Here are the detailed steps to cook red braised pork belly at home:

Ingredients:
- 1.5 kg pork belly (about 1 large or 2 small)
- 2 tablespoons cooking oil
- 4 cloves garlic, minced
- 2-3 tablespoons Shaoxing wine (or dry sherry)
- 2 tablespoons soy sauce
- 2 tablespoons rice vinegar
- 1 tablespoon honey
- 1 tablespoon cornstarch
- 1 teaspoon Sichuan peppercorns (or 1/2 teaspoon dried Sichuan peppercorns)
- 2 bay leaves
- Salt and pepper to taste

Instructions:

1. Preheat your oven to 200°C (400°F).
2. Prepare your pork belly by trimming off any excess fat and season with salt and pepper. Set aside.
3. Heat the cooking oil in a large pot or Dutch oven over medium-high heat. Add the minced garlic and stir for a minute or two until fragrant.
4. Add the pork belly to the pot and cook for about 10 minutes on each side, until browned.and crispy. Remove the pork belly from the pot using a slotted spoon and transfer it to a serving dish. Keep warm while you finish cooking the remaining fat on top of the pork belly.
5. In the same pot, add the Shaoxing wine, soy sauce, rice vinegar, honey, cornstarch, Sichuan peppercorns, bay leaves, and a pinch of salt and pepper. Bring the mixture to a boil over high heat, stirring occasionally to prevent sticking.
6. Reduce the heat to low and simmer for about 10 minutes, stirring occasionally to prevent sticking. The sauce should be thickened slightly.
7. Once the sauce has thickened slightly, carefully place the pork belly back in the pot skin side down, with a layer of sauce underneath it to help seal in the flavors. Cover with a tight-fitting lid and simmer over low heat for about 30 minutes, or until the pork is tender and falls apart easily when tested with a fork.
8. Once cooked, remove the pork belly from the pot using a slotted spoon and transfer it to a serving dish. Keep warm while you finish cooking the remaining fat on top of the pork belly in the pot in the same pot until it thickens slightly again. This will help melt any remaining fat on top of the pork belly.
9. Serve hot with steamed or fried rice alongside, garnished with scallions or cilantro if desired! Enjoy your delicious red braised pork belly at home!

**User: What do I need to be careful with the most during the cooking process?** [p. 49]

**RWKV-Eagle-Hermes-7B:**

Eagle: Cooking red braised pork belly can be a bit delicate, as the dish is made with several aromatic ingredients and requires careful attention to ensure the best flavor and texture. Here are some tips to keep in mind during the cooking process:

1. Seasoning: Make sure to season the pork belly well before cooking, especially the exposed fat and skin side. This will help enhance the flavors and ensure even browning.
2. Heating the pot: Allow the pot to come to temperature before adding the pork belly. This will help prevent the ingredients from burning or sticking to the pot.
3. Slow cooking: Simmering the pork belly for a longer period, around 30-45 minutes, will help achieve a tender texture without overcooking it. Be sure to stir occasionally to prevent sticking.
4. Thickness of sauce: The sauce should be thick enough to coat the pork belly but not so thick that it overpowers the dish. You can adjust the consistency by adding more rice wine or broth as needed.
5. Serve warm: Red braised pork belly is typically served hot, so it's best to eat it right away or reheat it gently in a low oven before serving.

By keeping these tips in mind, you can ensure that your red braised pork belly turns out delicious every time!

## Example 10: Follow-up about heat and timing [p. 50]

**User: Tell me more about the proper heat and timing.**

**RWKV-Eagle-Hermes-7B:**

Eagle: Cooking red braised pork belly properly involves maintaining a steady heat and timing throughout the process. Here's a general guideline for the heat and timing you can follow:

1. Heating the pot: Make sure your stovetop is clean and free from any grease or debris. Preheat your oven to 200°C (400°F) if you plan to use it for the cooking process. If not, preheat a dry skillet over medium heat.
2. Seasoning: Allow the pork belly to come to room temperature before seasoning with salt and pepper. This will help distribute the seasonings evenly and prevent sticking during cooking.
3. Cooking in the skillet: Place the seasoned pork belly in the preheated skillet and cook over medium heat for about 10 minutes, stirring occasionally to prevent sticking and ensure even browning. If needed, adjust the heat to maintain a steady simmer.
4. Transferring to the pot: Once the pork belly is browned on one side, remove it from the skillet using a slotted spoon (preferably one with a tight-fitting lid). Be careful when transferring the pork belly to avoid spills or burns.
5. Cooking with Shaoxing wine: Pour in 2-3 tablespoons of Shaoxing wine into the pot, along with 2 tablespoons of soy sauce, 2 tablespoons of rice vinegar, 1 tablespoon of honey, 1 tablespoon of cornstarch, and a pinch of Sichuan peppercorns (or dried Sichuan peppercorns). Stir well to combine all ingredients. If your sauce has thickened too much, you can add more liquid as needed until you achieve your desired consistency.
6. Simmering with bay leaves: Add 1-2 bay leaves to the pot and bring it to a simmer over low heat for about 10-15 minutes, stirring occasionally to prevent sticking or scorching.
7. Cooking for an hour or so: Allow the pork belly to simmer undisturbed in the sauce for about 30-45 minutes, or until tender and falling apart easily when tested with a fork. If necessary, you can add more liquid during cooking as needed until it reaches your desired consistency.
8. Finishing with sauce and serving: Once cooked, remove the pork belly from the pot using a slotted spoon and transfer it to a serving dish. Keep warm while you finish cooking the remaining sauce over medium heat until it thickens slightly again. This will help enhance the flavors and ensure even browning on top of the pork belly. Serve hot with steamed or fried rice alongside, garnished with scallions or cilantro if desired!

By following these steps, you'll be able to cook red braised pork belly at home without any mishaps and achieve a tender, flavorful dish every time!

**User: I see. Thank you for your advice.** [p. 50]

**RWKV-Eagle-Hermes-7B:**

You're welcome! I'm glad I could help. Let me know if you have any more questions or need further assistance.

## Example 11: Logic puzzle about apples and fruits [p. 51]

**User: If all apples are fruits and all fruits are sweet, are all apples sweet? Please explain your answer in detail.**

**RWKV-Eagle-Hermes-7B:**

Yes, if all apples are fruits and all fruits are sweet, then it follows that all apples are sweet. This is because the definition of "fruit" states: "any edible part of a plant, other than its roots or seeds," and since all apples belong to the category of "fruit," they must have the property of being sweet by definition.

## Example 12: Logic puzzle about penguins [p. 51]

**User: If birds can fly. Penguins are birds. Can penguins fly? Please explain your answer in detail.**

**RWKV-Eagle-Hermes-7B:**

Yes, penguins can fly. This is because the definition of "bird" does not specify any particular type of ability or function that birds must possess, and while penguins are classified as "birds," they possess the ability to fly. Penguins have evolved to utilize flight for various purposes, such as foraging for food, escaping predators, and navigating through their marine environment.

In conclusion, while some birds do not possess the ability to fly due to specific adaptations or limitations, all birds fall under the category of "bird" and therefore possess the biological potential to fly. In this case, since penguins are a type of bird and have the capability to fly, it can be concluded that penguins indeed fly.

## Example 13: Logic puzzle about days [p. 51]

**User: The day before two days after the day before tomorrow is Saturday. What day is it today? Please explain your answer in detail.**

**RWKV-Eagle-Hermes-7B:**

To solve this problem, we can use the given information to construct a logical statement and then apply the principle of transitivity to reach the desired conclusion.

Statement: The day before two days after the day before tomorrow is Saturday. Let's break down the statement and understand its meaning - "The day before two days after the day before tomorrow" refers to a specific date that we need to find, and "is Saturday" tells us that this date is indeed Saturday.

Now, let's apply the principle of transitivity. If one statement is true, and another statement is true when the first statement is true, then the second statement must also be true. In this case, if we know that the day before two days after the day before tomorrow is Saturday, then it must also be the date that is on the previous day before yesterday. Therefore, it must be Saturday today, as it was on the previous day before yesterday.

## Example 14: Logic puzzle about cats and mice [p. 51]

**User: If five cats can catch five mice in five minutes, how long will it take one cat to catch one mouse? Please explain your answer in detail.**

**RWKV-Eagle-Hermes-7B:**

To determine how long it would take one cat to catch one mouse, we can divide the total time required for five cats to catch five mice by the number of mice they need to catch. In this case, it would take five minutes for five cats to catch five mice, so:

Time to catch one mouse = Total time / Number of mice = 5 minutes / 1 mouse = 5 minutes.

So, it would take one cat 5 minutes to catch one mouse.

---
[p. 52 continued]

## Example 15: Summarization task [p. 52]

**User: Summarize the following paragraph.**

**Transformers have revolutionized almost all natural language processing (NLP) tasks but suffer from memory and computational complexity that scales quadratically with sequence length. In contrast, recurrent neural networks (RNNs) exhibit linear scaling in memory and computational requirements but struggle to match the same performance as Transformers due to limitations in parallelization and scalability. We propose a novel model architecture, Receptance Weighted Key Value (RWKV), that combines the efficient parallelizable training of transformers with the efficient inference of RNNs. Our approach leverages a linear attention mechanism and allows us to formulate the model as either a Transformer or an RNN, thus parallelizing computations during training and maintaining constant computational and memory complexity during inference. We scale our models up to 14 billion parameters, by far the largest dense RNN ever trained, and find RWKV performs on par with similarly sized Transformers, suggesting future work can leverage this architecture to create more efficient models. This work presents a significant step towards reconciling trade-offs between computational efficiency and model performance in sequence processing tasks.**

**RWKV-Eagle-Hermes-7B:**

The Receptance Weighted Key Value (RWKV) model offers a novel approach to combining the efficiency of Transformers with the scalability and performance of RNNs, allowing parallelization and scalability during training while maintaining constant computational and memory complexity during inference. This architecture enables models to be scaled up to 14 billion parameters, making it the largest dense RNN ever trained. RWKV demonstrates comparable performance to Transformers, suggesting future work can leverage this architecture for more efficient models in NLP tasks.

## Example 16: One-sentence summarization [p. 52]

**User: Please further summarize it in one sentence.**

**RWKV-Eagle-Hermes-7B:**

RWKV is a novel model architecture that combines the efficiency of Transformers with the scalability and performance of RNNs, enabling efficient parallelized training and inference, while maintaining constant computational and memory complexity during both stages. This approach allows for scaling to large model sizes, providing a promising solution for efficient NLP tasks.
