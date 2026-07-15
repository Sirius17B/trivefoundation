# THRIVE QUIZ TOPIC REFERENCE — Study Book v5.3
## A Study Guide for the Tech Challenge and Football Arena

*THRIVE — Technology, Hard work, Resilience, Innovation, Vision, and Excellence*
*For participants of the THRIVE Tech Challenge (50 questions per session) and Football Arena (25 questions per session)*

---

## Table of Contents

**Part One: Technology**
- Chapter 1: Artificial Intelligence — Foundations
- Chapter 2: Large Language Models and Generative AI
- Chapter 3: Robotics
- Chapter 4: Cybersecurity and Networks
- Chapter 5: Data Science and Analytics
- Chapter 6: Emerging Technology, IoT, and the Digital Economy
- Chapter 7: AI Ethics, Society, and Nigeria's Digital Future
- Chapter 8: Programming and Computational Thinking
- Chapter 9: Cloud, DevOps, and Systems Engineering
- Chapter 10: Data Engineering

**Part Two: Football**
- Chapter 11: The Laws of the Game
- Chapter 12: Tactics and Modern Football Philosophy
- Chapter 13: World Football History
- Chapter 14: Nigerian and African Football
- Chapter 15: Positions, Statistics, and the Modern Game

**Appendix A: Practice Question Answers**
**Appendix B: Key Terms Glossary**

---

# PART ONE: TECHNOLOGY

---

## Chapter 1: Artificial Intelligence — Foundations

### 1.1 What AI Actually Is

Artificial Intelligence is the field of computer science concerned with building machines that can perform tasks that normally require human intelligence: recognising speech, understanding language, identifying images, learning from experience, and making decisions.

Every AI system you interact with today is **narrow AI** (Artificial Narrow Intelligence, or ANI). It is exceptional at one specific task and useless at everything else. The chess program Deep Blue beat world champion Garry Kasparov in 1997 — a remarkable feat — but it could not hold a conversation, drive a car, or write a poem.

**Artificial General Intelligence (AGI)** — a machine that can learn and apply knowledge across any domain the way humans can — does not yet exist. This distinction matters enormously when you read news headlines about AI.

### 1.2 How Machines Learn

Traditional programming required humans to write explicit rules. Machine learning turned this upside down: given labelled examples, the system discovers its own patterns.

The three main types:

**Supervised learning** trains on labelled examples (this photo is a cat; that one is a dog). Used in medical diagnosis, fraud detection, spam filtering, and voice recognition.

**Unsupervised learning** has no labels. The system finds hidden structure in data: grouping customers by behaviour, detecting unusual network activity.

**Reinforcement learning** has an agent trying actions in an environment, receiving rewards for good ones and penalties for bad ones. AlphaGo used reinforcement learning to master Go, defeating the world champion 4-1 in 2016.

### 1.3 Key Concepts to Know

**Overfitting**: A model memorises training data rather than learning generalisable patterns. Performs brilliantly on training data but poorly on new data. Like a student who memorised every past exam question verbatim but fails any rephrased question.

**Transfer learning**: Using a model pre-trained on a large dataset as a starting point for a different but related task. Requires far less data than training from scratch.

**Emergent capabilities**: Abilities that appear in large models that were not present in smaller versions and were not explicitly trained for — arising from scale alone.

**The Turing Test**: A test where a human judge cannot distinguish AI text responses from human responses. Critics argue it tests deception not true understanding.

**AI hallucination**: When an AI generates false information stated with apparent confidence. LLMs are pattern completers, not knowledge databases — they generate statistically likely text, not verified truth.

### 1.4 Practice Questions — Chapter 1

1. A chess program beats the world champion but cannot drive a car. What AI concept does this illustrate?
   A) General AI — AI that exceeds humans in all domains
   **B) Narrow AI — highly capable at one specific task but unable to transfer ability to other domains** ✓
   C) Machine consciousness
   D) Supervised learning

2. What is the key difference between a rule-based AI system and a machine learning system?
   A) Rule-based systems are always faster
   **B) Rule-based systems follow explicit human-written rules; ML systems discover rules from data** ✓
   C) Rule-based systems require the internet; ML does not
   D) ML systems are always rule-based under the hood

3. An AI model performs brilliantly on training data but poorly on new unseen data. What is this called?
   A) Underfitting — the model did not learn enough
   **B) Overfitting — the model memorised the training data rather than learning generalisable patterns** ✓
   C) Data leakage — test data was seen during training
   D) Gradient explosion — a training instability

4. What is reinforcement learning?
   A) Teaching AI by giving it a massive text dataset
   **B) Training an AI agent through trial and error — rewarding good actions and penalising bad ones** ✓
   C) A technique for speeding up neural network training
   D) Programming explicit rules for the AI to follow

5. Why does diverse, representative training data matter for AI systems?
   A) More data always makes models run faster
   **B) AI systems learn patterns from data; biased or unrepresentative data produces biased AI that performs unfairly for underrepresented groups** ✓
   C) Data quantity matters more than quality or diversity
   D) Diverse data increases cost and should be minimised

---

## Chapter 2: Large Language Models and Generative AI

### 2.1 What an LLM Actually Is

An LLM is a neural network trained on vast amounts of text. The breakthrough architecture that made modern LLMs possible is called the **transformer**, described in the 2017 paper "Attention Is All You Need." Transformers use self-attention that allows the model to consider the relationship between every word in a sequence simultaneously.

LLMs can produce remarkably fluent, contextually appropriate text. But they hallucinate, have a knowledge cutoff date, and do not truly understand what they write.

### 2.2 Key Techniques

**Retrieval-Augmented Generation (RAG)**: Grounds LLM responses in verified, current information. Before answering, the system searches a knowledge base and retrieves relevant information included in the prompt.

**Chain-of-thought prompting**: Asks the model to reason step-by-step before reaching a conclusion. Research showed this dramatically improves accuracy on maths, logic, and multi-step problems.

**Fine-tuning**: Further trains a pre-trained LLM on a smaller, task-specific dataset to specialise its behaviour.

**RLHF (Reinforcement Learning from Human Feedback)**: Human raters evaluate AI responses. These ratings fine-tune the model to be more helpful, harmless, and honest.

**Constitutional AI** (Anthropic): An AI trained using a set of principles that guide its behaviour — the AI critiques and revises its own outputs against these principles during training.

### 2.3 Generative AI

**Discriminative AI** draws boundaries: is this photo a cat or dog?
**Generative AI** creates new instances: generate a photo of a cat wearing a hat.

A **GAN (Generative Adversarial Network)**: Two neural networks compete — a generator creates synthetic data trying to fool the discriminator, while the discriminator tries to distinguish real from generated data.

**Diffusion models**: Learn to gradually remove noise from random noise to create coherent images. Powers Stable Diffusion, DALL-E, and Midjourney.

### 2.4 Practice Questions — Chapter 2

1. What is the transformer architecture and why did it revolutionise AI?
   A) Physical hardware converting electricity to power AI chips
   **B) A neural network design from the 2017 paper 'Attention Is All You Need' — using self-attention mechanisms to process all parts of a sequence simultaneously** ✓
   C) A software framework for managing AI data pipelines
   D) A method of converting speech to text

2. What is retrieval-augmented generation (RAG) and what problems does it solve?
   A) A system for robots to reach objects and then generate a description
   **B) A system where an LLM retrieves relevant information from an external knowledge base before generating a response — addressing knowledge cutoffs and hallucination** ✓
   C) A method of generating larger amounts of synthetic training data
   D) A way to make LLMs generate text responses faster

3. What is a diffusion model?
   A) A model that makes AI training faster by diffusing learning across layers
   **B) A generative model that learns to gradually remove noise from random noise to create coherent images — powers Stable Diffusion, DALL-E, and Midjourney** ✓
   C) A model that spreads AI capabilities across different devices
   D) A way of mixing different AI models together

4. What is RLHF and why did it improve AI assistants?
   A) Humans physically training robots through demonstration
   **B) A technique where humans rate AI outputs and those ratings train the model to be more helpful, harmless, and honest** ✓
   C) Remote Learning and Human Facilitation — an education technology method
   D) Recursive Language Hierarchy Framework — a training architecture

5. What is zero-shot generalisation in AI?
   A) An AI that achieves perfect accuracy on the first try
   **B) The ability of a model to correctly handle tasks or classes it has never been explicitly trained on — using broader learned representations and reasoning** ✓
   C) A model that does not require any training data at all
   D) An AI that learns a task in zero seconds

---

## Chapter 3: Robotics

### 3.1 Why Robotics Is Hard — Moravec's Paradox

A computer can beat any human at chess, but a robot struggles to pick up a cup from a table. This is **Moravec's paradox**: tasks that are easy for humans (walking, recognising faces, grasping unfamiliar objects) are extraordinarily difficult for computers, while tasks hard for humans (chess, arithmetic) are relatively easy for computers.

Easy human tasks evolved over millions of years and rely on vast implicit knowledge that humans have never needed to make explicit. Nobody taught you to balance when you stand up.

### 3.2 Navigation: SLAM

**SLAM (Simultaneous Localisation and Mapping)**: A robot's ability to build a map of an unknown environment while simultaneously tracking its own location within that map. Roomba vacuum cleaners use simplified SLAM to navigate your floor. Mars rovers use it to navigate the Martian surface.

### 3.3 Types of Robots

**Collaborative robots (cobots)**: Have force and torque sensors detecting contact and stopping immediately — enabling them to safely work alongside human workers without safety cages.

**Soft robots**: Made from compliant, flexible materials (silicone, elastic polymers). Can handle fresh produce without bruising, navigate earthquake rubble, search inside the human body.

**Swarm robotics**: Large numbers of simple robots following basic rules, producing complex collective behaviour — inspired by ant colonies and bird flocking.

### 3.4 Key Concepts

**Digital twins**: Precise virtual simulations of physical systems updated in real time with sensor data. Used for testing, monitoring, and optimisation without risking the physical system.

**Sim-to-real transfer**: AI trained in a physics simulation often fails in the real world because simulations cannot perfectly model friction, sensor noise, lighting variations. Domain randomisation — training in many varied simulated environments — helps bridge this gap.

**The uncanny valley**: As robots become more human-like, human affinity increases — then drops sharply into discomfort just before perfect human likeness. This is why Pepper the robot is deliberately cartoonish.

### 3.5 Practice Questions — Chapter 3

1. What is SLAM in robotics?
   A) A programming language used specifically for robot control systems
   **B) Simultaneous Localisation and Mapping — a robot's ability to build a map of an unknown environment while simultaneously tracking its own location** ✓
   C) A safety mechanism that stops a robot immediately in emergencies
   D) A programming technique for synchronising multiple robot actuators

2. What is Moravec's paradox?
   A) The observation that robots are always better than humans if given enough time
   **B) The counterintuitive finding that tasks easy for humans (walking, recognising faces) are extraordinarily difficult for computers, while tasks hard for humans (chess, arithmetic) are relatively easy** ✓
   C) The paradox that more capable robots are always less safe
   D) The observation that robots become more useful as they become more autonomous

3. What is soft robotics?
   A) Robot control software that is easy to program and modify
   **B) Robots constructed from compliant, flexible materials (silicone, elastic polymers, textiles) rather than rigid metals — enabling them to deform, fit through tight spaces, grasp delicate objects safely** ✓
   C) Robots designed specifically for children as educational toys
   D) Robots with user-friendly interfaces that require no technical expertise

4. What is a collaborative robot (cobot) and how does it differ from traditional industrial robots?
   A) A robot that works with other robots only, separate from all humans
   **B) A robot designed to work safely alongside human workers using force limiting and sensors to prevent injury — contrasted with traditional industrial robots that must be physically separated from people behind safety cages** ✓
   C) A robot programmed collaboratively by multiple engineers simultaneously
   D) Two robots working together on a shared task without any human involvement

5. What is teleoperation in robotics?
   A) A robot operating fully autonomously at a great distance
   **B) A human operator controlling a robot remotely in real time — used in dangerous environments (nuclear sites, deep ocean, bomb disposal) and in surgery (da Vinci surgical system)** ✓
   C) A robot communicating with other robots remotely without human involvement
   D) A type of robot that can only function over a telephone network connection

---

## Chapter 4: Cybersecurity and Networks

### 4.1 The CIA Triad

All cybersecurity thinking begins with three core properties:
- **Confidentiality**: Only authorised parties access information. Encryption protects confidentiality.
- **Integrity**: Data is accurate and has not been altered. Hash functions provide integrity checks.
- **Availability**: Systems and data are accessible when needed. Ransomware attacks target availability.

### 4.2 Key Attack Types

**Social engineering**: Manipulating people psychologically to circumvent security — exploiting trust, authority, urgency, and helpfulness. The most sophisticated firewall is useless if an attacker can simply phone an employee and trick them into revealing their password.

**SQL injection**: User-supplied input is included directly in an SQL query string — allowing attackers to manipulate the query. Prevented by prepared statements that separate SQL code from data.

**Supply chain attack**: Compromising a trusted software vendor or update mechanism to reach all downstream customers. SolarWinds (2020): 18,000 organisations including US government agencies compromised through one supplier.

**Zero-day vulnerability**: A security vulnerability unknown to the software vendor — therefore with no patch available.

### 4.3 Defences

**Zero-trust security**: Never trust, always verify — every access request is authenticated regardless of location.

**Two-factor authentication (2FA)**: Requiring a second verification factor (a code sent to your phone, an authenticator app code) in addition to your password.

**End-to-end encryption (E2EE)**: Only the communicating parties can read messages — the service provider holds no decryption keys.

**Encryption vs Hashing**: Encryption is reversible with the right key. Hashing is one-way — the hash cannot be reversed. Passwords should be hashed, not encrypted.

### 4.4 Practice Questions — Chapter 4

1. What is the CIA triad in information security?
   A) The US Central Intelligence Agency's approach to digital security
   **B) Confidentiality (only authorised parties access data), Integrity (data is accurate and unaltered), and Availability (data is accessible when needed)** ✓
   C) Three different cybersecurity organisations with the same acronym
   D) A model specifically developed for cloud security architecture

2. What is social engineering in cybersecurity?
   A) Using social media platforms to promote products commercially
   **B) Manipulating people psychologically to circumvent security — exploiting trust, authority, urgency, and helpfulness to trick people into revealing credentials or taking unsafe actions** ✓
   C) A technique for engineering social networks and online communities
   D) Systematic engineering of social media recommendation algorithms

3. What is two-factor authentication?
   A) Using two different passwords for the same account
   **B) Requiring a second verification factor (a code sent to your phone, an authenticator app code, or biometrics) in addition to your password — even with your exact password, an attacker cannot log in without the second factor** ✓
   C) Logging in twice for added security
   D) Using two different email addresses for verification

4. What is a zero-day vulnerability?
   A) A vulnerability discovered on the first day of a software release
   **B) A security vulnerability unknown to the software vendor — therefore with no patch available — attackers can exploit them with no defence possible until the vendor learns of them** ✓
   C) A vulnerability that can only be exploited on a specific calendar date
   D) A security weakness that takes zero seconds to exploit

5. What is the difference between encryption and hashing?
   A) Encryption and hashing are the same process
   **B) Encryption is reversible — the ciphertext can be decrypted with the right key. Hashing is one-way — the hash cannot be reversed. Passwords are hashed, not encrypted, so that even if the database is stolen, plain-text passwords cannot be recovered** ✓
   C) Hashing is just a faster type of encryption
   D) Hashing uses a key that can be used to reverse the process

---

## Chapter 5: Data Science and Analytics

### 5.1 The Data Science Process

**Exploratory Data Analysis (EDA)** always comes first. Before building any model, examine the data: What are the distributions? Are there missing values? Are there impossible values? EDA surfaces data errors, redundant features, and non-obvious patterns.

**Feature engineering**: Using domain knowledge to transform raw data into inputs that help models learn effectively. An experienced data scientist can outperform an automated ML pipeline through better feature engineering.

### 5.2 xG — Data Science Meets Football

**Expected Goals (xG)** is a perfect example of data science applied to a real domain. Every shot is characterised by: distance from goal, angle, shot type, whether it was from open play or a set piece. Historical data tells us what fraction of shots in similar positions resulted in goals.

xG assigns each shot a probability. Summing xG of all shots in a match gives each team's expected goals total — a measure of how many goals the quality of their chances deserved.

### 5.3 Key Algorithms

**Random forest**: Trains many decision trees on random subsets of data and features, then combines their predictions. Far more stable than any individual tree.

**Gradient boosting (XGBoost, LightGBM)**: Builds trees sequentially, each new tree correcting the errors of the previous ones. Consistently wins Kaggle competitions on tabular data.

**The bias-variance tradeoff**: High bias (underfitting): a linear model for a clearly non-linear relationship — both training and test performance are poor. High variance (overfitting): a deep tree memorising training data — training excellent, test poor.

### 5.4 Practice Questions — Chapter 5

1. What is exploratory data analysis (EDA) and why is it always the first step?
   A) Analysis conducted without any specific questions in mind, purely for fun
   **B) The initial investigation of a dataset to discover patterns, spot anomalies, check assumptions, and form hypotheses — using summary statistics and visualisations — before any modelling is attempted** ✓
   C) A technique for cleaning corrupted data
   D) A method of quickly testing multiple models simultaneously

2. What is gradient boosting (XGBoost, LightGBM) and why does it dominate tabular data competitions?
   A) A method of gradually improving AI models by adding humans to the process
   **B) An ensemble method that builds trees sequentially, each new tree correcting the errors of the previous ones — by focusing computational effort on examples the current ensemble handles poorly, producing highly accurate models** ✓
   C) A technique for improving GPU gradient calculations during training
   D) A method of slowly increasing the size of a neural network over time

3. What is xG (Expected Goals)?
   A) Extra goals scored in extra time of a match
   **B) A statistical measure of the probability that a shot results in a goal, based on position, angle, shot type, and assist quality — allowing evaluation of chance quality independently of finishing luck** ✓
   C) A metric used only in professional video game football simulations
   D) Extra goals allowed in international friendly matches only

4. What is the bias-variance tradeoff in machine learning?
   A) The tradeoff between having biased employees and variable workloads
   **B) The fundamental tension between two sources of model error: bias (systematic error from overly simple models that miss real patterns — underfitting) and variance (error from overly complex models that are sensitive to noise — overfitting)** ✓
   C) The tradeoff between unfair AI and unpredictable AI
   D) A method of choosing between different AI algorithms for a problem

5. What is k-means clustering and give a Nigerian fintech application?
   A) A method of encrypting data using k different keys
   **B) An unsupervised ML algorithm that partitions data into k clusters by iteratively assigning each point to its nearest centroid — applied in Nigerian fintech: segmenting mobile money users by transaction patterns to tailor financial products to each segment's needs** ✓
   C) A method of finding the k most important features in a dataset
   D) An algorithm for sorting k items in a database efficiently

---

## Chapter 6: Emerging Technology, IoT, and the Digital Economy

### 6.1 5G: Beyond Faster Phones

5G is not simply "faster 4G". It introduces three distinct service categories:
- **eMBB** (enhanced Mobile Broadband): Up to 10 Gbps — faster internet
- **URLLC** (Ultra-Reliable Low Latency Communications): 1ms latency — for autonomous vehicles and remote surgery
- **mMTC** (massive Machine Type Communications): 1 million devices per km² — the infrastructure for massive IoT deployments

### 6.2 The Internet of Things

IoT is a network of physical devices embedded with sensors, software, and connectivity enabling them to collect and exchange data. The **Mirai botnet (2016)** demonstrated the danger: thousands of cheap CCTV cameras and routers with default passwords were hijacked to execute the largest DDoS attack ever recorded.

### 6.3 Fintech in Nigeria

Nigeria has become Africa's most developed fintech ecosystem. The building blocks:
- CBN's cashless policy (2012) pushed digital payments
- The BVN (Bank Verification Number) biometric system created reliable financial identity
- NIBSS provided instant payment infrastructure
- Enabling regulation allowed Paystack, Flutterwave, OPay, PalmPay, and Moniepoint to emerge

**Flutterwave** achieved unicorn status ($3B+ valuation). **Paystack** was acquired by Stripe for $200M (2020).

### 6.4 Blockchain

A distributed, append-only ledger where data is grouped into cryptographically linked blocks maintained by a decentralised network of nodes — solving the double-spend problem and enabling trustworthy record-keeping without a central authority.

### 6.5 Practice Questions — Chapter 6

1. What is 5G and how does it differ from 4G LTE?
   A) 5G is simply 4G with a better antenna design
   **B) 5G introduces three new use cases: eMBB (enhanced Mobile Broadband — up to 10 Gbps), URLLC (Ultra-Reliable Low Latency Communications — 1ms latency), and mMTC (massive Machine Type Communications — 1 million devices per km2) — representing a shift from human-centric to machine-centric networks** ✓
   C) 5G only works on new smartphones released after 2020
   D) 5G is identical to 4G but with a higher radio frequency

2. What is digital payments infrastructure and how has Nigeria led Africa in fintech?
   A) The physical hardware used to process payments
   **B) The systems enabling electronic money transfer — Nigeria has become Africa's fintech leader through CBN's cashless policy (2012), the BVN biometric identity system, NIBSS instant payment infrastructure, and enabling regulation that allowed the emergence of Paystack, Flutterwave, OPay, PalmPay, and Moniepoint** ✓
   C) A type of payment card used only in digital stores
   D) A government database storing payment information

3. What is blockchain at a technical level?
   A) A very long chain of computer code
   **B) A distributed, append-only ledger where data is grouped into cryptographically linked blocks maintained by a decentralised network of nodes — solving the double-spend problem and enabling trustworthy record-keeping without a central authority** ✓
   C) A type of encrypted hard drive for storing sensitive data
   D) A networking protocol for connecting computers in a chain

4. What is edge AI and why does it matter for African countries with unreliable connectivity?
   A) AI that works only at the edges of cities
   **B) Running AI inference directly on end devices (smartphones, edge servers, microcontrollers) rather than in the cloud — enabling real-time decisions without internet latency, continued operation when connectivity fails, and reduced bandwidth costs** ✓
   C) AI that operates at the boundaries of its capabilities
   D) A type of AI used only on laptop computers at the edge of desks

5. What is precision agriculture and how could it transform smallholder farming in Nigeria?
   A) Agriculture conducted with precise geometric field layouts
   **B) Using IoT sensors, drones, satellite imagery, GPS, and AI to monitor crops at individual plant level — applying water, fertiliser, and pesticide only where and when needed — dramatically increasing yield while reducing waste** ✓
   C) Agriculture managed by AI with no human involvement whatsoever
   D) A government programme for modernising only large commercial farms

---

## Chapter 7: AI Ethics, Society, and Nigeria's Digital Future

### 7.1 Technology Is Never Neutral

Technology reflects the values and power structures of those who create it. AI bias is not merely a technical problem — it is a social justice issue because biased AI systems can systematically disadvantage groups already facing discrimination.

Real documented consequences: MIT Media Lab found higher error rates for darker-skinned women in facial recognition systems. Healthcare algorithms in the US allocated less care to Black patients for equal health need.

### 7.2 AI for Social Good in Africa

Real AI applications addressing African priorities:

- **Ubenwa** (Nigeria/Montreal): AI diagnosing birth asphyxia from the sound of a baby's cry, recorded on a smartphone. Enables diagnosis in facilities without specialists.
- **Zipline** (Ghana, Rwanda): AI-optimised drone delivery of blood products and medicines to rural clinics. Delivers to 21 hospitals covering 7.7 million people in Rwanda.
- **Peek Vision** (Kenya): AI smartphone eye exam for blindness screening — mass screening in communities that have never seen an ophthalmologist.

### 7.3 Data Sovereignty

The principle that data is subject to the laws of the nation where it is collected and stored. If Nigerian citizens' data is stored on servers in Dublin, Irish and EU law applies — not Nigerian law.

Nigeria's NDPR (2019), Kenya's Data Protection Act (2019), and South Africa's POPIA are building regulatory frameworks asserting data sovereignty.

### 7.4 Responsible AI

A proactive commitment to: assessing potential harms before deployment, ensuring fairness across demographic groups, maintaining transparency about AI use, preserving human oversight and appeal mechanisms, and continuously monitoring deployed systems.

### 7.5 Practice Questions — Chapter 7

1. Why is AI bias a social justice issue and not merely a technical problem?
   A) Because it makes AI systems slower and less commercially viable
   **B) Because biased AI systems can systematically disadvantage groups already facing discrimination — a biased hiring algorithm excludes qualified candidates; a biased facial recognition system leads to wrongful arrests; a biased credit algorithm denies loans based on race — amplifying existing inequalities at scale** ✓
   C) Because it creates negative publicity that reduces technology company valuations
   D) Because it makes AI systems harder to program and maintain over time

2. What is technology transfer and why does it matter for Nigeria's development?
   A) The physical shipping of technology hardware from developed to developing countries
   **B) The movement of knowledge, skills, methods, and technologies to organisations or countries that can use them to build local capability — critical for Nigeria to move from technology consumer to technology producer** ✓
   C) Transferring money between technology companies through international wire transfers
   D) The promotion and export of Nigerian-developed technology products to other markets

3. What is data sovereignty and why is it important for African nations?
   A) The idea that data belongs to the person who created it
   **B) The principle that data is subject to the laws of the nation where it is collected and stored — for African nations: if Nigerian citizens' data is stored on servers in Dublin, Irish and EU law applies, not Nigerian law — African data sovereignty argues for local data centres, local data protection laws, and building local AI on local data** ✓
   C) A technical method of securing data from foreign access
   D) A type of database management system

4. What is AI for social good with a concrete example relevant to Africa?
   A) AI systems designed to be pleasant and polite in all user interactions
   **B) Applying AI capabilities to societal challenges where commercial incentive alone is insufficient — such as AI diagnosing birth asphyxia from a baby's cry recorded on a smartphone, enabling diagnosis in facilities without pathologists — Ubenwa (Nigeria/Montreal) demonstrates this approach** ✓
   C) AI developed exclusively by non-profit organisations for charitable purposes
   D) AI systems designed to replace human social workers in community services

5. What is the future of work and how will AI reshape jobs?
   A) All jobs will be eliminated by AI within 10 years
   **B) AI will transform rather than simply eliminate work — automating predictable tasks, augmenting knowledge workers (AI as a tool for lawyers, doctors, engineers — making them more productive), and creating new roles (AI trainers, prompt engineers, AI auditors) — economic research suggests tasks will change more than jobs will disappear entirely, but transition support is critical** ✓
   C) AI will have no impact on employment whatsoever
   D) AI will create more jobs than it eliminates with certainty

---

## Chapter 8: Programming and Computational Thinking

### 8.1 Algorithms and Big O Notation

An **algorithm** is a finite, precise set of instructions for solving a problem. **Big O notation** describes how an algorithm's resource requirements grow as input size increases.

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array index lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | List scan |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2ⁿ) | Exponential | Brute-force subset search |

O(n²) bubble sort on 1 million items: ~1,000 seconds. O(n log n) merge sort on 1 million items: ~0.02 seconds. Same data, 50,000x speed difference.

### 8.2 Object-Oriented Programming

OOP organises code into objects that combine data (attributes) and behaviour (methods). Four principles:
- **Encapsulation**: Hiding internal state
- **Inheritance**: Child classes inherit parent class behaviour
- **Polymorphism**: Objects of different types share interfaces
- **Abstraction**: Exposing necessary interfaces, hiding implementation details

### 8.3 Version Control and Git

Git tracks every change to every file in a codebase — who changed what, when, and why. Without version control, collaborative software development is chaos: overwriting each other's changes, losing track of what broke when.

### 8.4 Key Design Patterns

**The Observer Pattern**: An object (subject) maintains a list of dependents (observers) and notifies them automatically of state changes. JavaScript DOM events, React's state system, and Kafka consumers all use this pattern.

**The Repository Pattern**: Abstracts the data access layer. A repository interface defines what data operations are available without specifying how data is retrieved. Enables swapping storage backends (PostgreSQL in production, in-memory in tests).

**Dependency Injection (DI)**: Objects receive their dependencies from external sources rather than creating them internally. Makes testing easier (inject a fake database connection in tests).

### 8.5 Practice Questions — Chapter 8

1. What is Big O notation and why does algorithm choice matter at scale?
   A) A notation for measuring code quality from A to F
   **B) A framework describing how algorithm resource requirements grow with input size — from best to worst: O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n) linearithmic, O(n²) quadratic, O(2ⁿ) exponential — algorithm choice can be the difference between a system working and being unusable at scale** ✓
   C) A grading system for the quality of programming code
   D) A method of calculating how much memory a program needs

2. What is the CAP theorem in distributed systems?
   A) A theorem about the maximum capacity of databases
   **B) A fundamental result proving that a distributed system can guarantee at most two of three properties simultaneously: Consistency (every read receives the most recent write), Availability (every request receives a response), and Partition Tolerance (the system works despite network failures between nodes)** ✓
   C) A safety theorem about electrical capacitors in servers
   D) A method of calculating computational complexity in distributed systems

3. What is test-driven development (TDD) and what are its benefits?
   A) Testing software after development is complete
   **B) A development methodology where tests are written before the implementation code — the cycle: write a failing test (Red), write minimal code to pass it (Green), refactor the code (Refactor) — benefits: forces thinking about interface before implementation, creates a safety net enabling fearless refactoring** ✓
   C) A method of having users test software while it is being developed
   D) A type of software testing performed by a dedicated testing team

4. What is recursion?
   A) A programming loop that runs repeatedly
   **B) A function that calls itself to solve a problem by breaking it into smaller instances of the same problem — requires a base case (where recursion stops) and a recursive case — example: factorial(n): if n equals 0 return 1 (base case); else return n times factorial(n-1) (recursive case)** ✓
   C) A type of loop that runs backwards
   D) A programming error that causes infinite loops

5. What is technical debt?
   A) The money companies owe to tech suppliers
   **B) The accumulated cost of shortcuts, poor design decisions, and deferred refactoring in a codebase — creating future maintenance burden — named by Ward Cunningham as analogous to financial debt: useful short-term, but interest accumulates until it must be repaid through refactoring** ✓
   C) Debt owed to technology providers for software licences
   D) The financial cost of building software systems

---

## Chapter 9: Cloud, DevOps, and Systems Engineering

### 9.1 Cloud Service Models

- **IaaS** (Infrastructure as a Service): Raw compute, storage, networking. You manage the OS and above. Examples: AWS EC2, Google Compute Engine.
- **PaaS** (Platform as a Service): Development platforms. You manage your application code. Examples: Google App Engine.
- **SaaS** (Software as a Service): Complete applications. The provider manages everything. Examples: Gmail, Salesforce, Paystack.

### 9.2 SRE and Reliability

**SLI (Service Level Indicator)**: A metric measuring service behaviour (e.g. 99.5% of requests return in under 200ms).
**SLO (Service Level Objective)**: An internal target for an SLI (e.g. we aim for 99.9%).
**SLA (Service Level Agreement)**: A contractual commitment to customers with financial penalties for violations.

**Error budget**: If your SLO is 99.9% availability, you have 43.8 minutes of downtime per month as your error budget. Spend this budget on risky deployments and experiments.

**Blameless postmortem**: After each significant incident, a structured analysis of what happened — without blaming individuals. Engineers who fear blame hide mistakes, making systems less safe.

### 9.3 CI/CD

**Continuous Integration (CI)**: Developers frequently merge code to a shared branch, triggering automated builds and tests. Catches integration issues early.
**Continuous Delivery**: Extends CI — code is always in a deployable state but deployments require manual approval.
**Continuous Deployment**: Every code change that passes automated tests is automatically deployed to production.

### 9.4 The DORA Metrics

Four key metrics from Google's DevOps Research and Assessment that predict software delivery performance:
1. Deployment Frequency
2. Lead Time for Changes
3. Change Failure Rate
4. Time to Restore Service

Elite performers deploy multiple times daily with less than 5% failure rate and less than 1 hour restore time.

### 9.5 Practice Questions — Chapter 9

1. What is the cloud and what are the three main service models?
   A) A weather phenomenon affecting satellite internet
   **B) Delivering computing services over the internet — the three main models are: IaaS (Infrastructure as a Service — raw compute, storage, networking), PaaS (Platform as a Service — development platforms), and SaaS (Software as a Service — complete applications)** ✓
   C) A type of distributed file storage system only
   D) A single large server shared by many companies

2. What is SLO, SLA, and SLI in reliability engineering?
   A) Three types of service performance statistics
   **B) SLI (Service Level Indicator): a metric measuring service behaviour. SLO (Service Level Objective): an internal target for an SLI. SLA (Service Level Agreement): a contractual commitment to customers with financial penalties for violations** ✓
   C) Three types of software licences
   D) Three levels of cloud service pricing tiers

3. What is the DORA metrics framework for measuring DevOps performance?
   A) Four metrics for measuring developer happiness
   **B) Four key metrics from Google's DevOps Research and Assessment (DORA) that predict software delivery performance: Deployment Frequency, Lead Time for Changes, Change Failure Rate, and Time to Restore Service — elite performers deploy multiple times daily with less than 5% failure rate** ✓
   C) A set of project management metrics
   D) A framework for measuring software quality

4. What is serverless computing and what are its trade-offs?
   A) Computing without any physical servers anywhere
   **B) A cloud model where code (functions) is executed in response to events without the developer managing servers — the cloud provider handles provisioning, scaling, and maintenance — trade-offs: no server management, automatic scaling to zero (no cost when idle), but cold starts (latency when function has not run recently)** ✓
   C) Computing that requires no software — only hardware
   D) A type of distributed computing across many personal computers

5. What is chaos engineering and why do companies deliberately break their systems?
   A) Engineering that produces chaotic, unpredictable code
   **B) Deliberately introducing failures into a production system to test resilience and discover weaknesses before they cause unplanned outages — Netflix created Chaos Monkey (randomly terminates production servers) to ensure their system is resilient enough to handle arbitrary server failures** ✓
   C) A type of software testing for complex systems
   D) A management style for engineering teams

---

## Chapter 10: Data Engineering

### 10.1 ETL and ELT

**ETL (Extract, Transform, Load)**: Extract data from source systems, Transform it (cleans, normalises, aggregates), and Load it into a destination (data warehouse, data lake). The foundational pattern for moving data from operational systems to analytics systems.

**Modern ELT** (Extract, Load, Transform): Load raw data first, then transform inside the warehouse using SQL — enabled by cheap cloud warehouse compute.

### 10.2 Data Storage Architecture

**Data warehouse**: Optimised for analytical queries. Uses columnar storage and massively parallel processing. Examples: BigQuery (Google), Redshift (AWS), Snowflake.

**Data lake**: A central repository storing raw data in any format at any scale in cheap object storage (AWS S3, GCS).

**Lake house**: Combines data lake (cheap storage) with data warehouse capabilities (ACID transactions, schema enforcement). Implemented by Delta Lake, Apache Iceberg, Apache Hudi.

**Medallion architecture**: Bronze (raw, immutable), Silver (cleaned, validated), Gold (business-level aggregates for specific use cases).

### 10.3 Key Tools

**Apache Spark**: Distributed computing framework. In-memory processing (100x faster than Hadoop MapReduce for iterative algorithms). Used by Netflix, Uber, and Alibaba for petabyte-scale data processing.

**Apache Kafka**: Distributed event streaming platform. Events are retained and can be replayed. Multiple consumer groups each process the same events independently. Handles millions of events per second.

**dbt (data build tool)**: Enables data transformation in the warehouse using SQL with software engineering best practices — version control, testing, documentation, modularity.

**Apache Airflow**: Workflow orchestration platform. Data pipelines are defined as DAGs (Directed Acyclic Graphs) in Python. Schedules and monitors runs, retries failed tasks, alerts on failures.

### 10.4 Practice Questions — Chapter 10

1. What is an ETL pipeline and why is it fundamental to data engineering?
   A) An email tracking and logging system
   **B) Extract, Transform, Load — a data integration process that: Extracts data from source systems (databases, APIs, files, streams), Transforms it (cleans, normalises, aggregates, enriches), and Loads it into a destination (data warehouse, data lake) — the foundational pattern for moving data from operational systems to analytics systems** ✓
   C) A type of deep learning pipeline
   D) A programming pattern for web applications

2. What is Apache Kafka and what makes it central to real-time data architectures?
   A) A type of data storage system
   **B) A distributed event streaming platform — a highly scalable, fault-tolerant commit log where producers write events to topics and consumers read events — events are retained (consumers can replay from any offset), partitioned for scalability, replicated for fault tolerance, and consumers track their own position** ✓
   C) A database management system for streaming data
   D) A programming language for real-time systems

3. What is the medallion architecture in data lake design?
   A) A prize-based data management system
   **B) A layered data organisation approach with three zones: Bronze (raw, unprocessed data as ingested from sources — immutable, append-only), Silver (cleaned, validated, conformed data), Gold (business-level aggregates optimised for specific analytical use cases — reports, ML features, dashboards)** ✓
   C) A type of database caching technique
   D) A method of organising server hardware in tiers

4. What is dbt (data build tool)?
   A) A database backup tool
   **B) An open-source tool that enables data analysts and engineers to transform data in their warehouse using SQL and software engineering best practices — dbt brings: version control (transformation SQL in git), testing (assertions on data quality), documentation, modularity, and CI/CD to data transformation** ✓
   C) A type of data visualisation tool
   D) A programming language for data engineers

5. What is OLTP vs OLAP and why do systems specialise?
   A) OLTP is faster; OLAP is more secure
   **B) Online Transaction Processing (OLTP): optimised for many small, fast read/write transactions. Online Analytical Processing (OLAP): optimised for large analytical queries across historical data — columnar storage, denormalised star schema, no real-time writes needed** ✓
   C) OLTP is for web applications; OLAP is only for large enterprises
   D) OLTP uses SQL; OLAP uses a different query language

---

# PART TWO: FOOTBALL

---

## Chapter 11: The Laws of the Game

### 11.1 Overview

Football has 17 Laws, maintained by **IFAB** (the International Football Association Board, founded 1886). A standard match is 90 minutes. A match cannot start if either team has fewer than 7 players.

### 11.2 Offside

A player is in an offside position if any body part that can legally score or play the ball is closer to the opponent's goal line than both the ball *and* the second-last defender, at the moment the ball is played.

A player **cannot** be offside from a goal kick, a corner kick, or a throw-in.

### 11.3 Direct vs Indirect Free Kicks

A **direct free kick** can be scored without another player touching the ball first. Awarded for serious physical offences: kicking, tripping, pushing, striking, jumping at an opponent, or deliberate handball.

An **indirect free kick** requires the ball to touch at least one other player before entering the goal. Awarded for: goalkeeper holding the ball for more than 6 seconds, touching a deliberate back-pass from a teammate's feet, dangerous play, or obstruction.

### 11.4 VAR

VAR (Video Assistant Referee) reviews **only four situations**:
1. Goals and their build-up (including offside and handballs in the build-up)
2. Penalty decisions
3. Direct red card incidents
4. Mistaken identity (when the referee disciplines the wrong player)

VAR does **not** review yellow card decisions, corner kick versus goal kick decisions, or throw-in decisions.

### 11.5 Practice Questions — Chapter 11

1. When is a player in an offside position?
   A) When in the opponent's half
   **B) When any body part that can legally score is closer to the goal line than both the ball and the second-last defender when the ball is played** ✓
   C) When behind the ball
   D) When in their own penalty area

2. What does VAR stand for and what four situations can it review?
   **A) Video Assistant Referee — goals, penalties, red cards, and mistaken identity** ✓
   B) Virtual Action Review — reviewing all decisions made during a match
   C) Variable Angle Review — reviewing any disputed decision
   D) Video Analysis Recording — reviewing tactical decisions by coaches

3. What is the back-pass rule introduced in 1992?
   A) Goalkeepers must take all back passes from teammates with their feet
   **B) If an outfield player deliberately passes back to the goalkeeper using their feet, the goalkeeper cannot pick it up — violation results in an indirect free kick. This single rule transformed football — making it faster, more attacking, and more entertaining** ✓
   C) Back passes are automatically offside
   D) Only the captain can pass back to the goalkeeper

4. What changed in 2019 about goal kicks?
   A) Goalkeepers must now take goal kicks from outside the penalty area
   **B) The ball is in play as soon as it is kicked — teammates can receive it inside the penalty area — whereas previously it had to leave the area first** ✓
   C) Goal kicks must now be taken within 10 seconds of being awarded
   D) Opponents can enter the penalty area before the goal kick is taken

5. What is a direct free kick awarded for?
   A) The goalkeeper holding the ball for more than 6 seconds
   **B) Serious physical offences: kicking, tripping, pushing, striking, jumping at an opponent, or deliberate handball — a direct free kick can be scored without another player touching the ball first** ✓
   C) Dangerous play or obstruction
   D) Touching a deliberate back-pass from a teammate's feet

---

## Chapter 12: Tactics and Modern Football Philosophy

### 12.1 Formations

**4-3-3**: Used by Barcelona, Liverpool, and many top teams for its attacking width and midfield control. Three forwards provide width and pressing from the front.

**4-2-3-1**: A double pivot of two defensive midfielders shields the defence while the attacking midfielder (number 10) operates behind the striker. Very common at international level.

**3-5-2**: Three centre-backs with two wing-backs who are effectively midfielders when attacking but fullbacks when defending.

### 12.2 Pressing

**Pressing** — aggressively closing down opponents immediately after losing possession — has transformed modern football. Jürgen Klopp and Pep Guardiola made pressing the dominant tactical philosophy of the era.

**Gegenpress (counter-press)**: Win the ball back *immediately* after losing it, ideally in the opponent's half, before they can organise a counter-attack.

**Pressing triggers**: Specific cues that signal the whole team to press simultaneously — an opposition goalkeeper receiving the ball, a poor first touch, a specific player receiving with back to goal.

### 12.3 Key Tactical Concepts

**The false nine**: A centre-forward who drops deep into midfield, vacating the traditional striker position and creating confusion in the defence while wide forwards run into the vacated central space. Messi as false 9 under Guardiola at Barcelona (2009-12) is the definitive example.

**Inverted wingers**: Wide players positioned on the opposite side to their strong foot — a right-footed player on the left wing — who cut inside onto their stronger foot to shoot or create. Mohamed Salah (right-footed on the left at Liverpool).

**Tiki-taka**: A possession-based philosophy of quick, precise short passing and constant movement. Spain won Euro 2008, World Cup 2010, and Euro 2012 using tiki-taka.

**Positional play (juego de posición)**: Occupying the pitch intelligently — always having players in specific zones to ensure passing options in all directions.

### 12.4 Practice Questions — Chapter 12

1. What does pressing mean tactically in modern football?
   A) Defending very deep in your own half and waiting for mistakes
   **B) Aggressively closing down opponents quickly after losing possession to win the ball back in dangerous areas and disrupt the opponent's build-up** ✓
   C) Playing long, direct balls to bypass the midfield
   D) Using a physically rough style to intimidate opponents

2. What is gegenpress (counter-press)?
   A) A technique for managing post-match press conferences
   **B) Immediately and aggressively pressing opponents within seconds of losing possession, before they can organise — winning the ball back in the opponent's half while they are still disorganised** ✓
   C) A long-ball pressing strategy for knockout competitions
   D) A type of set piece press used in the final 10 minutes of close matches

3. What is an inverted winger?
   A) A winger moved to the opposite side of the pitch from normal
   **B) A wide player positioned on the opposite side to their strong foot — a right-footed player on the left wing — who cuts inside onto their stronger foot to shoot or create, rather than running to the byline to cross** ✓
   C) A winger inverted into a central midfield role as a surprise tactic
   D) A winger who exclusively defends and never contributes to attacking play

4. What is the false nine and who is its most famous exponent?
   A) The ninth player on the bench who comes on as a false starter
   **B) A centre-forward who drops deep into midfield, vacating the traditional striker position and creating confusion in the defence — Messi playing as false 9 under Guardiola at Barcelona (2009-12) is the definitive example** ✓
   C) A player who wears number 9 but plays in midfield
   D) A striker who plays on the left wing instead of through the middle

5. What is tiki-taka and which international team made it famous?
   A) A type of ball control technique taught in academies
   **B) A possession-based philosophy of quick, precise short passing and constant movement, creating positional superiority in small areas while pressing intensely when out of possession — Spain won Euro 2008, World Cup 2010, and Euro 2012 using tiki-taka** ✓
   C) A style of play that uses long direct balls exclusively
   D) A defensive formation used by Italian teams in the 1980s

---

## Chapter 13: World Football History

### 13.1 The Birth of the Game

Association football was codified on 26 October 1863 in London. FIFA was founded on 21 May 1904 in Paris. It now has 211 member associations — more than the United Nations.

The first World Cup was held in Uruguay in 1930. **Brazil** has won the most World Cups: 5 (1958, 1962, 1970, 1994, 2002).

### 13.2 Greatest Moments

**The 1970 Brazil squad**: Often called the greatest team in World Cup history. Won all 6 matches. Pelé, Jairzinho, Tostão, Rivelino, and captain Carlos Alberto.

**Diego Maradona's double at Mexico 1986**: In the quarter-final against England, Maradona scored both the most infamous goal (the Hand of God — punched with his hand) and the greatest goal in World Cup history (solo dribble from the halfway line past six players).

**The 2005 Champions League final — Miracle of Istanbul**: AC Milan led Liverpool 3-0 at half-time. Liverpool scored three goals in six second-half minutes to draw 3-3. Liverpool's goalkeeper Jerzy Dudek saved two penalties in the shootout.

### 13.3 The Bosman Ruling

In 1995, a European Court ruling established that EU citizens had the right to move freely between employers at the end of their contracts — clubs could no longer demand transfer fees for out-of-contract players. Player wages soared dramatically.

### 13.4 Total Football

Ajax Amsterdam under Rinus Michels and Johan Cruyff developed **total football** in the 1960s-70s — any outfield player could fulfil any position. If the left back advanced, a midfielder filled their position. The Dutch 1974 team made this philosophy famous globally.

### 13.5 Practice Questions — Chapter 13

1. Which country has won the most FIFA World Cup titles?
   A) Germany
   B) Italy
   C) Argentina
   **D) Brazil** ✓

2. What was the Hand of God goal?
   A) A miraculous save by a goalkeeper
   **B) Diego Maradona's deliberate handball goal against England at the 1986 World Cup quarter-final — undetected by the referee, described by Maradona as a little with the head of Maradona and a little with the hand of God** ✓
   C) A famous bicycle kick by Pelé at the 1970 World Cup final
   D) Roberto Carlos's famous free kick that curved impossibly into the net

3. What was the Bosman Ruling of 1995?
   A) A rule about player conduct in Italian football
   **B) A European Court ruling allowing EU footballers to move freely between clubs at contract expiry without transfer fees — permanently transforming football's labour market and significantly increasing player wages** ✓
   C) A rule banning foreign players from European competitions
   D) A FIFA rule imposing a global salary cap on professional footballers

4. What is total football?
   A) A football philosophy that requires all players to score at least one goal per season
   **B) A tactical philosophy where any outfield player can fulfil any position — if the left back advances, a midfielder fills their position — requiring all players to be technically excellent in any role. Developed by Ajax Amsterdam under Johan Cruyff in the 1960s-70s** ✓
   C) A style that uses every player in defence and attack simultaneously
   D) A training method where players practise every position over the course of a season

5. What happened in the 2005 Champions League final — the Miracle of Istanbul?
   A) Barcelona scored 5 goals in the second half to win
   **B) AC Milan led Liverpool 3-0 at half-time. Liverpool scored three goals in six second-half minutes to draw 3-3. Liverpool's goalkeeper Jerzy Dudek saved two penalties in the shootout. One of the most dramatic sporting events in history** ✓
   C) Manchester United scored in injury time in the final to win
   D) Real Madrid won the penalty shootout after a 0-0 draw

---

## Chapter 14: Nigerian and African Football

### 14.1 Nigeria's Football Heritage

The **Super Eagles** have three AFCON titles (1980, 1994, 2013) and six World Cup appearances since their debut in 1994.

Nigeria's greatest year may have been **1994**: World Cup debut at USA 1994 reaching the Round of 16, and winning AFCON in Tunisia in the same year.

**Atlanta 1996**: Nigeria won Olympic gold. The semi-final comeback against Brazil — 3-1 down, then three goals including Nwankwo Kanu's extra-time winner — and the 3-2 final victory over Argentina made stars of a generation.

### 14.2 The Legends

**Jay-Jay Okocha** (Augustine Azuka Okocha): Widely regarded as the most naturally gifted Nigerian player. Bolton Wanderers' advertising slogan: "Jay-Jay Okocha, so good they named him twice." Creative heartbeat of Nigeria's 1994 World Cup debut and the 1996 Olympic gold.

**Nwankwo Kanu**: Won the UEFA Champions League with Ajax in 1995. His goal in the 1996 Olympic semi-final against Brazil — equalising in extra time — is one of Nigerian sport's most iconic moments.

**Rashidi Yekini** (1963-2012): Nigeria's greatest striker. His emotional celebration after scoring Nigeria's first-ever World Cup goal against Bulgaria in 1994 — rushing to the net and grasping it with both hands — is one of Nigerian sport's most enduring images.

**Stephen Keshi** (1962-2016): Part of Nigeria's 1994 AFCON-winning squad as a player. Led Nigeria to AFCON 2013 glory as manager — one of only two Africans in history to win AFCON as both player and manager.

**Victor Osimhen** (born 1998, Lagos): Nigeria's present global superstar. His devastating pace, aerial ability, and clinical finishing helped Napoli win their first Serie A title in 33 years (2022-23).

**Asisat Oshoala** (born 1994, Ikorodu): Africa's greatest female footballer. Has won the African Women's Player of the Year award multiple times. Won the Champions League with Barcelona.

### 14.3 Enyimba FC

**Enyimba International FC** from Aba, Abia State — nicknamed "The People's Elephant" — won the CAF Champions League in **2003 and 2004**, becoming the first Nigerian club to win Africa's premier club competition, and the first club anywhere to successfully defend the title.

### 14.4 CAF and AFCON

**CAF** (Confederation of African Football) was founded in 1957 in Khartoum, Sudan. It now governs football across 54 member associations.

**AFCON** winners by number of titles: Egypt (7), Nigeria (3), Ghana (4), Cameroon (4).

**George Weah** of Liberia remains the only African-born player to have won the Ballon d'Or — claiming it in 1995 while playing for AC Milan and PSG. He later became President of Liberia in 2018.

### 14.5 Practice Questions — Chapter 14

1. How many times has Nigeria won the Africa Cup of Nations?
   A) 1
   B) 2
   **C) 3** ✓
   D) 4

2. What did Enyimba FC achieve in continental football?
   A) Winning the NPFL consecutively for 10 years
   **B) Winning the CAF Champions League in 2003 and 2004 — the first Nigerian club to win the competition and the first to defend it — the greatest achievement in Nigerian club football history** ✓
   C) Being the first Nigerian club to play in a European competition
   D) Being Nigeria's most supported club by fan attendance

3. What is Stephen Keshi's historic achievement?
   A) He was Nigeria's first international player to move to Europe
   **B) He is one of very few Africans to win AFCON as both a player (1994 with Nigeria) and as a national team head coach (2013 with Nigeria) — a rare double achievement placing him among the greatest figures in African football** ✓
   C) He scored the most goals ever in AFCON tournament history
   D) He was the first African manager appointed to manage a top European club side

4. Who scored Nigeria's first-ever World Cup goal and what was memorable about his celebration?
   A) Jay-Jay Okocha, who performed a somersault
   **B) Rashidi Yekini, who rushed to the net after scoring against Bulgaria in 1994 and grasped it with both hands in overwhelming joy — one of Nigerian sport's most enduring images** ✓
   C) Nwankwo Kanu, who dedicated the goal to his country
   D) Daniel Amokachi, who scored a hat-trick against Bulgaria

5. Which African player has won the Ballon d'Or?
   A) Jay-Jay Okocha (Nigeria, 2003)
   B) Didier Drogba (Ivory Coast, 2012)
   **C) George Weah (Liberia, 1995) — the only African-born player to win the award, while playing for AC Milan and PSG — he later became President of Liberia in 2018** ✓
   D) Samuel Eto'o (Cameroon, 2005)

---

## Chapter 15: Positions, Statistics, and the Modern Game

### 15.1 Understanding Positions

**The goalkeeper**: The only player who can handle the ball inside the penalty area. Modern goalkeepers are not just shot-stoppers: they organise the defence, command crosses, sweep behind the defensive line, and distribute the ball.

**Centre-backs**: Defend the central channel. Ball-playing ability has become as important as traditional defensive qualities at top-level football.

**Full-backs**: Have transformed from purely defensive players into crucial attacking contributors. Trent Alexander-Arnold and Andrew Robertson at Liverpool effectively played as auxiliary midfielders.

**The defensive midfielder (number 6)**: Screens the defence and recycles possession. The position became known as "the Makélélé role" after Claude Makélélé's effectiveness shielding Real Madrid's defence.

**The number 10 (attacking midfielder)**: The creative heart of the team — receiving between the lines, creating chances, and often scoring. Jay-Jay Okocha, Zidane, Ronaldinho, Messi, and Totti are its icons.

### 15.2 Statistics

**xG (Expected Goals)**: Quantifies shot quality. A shot from 5 metres directly in front of goal has xG ~0.8 (historically 80% are goals); a speculative 30-metre effort has xG ~0.03.

**PPDA (Passes Per Defensive Action)**: Measures pressing intensity — how many passes the opposition completes before a team makes a defensive action. Lower PPDA = more intense pressing.

**Progressive passes and carries**: Move the ball significantly toward the opponent's goal. These identify midfielders and defenders who drive the team forward.

### 15.3 Practice Questions — Chapter 15

1. What is xG (Expected Goals)?
   A) Extra goals scored in extra time of a match
   **B) A statistical measure of the probability that a shot results in a goal, based on position, angle, shot type, and assist quality — allowing evaluation of chance quality independently of finishing luck** ✓
   C) A metric used only in professional video game football simulations
   D) Extra goals allowed in international friendly matches only

2. What is the significance of the squad number 10 in football culture?
   A) It simply refers to the 10th substitute named on the team sheet
   **B) Historically the number 10 is the creative attacking midfielder or playmaker — associated with legends like Pelé, Maradona, Zidane, Ronaldinho, and Messi, carrying cultural significance beyond mere positional numbering** ✓
   C) It is assigned to the highest-paid player in every team
   D) It designates the 10th player to sign for the club in that specific season

3. What is the primary role of a modern goalkeeper?
   A) Score goals from penalty kicks and set pieces
   **B) Prevent goals — the only player allowed to handle the ball in the penalty area — while also organising the defence, initiating attacks with precise distribution, and commanding the penalty area during crosses** ✓
   C) Mark the opposition's main striker throughout the entire match
   D) Take all penalty kicks and free kicks for the team

4. What is PPDA (Passes Per Defensive Action)?
   A) A measure of how many passes a team makes before shooting
   **B) A metric measuring pressing intensity — how many passes the opposition completes before a team makes a defensive action (tackle, interception, foul). Lower PPDA means more intense pressing** ✓
   C) A measure of how many goals a team scores per defensive clearance
   D) A fitness metric for measuring a player's defensive work rate

5. What transformed full-backs from purely defensive players into attacking contributors?
   A) A rule change requiring full-backs to score at least one goal per season
   **B) The evolution of modern attacking football — under managers like Jürgen Klopp, full-backs like Trent Alexander-Arnold and Andrew Robertson effectively played as auxiliary midfielders, contributing goals, assists, and progressive passes while also defending** ✓
   C) Better physical training methods that made full-backs faster
   D) Tactical systems that moved full-backs permanently into midfield positions

---

# APPENDIX A: PRACTICE QUESTION ANSWERS

## Quick Reference Answer Key

All correct answers are marked **B** or specific letters in each chapter's practice questions. The following is the complete answer key for all 75 practice questions across 15 chapters.

### Part One: Technology

**Chapter 1 — AI Foundations**
1. B — Narrow AI
2. B — Rule-based vs ML
3. B — Overfitting
4. B — Reinforcement learning
5. B — Diverse data prevents bias

**Chapter 2 — LLMs and Generative AI**
1. B — Transformer architecture
2. B — RAG
3. B — Diffusion models
4. B — RLHF
5. B — Zero-shot generalisation

**Chapter 3 — Robotics**
1. B — SLAM
2. B — Moravec's paradox
3. B — Soft robotics
4. B — Cobots
5. B — Teleoperation

**Chapter 4 — Cybersecurity**
1. B — CIA triad
2. B — Social engineering
3. B — Two-factor authentication
4. B — Zero-day vulnerability
5. B — Encryption vs hashing

**Chapter 5 — Data Science**
1. B — Exploratory data analysis
2. B — Gradient boosting
3. B — xG definition
4. B — Bias-variance tradeoff
5. B — K-means clustering

**Chapter 6 — Emerging Technology**
1. B — 5G three use cases
2. B — Nigeria fintech
3. B — Blockchain technical
4. B — Edge AI
5. B — Precision agriculture

**Chapter 7 — AI Ethics**
1. B — AI bias as social justice issue
2. B — Technology transfer
3. B — Data sovereignty
4. B — AI for social good (Ubenwa)
5. B — Future of work

**Chapter 8 — Programming**
1. B — Big O notation
2. B — CAP theorem
3. B — Test-driven development
4. B — Recursion
5. B — Technical debt

**Chapter 9 — Cloud and DevOps**
1. B — Cloud service models
2. B — SLO/SLA/SLI
3. B — DORA metrics
4. B — Serverless computing
5. B — Chaos engineering

**Chapter 10 — Data Engineering**
1. B — ETL pipeline
2. B — Apache Kafka
3. B — Medallion architecture
4. B — dbt
5. B — OLTP vs OLAP

### Part Two: Football

**Chapter 11 — Laws of the Game**
1. B — Offside rule
2. A — VAR (four situations)
3. B — Back-pass rule
4. B — 2019 goal kick change
5. B — Direct free kick

**Chapter 12 — Tactics**
1. B — Pressing
2. B — Gegenpress
3. B — Inverted wingers
4. B — False nine (Messi)
5. B — Tiki-taka (Spain)

**Chapter 13 — World Football History**
1. D — Brazil (5 World Cups)
2. B — Hand of God goal
3. B — Bosman Ruling
4. B — Total football
5. B — Miracle of Istanbul

**Chapter 14 — Nigerian and African Football**
1. C — Nigeria: 3 AFCON titles
2. B — Enyimba CAF Champions League
3. B — Stephen Keshi double
4. B — Rashidi Yekini first goal
5. C — George Weah Ballon d'Or

**Chapter 15 — Positions and Statistics**
1. B — xG definition
2. B — Number 10 significance
3. B — Goalkeeper role
4. B — PPDA
5. B — Full-backs evolution

---

## Detailed Answer Explanations

Where a question might trip up a careful student, here is why the correct answer is correct:

**Ch1 Q1**: Deep Blue was extraordinary at chess but could not do anything else — this is the definition of narrow AI (ANI). AGI (General AI) would be able to transfer its learning across domains — we do not have this yet.

**Ch2 Q5**: Zero-shot means the model handles tasks it was *never explicitly trained on* — it uses learned representations to generalise. A model that was trained on something is not zero-shot for that task.

**Ch4 Q5**: People often confuse encryption and hashing. The key test: can you get the original back? Encryption: yes (with the key). Hashing: no. That is why passwords are hashed — even the database administrator cannot retrieve your original password.

**Ch6 Q3**: Blockchain is often confused with cryptocurrency. Blockchain is the underlying technology — a trustworthy shared record without a central authority. Cryptocurrency is one application of blockchain.

**Ch11 Q2**: VAR reviews *exactly four situations*. Many people add yellow cards, corners, and throw-ins — these are all incorrect. VAR cannot review yellow card decisions.

**Ch13 Q1**: Brazil has 5 World Cups (1958, 1962, 1970, 1994, 2002). Germany and Italy have 4 each. Argentina has 3 (2022 win adding to 1978 and 1986).

**Ch14 Q5**: George Weah (Liberia, 1995) is the *only* African-born Ballon d'Or winner. Note: African players who won it while playing for European clubs (Ronaldo, etc.) are not African-born. Weah won it while playing for AC Milan.

---

# APPENDIX B: KEY TERMS GLOSSARY

**AGI (Artificial General Intelligence)**: A hypothetical AI that can learn and apply knowledge across any domain like humans. Does not yet exist.

**Algorithm**: A finite, precise set of instructions for solving a problem.

**Attention Mechanism**: A component in neural networks that allows a model to dynamically weight the importance of different parts of the input when generating each output.

**Backpropagation**: An algorithm that efficiently computes gradients of the loss with respect to every parameter in a neural network, enabling gradient descent for deep networks.

**Big O Notation**: A mathematical notation describing how an algorithm's resource requirements grow with input size.

**Blockchain**: A distributed, append-only ledger where data is grouped into cryptographically linked blocks maintained by a decentralised network of nodes.

**CAF (Confederation of African Football)**: The governing body of football across Africa, founded in 1957.

**CIA Triad**: Confidentiality, Integrity, Availability — the three core objectives of information security.

**CNN (Convolutional Neural Network)**: A neural network architecture using convolutional layers that apply learned filters across spatial positions, particularly suited to image data.

**Context Window**: The maximum number of tokens an LLM can consider simultaneously when generating a response.

**Deep Learning**: Machine learning using neural networks with many layers that can learn hierarchical representations.

**Digital Twin**: A precise virtual simulation of a physical system, updated in real time with sensor data from the physical counterpart.

**E2EE (End-to-End Encryption)**: Encryption where only the communicating parties can read the messages; the service provider cannot decrypt them.

**Edge AI**: Running AI inference on end devices rather than in the cloud, enabling real-time decisions without internet latency.

**Federated Learning**: A technique where models train across many devices without centralising raw data — each device trains locally and only model updates are shared.

**Fine-tuning**: Further training a pre-trained LLM on a smaller, task-specific dataset to specialise its behaviour.

**Foundation Model**: A large AI model trained on broad, diverse data at scale, designed to be adapted for a wide range of downstream tasks.

**Gegenpress**: Immediately and aggressively pressing opponents within seconds of losing possession, before they can organise.

**Gradient Descent**: An optimisation algorithm that iteratively adjusts a model's parameters in the direction that reduces the error.

**Hallucination (AI)**: When an AI generates false or fabricated information stated with apparent confidence.

**IFAB (International Football Association Board)**: Founded 1886; maintains and amends the Laws of the Game.

**LLM (Large Language Model)**: An AI trained on vast amounts of text data that can generate, understand, translate, and reason about human language.

**Model Drift**: The degradation of a model's performance over time as real-world data distribution shifts from what the model was trained on.

**Narrow AI (ANI)**: AI that is highly capable at one specific task but unable to transfer that ability to other domains.

**NDPR (Nigeria Data Protection Regulation)**: Nigeria's data protection law (2019), governing personal data collection and processing.

**Overfitting**: When a model memorises training data rather than learning generalisable patterns — performs well on training data but poorly on new data.

**PPDA (Passes Per Defensive Action)**: A metric measuring pressing intensity — how many passes the opposition completes before a team makes a defensive action.

**Progressive Passing/Carrying**: Passes or runs with the ball that significantly advance it toward the opponent's goal.

**Prompt Engineering**: The skill of crafting effective instructions to get the most useful, accurate, or specific outputs from an LLM.

**RAG (Retrieval-Augmented Generation)**: A system where an LLM retrieves relevant information from an external knowledge base before generating a response.

**Reinforcement Learning**: Training an AI agent through trial and error — rewarding good actions and penalising bad ones until it learns an optimal strategy.

**RLHF (Reinforcement Learning from Human Feedback)**: A technique where humans rate AI outputs and those ratings train the model to be more helpful, harmless, and honest.

**SLAM (Simultaneous Localisation and Mapping)**: A robot's ability to build a map of an unknown environment while simultaneously tracking its own location within that map.

**Social Engineering**: Manipulating people psychologically to circumvent security — exploiting trust, authority, urgency, and helpfulness to trick people into revealing credentials.

**Supply Chain Attack**: A cyberattack targeting a trusted software vendor or update mechanism to reach many downstream victims.

**Tiki-Taka**: A possession-based football philosophy of quick, precise short passing and constant movement, creating positional superiority.

**Total Football**: A tactical philosophy where any outfield player can fulfil any position, requiring all-round technical ability.

**Transformer**: A neural network architecture using self-attention mechanisms to process all parts of a sequence simultaneously — the foundational architecture of all modern LLMs.

**Transfer Learning**: Using a model pre-trained on a large dataset as a starting point for a different but related task, requiring far less data and computation.

**xG (Expected Goals)**: A statistical measure of the probability that a given shot results in a goal, based on position, angle, shot type, and assist quality.

**Zero-Day Vulnerability**: A security vulnerability unknown to the software vendor — therefore with no patch available.

**Zero-Trust Security**: A security model assuming no user, device, or network segment is inherently trusted — requiring continuous verification of identity and authorisation for every access request.

---

*THRIVE — Technology, Hard work, Resilience, Innovation, Vision, and Excellence*
*For young Nigerians building the future.*
