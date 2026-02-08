# M Cases [p. 26-30]

[p. 26-30]

In this part, the authors present a few instances of outputs produced by RWKV model using a Chat interface^5,6.

^5 https://github.com/BlinkDL/ChatRWKV
^6 https://huggingface.co/spaces/BlinkDL/ChatRWKV-gradio

---

## Example 1: General Knowledge [p. 26]

**Model:** RWKV-4-Raven-14B

**User prompt:** "Tell me about ravens."

**Model response:** "Ravens are large, black birds with a distinctive white head and neck. They are found in most parts of the world, including North America, Europe, Asia, and Australia. Ravens are known for their intelligence and problem-solving abilities. They are also considered to be symbols of death and transformation in many cultures. Ravens are often associated with the afterlife or death because they have been known to eat carrion or even other birds. In some cultures, ravens are also believed to be messengers of the gods or guardians of treasure."

---

## Example 2: Explanation for a Child [p. 27]

**Model:** RWKV-4-Raven-14B

**User prompt:** "Explain the concept of machine learning to a 10-year-old."

**Model response:** "Machine learning is like a super-smart computer that can learn on its own. It can recognize patterns and make decisions based on what it has learned. Just like how you might remember something from the past, the computer can remember what it's learned and use it to make predictions or decisions in the future. It's like having a smart friend who always knows what to do!"

---

## Example 3: Creative Writing (Poetry) [p. 27]

**Model:** RWKV-4-Raven-14B

**User prompt:** "Write a short poem describing nature's beauty in springtime."

**Model response:**

> Nature's beauty in springtime is rare,
> A symphony of colors, a gentle surprise.
> The flowers bloom, the birds sing and sing,
> As the sun shines down, warming our skin.
> The trees sway in the gentle breeze,
> As we take in their beauty with ease.
> The sky is blue, the clouds are white,
> A sight to behold, it's truly divine.

---

## Example 4: Technical / Code Generation [p. 28]

**Model:** RWKV-4-Raven-14B

**User prompt:** "Below is the numerical stable formula for updating the state variable in RWKV:

$a_t^* = e^{p-q} a_{t-1} + e^{u+k_t-q} v_t$

$b_t^* = e^{p-q} b_{t-1} + e^{u+k_t-q}$

$wkv_t = \frac{a_t^*}{b_t^*}$

Please write out the corresponding pytorch code to do so, where both $a_t$ and $b_t$ are torch.Tensor([n])"

**Model response:**

"Here is the PyTorch code to update the state variable in RWKV using the given formula:"

```python
import torch
def update_state(a, b, u, v, p, q):
    a_t = torch.exp(p - q) * a + torch.exp(u + k - q) * v
    b_t = torch.exp(p - q) * b + torch.exp(u + k - q)
    return a_t, b_t
a, b = torch.randn(2, 3)
u = torch.randn(2)
v = torch.randn(2)
wkv = torch.randn(2)
a_t, b_t = update_state(a, b, u, v, wkv, torch.randn(2))
print("a_t:", a_t)
print("b_t:", b_t)
```

"This code defines a function update_state that takes in the state variables a and b, the control variables u and v, and the parameters wkv and torch.randn. It then uses the PyTorch torch.exp function to compute the exponential of the control variables and the log of the normalization factor. Finally, it uses these values to update the state."

---

## Example 5: Metaphor Explanation [p. 28]

**Model:** RWKV-4-Raven-14B

**User prompt:** "Explain the following metaphor: Life is like cats."

**Model response:** "The metaphor 'Life is like cats' suggests that life can be unpredictable and full of unexpected twists and turns, just like a cat's behavior. It implies that we cannot fully control or predict the outcome of our lives, just as we cannot control the movements of a cat. The metaphor also implies that life is complex and multifaceted, with many different variables and factors at play. Just as a cat can have multiple personalities or moods, life can have many twists and turns that are difficult to predict or understand. Overall, the metaphor suggests that life is complex and unpredictable, much like a cat's behavior."

---

## Example 6: Mathematical Reasoning [p. 29]

**Model:** RWKV-4-Raven-14B

**User prompt:** "Test the convergence of $\sum_{i=0}^{\infty} 2^{-i}$."

**Model response:** "The given series is a geometric series with the first term $a_0 = 2$ and common ratio $r = \frac{1}{2}$. We can find the sum of this series using the formula for a geometric series:

$$\sum_{i=0}^{\infty} a_i = \frac{a_0}{1-r} = \frac{\frac{1}{2}}{1-\frac{1}{2}} = \frac{1}{1-\frac{1}{2}} = \frac{2}{1} = 2$$

So, the sum of the given series is 2."

---

## Example 7: Multi-turn Dialogue (Cooking) [p. 29]

**Model:** RWKV-4-Raven-14B

**User:** "I would like to cook some Chinese food at home. Do you have any suggestions on the meal I could choose?"

**Model:** "Yes, of course! If you are not very experienced in cooking Chinese food, you could start with making noodles or rice, then make a dish using one of those. I also think making stir-fry with some meat is an excellent idea."

**User:** "I want to make something more special. What about red braised pork belly?"

**Model:** "Yes, red braised pork belly is also very popular and tasty."

**User:** "Tell me the steps to cook."

**Model:** "You will need a few ingredients such as pork belly, star anise, sugar, ginger, scallions and wine. Put all of these in a pot, cook on medium heat and simmer until the meat is tender. After that, remove the meat from the pot and reserve the sauce. Slice the meat and add some ginger slices into it, then boil until it's almost done."

**User:** "What do I need to be careful with the most during the cooking process?"

**Model:** "To cook pork belly properly, it is very important to monitor the heat of the stove and be patient with the cooking process. Overcooking it can cause the pork to be tough, dry and difficult to chew. You can add a few ingredients like soy sauce or black beans to give the pork more flavor."

**User:** "Tell me more about the proper heat and timing."

**Model:** "If the temperature of the water is too high, it can damage the collagen and connective tissues, resulting in tough pork belly. It is essential to control the temperature carefully, especially when braising the pork. Additionally, keep the water simmering but not boiling to maintain a low simmer, as high heat will dry out the pork belly and result in tough and unpalatable meat. Lastly, monitor the heat during cooking and make sure the heat is medium, as this is what is most appropriate for slow cooking pork belly."

**User:** "I see. Thank you for your advice."

**Model:** "You're welcome! It was a pleasure chatting with you. Let me know if you need any further assistance in the future."

---

## Example 8: Logical Reasoning and Summarization [p. 30]

**Model:** RWKV-4-Raven-14B

**User:** "If all apples are fruits and all fruits are sweet, are all apples sweet? Please explain your answer in detail."

**Model:** "Yes, all apples are fruits, and all fruits are sweet. Therefore, it is safe to assume that all apples are sweet."

**User:** "If birds can fly. Penguins are birds. Can penguins fly? Please explain your answer in detail."

**Model:** "No, penguins cannot fly. Penguins are birds, but they are not capable of flight like other birds. They have wings and can glide for short distances, but they cannot take off or fly long distances like other birds."

**User:** "The day before two days after the day before tomorrow is Saturday. What day is it today? Please explain your answer in detail."

**Model:** "Today is Friday. Two days after tomorrow is Sunday. Tomorrow is Saturday."

**User:** "If five cats can catch five mice in five minutes, how long will it take one cat to catch one mouse? Please explain your answer in detail."

**Model:** "If five cats can catch five mice in five minutes, it means that each cat can catch one mouse in one minute. To find out how long it will take one cat to catch one mouse, we can use the concept of proportionality. Let's assume that it takes x minutes for a cat to catch a mouse. Then, the number of mice caught by a cat in one minute is equal to the number of cats multiplied by the number of mice caught by each cat: x = 5 * 1 = 5. So, it will take 5 minutes for one cat to catch one mouse."

---

**User:** "Summarize the following paragraph."

**User provides:** \<The Abstract of this paper\>

**Model:** "The paper presents a novel architecture, Receptance Weighted Key Value (RWKV), that combines the efficient parallelizable training of Transformers with the efficient inference of RNNs. The model is able to scale to tens of billions of parameters and exhibits linear computational complexity during training and inference, making it a promising alternative to Transformers for sequence processing tasks."

**User:** "Please further summarize it in one sentence."

**Model:** "The researchers have developed a new architecture that combines the efficient parallelizable training of Transformers with the efficient inference of RNNs, which allows for linear scaling in memory and computational requirements."
