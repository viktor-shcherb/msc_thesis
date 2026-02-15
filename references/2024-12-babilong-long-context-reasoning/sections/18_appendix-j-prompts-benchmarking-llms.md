# Appendix J: Prompts Used to Benchmark Large Language Models [p. 22-25]

Each prompt starts with the description of the task followed by several examples inside the <example> </example> tags. The next section inside <context> </context> tags contains an instance of the task. We additionally duplicate the question with the QUESTION mark, in order for the model recognize the question in the large input prompts. The last sentences specify the required response format. [p. 22]

## QA1 task [p. 23]

```
I will give you context with the facts about positions of
different persons hidden in some random text and a question.
You need to answer the question based only on the information
from the facts. If a person was in different locations, use the
latest location to answer the question.
<example>
Charlie went to the hallway. Judith come back to the kitchen.
Charlie travelled to balcony. Where is Charlie?
Answer: The most recent location of Charlie is balcony.
</example>

<example>
Alan moved to the garage. Charlie went to the beach. Alan went
to the shop. Rouse travelled to balcony. Where is Alan?
Answer: The most recent location of Alan is shop.
</example>

<context>
{QA1 query with noise}
</context>

QUESTION: {QA1 question}
```

## QA2 task [p. 24]

```
I give you context with the facts about locations and actions
of different persons hidden in some random text and a question.
You need to answer the question based only on the information
from the facts.
If a person got an item in the first location and travelled to
the second location the item is also in the second location.
If a person dropped an item in the first location and moved to
the second location the item remains in the first location.
<example>
Charlie went to the kitchen. Charlie got a bottle. Charlie
moved to the balcony. Where is the bottle?
Answer: The bottle is in the balcony.
</example>

<example>
Alan moved to the garage. Alan got a screw driver. Alan moved
to the kitchen. Where is the screw driver?
Answer: The screw driver is in the kitchen.
</example>

<context>
{QA2 query with noise}
</context>

QUESTION: {QA2 question}
```

## QA3 task [p. 24]

```
I give you context with the facts about locations and actions
of different persons hidden in some random text and a question.
You need to answer the question based only on the information
from the facts.
If a person got an item in the first location and travelled to
the second location the item is also in the second location.
If a person dropped an item in the first location and moved to
the second location the item remains in the first location
<example>
John journeyed to the bedroom.Mary grabbed the apple. Mary went
back to the bathroom. Daniel journeyed to the bedroom. Daniel
moved to the garden. Mary travelled to the kitchen. Where was
the apple before the kitchen?
Answer: Before the kitchen the apple was in the bathroom.
</example>

<example>
John went back to the bedroom. John went back to the garden.
John went back to the kitchen. Sandra took the football. Sandra
travelled to the garden. Sandra journeyed to the bedroom. Where
was the football before the bedroom?
Answer: Before the kitchen the football was in the garden.
</example>

<context>
{QA3 query with noise}
</context>

QUESTION: {QA3 question}
```

## QA4 task [p. 25]

```
I will give you context with the facts about different people,
their location and actions, hidden in some random text and a
question.
You need to answer the question based only on the information
from the facts.
<example>
The hallway is south of the kitchen. The bedroom is north of
the kitchen. What is the kitchen south of?
Answer: bedroom
</example>

<example>
The garden is west of the bedroom. The bedroom is west of the
kitchen. What is west of the bedroom?
Answer: garden
</example>

<context>
{QA4 query with noise}
</context>

QUESTION: {QA4 question}
```

## QA5 task [p. 25]

```
I will give you context with the facts about locations and
their relations hidden in some random text and a question. You
need to answer the question based only on the information from
the facts.
<example>
Mary picked up the apple there. Mary gave the apple to Fred.
Mary moved to the bedroom. Bill took the milk there. Who did
Mary give the apple to?
Answer: Fred
</example>

<example>
l Jeff took the football there. Jeff passed the football to
Fred. Jeff got the milk there. Bill travelled to the bedroom.
Who gave the football?
Answer: Jeff
</example>

<example>
Fred picked up the apple there. Fred handed the apple to Bill.
Bill journeyed to the bedroom. Jeff went back to the garden.
What did Fred give to Bill?
Answer: apple
</example>

<context>
{QA5 query with noise}
</context>

QUESTION: {QA5 question}
```
