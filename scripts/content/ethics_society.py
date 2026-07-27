# Ethics, Society & Future Tech — 30 questions, applied-reasoning style.
QUESTIONS = [
{
 "q": "A documented US algorithm used in criminal sentencing was found to flag Black defendants as 'high risk' at a significantly higher rate than white defendants with similar records, even though race was never an explicit input to the model. Rejected defendants had no clear way to understand or challenge the specific reasoning behind their score. What does this scenario primarily illustrate the need for?",
 "options": [
   "Algorithmic accountability — ensuring automated decisions affecting fundamental rights and opportunities are fair, transparent, and can be understood and contested by the people they affect, not just technically accurate on average",
   "Federated learning — a technique for training a shared model across many devices without centralising raw data, a technical training method unrelated to whether a deployed sentencing algorithm's decisions can be understood or contested",
   "Knowledge distillation — training a smaller model to mimic a larger one's outputs, a technique for making AI cheaper to run, unrelated to whether an already-deployed sentencing algorithm's decisions are fair or contestable",
   "Zero-shot generalisation — a model's ability to handle tasks it wasn't explicitly trained on, a technical capability concept unrelated to whether a sentencing algorithm's decisions are fair, transparent, or contestable"
 ],
 "answer": 0,
 "explanation": "This scenario reflects a real, documented case (a US recidivism-prediction tool) illustrating why algorithmic accountability matters: automated decisions with serious real-world consequences need to be fair, explainable, and contestable — not just accurate on average — especially when they affect fundamental rights like liberty."
},
{
 "q": "MIT Media Lab research found that several commercial facial recognition systems had substantially higher error rates for darker-skinned women than for lighter-skinned men, despite each system reporting high overall accuracy. Why is this specifically a social justice concern rather than merely a narrow technical bug?",
 "options": [
   "Because a biased AI system deployed at scale systematically disadvantages an already-marginalised group in real, consequential ways (like wrongful identification), amplifying existing inequality rather than being a neutral, one-off technical glitch",
   "Because facial recognition technology itself is universally banned by international law in every country, making any accuracy discrepancy automatically a matter of criminal legal liability regardless of the specific cause",
   "Because this specific accuracy gap has no realistic connection to any real-world consequence for any individual person, making it a purely abstract, theoretical statistical curiosity with no genuine practical significance",
   "Because it proves conclusively that all forms of artificial intelligence are fundamentally and permanently incapable of ever achieving fairness across any demographic group under any possible future circumstance"
 ],
 "answer": 0,
 "explanation": "AI bias becomes a social justice issue specifically because it operates at scale and often on top of pre-existing inequality — a biased facial recognition system doesn't just make a random technical error, it systematically disadvantages an already-marginalised group in ways with real consequences, like wrongful identification or arrest, amplifying rather than correcting existing unfairness."
},
{
 "q": "In parts of northern Nigeria, a smallholder farmer without reliable electricity, a smartphone, or affordable data has essentially no path to using AI-powered farming advisory tools that a well-connected urban farmer can access freely. What broader concept does this specific gap illustrate?",
 "options": [
   "Digital inequality — unequal access to and effective use of digital technologies (devices, connectivity, skills, relevant local content), which compounds existing disadvantage for those already excluded from other opportunities",
   "Model collapse — the degradation of AI model quality across successive generations of training on synthetic data, a technical AI training phenomenon unrelated to unequal access to devices, connectivity, or digital skills",
   "Federated learning — a technique for training a shared AI model across many devices without centralising raw data, a specific technical training method unrelated to a farmer's basic lack of access to any digital device at all",
   "Constitutional AI — training an AI model to critique and revise its own outputs against written guiding principles, a specific AI safety training technique entirely unrelated to a farmer's basic lack of digital access"
 ],
 "answer": 0,
 "explanation": "Digital inequality covers exactly this kind of gap — unequal access to devices, connectivity, and digital skills — which compounds rather than merely coexists with other disadvantages, since the farmer excluded from digital tools also tends to be excluded from the other opportunities (education, financial services, markets) those tools increasingly gate access to."
},
{
 "q": "A 'free' social media app funds itself not through subscription fees but by collecting detailed behavioural data — what a user clicks, how long they linger, what makes them scroll faster — and selling predictive products built from that data to advertisers who want to influence future behaviour. What is this business model called?",
 "options": [
   "Surveillance capitalism — an economic system where personal behavioural data is collected, analysed, and commodified into predictive products sold to advertisers, underlying much of the 'free' internet's actual business model",
   "Federated learning — a technical training method where models are trained across many devices without centralising the raw underlying data, a specific technique for privacy-preserving training rather than a description of a business model",
   "Algorithmic accountability — the practice of ensuring automated decisions are fair, transparent, and contestable, a governance concept rather than a description of an underlying advertising-driven business model itself",
   "AI governance — the regulatory and institutional frameworks societies build to oversee AI development, a policy and oversight concept rather than a specific description of one company's own underlying business model"
 ],
 "answer": 0,
 "explanation": "Surveillance capitalism (a term popularised by Shoshana Zuboff) describes exactly this: 'free' services funded not by direct payment but by extracting and commodifying behavioural data into predictive products sold to advertisers — a business model with real implications for user autonomy and privacy that most users never explicitly agreed to in any meaningful sense."
},
{
 "q": "A tech company publishes a set of internal principles committing to assess potential harms before deploying any new AI feature, actively test for unfair treatment across demographic groups, and maintain a clear process for users to appeal an automated decision. What does this represent, and how does it differ from simply meeting the bare minimum legal requirement?",
 "options": [
   "Responsible AI as an ongoing organisational commitment — going beyond minimum legal compliance to proactively build in fairness assessment, transparency, and human appeal mechanisms as a continuous practice, not a one-time checklist",
   "Federated learning as a technical training method — a specific approach to training models across many devices without centralising data, a narrow technical practice distinct from a company-wide set of ethical operating principles",
   "AI governance as imposed exclusively by external government regulation — a description of only what a government or regulator requires from outside, rather than what a company voluntarily commits to doing on its own initiative",
   "Algorithmic accountability as a purely legal concept with no organisational or cultural dimension whatsoever, applying exclusively to what courts and regulators can enforce rather than to a company's own internal voluntary practices"
 ],
 "answer": 0,
 "explanation": "Responsible AI, done well, is a genuine cultural and organisational commitment that goes beyond whatever the bare legal minimum happens to require — proactively assessing harm, testing for fairness, and maintaining real appeal mechanisms as an ongoing practice, not a one-time compliance checkbox completed and then forgotten."
},
{
 "q": "Ubenwa, a Nigerian/Montreal AI system, analyses the sound of a newborn baby's cry using a smartphone microphone to help detect birth asphyxia in facilities without a specialist available to diagnose it directly. What broader category of AI application does this represent?",
 "options": [
   "AI for social good — applying AI capabilities to genuine societal challenges (like healthcare access gaps) where commercial incentive alone is often insufficient to drive investment, filling real infrastructure gaps rather than chasing profit alone",
   "Surveillance capitalism — an economic model built around collecting and commodifying behavioural data for advertisers, a description that doesn't match a medical diagnostic tool built specifically to help detect a health condition",
   "Model collapse — the gradual degradation of AI model quality across successive generations of training on synthetic data, a technical training phenomenon entirely unrelated to a medical diagnostic tool's actual real-world social purpose",
   "The uncanny valley — the discomfort people feel when a humanoid robot looks almost, but not quite, convincingly human, a robotics design concept entirely unrelated to a smartphone-based newborn cry analysis diagnostic tool"
 ],
 "answer": 0,
 "explanation": "AI for social good specifically describes applying AI capability to genuine societal challenges — health, education, agriculture — where the commercial incentive alone often isn't strong enough to drive investment on its own. Ubenwa is a real, concrete example: filling a genuine specialist-access gap in newborn care rather than chasing a purely commercial opportunity."
},
{
 "q": "A government agency imports a foreign-built AI system for public service delivery, but has no local engineers trained to maintain, adapt, or eventually replace it — creating an ongoing, indefinite dependency on the original foreign vendor. What development concept does this scenario illustrate the importance of?",
 "options": [
   "Technology transfer — the movement of knowledge, skills, and methods (not just finished products) to local organisations, which is what allows a country to move from being a technology consumer toward becoming a technology producer",
   "Model drift — the degradation of a deployed AI model's performance over time as real-world conditions shift away from what it was originally trained on, a technical performance-monitoring concept rather than a development or capacity-building concept",
   "Federated learning — a technique for training a shared AI model across many devices without centralising the underlying raw data, a specific technical training method rather than a broader concept about national technology dependency",
   "The uncanny valley — the discomfort people feel when a humanoid robot looks almost, but not quite, convincingly human, a robotics design concept entirely unrelated to a country's long-term technological capability and independence"
 ],
 "answer": 0,
 "explanation": "Technology transfer specifically emphasises moving knowledge and skills, not just delivering a finished product — training local engineers who can actually maintain, adapt, and eventually build comparable systems, rather than leaving a country perpetually dependent on the original foreign vendor for even routine maintenance."
},
{
 "q": "Economic research suggests that as AI automates routine tasks, radiologists don't disappear as a profession, but their day-to-day work shifts toward reviewing AI-flagged cases and handling complex, ambiguous ones the AI struggles with — while some who over-relied on automation lose the sharp manual-detection skills needed when the AI gets something wrong. What tension does this illustrate?",
 "options": [
   "The automation paradox — automating routine tasks often increases demand for human expertise on the remaining non-routine parts, but can also create a skills trap if people become dependent on automation for skills they can no longer reliably perform manually",
   "Surveillance capitalism — an economic model where personal behavioural data is collected and commodified for advertisers, a description of a business model entirely unrelated to how a medical profession's day-to-day tasks shift due to automation",
   "The uncanny valley — the discomfort people feel when a humanoid robot looks almost, but not quite, convincingly human, a robotics design concept entirely unrelated to how automation changes the nature of a human profession's tasks",
   "Digital inequality — unequal access to digital technologies and connectivity across different groups, a concept about access disparities rather than about how automation changes the actual nature of tasks within one specific profession"
 ],
 "answer": 0,
 "explanation": "The automation paradox captures both sides of this real tension: automating routine work often increases the relative value of human judgement on the remaining hard, ambiguous cases, while simultaneously risking a skills trap where over-reliance erodes the very manual expertise needed for the moments automation fails — both patterns genuinely observed in fields like radiology and aviation."
},
{
 "q": "Training a single large AI model has been estimated to emit hundreds of tonnes of CO2 equivalent, and running billions of daily queries across many AI-powered products multiplies that footprint further. Why has this become a genuine point of active research and debate, rather than a settled non-issue?",
 "options": [
   "Because AI's real energy consumption and associated emissions are non-trivial and growing rapidly with scale and usage, prompting active research into more efficient architectures, hardware, and renewable-powered data centres, weighed against AI's benefits",
   "Because training an AI model has been definitively proven to have precisely zero environmental impact of any kind, making any expressed concern about AI's carbon footprint entirely baseless, unfounded, and without any real supporting basis",
   "Because this specific concern applies exclusively to robots with physical moving parts, and has no meaningful connection whatsoever to software-only AI systems like large language models running purely as code on remote servers",
   "Because every single AI company in the world has already fully and completely solved this specific problem years ago, making it now a purely historical, no-longer-relevant concern with no remaining active research or discussion"
 ],
 "answer": 0,
 "explanation": "AI's real, measurable energy and carbon footprint — from training large models and from running massive query volumes at inference time — has become a genuine, actively researched concern as usage scales, prompting real work on more efficient architectures, better hardware, and renewable-powered data centres, weighed against AI's genuine capability benefits rather than being dismissed as baseless."
},
{
 "q": "A credit-scoring company's algorithm appears neutral on the surface — it doesn't ask for race or gender directly — but a researcher discovers it heavily weights postal code, which happens to correlate strongly with historically segregated neighbourhoods, indirectly reproducing racial disparities in loan approval. What does critically examining technology in this way illustrate?",
 "options": [
   "Thinking critically about technology means evaluating its actual real-world effects and embedded assumptions, not just its stated design intentions — a system can be technically 'neutral' on paper while still reproducing real discrimination through indirect proxies",
   "It proves that any algorithm using a customer's postal code as an input is, by definition, always and unavoidably illegal in every possible jurisdiction, regardless of what that specific postal code data is actually used to predict",
   "It proves that credit-scoring algorithms are fundamentally more discriminatory than a human loan officer would be in every single realistic comparison, without any need to actually study or compare the two approaches directly",
   "It has no real practical importance for how technology should actually be evaluated, since focusing on outcomes rather than a system's original stated design intentions is generally considered an unfair, illegitimate standard"
 ],
 "answer": 0,
 "explanation": "This illustrates why critically examining technology means evaluating its actual real-world effects, not just its surface-level design or stated intentions — a postal code isn't explicitly race, but it can function as a proxy that reproduces the same discriminatory pattern indirectly, which is exactly the kind of hidden effect surface-level 'neutrality' checks miss."
},
{
 "q": "The EU's AI Act classifies AI systems by risk level — banning certain uses outright, imposing strict requirements on 'high-risk' applications like hiring and medical devices, and requiring only basic transparency for lower-risk uses like chatbots. Meanwhile the US has relied more on voluntary commitments and sector-specific rules, and Nigeria is developing its own national AI strategy. What does this global variation illustrate?",
 "options": [
   "AI regulation approaches differ meaningfully across jurisdictions — reflecting different legal traditions, risk tolerances, and priorities — rather than there being one single, universally agreed-upon international standard that every country has simply adopted",
   "It proves that AI regulation is fundamentally impossible to implement in any country, since no two countries described here have adopted the exact identical regulatory framework or the exact identical set of specific legal requirements",
   "It proves that the EU's specific approach to AI regulation is the sole officially recognised international legal standard, and that every other country's differing approach should therefore be considered technically illegitimate",
   "It has no real practical significance for any company operating internationally, since a company's actual compliance obligations are entirely unaffected by which specific country or region its AI product happens to be deployed in"
 ],
 "answer": 0,
 "explanation": "This reflects the genuine current state of global AI governance: meaningfully different regulatory approaches across major jurisdictions, shaped by different legal traditions and priorities, rather than one single settled international standard — which has real practical consequences for any organisation building or deploying AI across multiple countries."
},
{
 "q": "A researcher wants to train an AI model on African clinical, genomic, and agricultural data, but the raw data itself is stored on servers in Europe, subject to European rather than African data protection law, and any resulting valuable AI product is owned by a foreign company with no obligation to share benefits locally. What concept captures the concern being raised here?",
 "options": [
   "Data sovereignty — the principle that data should be subject to the laws of the nation where it was collected, with African countries increasingly building frameworks (like Nigeria's NDPR) asserting more control over locally generated data and its resulting value",
   "Model collapse — the gradual degradation of AI model quality across successive generations of training on synthetic data, a technical training phenomenon unrelated to which specific country's laws govern data storage, ownership, or resulting value",
   "The uncanny valley — the discomfort people feel when a humanoid robot looks almost, but not quite, convincingly human, a robotics design concept entirely unrelated to where clinical, genomic, or agricultural data is physically stored or legally governed",
   "Federated learning — a technical training method where models are trained across many devices without centralising raw data, a specific technique rather than a broader legal and economic concept about who controls and benefits from data"
 ],
 "answer": 0,
 "explanation": "Data sovereignty captures exactly this concern: who controls, and who benefits economically from, data generated within a country — African countries building NDPR-style frameworks are asserting that locally generated data (and the value extracted from it) shouldn't automatically flow to and be controlled entirely by foreign entities with no local accountability."
},
{
 "q": "A health worker in a rural area with unreliable 2G connectivity uses a smartphone app that runs its malaria-diagnosis AI model directly on the device itself, requiring no live internet connection to analyse a blood slide photo and return a result. What technical approach makes this possible, and why does it matter specifically for this context?",
 "options": [
   "Edge AI — running AI inference directly on the end device rather than depending on a cloud connection, enabling real-time results and continued operation exactly where connectivity is expensive, slow, or unreliable, as in many rural African contexts",
   "Surveillance capitalism — an economic model built around collecting and commodifying user behavioural data for advertisers, a description of a business model entirely unrelated to why an offline-capable diagnostic tool would matter in this context",
   "The automation paradox — a tension where automating routine tasks increases demand for human expertise on remaining non-routine work while risking a skills-erosion trap, a labour-market concept distinct from a specific technical connectivity solution",
   "Digital inequality — unequal access to digital technologies, devices, and connectivity across different groups, a description of the underlying problem being addressed here rather than a description of the specific technical solution itself"
 ],
 "answer": 0,
 "explanation": "Edge AI runs the trained model directly on the device rather than requiring a live connection to a distant cloud server, making it specifically well suited to contexts with expensive, slow, or unreliable connectivity — exactly the rural clinic scenario described, where a cloud-dependent tool would simply be unusable when the connection drops."
},
{
 "q": "Nigeria's fintech sector — including companies like Flutterwave and Paystack, built on infrastructure like the CBN's cashless policy, the BVN biometric identity system, and NIBSS instant payments — has become one of the most developed in Africa. What underlying combination of factors most directly enabled this?",
 "options": [
   "A combination of enabling regulation, shared payment infrastructure, and a large underserved market created conditions where private fintech innovation could scale rapidly on top of public groundwork rather than having to build every layer from scratch",
   "It happened entirely by pure random chance, with no meaningful connection whatsoever to any specific government policy, shared payment infrastructure, identity system, or particular characteristic of the underlying Nigerian market itself",
   "Nigerian fintech growth is entirely explained by foreign companies directly and completely building the entire payments ecosystem from scratch, with genuinely no meaningful involvement whatsoever from any Nigerian company, regulator, or local infrastructure",
   "It happened specifically and exclusively because Nigeria banned all use of physical cash outright and entirely nationwide, forcing every single citizen and business to immediately adopt only fintech-based digital payment methods with no alternative"
 ],
 "answer": 0,
 "explanation": "Nigeria's fintech growth reflects a genuine combination of enabling public policy and shared infrastructure (the cashless policy, BVN identity system, NIBSS instant payment rails) that private companies like Flutterwave and Paystack could build on top of, rather than each having to construct foundational payment and identity infrastructure entirely from scratch — plus a large market genuinely underserved by traditional banking."
},
{
 "q": "A drone-based precision agriculture system identifies exactly which specific zones of a large farm are water-stressed and applies irrigation only there, rather than watering the entire field uniformly regardless of actual local need. Beyond simply saving water, what is the broader significance of this approach for smallholder farmers specifically?",
 "options": [
   "It can meaningfully increase yield while reducing waste of costly inputs like water and fertiliser, which matters disproportionately for smallholder farmers operating on tight margins where input costs represent a larger share of their overall limited resources",
   "It has no meaningful broader significance for smallholder farmers specifically, since the benefits of targeted, precision resource application are exactly and identically the same regardless of whether a farm is a small family plot or a large industrial operation",
   "It works by completely eliminating any remaining need for the farmer's own personal judgement, agricultural knowledge, or hands-on decision-making, since the drone system fully and entirely replaces the farmer's own role in every farming-related decision",
   "It is a purely theoretical, laboratory-only concept that has never actually been deployed or tested on any real, working farm anywhere in the world, making its practical real-world benefit for any type of farmer entirely unproven and speculative"
 ],
 "answer": 0,
 "explanation": "Targeted resource application matters disproportionately for smallholder farmers, where input costs (water, fertiliser) represent a larger relative share of tight overall margins compared to large industrial operations — meaning the same precision-agriculture technique that saves a big farm some money can meaningfully change a smallholder's actual profitability and food security."
},
{
 "q": "5G networks are described as enabling three distinct use cases simultaneously: extremely fast mobile broadband for streaming, ultra-reliable low-latency communication for things like remote surgery, and massive device connectivity for IoT sensors — using a technique called network slicing to let all three coexist on the same physical infrastructure. Why does this three-way split matter more than simply calling 5G 'faster 4G'?",
 "options": [
   "Because 5G is designed around fundamentally different use cases with different requirements (raw speed, ultra-low latency, or massive device count) rather than being purely a straightforward speed upgrade, representing a shift from human-centric to also machine-centric network design",
   "Because 5G networks are, in every practical respect, functionally and technically identical to 4G LTE networks, with the only actual difference between the two being an entirely arbitrary marketing name chosen by mobile network operators",
   "Because 5G exclusively and solely supports the specific use case of remote surgery, and does not meaningfully support either fast mobile broadband streaming or massive IoT sensor connectivity in any practical or realistic real-world sense",
   "Because 5G networks can only physically be used with brand new smartphones manufactured after a certain specific year, with genuinely no other meaningful technical distinction whatsoever separating 5G from any earlier generation of mobile network"
 ],
 "answer": 0,
 "explanation": "5G's real significance is architectural, not just raw speed: it's designed to serve genuinely different simultaneous use cases — the fast-lane for streaming, the critical-lane for latency-sensitive applications like remote surgery, and the IoT-lane for massive sensor device counts — representing a meaningful shift from networks designed primarily for human smartphone use toward also serving machine-to-machine communication at scale."
},
{
 "q": "A country debates a proposed law requiring companies to publicly disclose whenever a consequential decision (hiring, lending, insurance pricing) was made or significantly influenced by an AI system, giving affected people the right to request a human review. What is the most direct argument in favour of this kind of transparency requirement?",
 "options": [
   "People affected by consequential automated decisions deserve the ability to understand and potentially contest them, since without disclosure they may not even know an algorithm was involved, let alone have any meaningful path to challenge a wrong or unfair outcome",
   "This kind of transparency requirement would provide no genuine practical benefit of any kind to anyone whatsoever, since virtually no company anywhere in the world currently uses any form of AI for any consequential decision of this type",
   "Requiring this kind of disclosure would make it entirely and completely impossible for any company to ever use AI for hiring, lending, or insurance decisions ever again under any circumstances, effectively banning the practice outright",
   "This kind of transparency requirement is purely symbolic and carries no genuine legal or practical weight whatsoever, since no government or regulator anywhere has ever actually implemented or enforced anything resembling this kind of rule"
 ],
 "answer": 0,
 "explanation": "The core argument for disclosure and a human-review right is that people affected by consequential automated decisions need to actually know an algorithm was involved before they can meaningfully exercise any right to question or contest it — without disclosure, a wrongly-denied applicant may simply never learn there was even anything specific to challenge in the first place."
},
{
 "q": "AI-generated deepfake videos of political leaders, combined with the speed and reach of social media sharing, have made it meaningfully harder to distinguish authentic footage from fabricated content during politically sensitive moments. What does this scenario primarily illustrate about the intersection of AI and society?",
 "options": [
   "AI-generated content at scale creates genuinely new challenges for public trust and information integrity, requiring a combination of technical detection tools, platform policy, and public media literacy rather than any single simple fix",
   "This scenario proves that video evidence of any kind has now become entirely and completely useless as a source of information in absolutely every possible context, with no remaining practical value whatsoever in any situation",
   "This specific concern applies exclusively and only to political figures, and has genuinely no meaningful connection or relevance whatsoever to how deepfake technology might affect ordinary private individuals in any other context",
   "The problem is already fully and completely solved by existing technology today, with reliable, universally deployed automatic detection tools now able to instantly and perfectly catch every single deepfake video with zero errors"
 ],
 "answer": 0,
 "explanation": "The rise of convincing AI-generated video content genuinely raises the difficulty of maintaining public trust in visual evidence, especially during politically sensitive moments — a problem that realistically requires a combination of approaches (better detection tools, platform moderation policy, and public media literacy) rather than one simple technical fix, and one that also affects private individuals through things like non-consensual deepfake harassment, not just public figures."
},
{
 "q": "A city deploys AI-powered traffic cameras with facial recognition capability, initially justified purely as a traffic-violation enforcement tool, but the same camera network is later quietly repurposed to track the movements of political protesters. What does this scenario illustrate about the importance of considering a technology's potential uses beyond its original stated purpose?",
 "options": [
   "Technology built for one purpose can often be repurposed for another, sometimes more concerning one, which is part of why thinking critically about a system's full range of potential future uses — not just its initial stated justification — matters at the design and policy stage",
   "This kind of repurposing is technically impossible for any camera system to ever undergo, since a system's original stated purpose at the time of initial deployment permanently and irreversibly restricts every possible future technical use case",
   "Facial recognition technology used for traffic enforcement specifically has no meaningful technical capability whatsoever to also identify or track any individual person for any other unrelated purpose, making this entire scenario technically implausible",
   "This scenario has no realistic real-world basis and does not reflect any genuine, documented pattern of technology being repurposed beyond its original stated justification in any real city or country anywhere in the world"
 ],
 "answer": 0,
 "explanation": "This reflects a genuinely documented, real pattern of concern with surveillance infrastructure: capability built for one stated purpose (traffic enforcement) can be technically repurposed for another, sometimes far more concerning one (tracking protesters), which is exactly why critically examining a system's full range of potential uses — not just its initial justification — matters when such infrastructure is being designed, funded, and approved in the first place."
},
{
 "q": "A company markets its AI hiring tool as 'completely objective and bias-free' because it doesn't ask about race or gender directly, while independent testing later reveals it systematically down-ranks resumes containing certain names or graduating from certain historically under-resourced schools. What does this gap between the marketing claim and the testing result illustrate?",
 "options": [
   "Claims of AI 'objectivity' need to be independently verified against real-world outcomes, since the absence of an explicitly protected characteristic as an input doesn't guarantee the absence of indirect, proxy-based discrimination in the actual outputs",
   "It proves that the specific independent testing organisation that conducted this evaluation must have made a fundamental, obvious error, since any AI system that doesn't directly ask about race or gender is, by definition, always completely bias-free",
   "It proves that AI hiring tools should never under any circumstances be marketed using any language whatsoever, since using any descriptive marketing language at all for an AI product is inherently and unavoidably fundamentally dishonest",
   "It has no real broader significance beyond this one single specific company's hiring tool, and provides no meaningful lesson whatsoever that would generalise to how AI fairness claims about any other tool or company should be evaluated"
 ],
 "answer": 0,
 "explanation": "This illustrates why AI fairness claims genuinely need independent, outcome-based verification rather than being taken at face value based on stated design intentions — not directly asking about a protected characteristic doesn't prevent a model from learning correlated proxies (like certain names or schools) that reproduce the same discriminatory pattern indirectly, exactly the kind of gap real audits are designed to catch."
},
{
 "q": "An AI ethics board within a company has the formal authority to delay or block the launch of a new AI feature if it identifies unresolved fairness or safety concerns, and has actually exercised that power on at least one past product. How does this differ meaningfully from a company that has an ethics board that exists purely as a public relations statement with no actual authority?",
 "options": [
   "Real authority and a demonstrated willingness to actually exercise it (like delaying a launch) is what distinguishes a genuine accountability mechanism from a symbolic one that exists mainly to be mentioned in marketing or public relations materials",
   "There is no meaningful practical difference whatsoever between these two scenarios, since the mere existence of any ethics board, regardless of its actual formal authority or track record, is always exactly equally effective and meaningful",
   "A company's ethics board having genuine formal authority to block a product launch is illegal in most jurisdictions worldwide, and any board claiming to have exercised such authority must therefore be either exaggerating or fabricating that specific claim",
   "This distinction has no real broader significance for how responsible AI development should actually be evaluated at any company, since a board's formal authority is considered entirely irrelevant to a company's genuine underlying ethical commitment"
 ],
 "answer": 0,
 "explanation": "The meaningful test of a genuine accountability mechanism is real authority combined with a demonstrated willingness to actually use it — a board that has actually delayed or blocked a launch over a real concern is functioning very differently from one that exists mainly as a reassuring line in a company's public relations materials, with no track record of ever actually saying no to anything."
},
{
 "q": "A social media platform's recommendation algorithm is optimised purely to maximise time spent on the app, and independent research later finds it systematically promotes increasingly extreme content because outrage and extremity reliably keep people scrolling longer. What does this illustrate about the risks of optimising an AI system for a single narrow metric?",
 "options": [
   "Optimising purely for one narrow, easily-measured proxy metric (engagement time) can produce genuinely harmful unintended side effects, since the metric being maximised isn't the same thing as what's actually good for users or society",
   "It proves conclusively that all recommendation algorithms used by any social media platform anywhere are always specifically and deliberately designed from the outset with the explicit intention of promoting extreme content to every single user",
   "It has no real connection whatsoever to how AI systems are actually designed or optimised in practice, since this scenario describes a purely hypothetical situation that has never actually been documented or studied by any real independent researcher",
   "It proves that engagement time is mathematically impossible for any AI system to ever measure or optimise for in the first place, making the entire premise of this specific scenario technically implausible from a purely technical standpoint"
 ],
 "answer": 0,
 "explanation": "This reflects a genuine, well-documented pattern: optimising an AI system purely for an easily-measured proxy metric like engagement time can produce real, harmful unintended consequences, since the metric being maximised (time on app) isn't the same as what's actually good for the user or for society — a version of the same 'reward hacking' problem seen in reinforcement learning, applied at massive real-world scale."
},
{
 "q": "A country with limited domestic AI research capacity relies entirely on AI tools built and trained by foreign companies for critical public functions like welfare eligibility screening, with no local ability to audit, adapt, or challenge how those systems actually work. What risk does this dependency create beyond the purely technical concern of the tools' accuracy?",
 "options": [
   "A meaningful loss of local sovereignty and accountability over decisions that significantly affect citizens' lives, since the country has limited practical ability to understand, audit, adapt, or contest systems it doesn't control or fully understand",
   "No meaningful additional risk beyond pure technical accuracy exists in this specific scenario, since a foreign-built AI tool is, by definition, always guaranteed to be more accurate than any equivalent tool that could be built domestically",
   "This kind of dependency is a purely theoretical, hypothetical concern that has no realistic real-world basis or any actual documented precedent involving any real country relying on any foreign-built AI system for any public function",
   "The described dependency actually and directly increases the country's genuine long-term technological independence, since importing an already fully-built foreign AI system is definitionally the fastest possible route to real independent capability"
 ],
 "answer": 0,
 "explanation": "Beyond pure technical accuracy, this kind of dependency creates a real accountability and sovereignty gap: a country with no domestic capacity to audit, adapt, or meaningfully contest a foreign-built system used for a critical public function (like welfare eligibility) has limited practical recourse if that system is flawed, biased, or simply doesn't reflect local context and priorities — a genuine concern motivating investment in local technology transfer and capacity."
},
{
 "q": "Which of the following are genuine, documented reasons AI bias has real social consequences, rather than being a purely abstract technical concern? Select all that apply.",
 "options": [
   "Biased facial recognition systems have contributed to real, documented wrongful arrests",
   "Biased hiring algorithms can systematically exclude qualified candidates based on proxies for protected characteristics",
   "AI bias exclusively and only ever affects a company's internal engineering metrics, with no possible connection to any real person's actual life outcomes",
   "Biased healthcare allocation algorithms have been found to direct less care toward some racial groups for equivalent medical need"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Wrongful arrests linked to biased facial recognition, exclusionary hiring algorithms, and unequal healthcare allocation are all real, documented cases with genuine consequences for real people's lives — directly refuting the claim that AI bias is a purely internal, abstract engineering metric with no real-world impact."
},
{
 "q": "Which of the following are genuine components of what 'responsible AI' generally means in practice, based on how the term is used by organisations that take it seriously? Select all that apply.",
 "options": [
   "Assessing potential harms of a new AI feature before it's deployed, not only after problems are reported",
   "Maintaining a working process for affected users to appeal or contest an automated decision",
   "Simply complying with whatever the bare legal minimum happens to require in a given jurisdiction, and never proactively going beyond that",
   "Continuously monitoring a deployed AI system for issues, rather than treating a launch as the end of the responsibility process"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Proactive pre-deployment harm assessment, real user appeal mechanisms, and ongoing post-launch monitoring are all genuine, commonly cited components of responsible AI practice. Treating bare legal minimum compliance as the ceiling rather than the floor is actually the opposite of what responsible AI generally means — it's specifically framed as going beyond minimum compliance, not stopping exactly at it."
},
{
 "q": "A researcher argues that AI capable of detecting early-stage skin cancer from a smartphone photo should be prioritised for deployment in regions with few dermatologists, even if a slightly more accurate (but far more expensive and hardware-intensive) version exists that only wealthy hospitals could afford. What underlying value judgement is this argument making?",
 "options": [
   "That broad accessibility and real-world reach can sometimes matter more than achieving the absolute highest possible accuracy, especially when the alternative for underserved populations is having no diagnostic access at all, not a choice between two AI tools",
   "That accuracy is entirely and completely irrelevant to any medical AI application whatsoever, and that a diagnostic tool's actual real-world accuracy should never be considered a meaningful factor in any deployment decision under any circumstances",
   "That wealthy hospitals should be legally prohibited from ever using any more accurate or more expensive diagnostic technology, regardless of what other underserved regions elsewhere are currently able to access or afford",
   "That smartphone-based diagnostic tools are always technically superior in every single respect to any hospital-based diagnostic tool, making this entire described tradeoff between accessibility and accuracy essentially a false one"
 ],
 "answer": 0,
 "explanation": "This argument makes a genuine, debatable value judgement about prioritising accessibility and reach over marginal accuracy gains — reasoning that for an underserved population, the realistic alternative to a good-enough accessible tool often isn't a better tool, it's no diagnostic access at all, which changes the calculus compared to a context where the more accurate option is also genuinely available."
},
{
 "q": "A ride-hailing app's algorithm sets driver pay partly based on a passenger's likely willingness to pay a higher fare, inferred from signals like their phone battery level or the neighbourhood they're requesting from. When this practice was revealed, it caused public backlash even though it was technically not illegal in most places. What ethical concern does this scenario raise beyond legality?",
 "options": [
   "That a practice being technically legal doesn't automatically make it fair or ethical — using inferred vulnerability (like a low battery suggesting urgency) to charge some people more raises real fairness concerns independent of whether any specific law was actually broken",
   "That this practice is entirely and completely fictional and has never actually been reported or investigated by any journalist or researcher in connection with any real ride-hailing company anywhere in the world",
   "That phone battery level is technically impossible for any ride-hailing app's backend system to ever access or measure in the first place, making the entire scenario technically implausible from a purely technical standpoint",
   "That any pricing algorithm used by any company anywhere is automatically and always both fair and ethical by definition, provided only that the specific practice in question happens to not be explicitly illegal in that jurisdiction"
 ],
 "answer": 0,
 "explanation": "This scenario (reflecting real reporting on dynamic pricing practices) illustrates that legality and ethics are genuinely separate questions — a practice can be technically permitted while still raising real fairness concerns, particularly when it exploits inferred vulnerability or urgency rather than treating customers consistently, which is exactly why public and regulatory scrutiny of algorithmic pricing has grown."
},
{
 "q": "A school uses an AI-based proctoring tool during online exams that flags a student for 'suspicious behaviour' whenever their eyes move away from the screen — but the tool wasn't tested on students with certain eye conditions or students in poorly-lit rooms common in areas with unreliable electricity, leading to a disproportionate number of false flags for those groups. What does this scenario illustrate about deploying AI systems without adequately diverse testing?",
 "options": [
   "Insufficient testing across the real range of conditions and users a system will actually encounter can produce systematically unfair outcomes for specific groups, even when the harm wasn't the result of any deliberate, intentional design decision",
   "It proves that AI proctoring tools are always completely and entirely accurate for every single student under every possible condition, making the described false-flagging scenario technically impossible to actually occur in real deployment",
   "It has no real connection whatsoever to any broader pattern of AI bias, since eye-tracking software is claimed to be a fundamentally and completely different category of technology from every other type of AI system discussed",
   "It proves conclusively that the school deploying this specific proctoring tool must have done so with explicit, deliberate, and conscious malicious intent specifically targeting students with certain eye conditions or unreliable home electricity"
 ],
 "answer": 0,
 "explanation": "This illustrates a recurring, real pattern in AI bias: harm doesn't require malicious intent — insufficient testing across the actual diversity of real-world conditions and users (lighting, eye conditions, camera quality) a system will genuinely encounter can produce systematically unfair outcomes for specific groups, purely as a consequence of what was and wasn't included during development and testing."
},
{
 "q": "A tech ethicist argues that 'move fast and break things' is a reasonable philosophy for a photo-sharing app's new filter feature, but a dangerously inadequate one for an AI system making bail or medical treatment recommendations. What principle underlies this distinction?",
 "options": [
   "The appropriate level of caution, testing, and oversight before deployment should scale with the real-world stakes and potential harm of a system's failure, not be applied uniformly regardless of what's actually at risk",
   "There is no genuine, meaningful distinction between these two scenarios, and both a photo filter feature and a bail-recommendation system should always be developed and deployed using exactly identical processes and safeguards",
   "Bail and medical recommendation systems should never be built using any form of AI technology whatsoever under any circumstances, while photo filter features should always be built as quickly as technically possible with zero testing",
   "The 'move fast and break things' philosophy is considered equally reasonable and appropriate for literally every possible category of software application, regardless of what real-world consequences a failure might actually cause"
 ],
 "answer": 0,
 "explanation": "This reflects the same proportionate, risk-based reasoning that applies to security and engineering rigor more broadly: the appropriate level of caution and testing scales with actual real-world stakes — a buggy photo filter is a minor inconvenience, while a flawed bail or medical recommendation system can cause serious, sometimes irreversible harm to real people, which reasonably calls for meaningfully more caution and oversight before deployment."
},
{
 "q": "A community group in an underserved neighbourhood is invited to give feedback during the design phase of a new public AI-powered service (like an automated benefits eligibility screener) before it's finalised and deployed, rather than only being informed about it after launch. What is the value of this kind of early, participatory input?",
 "options": [
   "People who will actually be affected by a system often have direct, practical knowledge of edge cases, local context, and real needs that a design team working in isolation is likely to miss, making early input a genuine safeguard, not just a formality",
   "This kind of early community input has no genuine practical value whatsoever, since a technical design team is always definitionally better positioned to fully anticipate every possible real-world edge case without needing any outside input",
   "Early participatory input of this kind is required exclusively by international law in every single country, and its actual practical value to the resulting system's quality is considered entirely incidental and irrelevant to that legal requirement",
   "Community feedback gathered at the design phase can only ever be used symbolically for public relations purposes, and is claimed to never actually meaningfully influence any real technical decision made about how a system is eventually built"
 ],
 "answer": 0,
 "explanation": "People who will actually live with a system's consequences often have genuine, practical knowledge — local context, real edge cases, actual needs — that a design team working in isolation from affected communities is likely to miss, making early participatory input a real safeguard against building something technically functional but poorly fitted to (or actively harmful for) the people it's meant to serve."
},
]
