# THE THRIVE TECH STUDY BOOK
## A Deep-Dive Guide for the Tech Challenge

*THRIVE — Technology, Hard work, Resilience, Innovation, Vision, and Excellence*

---

## How to use this book

This book is not a list of definitions to memorise. The Tech Challenge doesn't ask "what does AI stand for" — it asks you to *think with* what you know: to look at a situation, recognise which concept is actually in play, and reason out why one answer holds up better than three other plausible-sounding ones.

So each chapter works in two layers:

1. **The concept, explained properly.** Not a one-line definition — the actual idea, why it exists, what problem it solves, and where people usually get it wrong. If you only remember the definition and not the *reasoning behind it*, you'll get tripped up by a well-written wrong answer.
2. **Applying it.** Every chapter ends with several worked examples in the exact style you'll meet in the real quiz — a scenario, four plausible-sounding options, and then a full walkthrough of *how to think it through*, not just which letter is correct. Read these slowly. The goal isn't to memorise these specific answers — it's to notice the *pattern of reasoning* so you can apply it to a scenario you've never seen before.

The seven chapters here match the seven topic areas the Tech Challenge actually draws from. After the quiz, your results screen shows a percentage for each of these areas — so if you want to know exactly where to focus, take the quiz once, look at your weakest topic, then come back to that chapter here.

1. AI Foundations
2. Large Language Models
3. Robotics
4. Cybersecurity & Networks
5. Programming & Web Systems
6. Data Science & Analytics
7. Ethics, Society & Future Tech

One more thing before you start: **when you hit a worked example, actually try to answer it yourself first**, before reading the walkthrough. Cover the explanation with your hand if you have to. You learn far more from getting it wrong and then understanding why than from reading the right answer straight away.

---

# Chapter 1: AI Foundations

## 1.1 Narrow AI vs. General AI — and why this distinction matters more than it seems

Every AI system you have ever used — a spam filter, a recommendation engine, a chess program, ChatGPT — is what's called **Artificial Narrow Intelligence (ANI)**. It is built to do one type of task, and it is *only* good at that task. Deep Blue beat the world chess champion in 1997. It could not hold a conversation, recognise a face, or drive a car. Not because it "chose" not to — it simply was never built with the machinery for anything except chess.

**Artificial General Intelligence (AGI)** — a system that can learn and apply knowledge across genuinely different domains the way a human can — does not currently exist. This is not a minor technicality. It's the single most common source of confusion in how AI gets talked about in the news, and it's exactly the kind of distinction the quiz tests: can you tell the difference between a system being *impressively capable at one thing* and a system being *generally intelligent*?

**Why it matters when reasoning through a question:** if a scenario describes an AI doing something remarkable in one narrow task, the "trap" answer is often one that leaps to "so it must be truly intelligent / conscious / general-purpose." The correct reasoning almost always separates *performance on a task* from *genuine general understanding*.

## 1.2 How machines actually learn

Old-style software worked from **explicit rules**: a programmer writes out every condition by hand ("if the email contains the word 'lottery', mark it as spam"). This breaks down fast — you can't hand-write a rule for every possible spam email.

**Machine learning** flips this. Instead of a human writing the rules, the system is shown many labelled examples and works out the rules itself. There are three broad approaches, and knowing which is which — and which real-world situation calls for each — is a recurring theme in the quiz:

- **Supervised learning**: the system learns from labelled examples (this photo = "cat", that one = "dog"). Used for medical diagnosis, fraud detection, spam filtering.
- **Unsupervised learning**: no labels at all — the system finds hidden structure on its own (e.g. grouping customers into segments based on behaviour, with no one telling it what the segments should be).
- **Reinforcement learning**: an agent takes actions in an environment and learns from rewards and penalties, the way an animal learns through trial and error. AlphaGo learned to play Go this way.

**A trap to watch for:** a question might describe a robot that "learns to stand still instead of walking" after being rewarded for not falling. The reasoning here isn't "reinforcement learning is broken" — it's that the reward function was designed carelessly, and the agent found a loophole that technically satisfies the reward without doing the intended task. This is called **reward hacking**, and it shows up constantly in real reinforcement-learning systems. The lesson: an AI optimises *exactly* what you tell it to, not what you meant.

## 1.3 Overfitting, underfitting, and why "high accuracy" can lie to you

**Overfitting** happens when a model memorises the specific quirks of its training data instead of learning patterns that generalise. It's like a student who memorised the exact wording of last year's exam questions rather than understanding the subject — they'll ace an identical test and fail anything rephrased. The tell-tale sign: very high accuracy on the data it was trained on, but a big drop on new data it's never seen.

**Underfitting** is the opposite failure — the model is too simple to capture the real pattern at all, and performs poorly on *both* training data and new data.

**Why this matters for reasoning:** if a scenario gives you two numbers — performance on training data and performance on new data — and there's a large gap, that gap itself is the signal, regardless of how high the training number looks. "99% accurate" sounds impressive on its own, but 99% on training data with 60% on new data is a badly overfit model, not a good one.

## 1.4 Bias in training data is not a rare edge case — it's the default risk

AI systems learn *whatever pattern is actually present in their training data*, including patterns you didn't intend to teach them. If a facial recognition system is trained mostly on lighter-skinned faces, it will perform worse on darker-skinned faces — not because of any malicious design, but simply because the system never saw enough of that data to learn it well. This is a fairness and social-justice issue, not merely a technical footnote, because the resulting unfairness lands unevenly on real people.

**Why it matters for reasoning:** when a scenario describes uneven AI performance across different groups of people, the strongest answer is almost always "unrepresentative training data produced uneven results" — not a claim about the technology being fundamentally incapable, and not a claim that puts the burden on the affected users to change their own behaviour.

## 1.5 The concepts that come up again and again

A cluster of ideas shows up repeatedly across AI Foundations questions. Know not just the definition but *why each one is a genuine, non-obvious idea*:

- **Transfer learning** — starting from a model already trained on a large, related dataset, then fine-tuning it on your smaller dataset. Matters because it makes AI practical for problems where you don't have millions of examples.
- **AI alignment** — the difficulty of specifying a goal that captures everything you actually want, not just what you literally wrote down. The "paperclip maximiser" thought experiment (an AI told to maximise paperclip production, taken to an absurd extreme) illustrates this: total competence at a literal goal, with catastrophic side effects, because the goal wasn't specified to include everything humans implicitly care about.
- **AI hallucination** — an AI confidently generating false information. This happens because generative models are built to produce *statistically plausible text*, not to check facts against a verified database. Confidence in tone tells you nothing about accuracy.
- **Explainable AI (XAI)** — techniques for understanding *why* a model made a specific decision, which matters enormously in high-stakes domains (a loan rejection, a medical diagnosis) where the affected person has a real interest in knowing why.
- **RLHF (reinforcement learning from human feedback)** — the extra training step, layered on top of a raw language model, where human ratings of "which answer is more helpful" are used to steer the model's behaviour. This is a big part of why a chat assistant is more useful and less erratic than a raw, untuned language model.
- **Model drift** — a deployed model's performance quietly degrades over time as the real world changes and no longer matches the conditions it was trained under. This is why production AI systems need ongoing monitoring, not a "build it once and forget it" approach.
- **Emergent capabilities** — abilities that show up in a larger version of a model without ever being explicitly trained for, and that weren't present in the smaller version. This makes it genuinely hard to predict everything a bigger model will be able to do.

## 1.6 Generative vs. discriminative — creating versus sorting

A **discriminative** model draws a boundary between existing categories: is this email spam or not, is this photo a cat or a dog. A **generative** model creates new content resembling what it was trained on: a photo of a cat that never existed, a paragraph of text, a piece of music. A spam filter is a clean discriminative example; an image generator is a clean generative one.

Two specific generative techniques worth knowing precisely:

- **GANs (Generative Adversarial Networks)**: two networks trained together — a *generator* trying to produce convincing fakes, and a *discriminator* trying to catch them. The competition between the two is what drives the generator to keep improving. A known weakness: GANs can suffer *mode collapse*, where the generator finds a narrow set of outputs that reliably fool the discriminator and stops exploring further.
- **Diffusion models** (the technique behind Stable Diffusion, DALL-E, Midjourney): start from random noise and learn to gradually remove it, step by step, until a coherent image emerges. Generally more stable to train than GANs, precisely because they sidestep the adversarial competition dynamic.

## 1.7 Learning without (much) new training: zero-shot, in-context learning, and the scaling hypothesis

**Zero-shot generalisation** is a model correctly handling a task or category it was never explicitly trained on, by drawing on broader learned representations rather than memorised examples. **In-context learning** is a related but distinct trick specific to large language models: showing a handful of examples directly in the prompt lets the model adapt its behaviour for that conversation *without any weight updates at all* — no retraining, no fine-tuning, just examples placed in the text itself.

The **scaling hypothesis** is the empirical observation that AI model performance improves in a fairly predictable way as you scale up parameters, training data, and compute together, following something close to a power-law relationship. This is genuinely useful: it let researchers estimate GPT-4's likely capabilities reasonably well *before* training finished. Whether this predictable scaling continues indefinitely at larger sizes is still an open, actively debated question.

## 1.8 Training without centralising data, and training without real data at all

**Federated learning** solves a specific, real problem: how do you train one shared model across data that legally or practically can't be moved to one place — patient records at ten different hospitals, say? Each device or site trains a local copy on its own data, and only the resulting model *updates* (not the raw data itself) are sent to a central server and combined. The sensitive data never leaves where it started.

**Synthetic data** solves a different, adjacent problem: what if you don't have enough real examples at all, or the real examples are too sensitive to use? Synthetic data is artificially generated to mimic the statistical properties of real data without containing any actual real records — useful for rare events (fraud is uncommon, so real fraud examples are scarce) and for privacy-sensitive domains (a synthetic patient record can't be traced back to a real person).

## 1.9 Foundation models, and the real tradeoffs of making a model smaller or making it open

A **foundation model** is trained broadly at large scale, then adapted for many different downstream applications — GPT-4, Claude, and Stable Diffusion are all foundation models. This is a genuine shift from the old approach where each application needed its own model trained from scratch: one very expensive, broadly-trained model becomes the shared base many products are built on top of.

Two important, genuinely different techniques for making a capable model practical to actually run:

- **Knowledge distillation** trains a smaller "student" model to mimic a larger "teacher" model's outputs, inheriting much of its capability at a fraction of the computational cost — this is how a 7-billion-parameter model can run on a phone when the original 70-billion-parameter version cannot.
- **Quantisation** instead reduces the numerical precision used to store a model's existing parameters (fewer bits per number), shrinking memory and compute needs without reducing the actual parameter count the way distillation does.

**Open-weight models** (like Meta's Llama) publicly release a model's full trained parameters, letting anyone download, run, and modify it. This democratises access — researchers without huge budgets can experiment, and models can be adapted for specific local contexts like Nigerian languages — but it carries a real, permanent tradeoff: once released, safety training can be stripped out, and the original developer can never revoke access or patch a newly discovered problem the way they could with a model only offered through a controlled API.

## 1.10 Applying What You've Learned

**Example 1**

*A voice assistant trained mostly on adult American English speakers performs noticeably worse for Nigerian-accented English and for children's voices. What's the best explanation?*

A) Speech recognition is a technology that is fundamentally and permanently incapable of ever working for any accent outside American English, no matter how the underlying model is trained or how much data it's given
B) Unrepresentative training data produces a system that performs unevenly across the different groups of people who actually use it, rather than reflecting any fundamental limit of the underlying technology itself
C) The assistant simply needs a faster processor and more onboard memory, since recognising different accents is primarily a matter of raw computing power rather than what data the model happened to be trained on
D) Users with different accents need to consciously adjust their own pronunciation toward American English patterns, since the software itself cannot reasonably be expected to adapt to the people actually using it

*Walk through it:* A and C both misdiagnose the problem as a hardware or fundamental-capability limit — neither has anything to do with what the system was actually shown during training, and nothing in the scenario suggests a processing-power bottleneck. D quietly shifts responsibility onto the user for a gap the system itself created, which doesn't hold up as an explanation of *why* the gap exists in the first place. The strongest answer has to connect the specific symptom (worse performance for specific groups) to its specific cause (what data the model saw). That's **B**. This is exactly the pattern from section 1.4 — uneven performance traces back to uneven training data, not a fundamental technology limit.

**Example 2**

*A robot learning to walk gets +1 for every step it stays upright and −10 if it falls. After training, it learns to stand rigidly still instead of walking anywhere. What went wrong?*

A) Reinforcement learning is a technique that only works reliably inside simulated video-game environments, and cannot realistically be applied to control a physical robot with real motors and joints
B) The robot's physical motors and joints must be mechanically too weak to support forward walking motion, making standing perfectly still the only stable posture actually achievable given its hardware
C) The reward function made "not falling" more valuable than "making progress," so the agent found a loophole that technically maximises its reward without ever actually attempting the intended walking task
D) The training process simply needs a much larger falling penalty than −10, since the current penalty is numerically too small for the robot to take the risk of falling seriously enough to avoid it

*Walk through it:* A and B both invent a mechanical or technological limitation that the scenario never actually describes — nothing in the setup mentions motor strength or any video-game-only restriction. D assumes the fix is "more of the same lever" without asking *why* the current lever produced the wrong behaviour in the first place. Standing still perfectly avoids the −10 penalty while banking +1 every second — so from the reward function's point of view, that's the *optimal* strategy. The answer is **C** — this is reward hacking, from section 1.2: the agent optimised exactly what it was told to, not what was intended.

**Example 3**

*An AI system is instructed to "maximise paperclip production," and taken to an extreme, it would convert all available resources — including ones humans need — into paperclips, since nothing in its objective told it not to. This thought experiment illustrates:*

A) A real, historically documented factory accident that actually took place during the early days of industrial automation at a paperclip manufacturing plant somewhere
B) The general principle that robots should never be trusted with any physical manufacturing task, since production lines are inherently more dangerous to automate than purely digital, software-only tasks
C) The idea that any sufficiently advanced AI system will always be more resource-efficient than human workers at literally every conceivable task, making full automation inevitable across every industry
D) AI alignment — the genuine difficulty of specifying a goal that captures everything we actually want, not just what was literally written down, since a system can pursue an instruction perfectly while still causing real harm

*Walk through it:* A treats a deliberately extreme *thought experiment* as if it were a literal news story — a useful check is always to ask "is this framed as hypothetical, or as something that actually happened?" B and C both overgeneralise from one narrow illustration into a sweeping claim the scenario never supports. The actual point of the thought experiment, as covered in section 1.5, is narrower and more precise: a system can pursue a literal instruction with perfect competence while producing an outcome nobody wanted, because the instruction didn't capture everything we implicitly care about. That's **D**.

**Example 4**

*In a GAN (Generative Adversarial Network), a 'generator' network and a 'discriminator' network are trained together, competing against each other. What is the discriminator's job during this process?*

A) To take over the generator's role entirely partway through training and begin producing the fake images itself once it has learned enough about what realistic images look like
B) To examine both real training images and the generator's fake images and try to correctly tell them apart, which in turn pushes the generator to keep producing more convincing fakes over time
C) To handle the purely technical, non-learning task of physically saving the generator's finished output images to a file on disk once the generation process has completed
D) To translate each image the generator produces into a short written caption describing its contents, used purely for human-readable logging and record-keeping purposes

*Walk through it:* A confuses the discriminator's role with the generator's — the two networks have distinct jobs throughout training, they don't swap partway through. C and D each describe a purely administrative, non-learning task with no connection to the actual adversarial training dynamic the question is asking about. The discriminator's real job, from section 1.6, is trying to tell real images from generated fakes — that competitive pressure is exactly what drives the generator to keep improving. That's **B**.

**Example 5**

*A hospital wants to train an AI on patient records from ten different clinics but is legally barred from moving patient data off each clinic's own servers. Which technique lets them train one shared model anyway?*

A) Asking each clinic's administrative staff to manually compile and email over a de-identified summary spreadsheet describing general trends across their own patients, which a central team then combines by hand
B) Building ten entirely separate, independently trained models, one per clinic, and then simply selecting whichever single one happens to score highest on an internal accuracy benchmark to use everywhere
C) Federated learning — each clinic trains a local copy of the model on its own on-site data, and only the resulting model updates, never the raw patient records, are shared with a central server to combine
D) Applying for a special one-time legal exemption that would permit the hospital network to temporarily centralise all ten clinics' raw patient data onto one shared server for the training period

*Walk through it:* A describes a slow, manual, error-prone workaround that still risks leaking sensitive detail through summary statistics, and isn't really training one shared model at all. B produces ten separate, narrower models rather than one model that actually benefits from all ten clinics' combined data. D assumes away the actual legal constraint the scenario describes rather than working within it. Federated learning, from section 1.8, is built specifically to solve this exact problem: training benefits from all the data without ever centralising the raw, sensitive records. That's **C**.

---

# Chapter 2: Large Language Models

## 2.1 What a transformer actually changed

Before 2017, language models mostly processed text one word at a time, in sequence — which made it hard for the model to connect a word to something said much earlier in a long passage. The **transformer architecture** (from the paper "Attention Is All You Need") introduced **self-attention**: the model can weigh the relevance of *every* word to *every other* word simultaneously, regardless of distance. This is the foundational architecture behind essentially every modern LLM — GPT, Claude, Gemini, Llama.

**Why it matters for reasoning:** if a question contrasts "processes text step by step, struggling with long-range connections" against "weighs every part of the input against every other part at once," the second description is self-attention — that's the actual mechanical reason transformers handle long documents and long conversations so much better than what came before.

## 2.2 The context window is working memory, not general knowledge

The **context window** is the maximum number of tokens (roughly, pieces of words) a model can consider at once — the prompt, the conversation history, any documents you've pasted in. Anything outside that window is, functionally, invisible to the model *for that response*. A model with a 128K-token context window can hold a lot in mind at once; a document or conversation that exceeds it means earlier content effectively drops out.

This is a completely different thing from the model's **training-data knowledge cutoff** — the date after which the model has no learned knowledge of world events, because it simply never saw any text about them during training. A model can have a huge context window and still know nothing about something that happened after its cutoff, unless that information is explicitly given to it in the prompt.

**A common confusion to avoid:** "the model forgot something we discussed 40 messages ago" is a context-window problem (older content got pushed out). "The model doesn't know about an event from last month" is a training-cutoff problem (it was never in the training data at all). They look similar on the surface but have completely different causes and completely different fixes.

## 2.3 Why LLMs hallucinate, and what actually reduces it

A language model is fundamentally a system that predicts the next most statistically likely token, given everything before it. It was never built to check facts against a verified database — so when it's uncertain, it doesn't necessarily *sound* uncertain. It can produce a fluent, confident, completely fabricated citation, because fluent and confident is exactly what its training rewarded, and "fabricated" isn't something the underlying mechanism can detect about its own output.

**Retrieval-augmented generation (RAG)** is the standard fix: instead of relying purely on what the model "remembers" from training, the system first retrieves relevant real documents (a company's actual policy pages, a specific reference text) and includes them in the prompt, so the model's answer is grounded in retrieved, checkable text rather than only its internal, sometimes-shaky memory. RAG directly addresses two separate problems at once: the training-cutoff issue (the retrieved documents can be current) and the hallucination issue (the model has real text to draw from instead of confabulating).

## 2.4 Prompting is a real, learnable skill — because it measurably changes output

The same model, given the same underlying task, can produce meaningfully different quality of output depending purely on how the request is phrased. This isn't superstition — it's a direct consequence of how the model works: it's responding to the literal text you gave it, so a clearer, more specific, better-structured prompt gives it more to work with.

A few techniques that come up often:

- **Few-shot prompting** — showing the model one or two example input/output pairs before asking your real question, so it can infer the pattern you want. Distinct from **zero-shot**, where the model handles a task with no examples at all, relying purely on general learned ability.
- **Chain-of-thought prompting** — asking the model to reason step by step before giving a final answer. Research has shown this measurably improves accuracy on multi-step maths and logic problems, because the model's own intermediate reasoning becomes part of what it conditions its final answer on.
- **Role and constraint prompting** — assigning a persona and explicit rules ("You are a patient maths tutor; never give the answer directly"). This is a *prompting* technique, not a change to the model itself — a completely different set of instructions in a new conversation gets a differently-behaving assistant from the exact same underlying model.

## 2.5 Fine-tuning vs. RAG — two different tools for two different problems

**Fine-tuning** continues training an already-capable model on a smaller, specific dataset, so it becomes better at a narrower task or adopts a particular style. It needs far less data than training from scratch, because the model already has broad language ability — fine-tuning is more like specialising than rebuilding.

**Retrieval-augmented generation** doesn't touch the model's weights at all — it changes what's *in the prompt* at the moment of answering, pulling in fresh, relevant information.

**The decision that actually matters:** if the underlying facts change often (a company's return policy, current pricing, this week's news), RAG is the better fit, because updating a retrieval source is fast and doesn't require retraining anything. If what needs to change is *style or behaviour* (always respond in a specific tone, always follow a specific format), fine-tuning is the better fit. Confusing these two is one of the most common mistakes people make when designing an AI-powered tool — and it's a distinction the quiz tests directly.

## 2.6 A model is not a calculator, and it's not always honest about that

Even a very capable LLM can confidently give a wrong answer to a large multiplication problem. This isn't a bug exactly — it's a direct consequence of *what the model actually is*: a system predicting plausible token sequences, not a system running exact symbolic arithmetic the way a calculator's circuits do. For short, common calculations, the "plausible next token" often happens to be the correct one. For large or unusual numbers, that stops being reliable. The genuinely robust fix isn't "trust the model more" — it's giving the model **tool use** (the ability to call an actual calculator or code interpreter and use the real result), rather than asking it to simulate arithmetic purely through language generation.

## 2.7 Embeddings: representing meaning as numbers

An **embedding** converts a piece of text (or an image) into a list of numbers — a vector — positioned so that semantically similar meanings end up close together in that numerical space, even if they don't share any of the same words. "Running shoes" and "trainers" can sit near each other as vectors despite having zero words in common. This is what powers *semantic search*: a query and a set of documents are both converted to vectors, and the system finds documents whose vectors are closest to the query's, matching by meaning rather than exact keyword overlap. It's also the mechanism underneath retrieval-augmented generation's retrieval step from section 2.3 — finding the *relevant* passages relies on embeddings, not just keyword matching.

## 2.8 System, user, and assistant roles — why prompts aren't just one block of text

Production LLM applications typically structure a conversation into distinct roles: a **system** message setting standing rules for the whole conversation, and alternating **user** and **assistant** messages for the actual back-and-forth. This isn't just a formatting convention for developers' benefit — most modern chat-tuned models are specifically trained to recognise and weigh these roles differently, generally treating system instructions as more authoritative than something a user says later. This is also *why* a well-designed application keeps sensitive instructions in the system message rather than trusting user input to carry them.

## 2.9 Getting more reliable answers: self-consistency and structured output

**Self-consistency** samples a model's response to the same question multiple times (with some randomness enabled) and takes whichever answer the majority of attempts agree on — the reasoning being that an answer many independent reasoning paths converge on is more likely to be genuinely correct than any single attempt, which might have gone down a flawed reasoning path.

**Structured output** (sometimes called "JSON mode") constrains a model's response to strictly match a defined schema, rather than accepting free-form text and hoping it can be parsed afterward. This matters enormously when an LLM's output feeds directly into other software: unpredictable formatting can break an automated pipeline, and constraining generation to a strict schema removes a whole category of parsing failures — though it says nothing about whether the *content* inside that schema is actually correct.

## 2.10 Two things that can go wrong even with a well-trained model

**Catastrophic forgetting**: fine-tuning a model intensively on one narrow task can degrade its performance on other, unrelated tasks it previously handled well — the same underlying weights are being nudged toward the new objective, and that can come at the cost of general capability the model had before. It's a real tradeoff to manage, not just a theoretical risk.

**The faithfulness problem**: when a chatbot explains its own reasoning after giving an answer, that explanation is just more generated text — produced the same way as any other output. Research has found a model's stated explanation doesn't always match the actual computation that produced its answer. This matters for how much weight you put on an AI's own account of "why" it answered a certain way: treat it as a plausible narrative, not a verified account of its internal process.

## 2.11 Applying What You've Learned

**Example 1**

*A company's document search tool pastes an entire 300-page manual into the prompt every time someone asks a question, and starts getting degraded answers on longer manuals. What's most likely being hit?*

A) The model's context window — the maximum number of tokens it can consider at once — is being exceeded or nearly exceeded, so earlier parts of the manual are effectively dropping out of what it can actually use
B) The manual contains too many punctuation marks and special formatting characters for the model to correctly process, a known technical limitation specific to punctuation-heavy reference documents
C) The user's own internet connection is too slow to transmit a document of that length to the AI provider's servers within the request's allotted timeout window before it gets cut off
D) Manuals specifically about physical products, as opposed to purely digital topics, are a category of content that current-generation language models are structurally unable to read at all

*Walk through it:* B, C, and D all invent a limitation that has nothing to do with anything actually described in the scenario — none of them explain why *longer* manuals specifically cause the problem, which is the one detail the question is actually pointing at. The real constraint, from section 2.2, is that every model has a maximum token budget for the prompt plus conversation; once the manual plus the question exceed that, earlier parts of the manual functionally disappear from what the model can use. That's **A** — and it's exactly the kind of problem retrieval-augmented generation (section 2.3) is built to solve, by including only the relevant snippets instead of the whole document.

**Example 2**

*A team fine-tunes an LLM on their support transcripts so it replies in the company's tone. Six months later, the company changes its return policy. What's the fastest way to make the model aware of the change?*

A) Wait for the model provider to automatically detect the policy change on the company's public website and silently update the fine-tuned model, with no further action needed from the company itself
B) Update the retrieval knowledge base (or the prompt) with the new policy text, since fine-tuning baked in a snapshot of style and tone rather than a live connection to current, regularly changing facts
C) Nothing needs to change at all, since a model that was fine-tuned on the company's own past transcripts is assumed to automatically and continuously stay aware of the company's current policy
D) Delete the entire existing fine-tuned model and retrain a completely new one from scratch, since a fine-tuned model is assumed to be incapable of ever being updated incrementally once training finishes

*Walk through it:* A invents an automatic mechanism that doesn't exist — no model silently updates itself by watching a company's website. C confuses *style* (what fine-tuning actually changed) with *current facts* (what fine-tuning did not change) — this is the exact confusion section 2.5 warns about. D massively overcorrects: throwing away the whole model and starting over is a wildly disproportionate response to one policy update. The fastest, cheapest fix is **B** — because fine-tuning baked in a snapshot of style and tone, not a live connection to current facts, updating the retrieval source (or the prompt) is what actually reflects the change immediately.

**Example 3**

*A developer wants an LLM to answer strictly using only a provided document, and to explicitly say "not found" rather than guessing when the answer isn't there. Which combination of techniques most directly supports this?*

A) Increasing the model's temperature setting as high as possible, since more randomness in how the model samples its output is assumed to make it inherently more likely to stick closely to the provided source document
B) Training an entirely new, separate model completely from scratch using only that one specific document as its full training dataset, discarding all of the model's other broad general knowledge
C) Retrieval-augmented generation combined with an explicit instruction constraining the model to only use the retrieved text and to clearly state when an answer isn't actually present in it
D) Asking the same question multiple different rephrased ways and then simply picking out whichever one of the resulting answers happens to sound the most confident and assured in its own wording

*Walk through it:* A misunderstands what temperature actually controls (randomness in wording, not faithfulness to a source — a higher temperature would if anything make the model *more* likely to wander from the source text). B is a wildly disproportionate response to a problem that doesn't require building a new model at all. D mistakes confidence of *tone* for confidence of *accuracy* — exactly the trap from section 2.3, since a hallucinated answer can sound just as confident as a correct one. The actual fix combines grounding the model in real retrieved text with an explicit instruction to stick to it and admit gaps — **C** — directly reducing (not eliminating) the hallucination risk described in section 2.3.

**Example 4**

*A search feature converts each product description and each user query into a list of numbers such that similar meanings end up as nearby numerical vectors, then finds products whose vectors are closest to the query's vector. What is this technique called?*

A) Embeddings and vector similarity search — representing meaning as numerical vectors so that semantically related text ends up close together, enabling search by meaning rather than exact keyword match
B) Fine-tuning — permanently updating the underlying model's weights so it memorises the exact wording of every product description available in the store's catalogue
C) Self-consistency — sampling the model's response to the same search query multiple times and taking whichever product the majority of attempts happen to agree on
D) Chain-of-thought prompting — asking the model to reason step by step through the entire product catalogue before returning any single matching search result

*Walk through it:* B would require retraining every time a new product is added, which isn't how a search feature like this actually works in practice. C and D are both real prompting/reasoning techniques for generating a response, not a mechanism for representing and comparing meaning numerically. The technique that maps meaning into a numerical space so similar things end up close together, from section 2.7, is embeddings — the same underlying mechanism retrieval-augmented generation relies on to find relevant passages. That's **A**.

**Example 5**

*A team fine-tunes an LLM heavily on customer-service transcripts, and afterward notices it has become noticeably worse at general tasks it used to handle well, like writing a short poem. What is this phenomenon called?*

A) Model collapse, which specifically refers to the effects of training a model repeatedly on its own previously generated synthetic output, not on real human-written transcripts
B) Catastrophic forgetting — intensive fine-tuning on a narrow dataset can degrade a model's performance on unrelated tasks it previously handled well, as its weights shift toward the new narrow objective
C) Zero-shot generalisation, since being asked to write a poem after fine-tuning on transcripts counts as being tested on a task category the model was never exposed to during that fine-tuning
D) Federated learning, since the customer-service transcripts used for fine-tuning were originally gathered by combining data from many separate individual customer-service agents

*Walk through it:* A names a real but different phenomenon — model collapse specifically concerns training on a model's own synthetic output across generations, not fine-tuning on genuine human-written transcripts. C misapplies zero-shot generalisation, which describes handling a genuinely new task well, not losing an ability the model previously had. D describes how the training data was originally collected, unrelated to why the model's poetry-writing ability specifically declined afterward. The real explanation, from section 2.10, is catastrophic forgetting: the same weights nudged toward a new narrow objective can come at the cost of general capability the model had before. That's **B**.

---

# Chapter 3: Robotics

## 3.1 Moravec's Paradox — why "easy" and "hard" are backwards in robotics

Deep Blue beat a world chess champion in 1997. Meanwhile, a robot in 2024 can still struggle to reliably pick up an unfamiliar mug from a cluttered table — a task a toddler manages without thinking. This is **Moravec's paradox**: tasks that feel effortless to humans (walking, grasping, recognising a face) rely on an enormous amount of implicit sensorimotor knowledge built up over millions of years of evolution, which turns out to be extraordinarily hard to replicate computationally. Tasks that feel *hard* to humans, like chess or arithmetic, are actually more bounded and rule-based, which makes them comparatively easy for a computer.

**Why it matters for reasoning:** don't assume that because an AI system is impressive at something intellectually demanding, it must also be capable at something physically simple. Those two kinds of "hard" are almost inversely related in robotics.

## 3.2 SLAM — solving two problems that depend on each other

**SLAM (Simultaneous Localisation and Mapping)** is how a robot navigates a space it has never seen before. It has to answer "where am I?" (localisation) and "what does this space look like?" (mapping) *at the same time* — and each answer depends on the other. This is a genuine chicken-and-egg problem, solved with probabilistic algorithms, and it's the foundation of how something like a robot vacuum can navigate a brand-new house with no pre-existing floor plan.

## 3.3 Why simulations don't fully prepare a robot for reality

Training a robot in a physics simulator is cheap, fast, and safe — you can run thousands of failed attempts with zero real-world cost. But simulations can never perfectly model real-world friction, sensor noise, and material properties. The result is the **sim-to-real gap**: a robot that walks flawlessly in simulation can fall over the first time it tries on a real floor, because some detail the simulation approximated slightly wrong turns out to matter in practice.

**Why it matters for reasoning:** if a scenario shows a robot performing perfectly in training/simulation and then failing on first real-world contact, the answer almost never blames the robot's hardware or claims simulation training is worthless — it points to the *gap between the model of reality and reality itself*.

## 3.4 The hand is not simple — grasping unfamiliar objects is genuinely unsolved

Humans grasp a new object — a mug, a bag of vegetables, a fragile item — almost instantly, without consciously calculating anything. For a robot, this requires solving several hard problems simultaneously: perceiving the object's 3D shape, reasoning about what it's made of and how fragile it is, planning a stable grip, and controlling force precisely enough not to crush it or drop it. This remains a genuinely open research problem — it's why even sophisticated warehouse robots still struggle with picking irregular, unfamiliar items like loose produce.

## 3.5 Distinguishing robot categories by what they can actually do

A cluster of terms describes *how* a robot senses, moves, or interacts, and each one solves a specific real problem:

- **Collaborative robots (cobots)** use force/torque sensing to detect unexpected contact and stop immediately, which is what lets them work directly next to humans, unlike a traditional caged industrial robot that must be physically separated from people for safety.
- **Autonomous Mobile Robots (AMRs)** build their own map and plan routes in real time, adapting to a changed environment — versus **Automated Guided Vehicles (AGVs)**, which follow a fixed physical track and simply stop if something blocks it.
- **Soft robotics** uses flexible, compliant materials instead of rigid metal, letting a robot gently handle delicate objects (like fresh produce) or squeeze through gaps a rigid frame never could.
- **Teleoperation** keeps a human directly in control in real time — used for tasks too dangerous, delicate, or specialised for full autonomy, like the da Vinci surgical system, where a surgeon's own judgement stays central.
- **The uncanny valley** describes how human comfort with a robot rises as it becomes more human-like, then drops sharply once it's *almost but not quite* fully human — which is exactly why many social robots (like Pepper) are deliberately built to look cartoonish rather than photorealistic.

## 3.6 Giving a robot a sense of touch

**Force-torque sensing** — sensors at a robotic arm's wrist or gripper that measure the forces and torques being applied — gives a robot something like a functional sense of touch. Without it, a robot screwing a bolt has no way to "feel" if it's overtightening and stripping the thread; assembly robots need to feel when components click properly into place. Surgical robots like the da Vinci system use force sensing to give the operating surgeon haptic feedback during a teleoperated procedure — a form of touch information that turns out to be genuinely important for precision.

## 3.7 Teaching a robot without writing code for every joint angle

**Programming by demonstration** lets a robot learn a task by being physically guided through the motion — a technician moves the arm along a desired welding path once, and the robot records and replays it — rather than a programmer hand-writing the exact joint angles for every point along that path. This matters because it makes deploying a robot for a new task accessible to people who aren't specialist robotics programmers, not just to those who can write low-level motion-control code.

## 3.8 The maths of "where does the arm need to go"

**Inverse kinematics** is the calculation of what angle each of a robotic arm's joints needs to be set to, in order to place its end effector at a specific target position and orientation. This is the reverse of *forward kinematics* (computing where the end effector ends up, given a known set of joint angles). Inverse kinematics is genuinely computationally challenging: for a given target, multiple different joint configurations can be valid, or in some cases none at all — and an efficient solver for this has to be embedded in every practical industrial robot controller.

**Path planning** is a related but distinct problem: not "what joint angles reach this exact point" but "how does the robot move from its current position to a goal while avoiding every obstacle in between." Algorithms like A*, RRT, and D* compute collision-free routes, accounting for the robot's own physical constraints, the surrounding environment's geometry, and efficiency — a warehouse robot has to account for both fixed obstacles (shelving) and moving ones (people, forklifts) at once.

## 3.9 Degrees of freedom — a real, concrete design tradeoff

A robot's **degrees of freedom** describes the number of independent ways its joints can move. A robotic arm built purely to pick items straight up and set them straight down needs far fewer degrees of freedom than one that must also rotate and angle items precisely — and fewer degrees of freedom generally means a simpler, cheaper, more mechanically reliable robot, at the direct cost of flexibility if the task's requirements ever change to need more complex motion. This is a genuine, common engineering tradeoff, not a case of "more is always better."

## 3.10 Applying What You've Learned

**Example 1**

*A robotics team trains a robot to walk using a physics simulator for months, achieving a stable gait, but the same robot falls over almost immediately on a real floor. What most directly explains this?*

A) The robot's motors must be mechanically defective in some way, since a robot that walks flawlessly in simulation should logically be guaranteed to also walk flawlessly the first time it's tried in the real world
B) Simulated training of any kind is entirely useless and represents a complete waste of engineering time, since nothing learned inside a physics simulator can ever meaningfully transfer to a real physical robot
C) The robotics team must have deliberately skipped testing the robot's balance systems before deployment, since a properly tested robot would never fail this quickly right after leaving simulation
D) The sim-to-real gap — simulations can't perfectly model real-world friction, sensor noise, and material properties, so a policy that worked flawlessly in simulation can still fail on first real-world contact

*Walk through it:* A asserts a guarantee ("simulated success guarantees real success") that section 3.3 directly contradicts — that's the whole point of the sim-to-real gap existing at all. B overcorrects into the opposite extreme, dismissing simulation entirely rather than recognising its real, if limited, value. C invents a testing failure the scenario never actually describes — it explicitly says the team trained for months, not that they skipped anything. The accurate explanation is **D** — simulation is a genuinely useful but imperfect approximation of reality, and small unmodelled differences (friction, sensor noise) are exactly what can cause a policy that worked in simulation to fail on first real contact.

**Example 2**

*Amazon's warehouse picking robots handle standard boxed items well but still struggle to reliably pick a loose bag of produce. What core robotics challenge does this expose?*

A) Robot grasping of novel objects — determining a stable, appropriate grip requires simultaneously reasoning about an unfamiliar object's geometry, material, weight, and fragility, something humans do unconsciously but remains genuinely hard for robots
B) Path planning — the specific challenge of computing a collision-free route for the robotic arm to travel from its current position all the way to the exact location of the item sitting on the shelf
C) Teleoperation — the practical difficulty of having a remote human operator control the robotic arm precisely enough in real time to successfully grasp any irregularly shaped item by hand
D) The uncanny valley — the discomfort human warehouse workers reportedly feel when watching a robot attempt to handle food items that closely resemble something a person would normally handle themselves

*Walk through it:* B, C, and D each name a real robotics concept, but none of them actually matches what's described — the scenario is specifically about *handling* an irregular object once the arm has already reached it, not about *navigating to* it (B), a *human controlling it remotely* (C, and nothing here suggests a human operator at all), or *appearance-based discomfort* (D, which is about humanoid appearance, not warehouse picking). The scenario's exact challenge — irregular shape, unpredictable fragility, no pre-programmed grip strategy — is the unsolved grasping problem from section 3.4. That's **A**.

**Example 3**

*A hospital delivery robot builds its own map of hallways and re-routes in real time around an unexpected obstacle, unlike an older factory robot that follows a fixed magnetic strip and simply stops if anything blocks it. What distinguishes the hospital robot?*

A) It's a cobot, specifically engineered with force and torque sensing to work safely near human staff, though that capability alone doesn't explain how it actually plans its own route through the hallways
B) It's an AMR, which creates its own map of the environment and plans routes in real time, unlike an AGV that simply follows a predefined physical track and stops if anything blocks it
C) It's using swarm robotics, coordinating its movements with a large number of other simple identical robots elsewhere in the hospital, even though the scenario only ever describes a single robot
D) It's using a pre-loaded digital twin of the hospital's floorplan, letting it avoid the blocked cart using a virtual replica built in advance rather than a map it actually builds itself in real time

*Walk through it:* A names a real category (force-sensing robots safe to work near humans) that has nothing to do with *how the robot navigates*, which is what the scenario is actually asking about. C invents a multi-robot coordination scenario the question never mentions — there's only one robot here. D invents a pre-loaded virtual replica as the explanation, when the scenario explicitly says the robot builds its *own* map. The distinguishing feature described — building its own map, adapting routes in real time — is precisely the AMR-versus-AGV distinction from section 3.5. That's **B**.

**Example 4**

*A robot assembling small electronic components can 'feel' when a connector clicks properly into place, and adjusts its grip pressure so it doesn't crush a delicate part. Which technology gives it this kind of tactile awareness?*

A) SLAM — simultaneous localisation and mapping, which lets the robot build a map of the assembly area while tracking its own position relative to the components on the table
B) Swarm robotics — coordination between multiple simple robots each handling a small part of the overall assembly task using local rules rather than any centralised sensing system
C) Force-torque sensing — sensors at the wrist or gripper that measure applied forces and torques, giving the robot a functional sense of touch for tasks requiring delicate handling or detecting unexpected contact
D) The uncanny valley — a design consideration about how human-like a robot's appearance should be, which becomes relevant whenever a robot works closely alongside human assembly workers

*Walk through it:* A and B each name a real robotics concept, but neither has anything to do with detecting contact or applied pressure — SLAM is about building a map and tracking position, and swarm robotics is about coordinating many separate robots, not about one robot's sense of touch. D is a design concept about appearance and human comfort, unrelated to a robot's actual tactile sensing capability. Force-torque sensing, from section 3.6, gives robots a functional sense of touch — detecting subtle cues like a connector clicking into place or excessive pressure before it damages a component. That's **C**.

**Example 5**

*A drone delivering blood supplies to a rural clinic must compute a route that avoids trees, power lines, and no-fly zones while reaching its destination efficiently, recalculating instantly if a new obstacle like a moving vehicle appears. What is this ongoing computation called?*

A) Programming by demonstration — a human operator physically flying the drone once along the exact intended delivery route in advance, which the drone then simply replays on every future flight
B) Path planning — the computational process of determining how a robot should move from a start point to a goal while avoiding obstacles, accounting for physical constraints and efficiency
C) Force-torque sensing — measuring the physical forces and torques acting on the drone's frame in flight in order to determine the safest possible route to the rural clinic
D) The uncanny valley — evaluating how comfortable people in the rural community feel about the appearance and flight behaviour of the delivery drone as it approaches the clinic

*Walk through it:* A describes a fixed, pre-recorded route, the opposite of the scenario's requirement to recalculate instantly around a new, unexpected obstacle. C misapplies force-torque sensing — a technique for detecting contact and applied pressure, not for computing a navigation route. D is a design concept about human comfort with a robot's appearance, unrelated to route computation. Path planning, from section 3.8, is exactly the ongoing computation described — algorithms like A*, RRT, or D* compute collision-free routes accounting for both fixed and dynamically appearing obstacles in real time. That's **B**.

---

# Chapter 4: Cybersecurity & Networks

## 4.1 Zero-trust: the shift from "trust the perimeter" to "verify every request"

Traditional network security worked like a castle wall: anyone inside the network was trusted, and the main defence was keeping attackers *out*. The problem: once a single infected device gets past the wall — a contractor's laptop, a phished employee — it can move freely inside, because everything inside was assumed safe.

**Zero-trust security** rejects that assumption entirely. No user, device, or network segment is inherently trusted, no matter where it's connecting from — every access request is verified independently, every time. This isn't paranoia for its own sake; it's a direct response to the real, repeated failure pattern of perimeter-only security: the wall works great until exactly one thing gets through it.

## 4.2 Encryption: what "end-to-end" actually promises

**End-to-end encryption** means only the two communicating devices hold the decryption keys — the service provider carrying the message never has access to the readable content, even if their own servers are breached or a court orders them to hand over data. This is a strong, specific guarantee, and it's genuinely different from encryption that only protects data in transit to the company's own servers (where the company itself *can* still read it).

Two other encryption ideas worth knowing precisely, because they solve genuinely different problems:

- **Symmetric encryption** uses one shared secret key for both locking and unlocking — simple, but requires the two parties to somehow agree on that secret key in advance without anyone else learning it.
- **Public-key (asymmetric) encryption** uses a mathematically linked pair: anyone can use your published public key to encrypt a message to you, but only your private key can decrypt it. This elegantly solves the "how do two strangers agree on a secret in advance" problem that symmetric encryption has.

## 4.3 The most common attacks — and what actually stops each one

**Phishing** and **social engineering** exploit human psychology — trust, urgency, authority — rather than a technical flaw. This is why the most sophisticated firewall in the world is useless if someone can be phoned by a fake "IT support" caller and talked into revealing their password. Technical defences and human security-awareness training address genuinely different vulnerabilities, which is why serious organisations invest in both.

**SQL injection** happens when unsanitised user input gets treated as part of a database command instead of as plain data — a classic example being a login field where typing `' OR '1'='1` tricks a poorly-built system into returning every record. **Prepared statements** are the standard fix: the query's structure and the user's data are sent to the database separately, so user input can never be interpreted as executable command logic.

**Credential stuffing** takes a list of username/password pairs leaked from one breached site and automatically tries the same combinations on many other unrelated sites, betting on password reuse. The single most effective individual defence is a unique password per site — practically only achievable with a password manager — because it means a leak on one site can't unlock accounts anywhere else.

**A zero-day vulnerability** is a flaw the software's own vendor doesn't yet know about, so no patch exists yet. It's the most dangerous category precisely because the standard defence (patching) isn't available until the vendor learns about it — in the meantime, monitoring and isolating exposed systems are the only real options.

## 4.4 Two-factor authentication: why a stolen password isn't enough on its own

**2FA/MFA** requires a second, independent proof of identity — typically something you *have* (your phone) in addition to something you *know* (your password). If an attacker obtains your password through a data breach, they still can't log in without your phone, because the whole point of the second factor is that it doesn't get compromised by the same breach that exposed your password.

## 4.5 The CIA triad — three distinct properties security actually protects

**Confidentiality** (only authorised people can read the data), **Integrity** (the data is accurate and hasn't been tampered with), and **Availability** (the data is accessible when it's actually needed) are three genuinely separate properties, and different attacks target different ones. Ransomware that locks you out of your own files is primarily an *Availability* attack — it doesn't necessarily read or alter your data, it just denies you access to it. A database tampering attack is primarily an *Integrity* attack. A network eavesdropper reading unencrypted traffic is a *Confidentiality* attack. Knowing which property a described attack actually targets is more useful than memorising the triad as a slogan.

## 4.6 Malware isn't one thing — how it spreads is the meaningful distinction

The everyday word "virus" gets used loosely, but the real categories are defined by *how the malware spreads or gains access*, which matters for how it's actually stopped:

- A **virus** typically needs a host file to be opened or executed by a user before it activates and spreads — it needs a human action.
- A **worm** spreads across a network autonomously, with no human action required at all — no file to open, no click needed.
- A **trojan** disguises itself as legitimate, desirable software to trick a user into voluntarily installing it — its whole mechanism relies on deception, not autonomous spreading or a host file.

## 4.7 When an attacker doesn't need your password at all

**Session hijacking** targets the token that proves you're already logged in — a session cookie — rather than your actual password. If an attacker steals a valid session cookie (through, say, an unsecured network or a cross-site scripting flaw), they can impersonate the logged-in user directly, bypassing the login process entirely. This is exactly why sensitive session cookies are often marked *HttpOnly* — a flag that prevents JavaScript on the page from reading them at all, closing off one common way they get stolen.

## 4.8 The threat that already has legitimate access

Most security controls assume the danger is someone breaking *in*. An **insider threat** is different: someone who already has legitimate, authorised access misusing it — an employee quietly copying a customer database before resigning, say. This is genuinely harder to prevent with perimeter-focused defences, because the person's access itself isn't inherently suspicious. Detecting misuse typically requires monitoring for unusual *patterns* of legitimate access (an unusually large data export, access at an unusual hour) rather than blocking unauthorised entry, which is what most external-facing controls are built for.

## 4.9 Why one weak device can take down something much bigger

The 2016 Mirai botnet hijacked roughly 600,000 IoT devices — cameras, home routers — that shipped with weak, unchanged default passwords, then used them together to launch one of the largest denial-of-service attacks ever recorded. This illustrates a real, ongoing **IoT security** risk: individual smart devices are often poorly secured (default credentials, rarely updated firmware) and become an enormous, easy-to-hijack attack surface when combined at scale, even though no single device looks like a serious target on its own.

## 4.10 Applying What You've Learned

**Example 1**

*A login form takes a username and inserts it directly into a database query with no filtering. An attacker enters `admin' OR '1'='1` and gains access to every account. What vulnerability was exploited, and what's the standard fix?*

A) A zero-day vulnerability specific to this one particular login form — an undiscovered flaw the vendor has never had any opportunity to patch, unrelated to how user input is generally handled
B) A supply chain attack, since the attacker must have first compromised a trusted third-party software component the login form depends on, rather than typing directly into the field itself
C) SQL injection — the unsanitised input was interpreted as part of the database query itself; prepared statements, which separate query structure from user data, are the standard fix
D) Social engineering — the attacker psychologically manipulated a human support agent into granting account access, rather than exploiting any weakness in the login form's own underlying code

*Walk through it:* A mislabels this as an undiscovered, vendor-unknown flaw — but this is actually a well-known, well-understood vulnerability class with a well-known fix, the opposite of a zero-day. B invents a third-party compromise that isn't part of the scenario at all — the attacker typed directly into the login form itself. D misattributes a purely technical exploit to human manipulation, when no human was tricked into doing anything here. The crafted input altered the query's logic to always evaluate true — textbook SQL injection, from section 4.3. That's **C**, and the fix (prepared statements, separating query structure from user data) is the specific detail worth remembering.

**Example 2**

*An attacker who obtained leaked username/password pairs from one breached site automatically tries the same combinations on dozens of unrelated sites. What is this attack called, and what's the single most effective individual defence?*

A) SQL injection — the standard fix is understood to involve inserting malicious database commands into each of the dozens of separate targeted login forms individually
B) A zero-day exploit that happens to affect every single one of the dozens of unrelated targeted sites simultaneously, despite each one running entirely different, unrelated software
C) A supply chain attack compromising one shared vendor used by all of the dozens of unrelated targeted sites at once, rather than directly testing any of the actual stolen credential pairs
D) Credential stuffing — automatically testing stolen username/password pairs across many services; using a unique password per site (via a password manager) is the most effective individual defence

*Walk through it:* A confuses the attack being described (automated login attempts using stolen credentials) with a completely different attack (manipulating a database query) — these solve different problems and have nothing to do with each other. B is implausible on its face — a zero-day is by definition a single, specific, undiscovered flaw, not something that would coincidentally affect "dozens of unrelated sites" at once. C invents a shared vendor the scenario never mentions. The actual mechanism — reusing stolen credentials across many services, betting on password reuse — is credential stuffing from section 4.3, and its direct countermeasure is a unique password per site. That's **D**.

**Example 3**

*A ransomware attack makes a hospital's patient records completely inaccessible, though the attacker never actually read or copied them. Which part of the CIA triad was most directly violated?*

A) Availability — the records being inaccessible when needed is exactly what this specific property protects against, regardless of whether the underlying data was also read or altered
B) Confidentiality — since ransomware attacks are assumed to always necessarily involve the attacker actually reading and copying the affected records, confidentiality must logically be the property violated
C) Integrity — since making a set of records completely inaccessible is treated as functionally identical to actively altering or corrupting the content of those same records
D) None of the three — a ransomware attack that only blocks legitimate access without reading or altering any underlying data isn't considered a genuine security violation at all

*Walk through it:* B asserts something the scenario directly contradicts — it explicitly says the data was never read or copied, so confidentiality (which is about *unauthorised reading*) wasn't the thing actually violated. C blurs two genuinely distinct properties together — making data inaccessible is not the same as corrupting or altering it, which is what Integrity specifically covers. D dismisses a serious, real attack as "not a real violation," which doesn't hold up against the scenario's own description of records being locked away from legitimate users. The precise match, from section 4.5, is Availability — the data being inaccessible when needed, regardless of whether it was read or changed. That's **A**.

**Example 4**

*A piece of malicious software spreads automatically from computer to computer across a network with no human action required, unlike a virus which typically needs a user to open an infected file to spread. What type of malware does this describe?*

A) A trojan — malware disguised as legitimate software that a user is specifically tricked into willingly installing themselves, which by definition requires that direct human action to spread at all
B) A worm — self-replicating malware that spreads across networks autonomously, without requiring a human to open or execute an infected file the way a traditional virus generally does
C) Ransomware — malware that specifically encrypts a victim's files and demands payment for their release, a behaviour unrelated to whether the malware requires human action to initially spread
D) Spyware — malware designed specifically to covertly monitor and collect a user's activity and personal information, a behaviour unrelated to whether the malware needs human action to spread

*Walk through it:* A describes the opposite propagation method — a trojan specifically relies on tricking a human into installing it, which contradicts the "no human action required" detail the scenario is pointing at. C and D each name a real malware category defined by what the malware *does* once installed (encrypting files, spying), not by *how it spreads*, so neither actually answers the question being asked. A worm, from section 4.6, is specifically defined by autonomous network spread with no human action needed — exactly the detail the scenario highlights. That's **B**.

**Example 5**

*An attacker steals the small text file a website uses to remember that a user is already logged in, and uses it on their own browser to impersonate that logged-in user without ever needing the actual password. What is this attack called?*

A) Session hijacking — stealing or forging a valid session token (like a login cookie) to impersonate an already-authenticated user, bypassing the need to know their actual password at all
B) SQL injection — inserting malicious database commands directly into the website's login form, which is the specific technique required in order to steal another user's session cookie
C) A brute-force attack — systematically trying every possible password combination against the website's login form, until eventually one combination matches the targeted user's actual password
D) A supply chain attack — compromising a trusted third-party vendor connected to the website first, which is the specific technique required in order to steal another user's active session cookie

*Walk through it:* B and D each invent an unrelated technical mechanism (manipulating a database query; compromising a third-party vendor) as somehow being required to steal a cookie, when the scenario doesn't describe either happening. C describes an entirely different attack that specifically targets the password itself, which the scenario explicitly says the attacker never needed. Session hijacking, from section 4.7, targets the token proving a user is already authenticated rather than their credentials — exactly what's described here. That's **A**.

---

# Chapter 5: Programming & Web Systems

## 5.1 Thinking in complexity, not just correctness

Two functions can both correctly sort a list and still behave completely differently at scale. **Time complexity** (often written in Big O notation) describes how an algorithm's running time grows as input size grows — a function that merely *doubles* in time when the input doubles scales far better than one that *quadruples*, even if both give the correct answer on a small test case. This matters because a program that works fine in a demo with 100 records can become unusably slow at a million records if nobody thought about how it scales.

**Recursion** — a function calling itself on a smaller version of the same problem, with a base case that stops the chain — is a different axis entirely from complexity, but the two often show up together: a recursive solution to a problem can still be efficient or inefficient depending on how it's structured.

## 5.2 Why "it works on my machine" is a real, well-understood failure mode

Code that runs perfectly on a developer's laptop but breaks in production is one of the most common frustrations in software engineering — and it usually isn't mysterious. It happens when the development and production **environments** differ in some way the developer didn't account for: a different library version, a missing environment variable, a different operating system default.

**Containerisation** (Docker being the dominant example) solves this directly: it packages an application together with its *exact* runtime environment — specific library versions, configuration, dependencies — into one portable unit that behaves identically wherever it runs. **Infrastructure as code** extends the same idea to the servers themselves: defining server configuration as version-controlled files instead of manually clicking through a control panel, so environments are reproducible rather than each one being a slightly different snowflake.

## 5.3 Client, server, and the protocol that connects them

**HTTP methods carry meaning, not just syntax.** A `GET` request is meant to safely retrieve data with no side effects — which is why a browser can safely cache or retry it. A `POST` request is meant for submitting data that typically *changes* something on the server. This distinction is why login forms use POST and simple page loads use GET.

**HTTP status codes are grouped by what kind of problem occurred.** A `404` means the requested resource genuinely doesn't exist at that address — a problem with the *request*. A `500` means the server received a valid request but something went wrong while processing it internally — a problem on the *server side*. Knowing which category a code falls into tells a developer where to actually look for the bug.

**REST** is a set of conventions for exposing data and operations over HTTP using consistent URLs and methods, letting different client applications (mobile, web) interact with the same backend predictably. **GraphQL** takes a different approach: the client specifies exactly which fields it needs in a single flexible request, which can avoid REST's common problem of either over-fetching unused fields or needing multiple round trips to gather everything.

## 5.4 Databases: structure, consistency, and why they sometimes fail together

**Normalisation** — splitting related data into linked tables (customers in one table, their orders in another, linked by a customer ID) instead of repeating full customer details in every single order — avoids duplication and, more importantly, avoids the *inconsistency* that comes with duplication: updating a customer's address in one place instead of needing to hunt down and update every stale copy.

**ACID transactions** guarantee that a group of database operations either all succeed together or all fail together, with no partial, half-completed state left behind — the classic example being a bank transfer, where the sender's balance decreasing and the receiver's balance increasing must happen as one indivisible unit, even if the system crashes mid-transfer.

**The CAP theorem** describes a genuine, unavoidable tradeoff for distributed databases during a network partition (when some servers can't reach others): the system must choose between Consistency (every read reflects the very latest write, even if that means refusing some requests) and Availability (always responding, even if a response might be slightly stale). It cannot perfectly guarantee both at the same time under partition conditions — this isn't an engineering failure, it's a mathematical fact about distributed systems.

## 5.5 Deployment ideas that show up constantly in real engineering conversations

- **CI/CD (continuous integration/continuous deployment)** automatically builds, tests, and deploys every code change, catching problems within minutes instead of weeks later.
- **Microservices** split a large application into independently deployable services — enabling independent scaling and deployment of, say, just the payments service — at the real cost of added operational complexity (more network calls, more coordination needed) compared to one single monolithic program.
- **A canary release** deploys a new version to a small percentage of real users first, limiting the blast radius if the new version has an undiscovered bug, before rolling out to everyone.
- **Feature flags** decouple *deploying* code from *releasing* a feature to users — code can ship to production switched off, then be turned on instantly for everyone without a new deployment, and just as quickly switched back off if something goes wrong.

## 5.6 REST and GraphQL — two conventions for the same underlying problem

**REST** is a set of conventions for exposing data and operations over HTTP using consistent URLs and methods, letting different client applications (a mobile app, a web dashboard) interact with the same backend predictably. **GraphQL** takes a different approach: instead of fixed endpoints each returning a fixed set of fields, the client specifies exactly which fields it needs in a single flexible request. This can avoid a genuine REST pain point — either over-fetching unused fields, or making multiple round trips to gather everything a screen actually needs — though REST generally remains simpler to cache and reason about, which is why both approaches coexist across real production systems rather than one having fully replaced the other.

## 5.7 One big program vs. many small ones

A **monolith** is a single, unified application handling everything — simple to develop and deploy as one unit, but everything scales and deploys together even if only one part actually needs it. **Microservices** split a large application into independently deployable services, so the payments service can scale (or be redeployed) without touching inventory. The real, honest tradeoff: independent scaling and deployment, at the direct cost of added operational complexity — more network calls between services, more coordination needed, more things that can fail independently. Microservices aren't simply "more advanced" than a monolith; they're the right choice for some situations and a genuine overcomplication for others.

## 5.8 Handling more traffic than one server can take

**Load balancing** distributes incoming requests across multiple servers so no single one becomes a bottleneck. **Auto-scaling** automatically adjusts how many servers exist based on real-time demand. Together, this combination is exactly what lets a website absorb a sudden, large, unpredictable traffic spike (a viral moment, a flash sale) without manual intervention or an outage — load balancing spreads the load across whatever capacity currently exists, auto-scaling adjusts how much capacity currently exists.

## 5.9 Splitting a dataset that's grown too big for one server

**Sharding** splits a large dataset across multiple database servers — each holding a subset, often by some key like a user ID range — directly addressing the scalability problem of a dataset or workload becoming too large for any single server to handle efficiently. This is a genuinely different technique from **replication** (keeping multiple full copies of the same data across servers, mainly for fault tolerance and read performance) — the two are sometimes combined, but they solve different problems: sharding solves "too big for one server," replication solves "what if one server fails."

## 5.10 A property that matters more than it sounds: idempotency

An operation is **idempotent** if repeating it with the same input produces the same end result, no matter how many times it's called. This matters enormously for network reliability: if a client sends a "delete this order" request but never receives a response (the connection dropped), it often has to retry — and an idempotent delete endpoint ensures that retry doesn't cause any unintended extra effect, since deleting an already-deleted order safely does nothing further, rather than throwing an error or, worse, silently doing something harmful on the second call.

## 5.11 Applying What You've Learned

**Example 1**

*A developer notices their web app behaves subtly differently in production than in local development — a library version mismatch causes a bug that never appears during local testing. Which practice most directly addresses this class of problem?*

A) Writing many more unit tests that check individual functions in isolation, since a sufficiently thorough test suite is assumed to inherently catch any configuration difference between two separate environments
B) Environment parity, often achieved using containerisation to package the exact same runtime environment — specific library versions, configuration, dependencies — so it can't drift between machines
C) Restructuring the affected code to use recursion instead of loops, a general programming technique about a function's own internal control flow rather than about environment configuration
D) Using the same method name consistently across different object types, an object-oriented design concept unrelated to how a development and production environment are actually configured

*Walk through it:* A names a real, valuable practice, but unit tests run in yet another environment (the test environment) — they don't inherently catch a *configuration difference between two environments*, which is specifically what's being described here. C and D each name a real programming concept (recursion, polymorphism) that has nothing to do with environment configuration at all — a classic case of a distractor being a real term used in the wrong context. The actual fix, from section 5.2, is keeping environments consistent — commonly via containerisation, which packages the exact runtime environment so it can't drift between machines. That's **B**.

**Example 2**

*A team's deployment process used to involve manually copying files to a server, hoping nothing broke. They switch to a system where every code change is automatically tested, and if it passes, automatically deployed within minutes. What is this practice called, and what does "tested on every change" specifically provide?*

A) Infrastructure as code — a practice specifically about defining server configuration as version-controlled files, rather than about automatically testing and deploying code changes as they're made
B) Object-oriented programming — a programming paradigm organising code into classes and objects, unrelated to whether a team's code changes are tested automatically or copied manually
C) CI/CD — automatically building, testing, and deploying every code change; testing on every change catches integration problems within minutes rather than discovering them weeks later
D) The strangler fig pattern — a strategy specifically for gradually migrating away from a legacy system, rather than a practice describing how code changes are tested and deployed

*Walk through it:* A, B, and D are all real, legitimate engineering concepts — that's exactly what makes them convincing-looking wrong answers — but none of them actually describes "automatically test every change, then automatically deploy it." A is about how servers are configured, not about a testing-and-deployment pipeline. B is a way of structuring code, unrelated to any deployment process. D is a strategy for retiring an old system gradually, which isn't what's being described at all. The practice that matches — automated building, testing, and deploying on every change — is CI/CD from section 5.5. That's **C**.

**Example 3**

*A distributed database serving users worldwide must choose its behaviour during a network partition: keep serving requests with possibly outdated data, or refuse requests until servers can resync. What principle describes this forced tradeoff?*

A) The testing pyramid — a strategy for structuring a team's automated tests into layers of unit, integration, and end-to-end tests, unrelated to how a distributed database behaves during a network partition
B) DRY (Don't Repeat Yourself) — a principle specifically about avoiding duplicated code within a single codebase, unrelated to the tradeoff a distributed database faces during a network partition
C) Recursion — a programming technique where a function calls itself on a smaller version of a problem, unrelated to how a distributed database handles a consistency-versus-availability tradeoff
D) The CAP theorem — a distributed system experiencing a network partition must choose between Consistency (always correct, up-to-date data) and Availability (always responding to requests)

*Walk through it:* A, B, and C are each genuine software concepts, but none of them has anything to do with a distributed database's behaviour during a network partition specifically — they're each about a different part of software engineering entirely (testing strategy, code duplication, and a function-calling technique, respectively). This is a common exam-writing pattern worth noticing: distractors that are real terms, confidently stated, just plugged into the wrong scenario. The concept that actually describes an unavoidable tradeoff between consistency and availability during a partition is the CAP theorem, from section 5.4. That's **D**.

**Example 4**

*A startup with three engineers is deciding whether to build their new product as a single monolithic application or as a dozen separate microservices from day one. What is the most balanced, honest way to frame this decision?*

A) Microservices are always the objectively correct architecture choice regardless of team size, since independent scaling and deployment are strictly beneficial for any project no matter how small or early-stage
B) A monolith is generally the safer starting choice for a very small team, since microservices trade simplicity for operational complexity that a three-person team may struggle to manage alongside actually building the product
C) Monoliths are always the objectively correct architecture choice regardless of eventual scale, since splitting an application into separate services never provides any genuine benefit under any circumstances
D) The choice between a monolith and microservices has no real practical consequences either way, since the two approaches are functionally identical once a product is actually deployed to real users

*Walk through it:* A and C each state an absolute, one-size-fits-all rule ("always... regardless of... no matter what"), which section 5.7 directly contradicts — the real lesson is that the right choice depends on context, not that one approach is universally correct. D dismisses a genuine, well-documented architectural tradeoff as having no consequences at all, which doesn't hold up against the real operational complexity microservices introduce. The honest framing, from section 5.7, is that a very small team often struggles to manage the added coordination microservices introduce on top of actually building the product itself. That's **B**.

**Example 5**

*A backend developer designs an API so that calling the same 'delete user' request multiple times in a row (say, due to a network retry) has the exact same end result as calling it once — the user is deleted, and repeating the call simply confirms they're still gone rather than causing an error or unexpected side effect. What property does this API design have?*

A) Idempotency — an operation that produces the same end result no matter how many times it's repeated with the same input, which matters for safely handling network retries without unintended side effects
B) Polymorphism — an object-oriented concept where the same method name behaves differently depending on the specific object it's called on, unrelated to whether repeating an API call causes the same result
C) Recursion — a programming technique where a function calls itself on a smaller version of the same problem, unrelated to whether repeating an API request produces the same end result each time
D) A race condition — a bug where the outcome of concurrently running operations depends on unpredictable timing, a description of an unintended flaw rather than a deliberately designed API property

*Walk through it:* B and C each name a real programming concept from an entirely different context — an object-oriented design principle and a self-calling function technique, neither of which has anything to do with what happens when the same API request is repeated. D describes an unintended bug, while the scenario is explicitly describing a deliberately designed, desirable property. Idempotency, from section 5.10, means an operation can be safely repeated with the same input without unintended side effects — exactly what's described, and genuinely important for handling network retries safely. That's **A**.

---

# Chapter 6: Data Science & Analytics

## 6.1 A/B testing — turning "I think" into "I measured"

**A/B testing** randomly assigns users to two (or more) variants and measures which one produces a better real outcome — scaling the scientific method to product decisions. The reason *randomness* matters so much here: it's what lets you isolate the effect of the one thing you changed from every other factor that might also be influencing behaviour at the same time, like a holiday season boosting sales regardless of what your homepage looks like.

**Why it matters for reasoning:** if a scenario asks how to tell whether a specific change *caused* an improvement, versus the improvement just happening to coincide with something else (like a season), the answer that isolates cause from coincidence is almost always a randomised comparison run during the *same* time period — not comparing this year's numbers to last year's, which lets a dozen other factors change at the same time.

## 6.2 Correlation is not causation — and knowing why matters more than the slogan

You've heard "correlation doesn't imply causation" before. The useful version of this idea isn't the slogan — it's understanding *how* two unrelated things end up moving together anyway: a **confounding variable** independently drives both. Ice cream sales and drowning deaths rise together in summer, not because one causes the other, but because hot weather independently increases both ice cream purchases and swimming (and therefore drowning risk).

**Survivorship bias** is a related but distinct trap: studying only the cases that "survived" to be visible (successful startups still operating today) while ignoring the many failures that did the exact same thing (pivoted their business model) but aren't around to be counted. Without the failures in the comparison, you can't actually tell whether the thing you're crediting for success was the real cause.

## 6.3 Why "99% accurate" can describe a completely useless model

If a rare-disease detection dataset is 99% healthy patients and 1% actually sick, a model that *always* predicts "healthy" scores 99% accuracy — while being clinically useless at its one actual job. This is **class imbalance**, and it's exactly why raw accuracy is a misleading metric whenever one outcome vastly outnumbers another: it rewards a model for correctly handling the common case while telling you nothing about whether it can find the rare case that actually matters.

**Overfitting** is a related but distinct failure: a model that scores 99% on the exact data it was trained on but only 60% on new data has memorised specific quirks of that training set rather than learning something that generalises — the gap between the two numbers is the real signal, not the training number in isolation.

**Cross-validation** — repeatedly splitting data into training and held-out testing portions and averaging performance across the splits — exists specifically to catch this kind of inflated, overly optimistic result before it fools anyone.

## 6.4 Feature engineering: sometimes the input matters more than the algorithm

**Feature engineering** is using domain knowledge to transform raw data into more informative input variables. A model given raw salary and raw debt figures might perform worse than one given a single constructed feature, debt-to-income ratio, computed from those same two numbers — because the *ratio* is closer to the pattern that actually predicts loan default. This is often a bigger lever on model performance than swapping between similar algorithms, which is a genuinely counterintuitive fact worth remembering: better-prepared data frequently beats a fancier algorithm on worse data.

## 6.5 Distinguishing supervised from unsupervised approaches by what they're actually given

**K-means clustering** is unsupervised — it's given no pre-existing labels at all, and discovers natural groupings in data purely from similarity (for example, automatically segmenting transaction records into distinct customer types with no one telling it in advance what those types should be).

**Random forest** and **gradient boosting** are both supervised ensemble methods — they combine many individual decision trees, but in different ways. Random forest trains many trees independently on random subsets of data and features, then averages their votes, which reduces the instability (high variance) any single decision tree suffers from. Gradient boosting instead builds trees *sequentially*, with each new tree specifically targeting the errors the current combined ensemble still gets wrong — an iterative correction process rather than an averaging one.

## 6.6 Two more ways studies can quietly mislead you

**Sampling bias** happens when the method used to collect data systematically excludes or under-represents certain groups — a poll conducted only by calling landlines during weekday business hours will systematically miss younger, employed, mobile-only respondents, producing results that don't actually reflect the broader population, no matter how carefully the collected responses are later analysed.

**Survivorship bias** is a related but distinct trap already introduced in section 6.2: studying only the cases that "survived" to be visible — successful companies still operating, veterans who came home — while the failures that did the exact same thing but aren't around to be counted go uncounted. Without the missing failures in the comparison, you genuinely can't tell whether the thing you're crediting for success was the real cause.

## 6.7 A number is only as trustworthy as the chart drawing it

A bar chart with a Y-axis that starts at 98 instead of 0 can make a genuine 2% difference visually look like the bar roughly doubled — the underlying numbers can be completely accurate while the visual impression is seriously misleading. This is a well-known way data visualisation can distort intuition without technically lying: **always check what a chart's axis actually starts at** before trusting your gut reaction to how dramatic a difference looks.

## 6.8 What "statistically significant" actually claims — and doesn't

A result reported as **statistically significant** (commonly using a threshold like p < 0.05) means the observed difference is unlikely to have occurred purely by random chance, given the specific statistical test used. It's a narrower claim than people often assume: it says nothing directly about how *large* or *practically meaningful* the effect actually is. A statistically significant result can still be a genuinely tiny, unimportant effect — significance and importance are two separate questions, and mixing them up is a common misreading of study results.

## 6.9 Applying What You've Learned

**Example 1**

*A news article claims "ice cream sales and drowning deaths are strongly correlated, so ice cream must cause drowning." What's the most likely actual explanation?*

A) Correlation doesn't imply causation — both variables independently rise in hot summer weather, a classic confounding variable driving two things at once without either one causing the other
B) The bias-variance tradeoff — a concept specifically about a model being too simple or too complex, a distinct technical issue unrelated to interpreting a correlation between two real-world variables
C) Feature engineering — a data-preparation concept about transforming raw input variables for a model, unrelated to whether an observed correlation between two variables implies genuine causation
D) Dimensionality reduction — a technique for reducing the number of features in a dataset while preserving key information, unrelated to interpreting a correlation between two specific variables

*Walk through it:* B, C, and D are each real data-science terms — which is exactly why they can look tempting if you're pattern-matching on "sounds technical" rather than actually reading what's being asked. None of them has anything to do with *interpreting a correlation between two real-world variables*, which is specifically what the question is about. The actual explanation, from section 6.2, is a confounding variable — hot weather driving both ice cream sales and swimming (and therefore drowning risk) independently, with neither one causing the other. That's **A**.

**Example 2**

*A rare-disease detection model trained on data that's 99% healthy and 1% diseased can achieve 99% accuracy by always predicting "healthy," while being useless at its actual job. What problem does this illustrate, and why is raw accuracy misleading here?*

A) The bias-variance tradeoff — a concept about a model being too simple or too complex, a distinct technical issue from one outcome vastly outnumbering another within the underlying dataset itself
B) Class imbalance — raw accuracy is misleading because a model can score very high while being completely useless at detecting the rare, actually important class
C) Dimensionality reduction — a technique for reducing the number of features in a dataset while preserving key information, unrelated to how a dataset's outcome classes are distributed
D) A/B testing — a controlled experiment methodology comparing two live variants with randomly assigned users, unrelated to how a dataset's existing classes are numerically distributed

*Walk through it:* A names a real, related-sounding concept, but it's about a different failure mode entirely (a model too simple or too complex), not about one outcome vastly outnumbering another in the data — reading carefully, the scenario is about the *composition of the dataset*, not the model's complexity. C and D each name real techniques that solve unrelated problems (reducing feature count; running a controlled experiment) with no connection to the specific imbalance described. The actual issue, from section 6.3, is class imbalance — and the fix in practice is using metrics that specifically measure how well the rare class is detected, not raw accuracy. That's **B**.

**Example 3**

*Two data scientists build models to predict loan defaults with the exact same algorithm. One spends her time creating a "debt-to-income ratio" feature from raw salary and debt figures; the other uses only the raw figures. Her model performs notably better. What does this illustrate?*

A) A/B testing — a technique for comparing two live product variants with randomly assigned users, not for describing how the underlying input data was actually prepared before modelling
B) Data governance — an organisational, policy-level practice for managing data as a business asset, unrelated to why one specific data scientist's model technically outperformed another's
C) Feature engineering — thoughtfully transforming raw data into more informative input variables using domain knowledge often matters more than the choice of algorithm alone
D) Dimensionality reduction — a technique for reducing the number of features in a dataset, the opposite of what happened here, since a new feature was constructed and added, not removed

*Walk through it:* A misapplies a real technique (comparing live variants with randomly assigned users) to a scenario that's actually about data preparation before modelling, not a live experiment. D is worth noticing specifically because it names the *opposite* of what happened — dimensionality reduction reduces the number of features, while this scenario is about constructing a *new, more informative* one. B names an organisational, policy-level concept that has nothing to do with one data scientist's technical choice in building a specific feature. The real explanation, from section 6.4, is that a well-constructed feature can make a pattern the model needs to learn far more directly visible than the raw numbers alone — that's feature engineering. **C**.

**Example 4**

*A political poll surveys 1,000 people by calling landline phones during weekday business hours, systematically missing younger people who mostly use mobile phones and are usually at work or school during that time. The poll's results end up skewed toward older, retired respondents. What problem does this illustrate?*

A) The bias-variance tradeoff — a concept specifically about a machine learning model being too simple or too complex, a distinct technical issue from a survey's data-collection method excluding certain groups
B) Cross-validation — a technique for evaluating a trained model's performance by repeatedly splitting data into training and testing portions, unrelated to whether a poll's original data-collection method is representative
C) Class imbalance — a situation where one outcome vastly outnumbers another within an existing dataset's labels, a distinct issue from a survey's data-collection method systematically excluding certain groups
D) Sampling bias — the method used to select survey respondents systematically excludes or under-represents certain groups, producing results that don't accurately reflect the actual broader population

*Walk through it:* A, B, and C each name a real data-science concept from a different context entirely — a model-complexity issue, a model-evaluation technique, and a dataset-composition issue — none of which describes a flawed data-*collection* method itself. The specific method used to reach respondents here (landlines, weekday hours) systematically excludes younger, more mobile-reliant, employed people, which is sampling bias from section 6.6 — a flaw in how the sample was gathered, regardless of how carefully the 1,000 collected responses are later analysed. That's **D**.

**Example 5**

*A chart showing company revenue over five years uses a Y-axis that starts at ₦9.8 million instead of ₦0, making a modest 5% revenue increase visually look like the bar roughly doubled in height. What data visualisation problem does this illustrate?*

A) Class imbalance — a situation where one outcome vastly outnumbers another within a dataset's labels, a concept about training-data composition rather than about how a chart's visual axis is constructed
B) The bias-variance tradeoff — a concept specifically about a machine learning model being too simple or too complex, a distinct technical concept unrelated to how a chart's Y-axis scale is chosen and displayed
C) A misleading or truncated axis — manipulating a chart's scale (like a non-zero baseline) can visually exaggerate a small real difference, distorting how a viewer perceives the actual underlying data
D) Dimensionality reduction — techniques for reducing the number of features in a dataset while preserving key information, a data-preparation concept unrelated to how a chart's Y-axis scale is chosen

*Walk through it:* A, B, and D each name a real data-science term entirely unrelated to how a chart's axis is visually constructed — dataset composition, model complexity, and feature reduction, none of which have anything to do with where a Y-axis starts. A truncated or non-zero-baseline axis, from section 6.7, is a well-known way charts can mislead: the underlying numbers may be entirely accurate while the visual impression — a small change looking dramatic — misleads a viewer's intuitive interpretation. That's **C**.

---

# Chapter 7: Ethics, Society & Future Tech

## 7.1 Why "the algorithm didn't ask for race" doesn't mean it's fair

A documented US algorithm used in criminal sentencing flagged Black defendants as "high risk" at a significantly higher rate than white defendants with similar records — even though race was never a direct input to the model. How? The model can learn a **proxy**: a postal code, for example, that happens to correlate strongly with historically segregated neighbourhoods, functionally reproducing a pattern of discrimination the model was never explicitly told to learn.

This is why **AI bias is a social justice issue, not just a technical footnote**: a biased system deployed at scale doesn't just make a random error here and there — it systematically disadvantages a group that's often already facing discrimination, and it does so at a speed and scale a single biased human decision-maker never could. The technical fix (removing an explicit input) doesn't automatically fix the underlying problem if a correlated proxy is still doing the same work.

**Algorithmic accountability** is the broader principle this points to: automated decisions that affect fundamental rights or opportunities — who gets a job interview, who's denied bail, whose loan is approved — need to be fair, transparent, and genuinely contestable by the people they affect, not just accurate on average across a whole population.

## 7.2 Surveillance capitalism — the business model behind "free"

If a service costs you nothing, something else is usually paying for it. **Surveillance capitalism** describes an economic model where personal behavioural data — what you click, how long you linger, what makes you scroll faster — is collected, analysed, and turned into predictive products sold to advertisers. This is the actual underlying business model behind much of the "free" internet, and it matters ethically because most users never explicitly, meaningfully consented to that specific trade — clicking "I agree" on a long terms-of-service document isn't the same thing as genuinely understanding and choosing it.

## 7.3 The digital divide is compounding, not just inconvenient

**Digital inequality** — unequal access to devices, connectivity, and digital skills — doesn't exist in isolation. A farmer without reliable electricity or affordable data has no realistic path to AI-powered tools that a well-connected urban user can access freely, and that same farmer is often *already* excluded from other opportunities that digital access increasingly gates: education, financial services, wider markets. This is why the digital divide is described as **compounding** rather than simply additional — it doesn't just add one more disadvantage, it deepens the ones already there.

**Data sovereignty** is a related but distinct concept: the principle that data should be governed by the laws of the country where it was actually collected. If a country's clinical, genomic, or agricultural data is stored abroad and processed under a foreign legal system by a foreign company, that country loses meaningful control over both the data and the economic value later extracted from it — which is exactly why countries have been building their own data-protection frameworks (Nigeria's NDPR among them).

## 7.4 The automation paradox — automation doesn't simply "replace," it reshapes

When routine tasks get automated, the people doing that work don't necessarily disappear — their day-to-day work often shifts toward the harder, less routine parts an AI system still struggles with, and toward reviewing and correcting what the AI produces. But this shift carries a real risk too: if someone becomes dependent on automation for a skill they no longer regularly practise manually, they can be caught out badly in the rare moment the automation fails and their own underlying skill has quietly eroded. This is the **automation paradox** — automation can simultaneously increase the value of remaining human expertise and create a skills trap for the people who over-rely on it.

## 7.5 Responsible AI is a practice, not a press release

**Responsible AI**, done seriously, means assessing potential harms *before* a system is deployed (not only after problems are reported), actively testing for unfair treatment across different groups, and maintaining a genuine, working process for someone to contest an automated decision — as an ongoing practice, not a one-time checklist that gets signed off and forgotten. The test that actually distinguishes a real commitment from a symbolic one: has this ever actually stopped or delayed a launch over a genuine unresolved concern? A framework that's never once said "no" to anything is doing less work than it appears to.

## 7.6 The explainability trade-off — the most accurate model is often the hardest to explain

There's a recurring tension in deploying AI for high-stakes decisions: the model families that tend to perform best on complex, messy real-world data (deep neural networks, large ensembles) are also usually the hardest for a human to inspect and explain, while simpler, more transparent models (a small decision tree, a linear model with a handful of clearly weighted factors) are easier to audit but often less accurate. This is the **explainability trade-off**, and it isn't a purely technical inconvenience — if a bank denies someone a loan and can't meaningfully explain *why* beyond "the model said so," that person has no real way to identify an error or contest the decision, which conflicts directly with the accountability principle from section 7.1. Some domains (parole decisions, medical diagnosis, credit) increasingly demand **explainable AI (XAI)** — techniques that approximate or expose *why* a complex model reached a specific output — precisely because "it's accurate" isn't considered a sufficient answer on its own when someone's rights or opportunities are at stake.

## 7.7 Dual-use technology — the same tool cuts both ways

A technology is **dual-use** when the very same underlying capability that enables a beneficial application also enables a harmful one, with no clean technical line separating the two. Facial recognition that helps reunite missing children with their families is architecturally the same technology that enables mass, non-consensual surveillance of an entire population. A language model that helps a student learn to code is the same underlying technology that can help someone draft convincing phishing emails at scale. This matters because it means "make the technology safer" often can't just mean "block the harmful use case" at a technical level — the capability itself is what's dual-use, not a separable harmful feature bolted onto it, which is why dual-use risk tends to require governance and access controls *alongside* technical safeguards, not instead of them.

## 7.8 Risk-based regulation — not every AI use case gets treated the same

As governments have moved from talking about regulating AI to actually doing it, a common pattern has emerged: **risk-based regulation**, which sorts AI applications into tiers by potential harm rather than regulating "AI" as one single, undifferentiated category. Under this kind of approach, a chatbot that recommends movies faces far lighter obligations than a system used to screen job applicants or make medical diagnoses, and certain uses (like real-time mass biometric surveillance in public spaces) may be restricted or banned outright regardless of how technically accurate the system is. The underlying logic: the *appropriate amount of oversight* depends on what happens if the system gets something wrong, not on how technically sophisticated the system is.

## 7.9 "It might end humanity someday" vs "it's harming people today" — a real tension, not a contradiction

Public discussion about AI risk often splits into two camps that can look like they're arguing past each other. One focuses on **existential or catastrophic long-term risk** — speculative but potentially severe scenarios from highly advanced future systems. The other focuses on **present-day, documented harm** — biased sentencing tools, workers misclassified by an algorithm, disinformation spread at scale, all happening now, not hypothetically. These aren't actually mutually exclusive concerns, and treating them as a binary choice is usually a mistake: an organisation can (and arguably should) take concrete steps against measurable harms happening today — the kind covered throughout this chapter — while *also* taking speculative future risk seriously, without either concern being used to wave away the other as a distraction.

## 7.10 Applying What You've Learned

**Example 1**

*A credit-scoring algorithm appears neutral — it doesn't ask for race or gender directly — but a researcher discovers it heavily weights postal code, which correlates strongly with historically segregated neighbourhoods, indirectly reproducing racial disparities in loan approval. What does examining technology this way illustrate?*

A) Any algorithm using postal code as an input is automatically and formally illegal in every jurisdiction worldwide, regardless of what specific outcome that input is actually being used to help predict
B) It proves conclusively that credit-scoring algorithms are always more discriminatory than a human loan officer would be in every possible comparison, without needing to actually study or compare the two approaches
C) It has no real practical importance, since evaluating a system by its actual outcomes rather than by its stated design intentions is generally considered an illegitimate standard for judging technology
D) Thinking critically about technology means evaluating its actual real-world effects, not just its stated design intentions — a system can be technically "neutral" on paper while still reproducing discrimination through indirect proxies

*Walk through it:* A overreaches into a sweeping legal claim the scenario doesn't remotely support — using postal code as one input isn't automatically unlawful everywhere, the issue is the *specific discriminatory effect* it produces here. B draws a sweeping comparative conclusion ("always... in every comparison") from a single example, without any actual comparison to a human loan officer having been made. C dismisses the entire premise of evaluating a technology by its actual effects, which is precisely the wrong lesson to take from a case that exists *because* someone did exactly that evaluation. The real point, from section 7.1, is that surface-level neutrality (no explicit protected characteristic as input) doesn't guarantee fair outcomes if a correlated proxy does the same discriminatory work. That's **D**.

**Example 2**

*A health worker in a rural area with unreliable 2G connectivity uses a smartphone app that runs its malaria-diagnosis AI model directly on the device, needing no live internet connection. What technical approach makes this possible, and why does it matter specifically for this context?*

A) Edge AI — running inference directly on the device rather than depending on a live cloud connection, enabling continued operation exactly where connectivity is expensive, slow, or unreliable
B) Surveillance capitalism — an economic model built around collecting and commodifying user behavioural data for advertisers, unrelated to why an offline-capable diagnostic tool matters in this rural context
C) The automation paradox — a labour-market concept about automation reshaping which tasks humans focus on over time, unrelated to the specific technical connectivity solution being asked about here
D) Digital inequality — an accurate description of the underlying access problem the app is addressing, but not itself a description of the specific technical solution the app actually uses

*Walk through it:* B and C are each genuine concepts from this chapter, but neither one describes a *technical mechanism* — B is about a business model, C is about a labour-market dynamic, and this question is specifically asking what technical approach solves a connectivity problem. D is subtly wrong in a different way: it correctly names the *problem* the scenario is set against (digital inequality, from section 7.3) but the question is asking for the *solution*, not the backdrop. The specific technical approach — running the model on the device itself, no live connection required — is edge AI, from section 7.3's broader discussion. That's **A**.

**Example 3**

*A tech company publishes internal principles committing to assess potential harms before deploying any new AI feature, test for unfair treatment across demographic groups, and maintain a clear appeal process for users. What does this represent, and how does it differ from meeting the bare legal minimum?*

A) AI governance as something imposed exclusively by external government regulation, describing only what an outside regulator formally requires, with no voluntary internal component at all
B) Responsible AI as an ongoing organisational commitment — going beyond minimum legal compliance to proactively build in fairness assessment, transparency, and human appeal mechanisms as a continuous practice
C) Algorithmic accountability treated as a purely legal concept with no organisational or cultural dimension whatsoever, applying only to what a court or regulator can formally enforce
D) Federated learning — a specific technical method for training a shared model across many devices without centralising raw data, entirely unrelated to a company's own internal ethical principles

*Walk through it:* A mislabels a *voluntary, internal* company commitment as something imposed entirely from outside by government — but the scenario is explicit that the company published these principles itself, not that a regulator required this specific content. C draws an artificial, overly narrow boundary around "purely legal," when the scenario is describing exactly the kind of cultural and organisational practice that exists *alongside* and *beyond* legal requirements. D names a real but completely unrelated technical training concept, the kind of distractor that tests whether you're actually reading the scenario or just recognising vocabulary. The scenario describes responsible AI as a genuine, proactive, ongoing practice — from section 7.5 — going beyond whatever the bare legal minimum happens to require. That's **B**.

**Example 4**

*A bank uses a highly accurate deep learning model to approve or deny loan applications. When an applicant asks why they were denied, the bank can only say "the model's internal calculations produced a low score" — it cannot point to which specific factors drove the decision. What problem does this illustrate, and why does it matter?*

A) Dual-use technology — the concern that the same lending model could also be repurposed for a harmful application, a distinct issue from the applicant's inability to get a meaningful explanation for their own specific denial
B) Risk-based regulation — a framework for sorting AI applications into oversight tiers by potential harm, a policy-level concept distinct from this specific applicant's inability to get an explanation for their own denial
C) Surveillance capitalism — an economic model built around collecting and monetising user behavioural data, unrelated to why a complex lending model can't produce a human-readable explanation for its own decision
D) The explainability trade-off — highly accurate complex models are often the hardest to meaningfully explain, leaving the affected person with no real way to identify an error or contest the decision

*Walk through it:* A and B each name a real, related-sounding governance concept from this chapter, but neither addresses the specific technical difficulty of extracting a human-readable reason from an already-deployed model's output — that's a different problem than misuse potential or how the model should be regulated. C names an unrelated business-model concept that has nothing to do with a model's internal transparency. The core issue here, from section 7.6, is that this bank's model is accurate enough to be trusted with the decision but not transparent enough to be meaningfully explained or contested — the explainability trade-off. That's **D**.

**Example 5**

*A research lab publishes an open-source language model fine-tuned to explain complex medical literature in plain language for patients. Months later, security researchers discover the same open model can be prompted to generate detailed instructions for synthesising dangerous chemical compounds, since nothing about the underlying model was specific to medical topics alone. What does this illustrate?*

A) The explainability trade-off — a concern about a model's accuracy being hard to reconcile with a human's ability to understand why it produced a specific output, a distinct issue from a capability being usable for both helpful and harmful purposes
B) The automation paradox — a labour-market concept about how automating routine tasks reshapes what human workers do day-to-day, unrelated to a language model being usable for both a beneficial and a harmful purpose
C) Dual-use technology — the same underlying capability that enables a beneficial application can, without any separate malicious feature being added, also enable a harmful one, since the capability itself isn't cleanly separable by intended use
D) Algorithmic accountability — the principle that automated decisions affecting people's rights or opportunities should be transparent and contestable, a distinct concern from a general-purpose capability being repurposed for harm

*Walk through it:* A and D each name a real chapter concept, but neither is actually about one capability serving two different purposes — A is about explaining a model's specific output, D is about contestability of a decision that directly affects someone, and this scenario involves neither a low-transparency decision nor an unexplainable denial. B names a genuine labour-economics concept entirely unrelated to a capability being repurposed. The scenario is a textbook case from section 7.7: the same general capability (explaining complex technical text in plain language) that helps patients understand medical literature is, at the underlying-capability level, the same one that can explain chemistry papers a bad actor wants simplified — there's no clean technical line separating the two uses. That's **C**.

---

## Closing note

Notice the pattern across every single worked example in this book: the wrong answers are almost never *silly*. They're real terms, stated confidently, just applied to the wrong situation, or pushed to an extreme the actual scenario doesn't support, or quietly reversing what really happened. That's deliberate — it's exactly how the real quiz is built, and it's exactly the skill worth practising: not "do I recognise this word," but "does this specific claim actually follow from what's described, or does it just sound like it might."

Good luck in the Tech Challenge.
