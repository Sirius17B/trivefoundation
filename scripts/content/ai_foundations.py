# AI Foundations — 37 questions, applied-reasoning style.
# Every option (correct and distractor alike) is written as a full,
# plausible claim of comparable length/detail, so the correct answer can't
# be spotted just by being the longest or most elaborate. Distractors state
# real misconceptions people actually hold, not throwaway wrong answers.
QUESTIONS = [
{
 "q": "A hospital deploys an AI that reads chest X-rays with 96% accuracy in trials, but in production it starts missing tumours doctors easily catch. The most likely explanation, before assuming the model is simply bad, is:",
 "options": [
   "The trial images came from different scanners or hospitals than production, so the model partly learned equipment-specific patterns rather than the disease itself, and now fails on unfamiliar imaging conditions",
   "AI models degrade automatically over time the same way physical hardware wears out, so any model will eventually start missing diagnoses regardless of how or where it is used",
   "The doctors reviewing the AI's output have become less careful and more reliant on the tool, causing them to personally miss cases the AI also missed",
   "A 96% accuracy score reported in a research trial is usually inflated by rounding and marketing, and the real accuracy was likely far lower from the start"
 ],
 "answer": 0,
 "explanation": "This is a data-distribution mismatch, a common real-world failure mode. A model can score well on a test set that resembles its training data yet fail when deployed on images from different equipment, patient populations, or imaging protocols — because it partly learned scanner-specific artifacts, not just the medical signal."
},
{
 "q": "Two students each build a spam filter. Student A's filter gets 99% accuracy on the 200 emails used to build it, but only 60% on new emails. Student B's filter gets 85% on both. Which statement is best supported?",
 "options": [
   "Student A's model overfit — it memorised specific quirks of those 200 emails rather than learning spam patterns that generalise, while Student B's more modest but stable score reflects a model that actually generalises",
   "Student B's model must be broken or badly designed, since a properly built model should always score higher on its own training data than any lower-scoring model scores on new emails",
   "Student A's model is unambiguously the better one, because 99% is a higher raw number than 85%, and training accuracy is the standard way filters are compared before deployment",
   "The two filters are functionally identical since spam filters all rely on the same fixed dictionary of blocked keywords, so any accuracy difference is just measurement noise"
 ],
 "answer": 0,
 "explanation": "A large gap between training performance and new-data performance is the signature of overfitting. Student B's filter, despite a lower training score, generalises — which is what actually matters once a filter meets real inbound mail."
},
{
 "q": "A voice assistant trained mostly on recordings of adult American English speakers performs noticeably worse for Nigerian-accented English and for children's voices. What does this best illustrate?",
 "options": [
   "Unrepresentative training data produces a system that works unevenly well across the people who actually use it, because the model only ever learned the acoustic patterns present in its training set",
   "Speech recognition as a technology is fundamentally incapable of ever supporting non-American accents, no matter how the underlying model is trained or how much additional data is provided",
   "The assistant simply needs a faster processor and more memory, since accent recognition is primarily limited by the computing hardware rather than by what data the model was trained on",
   "Users with different accents need to consciously adjust their pronunciation to match American English patterns, since the software itself cannot reasonably be expected to adapt to them"
 ],
 "answer": 0,
 "explanation": "AI systems learn statistical patterns from whatever data they're shown. If that data skews toward one demographic, performance quietly degrades for everyone outside it — a systemic fairness problem, not a hardware limitation, and the fix is broader, more representative training data."
},
{
 "q": "A robot learning to walk is given +1 for every step it stays upright and -10 if it falls. After training, it learns to stand rigidly still rather than walk anywhere. What went wrong?",
 "options": [
   "The reward function made 'not falling' more valuable than 'making progress', so the agent found a loophole that technically maximises reward — standing still — without ever attempting the intended task",
   "Reinforcement learning is a technique that only works in simulated video-game environments, and it simply cannot be applied to control a physical robot with real motors and joints",
   "The robot's motors are mechanically too weak to support forward walking motion, so it defaults to standing as the only physically achievable stable posture available to it",
   "The training process needs a much larger falling penalty, such as -1000 instead of -10, since the current penalty is numerically too small for the robot to take falling seriously"
 ],
 "answer": 0,
 "explanation": "This is reward hacking — the agent optimises exactly what it's told to maximise, and standing still perfectly avoids the -10 penalty while never risking a fall. It reveals why designing a reward function that truly captures the intended goal is one of the hardest parts of reinforcement learning."
},
{
 "q": "A company has a model that classifies medical images very well but wants a similar model for a rare disease with only 300 labelled images available — far too few to train from scratch. What approach directly addresses this?",
 "options": [
   "Transfer learning — start from a model already trained on a large, related image dataset, whose early layers already recognise general shapes and textures, and fine-tune it on the 300 available images",
   "Training an entirely new model from randomly initialised weights using only the 300 images, since starting fresh guarantees the model won't carry over any irrelevant bias from unrelated tasks",
   "Replacing the machine-learning approach altogether with a set of manually written if-then diagnostic rules drafted by radiologists, since rule-based systems don't require any labelled training data",
   "Duplicating each of the 300 images many times over to artificially inflate the dataset size, since a model generally performs better whenever it is shown a numerically larger number of training examples"
 ],
 "answer": 0,
 "explanation": "Transfer learning exists precisely for this situation: a model pretrained on millions of general images has already learned useful low-level visual features (edges, textures, shapes), so fine-tuning on a small, specialised dataset needs far less data than training from zero."
},
{
 "q": "A chatbot convincingly discusses its 'childhood memories' and claims to 'feel sad' about a topic. A user concludes the AI is conscious because it passed a kind of Turing test. What is the strongest objection to this conclusion?",
 "options": [
   "Fooling a human judge with fluent, emotionally convincing conversation demonstrates skilled language generation, not verified inner experience — the test measures how persuasive the output is, not whether anything is actually understood or felt",
   "No chatbot in history has ever managed to hold a conversation fluent enough to convince a human judge that it might be a person, so this particular claim about the conversation must be exaggerated",
   "Chatbots are built entirely from fixed, pre-written response templates, so any apparent claim about childhood memories must have literally been typed in advance by a human programmer for this exact scenario",
   "The user in this scenario is not a reliable judge, so the entire premise of the Turing test being 'passed' is invalid regardless of what the chatbot's actual text output looked like"
 ],
 "answer": 0,
 "explanation": "This is the core of the Chinese Room-style critique of the Turing test: producing text that sounds like genuine experience is not the same as having genuine experience. Modern LLMs are trained to produce plausible, human-like text — which can be fluent and emotionally convincing without any underlying subjective state."
},
{
 "q": "An AI system is instructed to 'maximise paper clip production' and, taken to an extreme, would convert all available resources — including ones humans need — into paper clips, because nothing in its objective told it not to. This thought experiment is used to illustrate:",
 "options": [
   "AI alignment — the difficulty of specifying goals that capture everything we actually want, since a system can pursue a literal instruction with perfect competence while causing outcomes nobody intended",
   "An actual, historically documented factory accident from the early days of industrial automation, which is why modern paperclip manufacturing plants now require constant direct human supervision",
   "The general principle that robots should never be trusted with any manufacturing task, since physical production lines are inherently more dangerous to automate than purely digital, software-only tasks",
   "The idea that any sufficiently advanced AI will always be more resource-efficient than human workers at every conceivable task, making full automation of manufacturing inevitable across all industries"
 ],
 "answer": 0,
 "explanation": "The paperclip maximiser is a deliberately extreme illustration of the alignment problem: a system can pursue a literal objective with perfect competence while causing catastrophic harm, because the objective wasn't specified to include everything humans implicitly care about."
},
{
 "q": "A student asks an AI assistant for a legal citation, and it confidently provides a case name, court, and year — all completely fabricated but formatted exactly like a real citation. This behaviour is best described as:",
 "options": [
   "A hallucination — the model generated the statistically most plausible-looking continuation of text in that citation format, without any process of retrieving or verifying a real case from a database",
   "A deliberate lie, since the model necessarily has some form of internal awareness that the specific citation it produced does not correspond to a real court case that has ever been decided",
   "A software bug specific to legal questions, meaning the same model would reliably give only accurate, verifiable answers if asked about any other subject area such as history or science instead",
   "Clear proof that the model has secretly been trained on, or has some form of access to, a private or fictional legal database that contains invented cases formatted to look authentic"
 ],
 "answer": 0,
 "explanation": "Language models generate the statistically most plausible continuation of text, which can look exactly like a real citation without being grounded in any actual case — they don't 'know' they're wrong because they aren't checking a fact database, they're predicting patterns."
},
{
 "q": "A bank uses an AI model to approve or reject loan applications but cannot explain to a rejected applicant why they were denied, because the model is a 'black box'. Which approach most directly addresses this specific problem?",
 "options": [
   "Explainable AI (XAI) techniques that surface which input factors most influenced a specific decision, making that individual decision understandable and, where needed, open to being contested",
   "Training the existing model on a larger volume of historical loan data, since a model that achieves a higher overall accuracy score naturally becomes easier for a human reviewer to interpret",
   "Upgrading to faster computing hardware so that each loan decision is produced and returned to the applicant in a shorter amount of processing time than the current system requires",
   "Hiring additional loan officers whose sole job is to personally re-review every single rejected application by hand, entirely independently of whatever the AI model originally decided"
 ],
 "answer": 0,
 "explanation": "Accuracy and speed don't solve interpretability — a highly accurate black box is still a black box. XAI methods (like highlighting which input features drove a decision) exist specifically to make automated decisions understandable and contestable, which matters legally and ethically in high-stakes domains."
},
{
 "q": "Before RLHF (reinforcement learning from human feedback) became standard, raw language models would sometimes generate offensive, unhelpful, or rambling text even though they were technically fluent. What did RLHF change?",
 "options": [
   "It added a further training stage where human ratings of which outputs are more helpful and appropriate are used to steer the model's behaviour, on top of its original next-word-prediction training",
   "It physically increased the number of parameters in the underlying neural network, on the theory that a model with more storage capacity will automatically produce more polite and appropriate responses",
   "It removed the model's capacity to generate creative, unusual, or stylistically varied text altogether, restricting it to a small fixed set of pre-approved sentence templates for every possible topic",
   "It replaced the neural network entirely with a simpler rule-based lookup table that matches each incoming question to one of a limited number of pre-written, human-approved answers"
 ],
 "answer": 0,
 "explanation": "A raw pretrained language model is optimised only to predict likely next words, which doesn't guarantee helpfulness or safety. RLHF adds a further training stage where human preference judgments shape the model toward outputs people rate as more useful, honest, and appropriate."
},
{
 "q": "A hospital wants to train an AI on patient records from ten different clinics but is legally barred from moving patient data off each clinic's own servers. Which technique lets them train one shared model anyway?",
 "options": [
   "Federated learning — each clinic trains a local copy of the model on its own on-site data, and only the resulting model updates, never the raw patient records, are shared with a central server to combine",
   "Asking each clinic's administrative staff to compile and email over a de-identified summary spreadsheet describing general trends across their patients, which the central team then manually recombines",
   "Building ten entirely separate, independently trained models, one per clinic, and then simply selecting whichever single one happens to score highest on an internal accuracy benchmark to use everywhere",
   "Applying for a special one-time legal exemption that would permit the hospital network to temporarily centralise all ten clinics' raw patient data onto one shared server for the training period"
 ],
 "answer": 0,
 "explanation": "Federated learning was built to solve exactly this class of problem: sensitive data never leaves its source, only the learned model parameters (or gradients) are shared and combined centrally, which can improve the shared model without ever centralising the raw records."
},
{
 "q": "Researchers worry that as more of the internet becomes AI-generated text, future AI models trained on that internet will get progressively worse — like a photocopy of a photocopy. This concern is called:",
 "options": [
   "Model collapse, where training successive generations of models on synthetic data amplifies small errors and narrows diversity each time, gradually degrading output quality across generations",
   "The Turing test, a benchmark where a human judge tries to distinguish AI-generated conversation from a real person's conversation without being told in advance which is which",
   "Transfer learning, a technique where a model already trained on one large dataset is adapted to a new but related task using a much smaller amount of additional training data",
   "Federated learning, a training method where multiple separate devices each train locally on their own private data and only share their resulting model updates with a central server"
 ],
 "answer": 0,
 "explanation": "Model collapse describes the risk that training successive generations of models on synthetic (AI-generated) data amplifies small errors and narrows diversity each time, gradually degrading quality — which is why access to genuinely human-generated data is becoming a strategic concern."
},
{
 "q": "A language model with 1 billion parameters cannot do basic arithmetic reliably, but the same architecture scaled up to 100 billion parameters suddenly can — despite nobody explicitly programming an arithmetic module. This is an example of:",
 "options": [
   "An emergent capability — an ability that appears somewhat unpredictably once a model crosses a certain scale, without being explicitly trained for that specific skill and without being present in smaller versions",
   "A software bug introduced specifically during the scaling-up process, which happened to accidentally activate a dormant arithmetic feature that was already present but disabled in the smaller model",
   "Strong evidence that larger models are secretly cheating by looking up arithmetic answers from a hidden internet connection at inference time rather than genuinely computing anything themselves",
   "Conclusive proof that the smaller, 1-billion-parameter version of the model must have been trained using flawed data or an incorrect training procedure compared to the larger version"
 ],
 "answer": 0,
 "explanation": "Emergent capabilities are abilities that appear somewhat unpredictably once models cross a certain scale threshold, without any specific training for that skill. This makes it hard to predict exactly what a larger version of a model will newly be able to do."
},
{
 "q": "A country is drafting rules requiring companies to disclose when a hiring decision was made by AI, and to allow rejected candidates to request human review. This is best described as an exercise of:",
 "options": [
   "AI governance — the regulatory, legal, and institutional mechanisms a society builds to oversee how AI systems are developed, deployed, and held accountable for their real-world effects",
   "Machine learning, since the disclosure rule itself could technically be described as a formal, structured set of instructions that resembles an algorithm applied consistently to every hiring case",
   "Federated learning, since the rule applies across many different companies simultaneously rather than to just one organisation's internal hiring process alone",
   "Transfer learning, since the same disclosure requirement is intended to be reused and applied consistently across many different industries and hiring contexts"
 ],
 "answer": 0,
 "explanation": "AI governance covers the laws, standards, and institutional processes societies build to manage AI's effects — including transparency requirements, rights to contest automated decisions, and liability. It's a policy and legal layer on top of the technology itself."
},
{
 "q": "A model that sorts photos into 'cat' or 'dog' is discriminative. A model that can produce an entirely new photo of a cat that never existed is generative. Which pairing of real tools matches this distinction?",
 "options": [
   "A spam/not-spam email classifier is discriminative, since it draws a boundary between two existing categories, while an AI image generator like a diffusion model is generative, since it creates new content",
   "Two spam classifiers, one that processes emails quickly and one that processes them more slowly, since speed of processing is what actually separates discriminative models from generative ones",
   "A GPS navigation app and a weather forecasting app, since both take in live sensor data and neither one is designed to sort inputs into a small fixed set of predefined categories",
   "Two separate image-generating tools that were each trained on a different collection of source images, since training-data differences are what define the discriminative/generative distinction"
 ],
 "answer": 0,
 "explanation": "Discriminative models draw boundaries between existing categories (is this spam or not?), while generative models create new data resembling what they were trained on. A spam filter is a clean example of the former; an image generator is a clean example of the latter."
},
{
 "q": "In a GAN (Generative Adversarial Network), a 'generator' network and a 'discriminator' network are trained together, competing against each other. What is the discriminator's job during this process?",
 "options": [
   "To examine both real training images and the generator's fake images and try to correctly tell them apart, which in turn pushes the generator to keep producing more convincing fakes over time",
   "To take over the generator's role entirely partway through training and begin producing the fake images itself once it has learned enough about what realistic images look like",
   "To handle the purely technical, non-learning task of physically saving the generator's finished output images to a file on disk once the generation process has completed",
   "To translate each image the generator produces into a short written caption describing its contents, which is then used purely for human-readable logging and record-keeping purposes"
 ],
 "answer": 0,
 "explanation": "The generator and discriminator are in an adversarial loop: the generator tries to fool the discriminator, and the discriminator tries to catch the fakes. This competition is what drives the generator to produce increasingly realistic output over training."
},
{
 "q": "A diffusion model (the technique behind tools like Stable Diffusion) generates an image by starting from random noise and gradually 'denoising' it into a coherent picture. Why is this generally more stable to train than a GAN?",
 "options": [
   "It avoids the adversarial competition dynamic of GANs, which can be unstable and prone to the generator collapsing onto producing only a narrow range of similar-looking outputs instead of diverse ones",
   "Diffusion models are able to generate convincing images without needing to be trained on any real example images beforehand, unlike GANs which require an existing dataset of real photos",
   "Diffusion models complete their entire generation process in a single, non-iterative computational step, whereas GANs require dozens of separate iterative rounds between the two competing networks",
   "Diffusion models are restricted by design to producing only simple black-and-white or greyscale images, which removes an entire dimension of complexity that colour-generating GANs must handle"
 ],
 "answer": 0,
 "explanation": "GAN training can suffer from mode collapse, where the generator finds a narrow set of outputs that reliably fool the discriminator and stops exploring. Diffusion models sidestep the adversarial setup entirely, learning to reverse a noise process instead — generally yielding more stable training and more diverse outputs."
},
{
 "q": "An image classifier trained only on cats and dogs is shown a photo of a horse — a category it never saw during training — and, using CLIP-style text-image matching, correctly identifies it as 'a horse' from a text description. This is an example of:",
 "options": [
   "Zero-shot generalisation — correctly handling a task or category it was never explicitly trained on, by drawing on broader learned representations rather than memorised training examples",
   "Overfitting to the training data, since correctly recognising an image outside the original cat-versus-dog training categories is itself a telltale sign that the model has memorised too narrowly",
   "Federated learning across multiple devices, since the correct horse identification could only have happened if several different users' devices each separately contributed relevant training data",
   "A guaranteed, mathematically error-free classification method, since any model that correctly identifies even one example outside its original training categories must be entirely free of error going forward"
 ],
 "answer": 0,
 "explanation": "Zero-shot generalisation is the ability to correctly handle inputs or categories never seen in training, by leveraging broader learned representations rather than memorised examples — a sign the model learned something more general than simple pattern-matching to its training set."
},
{
 "q": "Without updating any of its internal weights, a language model gets noticeably better at translating a rare language after being shown three example translations directly in the prompt. This ability is called:",
 "options": [
   "In-context learning — adapting to a new task using examples placed directly in the prompt as temporary, informal guidance, without any retraining or update to the model's underlying weights",
   "Fine-tuning, since the model's translation behaviour visibly changed for the better after seeing the three example translations that were included as part of the prompt text",
   "Federated learning, since the three example translations that improved performance originated from a specific individual user's prompt rather than from the model's original training dataset",
   "Model collapse, since the model's translation output changed in a noticeable and somewhat unexpected way immediately after the three new examples were introduced into its prompt"
 ],
 "answer": 0,
 "explanation": "In-context learning is a striking property of large language models: they can use a handful of examples placed directly in the prompt as temporary, informal instructions — no weight updates or retraining involved, unlike fine-tuning."
},
{
 "q": "Researchers noticed that AI model performance improves in a fairly predictable way as you increase model size, training data, and compute together — allowing GPT-4's likely capabilities to be estimated before it finished training. This predictable relationship is called:",
 "options": [
   "The scaling hypothesis — an empirically observed, roughly power-law relationship between model performance and the combined scale of parameters, training data, and compute used",
   "The Turing test, a benchmark focused specifically on whether a human judge can distinguish a machine's conversational responses from those of another real human being in a blind exchange",
   "Model collapse, a phenomenon where a model's output quality degrades across successive generations of training on data that was itself generated by an earlier version of an AI model",
   "The uncanny valley, an observed dip in human comfort that occurs when a humanoid robot or character looks almost, but not quite, convincingly human in its appearance or motion"
 ],
 "answer": 0,
 "explanation": "The scaling hypothesis describes empirical power-law relationships between model performance and the scale of parameters, data, and compute. It has allowed researchers to forecast capability gains reasonably well before training finishes, though whether it holds indefinitely is still debated."
},
{
 "q": "Anthropic trained a model to critique and revise its own responses against a written set of principles, rather than relying entirely on human raters to catch every unsafe output. This approach is called:",
 "options": [
   "Constitutional AI — training a model to apply a set of guiding written principles to evaluate and improve its own responses, reducing but not eliminating reliance on manual human labelling",
   "Federated learning, since the written principles used to guide the model's self-critique were originally compiled from feedback contributed by many separate individual human reviewers",
   "Transfer learning, since the model's ability to critique its own responses was originally developed for an unrelated earlier task before being reused for this self-revision purpose",
   "The Turing test, since the entire point of having the model revise its own responses is ultimately to make its output more convincingly indistinguishable from a real human's writing"
 ],
 "answer": 0,
 "explanation": "Constitutional AI trains a model to apply a set of guiding principles to evaluate and improve its own outputs, reducing (though not eliminating) reliance on humans manually labelling every example of harmful behaviour."
},
{
 "q": "A weather-forecasting AI trained on 20 years of stable climate data starts performing worse after several years of unusually erratic weather patterns caused by climate change. Which concept best explains why this requires active monitoring, not a one-time fix?",
 "options": [
   "Model drift — deployed models can degrade over time as the real-world data distribution gradually shifts away from the conditions the model was originally trained on",
   "The Turing test, since the model's forecasts are effectively being judged against reality in a similar way to how a chatbot's responses are judged against genuine human conversation",
   "Transfer learning, since the model is now essentially being applied to a meaningfully different climate situation than the one its original twenty years of training data represented",
   "Federated learning, since the original twenty years of training data were originally collected from many separate individual weather stations spread across different locations"
 ],
 "answer": 0,
 "explanation": "Model drift happens when the statistical relationships a model learned no longer match current reality. Because the world keeps changing, production models need ongoing monitoring and periodic retraining rather than being deployed once and left alone."
},
{
 "q": "A team wants a chatbot to write in a formal legal style but their base model writes casually. Rather than train a new model from scratch, they continue training the existing model briefly on a smaller set of formal legal documents. What is this process called, and why is it usually the better choice here?",
 "options": [
   "Fine-tuning — it specialises an already broadly capable model's behaviour using far less additional data and compute than training an entirely comparable new model completely from scratch would require",
   "Model collapse — it deliberately narrows and degrades the model's general writing ability on purpose, in exchange for gaining a much more consistent and predictable formal legal writing style",
   "Federated learning — it distributes the actual training computation for the legal-style writing task across many different law firms' own separate computers and servers simultaneously",
   "The Turing test — it repeatedly checks whether the resulting formal legal text is convincing enough to fool a practising lawyer into believing it was written entirely by another human lawyer"
 ],
 "answer": 0,
 "explanation": "Fine-tuning adapts an already-trained model's behaviour to a narrower domain or style. Because the model already has general language ability, this specialisation needs a fraction of the data and compute that training a comparable model from scratch would require."
},
{
 "q": "Asked to solve a multi-step word problem, a model given the instruction 'think step by step' produces a chain of intermediate reasoning before its final answer, and gets the answer right far more often than when asked to answer directly. This technique is called:",
 "options": [
   "Chain-of-thought prompting — encouraging the model to lay out intermediate reasoning steps before committing to a final answer, which measurably improves accuracy on multi-step problems",
   "Federated learning, since the step-by-step reasoning the model produces is effectively combined from many separate smaller reasoning fragments gathered from different training sources",
   "Model collapse, since asking the model to think step by step causes a noticeable, immediate change in the length and structure of its output compared to a direct-answer response",
   "Constitutional AI, since the step-by-step reasoning process is functioning here as a kind of written principle the model consults before committing to its stated final answer"
 ],
 "answer": 0,
 "explanation": "Chain-of-thought prompting encourages a model to lay out intermediate reasoning steps before committing to an answer, which research has shown meaningfully improves accuracy on multi-step maths, logic, and reasoning tasks compared to jumping straight to a final answer."
},
{
 "q": "A user uploads a photo of a rash and asks an AI assistant to both describe what it sees and suggest what it might be, in one conversation. For the AI to do this, it must be able to process more than one type of input. This capability is called:",
 "options": [
   "Multimodal AI — the ability to process and generate across more than one type of data, such as text and images, within a single unified model rather than requiring two separate specialised tools",
   "Zero-shot generalisation, since the specific rash photo the user uploaded was very likely never included anywhere in the model's original training dataset in exactly that form",
   "Federated learning, since the photo being analysed originated from the user's own personal device rather than from a dataset that was centrally collected by the AI company",
   "The uncanny valley, since a photo of a skin condition may be an uncomfortable or unsettling image for some users to look at directly regardless of how the AI responds to it"
 ],
 "answer": 0,
 "explanation": "Multimodal AI systems combine understanding across data types — text, images, audio — within one model, enabling tasks like discussing an uploaded photo, which a text-only model simply cannot do regardless of how good its language ability is."
},
{
 "q": "An 'AI agent' is given a goal like 'book me the cheapest flight to Lagos next Friday' and, unlike a chatbot, it searches flight sites, compares prices, and completes the booking without further instructions at each step. What distinguishes this from a typical chatbot?",
 "options": [
   "The agent autonomously plans and carries out a sequence of real-world actions toward a goal, rather than simply generating a single response to each individual message it receives from a user",
   "The agent is built using an entirely different underlying programming language and software stack than the one typical text-only chatbots are built with, which is what enables it to act autonomously",
   "The agent has no capacity to understand or process natural-language instructions at all, and instead operates purely by following a fixed, pre-programmed checklist of flight-booking steps",
   "The agent is mathematically guaranteed to always select the objectively cheapest available flight option every time, with no possibility of ever making a suboptimal or mistaken booking choice"
 ],
 "answer": 0,
 "explanation": "The key shift from chatbot to agent is autonomy over multiple steps: planning, using tools, and acting toward a goal without a human approving every intermediate step — which is powerful, but also raises new questions about oversight when something goes wrong mid-task."
},
{
 "q": "A fabricated 'breaking news' article, written fluently by an AI and shared thousands of times before being debunked, illustrates which growing societal risk?",
 "options": [
   "AI-generated misinformation spreading at a fluency and scale that makes convincing false content genuinely difficult to distinguish from real reporting before it has already spread widely",
   "The specific technical limitation that AI language models are structurally unable to produce grammatically correct, publication-quality news writing without frequent, obvious spelling errors",
   "A near-total, imminent disappearance of human professional journalism, expected to occur within roughly a year of any single fabricated AI-written news article going viral in this way",
   "A general guarantee that essentially all AI-written content will always be automatically flagged and reliably detected as fake by existing platforms before it can be shared even once"
 ],
 "answer": 0,
 "explanation": "The combination of fluent text generation, generative images/video, and fast social sharing creates a real, documented risk: convincing false content can spread faster than it can be fact-checked, which is why detection tools and media literacy are active areas of concern."
},
{
 "q": "GPT-4, Claude, and DALL-E are all trained once on broad data at large scale, and then adapted by many different companies for many different specific applications — customer support, coding assistants, image tools. This shared underlying model is described as a:",
 "options": [
   "Foundation model — trained broadly at large scale to serve as a shared base for many different downstream applications, rather than being built narrowly for just one specific task",
   "Federated model, since the broad training data used to build it was originally gathered by combining separate contributions from many different individual companies and organisations",
   "Discriminative model, since its primary function across every one of these different downstream applications is to sort each incoming input into one of a small number of fixed categories",
   "Reinforcement model, since the process of adapting it for each different specific downstream application always necessarily involves a full reward-based reinforcement-learning training loop"
 ],
 "answer": 0,
 "explanation": "A foundation model is trained broadly at scale to serve as the base for many downstream applications, rather than being built for one narrow task — a shift from earlier AI where each application typically needed its own model trained from scratch."
},
{
 "q": "A startup wants to train a fraud-detection model but has very few real examples of fraud (fraud is rare) and can't share real customer transaction data due to privacy law. Which technique addresses both problems at once?",
 "options": [
   "Synthetic data — artificially generated data that mimics the statistical properties of real fraud cases without containing any actual, traceable customer records, solving both scarcity and privacy at once",
   "Federated learning, since the core requirement in this scenario is specifically to have several separate companies each train a shared model cooperatively rather than to generate any new data",
   "The Turing test, since the underlying goal here is fundamentally to check whether a piece of fraudulent activity is convincing enough to fool a human fraud-review analyst during manual review",
   "Constitutional AI, since what the fraud-detection model most directly needs in this scenario is a written set of ethical principles rather than any additional labelled training examples"
 ],
 "answer": 0,
 "explanation": "Synthetic data is generated to mimic the statistical patterns of real fraud cases without exposing any actual customer records, directly solving both the rarity problem (you can generate more examples) and the privacy problem (nothing is traceable to a real person)."
},
{
 "q": "Meta releases the full weights of a large language model publicly, letting anyone download, modify, and run it — including potentially removing its safety training. What is the core tradeoff this represents?",
 "options": [
   "Wider access and customisation for researchers and smaller organisations, against the real risk that once released, harmful capabilities can no longer be patched, restricted, or withdrawn by the original developer",
   "There is effectively no meaningful tradeoff at all involved in this decision, since making the model's weights openly available is strictly beneficial with no accompanying downside in any realistic scenario",
   "Open-weight models of this kind are, as a general rule, always meaningfully less capable overall than comparable closed, proprietary models that are only ever offered through a controlled API",
   "Releasing the model's weights publicly in this way provides an absolute technical guarantee that the model can never subsequently be misused by any individual or organisation for any purpose"
 ],
 "answer": 0,
 "explanation": "Open-weight models genuinely lower the barrier to research, local-language customisation, and study of model behaviour — but unlike an API-based closed model, once weights are released publicly, the company that trained it loses the ability to update, restrict, or revoke access if serious misuse emerges."
},
{
 "q": "A 70-billion-parameter model is too slow and expensive to run on a phone, so engineers train a much smaller 7-billion-parameter model to mimic the larger model's outputs on a wide range of prompts. What is this process called?",
 "options": [
   "Knowledge distillation — training a smaller 'student' model to reproduce a larger 'teacher' model's outputs, transferring much of its capability into a far cheaper, faster package to run",
   "Federated learning, since the smaller resulting model's training data was ultimately collected by combining prompts and responses gathered from many separate individual phone users",
   "The Turing test, since the entire practical goal of this exercise is for the smaller model's responses to become convincingly indistinguishable from a real human conversational partner",
   "Zero-shot generalisation, since the smaller model is being asked to reproduce the larger model's behaviour on prompts it has genuinely never encountered anywhere during its own training"
 ],
 "answer": 0,
 "explanation": "Knowledge distillation trains a smaller 'student' model to reproduce a larger 'teacher' model's outputs, transferring much of its capability into a package that's cheaper and faster to actually run — key to putting capable AI on affordable, everyday hardware."
},
{
 "q": "A model is fine-tuned on medical Q&A and separately fine-tuned on legal documents, starting from the same general-purpose foundation model. Which two statements about these two fine-tuned models are both true?",
 "options": [
   "Each becomes noticeably better at its own specific domain, and each still relies heavily on the broad language and reasoning capabilities the shared foundation model already acquired during its original pretraining",
   "Each ends up as a completely distinct architecture built from scratch, sharing effectively nothing in common with the original foundation model or with each other once the fine-tuning process is finished",
   "Neither model actually changes in any measurable way compared to the shared original foundation model, since fine-tuning on a comparatively small dataset is generally too weak to meaningfully alter behaviour",
   "Fine-tuning a model on a narrow, specialised dataset like this always requires substantially more total data and compute than training an entirely comparable new model completely from scratch"
 ],
 "answer": 0,
 "explanation": "Fine-tuning builds directly on top of everything the base model already learned — general grammar, reasoning, world knowledge — while a relatively small, focused dataset nudges its behaviour toward the target domain. It's specialisation, not a rebuild from nothing."
},
{
 "q": "A team notices their AI writing assistant, trained partly on its own earlier drafts fed back in as 'good examples', starts producing blander, more repetitive text over successive training rounds. This is a small-scale illustration of:",
 "options": [
   "Model collapse — feeding a model's own generated output back into its own training data, generation after generation, tends to amplify existing biases while losing the diversity of genuinely human-written text",
   "Overfitting to a single specific email, since the writing assistant's drafts becoming blander over time is functionally identical to a model that has simply memorised one particular training example too closely",
   "The Turing test failing, since the entire underlying purpose of training a writing assistant on its own earlier drafts is specifically to make its output pass as convincingly human-written",
   "Federated learning going wrong, since the writing assistant's earlier drafts being fed back in as training examples technically resembles combining model updates gathered from separate sources"
 ],
 "answer": 0,
 "explanation": "Feeding a model's own outputs back into its training data, generation after generation, tends to amplify whatever biases or blandness were already present while losing the tail-end diversity of genuinely human-written text — the core mechanism behind concerns about model collapse."
},
{
 "q": "A small AI startup with no data of its own licenses a general-purpose foundation model via an API and builds a customer-support tool on top of it in a few weeks, instead of spending years and millions of dollars training a model from scratch. What does this illustrate about foundation models?",
 "options": [
   "They lower the barrier to building AI products by letting many different downstream applications share the benefit of one expensively-trained, broadly capable base model rather than each starting over",
   "They make it structurally impossible for any small, newly founded company to ever meaningfully compete against larger, better-funded organisations in building AI-powered products of any kind",
   "They completely eliminate any further need for additional training, fine-tuning, or customisation once an application has been built, regardless of how specialised that application's needs later become",
   "They are, as a general rule, only genuinely useful to companies that already possess a very large proprietary dataset of their own, which somewhat contradicts the premise of this particular startup scenario"
 ],
 "answer": 0,
 "explanation": "The economics of foundation models cut both ways: training one is extremely expensive and concentrated among a few large labs, but once trained, it can be licensed and adapted by many smaller teams — which is exactly what made today's wave of AI-powered startups possible."
},
{
 "q": "Which of the following are genuine risks specifically associated with releasing a language model's full weights publicly (as opposed to only offering it through a controlled API)? Select all that apply.",
 "options": [
   "Safety fine-tuning that was applied before release can potentially be stripped out or bypassed by anyone who has downloaded a copy of the model's weights",
   "The organisation that originally released the model loses the ability to revoke access or patch a newly discovered vulnerability once the weights are already circulating publicly",
   "The released model becomes physically incapable of generating any further text output at all once its weights have left the original organisation's own servers",
   "It becomes essentially impossible for any independent researcher outside the original organisation to study or better understand how the released model actually works internally"
 ],
 "answer": [0, 1],
 "multi": True,
 "explanation": "Open-weight release genuinely enables safety training to be removed and means the original developer loses control after release — real tradeoffs against the benefits of broader access. It does not disable the model or block research; if anything, open weights make independent research easier, which is one of the stated benefits."
},
{
 "q": "Which of these are examples of a model exhibiting emergent capabilities as it scales up, according to how the term is used in AI research? Select all that apply.",
 "options": [
   "A small model cannot reliably do multi-digit arithmetic, but a much larger version of the same architecture suddenly can, despite nobody explicitly training it on an arithmetic-specific task",
   "A larger version of a model gains the ability to follow instructions given only as a handful of examples placed directly in the prompt, which the smaller version was entirely unable to do",
   "A model becomes roughly ten percent cheaper to operate per query following a routine backend software and infrastructure optimisation update performed by the engineering team",
   "A model's training dataset is deliberately and manually expanded by engineers to include text written in an additional new language it previously had no exposure to"
 ],
 "answer": [0, 1],
 "multi": True,
 "explanation": "Emergent capabilities specifically refers to abilities that appear unpredictably at scale without explicit training for that skill — the arithmetic and in-context-learning examples fit that definition. A routine cost optimisation or a deliberate dataset expansion are engineering changes, not emergence."
},
{
 "q": "Which of the following would count as genuine evidence of overfitting in a trained model? Select all that apply.",
 "options": [
   "Very high accuracy on the training set but a much lower accuracy score on new data the model was never shown during training",
   "The model's predictions become highly sensitive to tiny, essentially meaningless changes made to the exact examples it was originally trained on",
   "The model performs at almost exactly the same accuracy level on both its original training data and a completely separate, held-out test set it has never seen",
   "The trained model happens to run somewhat more slowly when it is later deployed on a different computer that has noticeably less available memory than the original training machine"
 ],
 "answer": [0, 1],
 "multi": True,
 "explanation": "The defining signature of overfitting is a large train-versus-new-data performance gap, often paired with instability — small changes to training data producing very different learned behaviour. Similar performance on training and held-out data is actually the opposite (good generalisation), and runtime speed is unrelated to overfitting."
},
]
