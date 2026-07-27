# Cybersecurity & Networks — 65 questions, applied-reasoning style.
# (General web/cloud infrastructure like Docker, Kubernetes, OSI model, TLS
# handshake mechanics live in the Programming & Web Systems batch instead —
# this batch focuses on security concepts, attacks, and defences.)
QUESTIONS = [
{
 "q": "A company used to trust any device connected to its internal office network by default, but after a contractor's infected laptop spread malware widely inside the network, they switch to requiring every single access request — even from inside the building — to be separately verified. What security model have they adopted?",
 "options": [
   "Zero-trust security — assuming no user, device, or network segment is inherently trustworthy, and requiring continuous verification for every access request regardless of location",
   "End-to-end encryption — ensuring that only the two people directly communicating can read their messages, with no server or intermediary able to access the plaintext content",
   "A honeypot system — deliberately exposing a fake, vulnerable-looking system to attract and study attackers rather than actually restricting real access to genuine internal systems",
   "Two-factor authentication — requiring a second verification code in addition to a password before any user is allowed to log into any internal company system or resource"
 ],
 "answer": 0,
 "explanation": "Traditional perimeter security trusted everything inside the network boundary — a single infected device could then move freely. Zero-trust flips this: 'never trust, always verify', authenticating every access request regardless of whether it originates inside or outside the office network."
},
{
 "q": "Even if WhatsApp's own servers were hacked or the company were legally compelled to hand over message contents, the messages themselves would remain unreadable gibberish to anyone but the two people chatting. What property of the messaging system makes this true?",
 "options": [
   "End-to-end encryption — only the communicating devices hold the decryption keys, so the service provider itself never has access to the readable, unencrypted content at any point",
   "Zero-trust security — the messaging app treats every single message as untrustworthy by default and therefore refuses to store or transmit any message content on its own servers",
   "A firewall — a network security barrier that filters incoming and outgoing traffic to WhatsApp's servers, which is the specific mechanism that prevents anyone from reading message content",
   "Two-factor authentication — requiring a secondary verification step when logging into WhatsApp, which is the specific mechanism responsible for keeping message content unreadable to outsiders"
 ],
 "answer": 0,
 "explanation": "End-to-end encryption means decryption keys exist only on the users' own devices, never on the provider's servers — so even a full server breach, or a legal order compelling the company to comply, cannot produce readable message content the company itself never had access to."
},
{
 "q": "A small hospital gets hit by ransomware, but instead of being written by the attacker who deployed it, the ransomware was rented from a criminal platform that also handled the ransom negotiation, taking a cut of the payment. What does this illustrate about modern cybercrime?",
 "options": [
   "Ransomware-as-a-service has professionalised cybercrime, letting people with little technical skill rent ready-made attack tools and support services, dramatically lowering the barrier to launching serious attacks",
   "The hospital's own IT staff must have deliberately built and deployed the ransomware themselves, since ransomware can only realistically be installed by someone with legitimate internal system access",
   "Ransomware attacks of this kind are now technically impossible to carry out against hospitals specifically, due to strict healthcare-sector regulations that supposedly prevent this category of attack entirely",
   "This particular case must be a rare, one-off event with no broader pattern, since criminal platforms renting out attack tools to third parties are not something that has been documented before"
 ],
 "answer": 0,
 "explanation": "Ransomware-as-a-service (RaaS) platforms provide the malware, victim-management infrastructure, and even negotiation support to affiliates for a cut of proceeds — meaning technical skill is no longer the barrier to launching a serious ransomware attack, which has contributed significantly to the scale of the modern ransomware epidemic."
},
{
 "q": "In 2020, attackers compromised a single software vendor's update mechanism and, through that one entry point, gained access to roughly 18,000 of the vendor's customer organisations, including US government agencies. What kind of attack does this describe?",
 "options": [
   "A supply chain attack — compromising a trusted vendor, update mechanism, or shared component to reach all of that vendor's downstream customers through a single point of compromise",
   "A denial-of-service attack — flooding the vendor's servers with an overwhelming volume of fake traffic specifically intended to make their software update service completely unavailable to legitimate users",
   "Social engineering — psychologically manipulating individual employees at each of the 18,000 separate customer organisations one at a time into personally installing the malicious update themselves",
   "A zero-trust breach — specifically exploiting a weakness in an organisation's zero-trust security policy, which by definition can only occur inside a single organisation rather than across many"
 ],
 "answer": 0,
 "explanation": "This describes the SolarWinds attack: compromising one widely-trusted software supplier's update mechanism gave attackers a single point of entry into thousands of downstream organisations at once — the defining feature of a supply chain attack, and exactly why vendor security and update integrity matter so much."
},
{
 "q": "A company hires an outside security firm to actively try to break into its own systems — attempting to breach servers, escalate privileges, and extract data — and then documents every weakness found so it can be fixed. What is this practice called?",
 "options": [
   "Penetration testing — authorised, simulated cyberattacks carried out by security professionals to find and document vulnerabilities before real, malicious attackers can discover and exploit them",
   "Ransomware-as-a-service — a criminal business arrangement where the outside security firm is actually secretly deploying ransomware against the company under the guise of a legitimate security test",
   "A supply chain attack — the company deliberately compromising its own trusted software vendors as part of the security test, in order to evaluate how well its own defences would respond",
   "Zero-trust security — a security model the company is adopting purely by hiring the outside firm, entirely independent of whether any actual system testing or attempted breach ever takes place"
 ],
 "answer": 0,
 "explanation": "Penetration testing is ethical, authorised hacking: professionals are deliberately hired to attack an organisation's own systems the way a real attacker would, so that discovered weaknesses can be documented and fixed proactively — a widely used, often regulation-required practice."
},
{
 "q": "A software team used to hand their finished code to a separate security team for review right before release, often finding serious vulnerabilities too late to fix cheaply. They switch to running automated security scans on every single code change as it's written. What is this shift called?",
 "options": [
   "DevSecOps — integrating security practices throughout the development lifecycle rather than treating it as a separate, late-stage review, catching vulnerabilities within minutes of being introduced rather than months later",
   "Zero-trust security — requiring every individual line of code written by any developer to be separately re-verified by a human reviewer before it is permitted to be committed to the shared codebase",
   "Penetration testing — hiring an external security firm to specifically attempt to break into the software product itself immediately after every single code change is committed by any developer",
   "End-to-end encryption — ensuring that the source code itself remains encrypted and unreadable to anyone except the original developer who personally wrote that specific section of code"
 ],
 "answer": 0,
 "explanation": "DevSecOps embeds automated security scanning directly into the development pipeline, catching vulnerabilities in minutes as code is written rather than in a late, separate review stage where fixes are far more expensive and disruptive — a 'shift left' approach that's proven dramatically cheaper and more effective."
},
{
 "q": "A ransomware attack makes a hospital's patient records completely inaccessible, even though the records themselves were never actually stolen or read by the attacker. Which part of the classic CIA security triad (Confidentiality, Integrity, Availability) was most directly violated?",
 "options": [
   "Availability — the records being inaccessible when needed is exactly what this property protects against, regardless of whether the data was also read or copied by the attacker",
   "Confidentiality — since ransomware always necessarily involves the attacker reading and copying every affected record, confidentiality must logically be the property that was violated here",
   "Integrity — since making data inaccessible is definitionally identical to altering or corrupting that same data, integrity is the correct property that was violated in this specific case",
   "None of the three — ransomware attacks that only block access without altering or copying any data are not considered a security violation under the standard CIA triad framework at all"
 ],
 "answer": 0,
 "explanation": "The CIA triad separates three distinct security properties: Confidentiality (only authorised parties can read data), Integrity (data is accurate and unaltered), and Availability (data is accessible when needed). Ransomware that blocks access without reading or altering the underlying data is a textbook Availability attack specifically."
},
{
 "q": "An attacker calls a company's help desk pretending to be a senior executive locked out of their account, creating urgency and pressure until a support agent resets the password without following normal verification steps. What category of attack is this, and why is it often more effective than a purely technical hack?",
 "options": [
   "Social engineering — manipulating human trust, authority, and urgency to bypass security controls, which is often more effective than a technical attack because humans, not systems, are frequently the weakest link",
   "A zero-day exploit — taking advantage of a previously unknown software vulnerability in the help desk's ticketing system, which the attacker discovered before the vendor had any chance to patch it",
   "A supply chain attack — compromising a trusted third-party vendor connected to the help desk's systems, then using that vendor's own compromised access to directly reset the executive's password",
   "A distributed denial-of-service attack — overwhelming the help desk's phone lines with an enormous volume of fake calls specifically in order to force a rushed, less carefully verified password reset"
 ],
 "answer": 0,
 "explanation": "Social engineering exploits psychology rather than software flaws — urgency, authority, and helpfulness are classic levers. Even a technically airtight system can be bypassed if a human is manipulated into taking an unsafe action, which is why security awareness training is as important as any firewall or encryption scheme."
},
{
 "q": "Security researchers warn that a sufficiently powerful future quantum computer could break the RSA and ECC encryption schemes that currently protect most internet traffic, and organisations are being urged to begin migrating to newer, quantum-resistant algorithms now. Why start migrating years before such a computer might even exist?",
 "options": [
   "Encrypted data intercepted and stored today could potentially be decrypted retroactively once a sufficiently powerful quantum computer eventually exists, so long-lived sensitive data needs quantum-resistant protection well in advance",
   "Quantum computers are already widely commercially available today and are actively being used right now by ordinary criminal groups specifically to break everyday internet encryption in real time",
   "RSA and ECC encryption schemes have already been fully broken using entirely conventional, non-quantum computers, making urgent migration to newer algorithms a response to a present, not future, threat",
   "Quantum-resistant algorithms are simpler and computationally cheaper to implement than RSA or ECC, so the urgency to migrate is purely about reducing computing costs rather than about any security threat"
 ],
 "answer": 0,
 "explanation": "This is the 'harvest now, decrypt later' concern: an adversary can capture and store encrypted traffic today, and if a sufficiently powerful quantum computer arrives years from now, retroactively decrypt anything still sensitive at that point — which is why organisations handling long-lived sensitive data are urged to migrate to post-quantum cryptography well before quantum computers are actually capable of breaking today's encryption."
},
{
 "q": "A bank requires customers to enter both their password and a one-time code sent to their phone before logging in. If an attacker steals a customer's password in a data breach, why can't they immediately access the account?",
 "options": [
   "Two-factor authentication requires a second, independent verification factor — something the legitimate user physically has, like their phone — which the attacker doesn't possess even if they've stolen the password",
   "Banks change every customer's password automatically and immediately the moment any data breach occurs anywhere, which is the actual mechanism that prevents the attacker from accessing the account",
   "Passwords stolen in a data breach are always automatically and permanently invalid from that exact moment forward, regardless of whether the account also has any additional login requirement enabled",
   "The attacker's device is automatically and permanently blocked from the bank's network the instant they attempt to use any stolen password, entirely independent of whatever second factor is required"
 ],
 "answer": 0,
 "explanation": "Two-factor authentication (2FA) requires something beyond just a password — typically a code from a device only the legitimate user has physical access to — so a stolen password alone, however it was obtained, is insufficient to log in, meaningfully reducing the impact of common password breaches."
},
{
 "q": "A login form takes a username and inserts it directly into a database query without any filtering. An attacker enters `admin' OR '1'='1` as the username and gains access to every account in the system. What vulnerability did they exploit, and what is the standard fix?",
 "options": [
   "SQL injection — unsanitised user input was interpreted as part of the database query itself; prepared statements, which separate the query structure from user-supplied data, are the standard fix",
   "A zero-day vulnerability — a previously undiscovered flaw specific to this one login form that the vendor has never had any opportunity to patch, unrelated to how user input is generally handled",
   "A supply chain attack — the attacker compromised a trusted third-party software component the login form depends on, rather than directly manipulating the text entered into the username field itself",
   "Social engineering — the attacker psychologically manipulated a human support agent into granting account access, rather than exploiting any weakness in the login form's own underlying code"
 ],
 "answer": 0,
 "explanation": "This is a classic SQL injection: because the raw input was concatenated directly into the query, the attacker's crafted text altered the query's logic to always evaluate true, bypassing authentication. Prepared statements fix this by sending the query structure and the user-supplied data separately, so user input can never be interpreted as executable query logic."
},
{
 "q": "A software vendor discovers, through an active real-world attack, that hackers are exploiting a flaw in their product that the vendor themselves had no prior knowledge of and therefore had no patch ready for. What is this category of vulnerability called?",
 "options": [
   "A zero-day vulnerability — a flaw unknown to the vendor, with no patch available, meaning the only defences available until a fix is released are things like monitoring and isolating vulnerable systems",
   "A supply chain attack — a vulnerability introduced specifically through a trusted third-party vendor or component rather than existing directly within the primary vendor's own original software product",
   "A social engineering attack — a vulnerability that specifically requires manipulating a human being psychologically, rather than existing as a flaw in the software's own underlying code or logic",
   "A DevSecOps failure — a vulnerability that specifically and only occurs when a development team has completely failed to run any automated security scanning during their software's build pipeline"
 ],
 "answer": 0,
 "explanation": "A zero-day vulnerability is unknown to the vendor at the time it's being actively exploited, meaning there's no patch yet available — the most dangerous category of vulnerability, since defenders are limited to indirect measures like anomaly monitoring and isolating exposed systems until a fix ships."
},
{
 "q": "An email claiming to be from a bank asks the recipient to 'urgently verify your account' by clicking a link that leads to a fake login page designed to steal credentials. What is this attack called, and what design feature makes it effective?",
 "options": [
   "Phishing — a fraudulent message designed to trick the recipient into revealing credentials or clicking a malicious link, often effective because it exploits urgency and imitates a trusted, familiar sender",
   "A supply chain attack — compromising the bank's actual software vendor first, which is the technique that is specifically required in order to send a fraudulent email that merely appears to be from the bank",
   "SQL injection — inserting malicious database commands directly into the fraudulent email's text itself, which is the specific mechanism responsible for stealing the recipient's login credentials",
   "A zero-day exploit — taking advantage of a previously undiscovered flaw specifically in the recipient's email client software, unrelated to anything about the message's actual visible content or wording"
 ],
 "answer": 0,
 "explanation": "Phishing exploits trust, urgency, and visual similarity to a legitimate sender to trick people into handing over credentials or clicking malicious links — it's a social-engineering-driven attack delivered via email, not a technical exploit of the email software itself."
},
{
 "q": "A company's network is designed so that a compromised device in the guest WiFi zone cannot directly reach the finance department's internal servers, because the two zones are kept on entirely separate, restricted network segments. What security principle does this illustrate?",
 "options": [
   "Network segmentation — dividing a network into isolated zones so that a compromise in one segment doesn't automatically grant an attacker access to more sensitive segments elsewhere on the same network",
   "End-to-end encryption — ensuring that any data which does manage to travel between the guest WiFi zone and the finance servers is unreadable to anyone except the two directly communicating parties",
   "Two-factor authentication — requiring devices on the guest WiFi zone to provide a second verification factor before they are permitted to physically connect to the guest network in the first place",
   "Penetration testing — the process of a hired security firm attempting, on a periodic basis, to move from the guest WiFi zone into the finance department's servers to test the company's network defences"
 ],
 "answer": 0,
 "explanation": "Network segmentation limits how far an attacker can move after an initial compromise by isolating sensitive systems on separate network zones with restricted paths between them — a core 'defence in depth' principle, since it assumes any single control might eventually fail and limits the blast radius when it does."
},
{
 "q": "A company stores customer passwords not as plain readable text, but as scrambled values produced by a one-way mathematical function, with a unique random value added per password before scrambling. Even the company itself cannot reverse this process to see the original password. What two techniques does this describe together?",
 "options": [
   "Hashing and salting — hashing produces a one-way scrambled value that can't be reversed back to the original password, and salting adds a unique random value per password to prevent identical passwords from producing identical stored values",
   "Two-factor authentication and zero-trust security — requiring both a password and a separate verification code, combined with treating every login attempt as untrusted regardless of where it originates from",
   "End-to-end encryption and penetration testing — encrypting the password so only the two communicating parties can read it, combined with periodically hiring an outside firm to test the storage system's security",
   "Network segmentation and DevSecOps — storing passwords on an isolated network segment separate from other company data, combined with running automated security scans on the password storage code"
 ],
 "answer": 0,
 "explanation": "Password hashing (a one-way function that can't practically be reversed) combined with a unique random salt per password (preventing identical passwords from producing identical stored hashes, which would otherwise make pattern-based cracking easier) is the standard practice for storing passwords securely — genuinely different from reversible encryption."
},
{
 "q": "A website is suddenly flooded with millions of fake requests per second from thousands of hijacked devices around the world, overwhelming its servers and making it completely unreachable for real customers. What is this attack called?",
 "options": [
   "A distributed denial-of-service (DDoS) attack — overwhelming a target with traffic from many compromised devices at once, aiming to exhaust its capacity to serve legitimate users rather than to steal any data",
   "A SQL injection attack — inserting malicious database commands into millions of separate website requests simultaneously, which is the specific technique used to make the entire website unreachable at once",
   "A phishing attack — sending millions of fraudulent emails to the website's actual customers at the same time, which indirectly causes the resulting flood of concerned customer traffic to the real website",
   "A zero-day exploit — taking advantage of a single previously undiscovered software flaw, which by itself is what causes the website to receive millions of simultaneous requests from around the world"
 ],
 "answer": 0,
 "explanation": "A distributed denial-of-service attack floods a target with overwhelming traffic from many sources at once (often a botnet of hijacked devices), aiming purely to exhaust its capacity to serve legitimate traffic — an Availability attack, distinct from attacks that aim to steal or alter data."
},
{
 "q": "After discovering a data breach, a company's incident response plan requires them to notify affected customers within a specific number of days, contain the breach, and report it to a data protection regulator. In Nigeria, which regulation most directly governs these breach notification obligations?",
 "options": [
   "The Nigeria Data Protection Regulation (NDPR) — governing how personal data is collected, processed, and protected in Nigeria, including breach handling and notification obligations",
   "The CIA triad — a security framework describing Confidentiality, Integrity, and Availability, which does not itself carry any legal breach notification requirement for organisations operating in Nigeria",
   "Two-factor authentication standards — a technical security control requirement that has no direct connection to any legal obligation to notify customers or regulators after a data breach occurs",
   "DevSecOps guidelines — a set of software development practices that integrate security into the development lifecycle, unrelated to any legal or regulatory breach notification requirement"
 ],
 "answer": 0,
 "explanation": "The NDPR is Nigeria's framework governing personal data protection, including obligations around how organisations must handle and report data breaches — a legal and regulatory layer that exists alongside (and is enforced independently of) an organisation's technical security controls."
},
{
 "q": "A company deliberately sets up a decoy server that looks like a valuable target, with no real data on it, specifically to attract attackers and study their techniques without risking any genuine company system. What is this decoy called?",
 "options": [
   "A honeypot — a deliberately exposed, fake system designed to attract attackers, letting defenders study attack techniques and sometimes detect intrusions early, without risking real assets",
   "A firewall — a network security barrier that filters incoming and outgoing traffic, which by definition cannot itself be configured to appear as an attractive, seemingly vulnerable target to attackers",
   "A zero-trust network — a security architecture that fundamentally requires every single request to be independently verified, which is unrelated to the concept of deliberately deploying any decoy system",
   "An air-gapped system — a computer or network that is physically and completely disconnected from the internet or any other outside network, which by definition cannot attract any remote attacker at all"
 ],
 "answer": 0,
 "explanation": "A honeypot is a deliberately exposed decoy system with no real value, designed specifically to attract attackers so their techniques can be studied (or an intrusion detected early) without risking genuine company assets — a defensive and intelligence-gathering tool, distinct from a firewall or network segmentation."
},
{
 "q": "A nuclear power plant's most critical control systems are kept on a network with absolutely no physical or wireless connection to the internet or to any other network, specifically to prevent any remote attack. What is this security approach called?",
 "options": [
   "Air-gapping — physically isolating a critical system from all outside networks so it cannot be reached remotely, though it remains vulnerable to attacks delivered through physical access, such as an infected USB drive",
   "Zero-trust security — a security model requiring every single access request to be separately verified, which necessarily also requires the system to remain fully connected to the internet at all times",
   "End-to-end encryption — ensuring that any data which does travel to or from the critical system remains unreadable to anyone except the two directly communicating parties on either end of the connection",
   "Penetration testing — periodically and specifically hiring an outside security firm to attempt to physically break into the nuclear plant's building in order to directly access its most critical control systems"
 ],
 "answer": 0,
 "explanation": "Air-gapping removes all network connectivity as an attack vector, making remote attacks essentially impossible — but it isn't a complete solution, since physical access vectors like an infected USB drive (as famously exploited by the Stuxnet attack on isolated industrial systems) remain a real risk."
},
{
 "q": "An attacker who obtained a list of leaked username-password pairs from one breached website automatically tries the exact same combinations on dozens of other unrelated websites, hoping some users reused their password. What is this attack called, and what is the most effective individual defence against it?",
 "options": [
   "Credential stuffing — automatically testing stolen username-password pairs across many services; using a unique password per site (often via a password manager) is the most effective individual defence",
   "SQL injection — inserting malicious database commands into the login form of each of the dozens of separate websites, which is the specific technique used to test the stolen username-password pairs",
   "A zero-day exploit — taking advantage of a previously undiscovered software flaw present in every one of the dozens of unrelated websites being targeted with the same stolen credential list",
   "A supply chain attack — compromising a shared third-party vendor used by all of the dozens of unrelated websites simultaneously, rather than directly testing any of the actual stolen credential pairs"
 ],
 "answer": 0,
 "explanation": "Credential stuffing exploits password reuse across services: a breach at one site becomes a master key to any other account where the victim reused the same password. Using a unique password per site — practically achievable only with a password manager for most people — directly neutralises this specific attack, since a leak on one site no longer unlocks accounts elsewhere."
},
{
 "q": "A login page requires users to identify all the images containing a bicycle before allowing a login attempt, specifically to distinguish human users from automated scripts. What is this kind of check generally called, and what specific problem is it designed to address?",
 "options": [
   "A CAPTCHA — a challenge designed to be easy for humans but hard for automated bots, used to prevent automated scripts from mass-attempting logins, creating fake accounts, or scraping content at scale",
   "Two-factor authentication — a security measure requiring a second independent verification factor, of which an image-identification challenge like this is considered one of the standard recognised forms",
   "A honeypot — a deliberately exposed decoy system, of which requiring users to identify bicycle images before logging in is considered one specific standard implementation used by many companies",
   "End-to-end encryption — a technique ensuring that only the communicating parties can read message content, of which visual challenges like bicycle-image identification are considered one common form"
 ],
 "answer": 0,
 "explanation": "CAPTCHAs are specifically designed to be easy for humans but difficult for automated scripts, defending against bot-driven abuse like mass account creation, credential-stuffing attempts, or large-scale content scraping — a different purpose from 2FA, which verifies a specific human's identity rather than distinguishing humans from bots generally."
},
{
 "q": "A company's security policy requires that sensitive customer data be encrypted both while it's stored on their servers and while it's being transmitted over the network between systems. Why is protecting both states necessary, rather than just one?",
 "options": [
   "Data at rest (stored) and data in transit (being transmitted) face different threats — a stolen hard drive exposes unencrypted stored data, while network interception exposes unencrypted transmitted data — so both need independent protection",
   "Encrypting data in only one of these two states is always technically impossible for any real computer system to actually implement, which is the specific reason both states must be protected together",
   "Data at rest and data in transit are simply two different names for the exact same underlying technical state, so encrypting one automatically and necessarily also encrypts the other at the same time",
   "This requirement exists purely for regulatory compliance reasons with no genuine underlying security benefit, since encrypting data in only one of the two states would provide fully equivalent real protection"
 ],
 "answer": 0,
 "explanation": "Encryption at rest and encryption in transit protect against genuinely different threat scenarios: a stolen or improperly accessed storage drive exposes data at rest if unencrypted, while a network eavesdropper (like on unsecured WiFi) exposes data in transit if unencrypted — real, independent risks that require separately implemented protections."
},
{
 "q": "An employee who legitimately has access to a company's customer database quietly copies sensitive records and sells them to a competitor before resigning. What category of security risk does this represent, and why can it be harder to prevent than an external hacking attempt?",
 "options": [
   "An insider threat — someone with legitimate authorised access misusing it, which can be harder to prevent than external attacks because the person's access itself isn't inherently suspicious, unlike an unauthorised outsider breaking in",
   "A zero-day exploit — the employee is taking advantage of a previously unknown software vulnerability in the database system, which happens to only be exploitable by someone who already has legitimate access",
   "A distributed denial-of-service attack — the employee is intentionally overwhelming the customer database with traffic in order to make it completely unavailable to other legitimate company employees",
   "A supply chain attack — the employee is functioning as a compromised third-party vendor within the company's own systems, rather than as a directly and legitimately employed member of staff"
 ],
 "answer": 0,
 "explanation": "Insider threats are particularly hard to prevent with traditional perimeter-focused defences, because the person already has legitimate credentials and access — detecting misuse typically requires monitoring for unusual patterns of legitimate access (like an unusually large data export) rather than blocking unauthorised entry, which is what most external-facing security controls are built for."
},
{
 "q": "An organisation regularly runs simulated phishing emails against its own staff, then provides short, immediate training to anyone who clicks the fake malicious link. What does this practice most directly acknowledge about cybersecurity?",
 "options": [
   "Technical defences alone aren't sufficient — since humans are frequently the weakest link in a security chain, ongoing security awareness training is a necessary complement to firewalls, encryption, and other technical controls",
   "Simulated phishing training is purely a legal formality with no genuine effect on reducing real successful phishing attacks, and organisations only run these programmes to reduce their own liability",
   "Any employee who clicks a simulated phishing link even once should always be immediately terminated from their position, since this is the only proven effective response to this kind of security lapse",
   "Real phishing attacks have become entirely obsolete and are no longer a genuine security threat to any organisation, making this kind of ongoing simulated training programme fundamentally unnecessary today"
 ],
 "answer": 0,
 "explanation": "Simulated phishing exercises directly test and reinforce the human layer of an organisation's defences, reflecting the well-documented reality that technical controls alone don't stop attacks that specifically target human judgement and trust — training is a necessary complement, not a replacement, for technical security measures."
},
{
 "q": "A smart doorbell camera ships with a default admin password of 'admin' that most owners never change, and years later, hundreds of thousands of these cameras are hijacked and used together to launch a massive denial-of-service attack against an unrelated target. What vulnerability class does this illustrate?",
 "options": [
   "Poor IoT device security — Internet of Things devices are often shipped with weak default credentials and infrequent security updates, making them an easy, large-scale target for attackers to hijack and weaponise",
   "A supply chain attack — the doorbell manufacturer's own trusted software vendor was directly compromised first, which is the specific technique required in order to hijack hundreds of thousands of separate cameras",
   "SQL injection — malicious database commands were inserted directly into each individual doorbell camera's login form, which is the specific technique that allowed hundreds of thousands of them to be hijacked",
   "A zero-trust failure — the doorbell cameras were specifically configured using a zero-trust security model, which is what directly enabled the large-scale hijacking of hundreds of thousands of separate devices"
 ],
 "answer": 0,
 "explanation": "This describes the real pattern behind the Mirai botnet: IoT devices with weak default credentials and rarely updated firmware make an enormous, easy-to-hijack attack surface, which attackers can combine into a botnet capable of launching devastating large-scale denial-of-service attacks against unrelated targets."
},
{
 "q": "A user connects to public café WiFi and, without any additional protection, an attacker on the same network is able to intercept and read their unencrypted traffic between their laptop and a website. Which two technologies would each independently help protect against this specific risk? Select all that apply.",
 "options": [
   "Using a VPN, which encrypts traffic between the device and the VPN server, protecting it from anyone else on the local café WiFi network",
   "Only visiting websites that use HTTPS, which encrypts traffic between the browser and that specific website using TLS",
   "Increasing the WiFi router's broadcast signal strength, which is the setting that determines whether traffic on the network is encrypted",
   "Disabling the laptop's firewall temporarily while connected to the public café WiFi network specifically"
 ],
 "answer": [0, 1],
 "multi": True,
 "explanation": "A VPN encrypts traffic to a trusted VPN endpoint, and HTTPS encrypts traffic to the specific website being visited — both genuinely protect against a local network eavesdropper on unsecured public WiFi. Signal strength has nothing to do with encryption, and disabling a firewall would make the situation worse, not better."
},
{
 "q": "An attacker sets up a fake WiFi hotspot in a coffee shop with a name identical to the shop's real network, then intercepts and modifies traffic from anyone who unknowingly connects to it instead of the real network. What is this general category of attack called?",
 "options": [
   "A man-in-the-middle attack — secretly intercepting (and potentially altering) communication between two parties who believe they are communicating directly with each other or with a legitimate service",
   "A zero-day exploit — taking advantage of a previously undiscovered software vulnerability specific to the coffee shop's real WiFi router, unrelated to setting up any separate fake network of any kind",
   "SQL injection — inserting malicious database commands directly into the traffic of anyone who connects to the fake WiFi hotspot, which is the specific technique used to intercept their communications",
   "Ransomware-as-a-service — renting ready-made attack tools from a criminal platform, which is the specific technique required in order to set up a fake WiFi hotspot with a name matching a real one"
 ],
 "answer": 0,
 "explanation": "A man-in-the-middle attack positions the attacker between two parties who believe they're communicating directly, letting them intercept, read, or alter traffic — a fake WiFi hotspot mimicking a legitimate one is a classic, low-tech real-world example of this attack pattern."
},
{
 "q": "A bank uses a customer's fingerprint or face scan, rather than a password, to unlock their mobile banking app. What is the primary security tradeoff of biometric authentication compared to a traditional password?",
 "options": [
   "Biometrics are convenient and hard to forget, but unlike a compromised password, a compromised biometric trait (like a leaked fingerprint template) generally cannot simply be 'changed' the way a password can",
   "Biometric authentication provides no meaningful security benefit whatsoever compared to a password, and banks that use it are doing so purely for marketing purposes rather than any genuine security reason",
   "Biometrics are always mathematically impossible to forge or spoof under any circumstances, making them a strictly and unconditionally superior replacement for every possible password-based system",
   "Biometric data, unlike a password, is never stored anywhere by the bank, which is the specific reason it is considered by security researchers to be completely immune to any form of data breach"
 ],
 "answer": 0,
 "explanation": "Biometrics offer real convenience and resist certain attacks (like credential stuffing, since you can't 'reuse' a fingerprint across services in the way passwords get reused) — but a fundamental tradeoff is that if a biometric template is ever compromised, the person can't simply reset it the way they'd reset a leaked password, since their fingerprint or face doesn't change."
},
{
 "q": "A company's security team notices unusually large volumes of data being copied from an internal server to an external address late at night, and their monitoring system automatically flags and blocks the transfer for investigation. What kind of security tool most directly enabled this detection?",
 "options": [
   "An intrusion detection/prevention system (IDS/IPS) — monitoring network traffic for suspicious patterns and automatically flagging or blocking activity that deviates from normal, expected behaviour",
   "A honeypot — a decoy system with no real data, which by design cannot detect or block any unusual activity occurring on the company's actual genuine internal servers late at night",
   "End-to-end encryption — a technique that makes message content unreadable to anyone except the two communicating parties, which has no role in detecting or blocking unusual data transfer volume",
   "Two-factor authentication — a login security measure requiring a second verification factor, which has no role in monitoring or blocking data transfers that occur after a user has already logged in"
 ],
 "answer": 0,
 "explanation": "Intrusion detection and prevention systems monitor network traffic patterns for anomalies — like an unusually large, oddly-timed data transfer — and can automatically flag or block suspicious activity, complementing perimeter defences by watching for suspicious behaviour that's already inside the network."
},
{
 "q": "A software vendor releases a patch fixing a serious vulnerability in their product, but a company takes eight months to actually install it on their systems. During those eight months, what is the company's actual risk exposure?",
 "options": [
   "Ongoing and serious — once a patch is public, attackers can study exactly what it fixes and target unpatched systems specifically, meaning delayed patching leaves a known, now-public vulnerability exploitable for as long as the delay lasts",
   "None at all, because releasing a patch automatically and immediately protects every affected system worldwide the moment the vendor publishes it, regardless of whether any individual company actually installs it",
   "Lower than before the patch was released, because the mere existence of an available patch is itself sufficient to deter any realistic attacker from attempting to exploit the underlying vulnerability",
   "Identical to the risk faced by every other company in the world, because patch timing has no meaningful bearing whatsoever on an individual organisation's actual specific exposure to this vulnerability"
 ],
 "answer": 0,
 "explanation": "A public patch effectively also publishes a roadmap of the vulnerability it fixes, since attackers can compare the patched and unpatched code to understand exactly what to exploit — making prompt patching genuinely important, and slow patching a real, ongoing, and often actively targeted risk."
},
{
 "q": "Which of the following are legitimate, commonly recommended components of a strong password policy, according to current security guidance? Select all that apply.",
 "options": [
   "Using a unique password for each different account or service, rather than reusing the same one everywhere",
   "Using a password manager to generate and store long, random passwords the user doesn't need to memorise",
   "Requiring users to change every password every single day regardless of whether any breach has actually occurred",
   "Enabling two-factor authentication in addition to a strong password wherever it's available"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Password uniqueness, password managers, and 2FA are all genuinely recommended current practices. Forced daily password changes with no evidence of compromise is actually discouraged by modern security guidance (like NIST's), since it tends to push users toward weaker, more predictable passwords and password-reuse patterns rather than improving security."
},
{
 "q": "Which of the following attacks specifically rely on manipulating human psychology (trust, urgency, authority, or helpfulness) rather than exploiting a purely technical software flaw? Select all that apply.",
 "options": [
   "A phishing email impersonating a bank to trick someone into entering their login credentials on a fake page",
   "A phone call from someone impersonating IT support, pressuring an employee to reveal their password over the phone",
   "A SQL injection attack exploiting unsanitised input in a website's login form",
   "An attacker leaving a USB drive labelled 'Confidential Salaries' in an office car park, hoping curiosity leads someone to plug it into a company computer"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Phishing, pretexting phone calls, and the 'baiting' USB drive trick are all classic social engineering techniques exploiting human psychology rather than a software bug. SQL injection, by contrast, exploits a specific technical flaw in how a system processes input — a purely technical vulnerability, not a manipulation of any person."
},
{
 "q": "A company purchases a cyber insurance policy to help cover costs if they suffer a major data breach. Which of the following is the most accurate description of what cyber insurance actually does for the company's overall security posture?",
 "options": [
   "It helps manage the financial impact of a breach (like legal costs, notification costs, and some recovery expenses), but it does not itself prevent breaches or replace the need for genuine technical and organisational security measures",
   "It technically prevents breaches from occurring in the first place, since insurance companies directly monitor and secure every policyholder's network infrastructure as a condition of coverage",
   "It completely eliminates the need for the company to implement any technical security controls at all, since any resulting financial losses will simply be fully covered by the insurance policy regardless of cause",
   "It is legally required in essentially every jurisdiction worldwide for any company that stores any customer data whatsoever, functioning as a direct substitute for regulatory compliance obligations like the NDPR"
 ],
 "answer": 0,
 "explanation": "Cyber insurance is a financial risk-management tool — helping absorb the cost impact of an incident — not a technical control that prevents breaches from happening, and it typically doesn't remove an organisation's own responsibility to implement genuine security measures or comply with regulations like the NDPR."
},
{
 "q": "A development team designs a new payment feature by first identifying every way an attacker might try to steal payment details or manipulate a transaction, then builds specific defences against each identified scenario before writing the actual production code. What practice does this describe?",
 "options": [
   "Threat modelling — systematically identifying potential attack scenarios and designing defences against them proactively, ideally before a system is even fully built, rather than reacting to attacks after deployment",
   "Penetration testing — hiring an outside security firm to attempt an actual real attack against the finished, fully deployed payment feature after it has already been built and released to real customers",
   "A honeypot — deliberately deploying a fake, decoy version of the new payment feature specifically to attract and study real attackers, rather than to identify potential attack scenarios in advance",
   "DDoS mitigation — a specific technique for absorbing and filtering large volumes of malicious network traffic, unrelated to identifying potential ways an attacker might manipulate a payment transaction"
 ],
 "answer": 0,
 "explanation": "Threat modelling is a proactive design-phase practice: systematically thinking through how a system could be attacked and building defences against those specific scenarios before (or while) it's built, complementing later-stage practices like penetration testing that test an already-built system."
},
{
 "q": "An attacker tries every possible combination of characters against a login form until one happens to match the correct password, given enough time and no rate limiting. What is this attack called, and what is a common, effective defence against it?",
 "options": [
   "A brute-force attack — systematically trying every possible password combination; rate-limiting login attempts (and requiring longer, more complex passwords) makes this approach impractically slow for an attacker",
   "SQL injection — inserting malicious database commands directly into the login form in order to systematically try every possible password combination against the underlying database itself",
   "A supply chain attack — compromising the login form's underlying third-party software vendor first, which is the specific technique required in order to systematically try password combinations",
   "Social engineering — psychologically manipulating a human support agent into personally providing every possible password combination for the specific account being targeted by the attacker"
 ],
 "answer": 0,
 "explanation": "A brute-force attack relies on sheer trial-and-error volume. Rate-limiting (locking out or slowing down after repeated failed attempts) combined with longer, higher-entropy passwords makes the sheer number of combinations an attacker would need to try impractically large — a straightforward, effective, and widely implemented defence."
},
{
 "q": "A company's data protection officer explains that under Nigeria's NDPR, if a data breach affects a large number of individuals, the company generally must notify both the regulator and, in serious cases, the affected individuals themselves — not just quietly fix the issue internally. What is the underlying rationale for requiring this kind of notification?",
 "options": [
   "Affected individuals need the opportunity to protect themselves (such as changing reused passwords or watching for fraud), and regulatory oversight creates real accountability pressure for organisations to take data protection seriously",
   "Breach notification requirements exist purely as a bureaucratic formality with no genuine practical benefit to anyone, imposed on companies solely to generate additional government paperwork and administrative fees",
   "Notifying affected individuals about a breach is what actually causes the underlying technical vulnerability to be automatically and immediately patched by the company's own development team without further action",
   "This kind of requirement only exists in Nigeria specifically and reflects no broader international consensus or comparable practice anywhere else, such as the EU's GDPR or other data protection frameworks"
 ],
 "answer": 0,
 "explanation": "Breach notification rules (found in the NDPR, GDPR, and similar frameworks worldwide) exist because affected individuals often can't protect themselves against a breach they don't know happened, and public/regulatory accountability creates a genuine incentive for organisations to invest seriously in security rather than quietly absorbing incidents."
},
{
 "q": "A hospital's patient monitoring devices run outdated software full of known vulnerabilities, but replacing them all at once would be extremely costly and disruptive to ongoing patient care. As an interim measure, the hospital places all these devices on a separate, tightly restricted network segment with no direct internet access. What security principle does this interim measure reflect?",
 "options": [
   "Defence in depth combined with network segmentation — since a full fix (replacing the devices) isn't immediately feasible, isolating the vulnerable devices reduces their exposure and limits potential damage in the meantime",
   "Zero-day patching — the hospital has effectively created and applied its own official software patch to fix the underlying vulnerabilities directly on each individual outdated patient monitoring device",
   "End-to-end encryption — isolating the vulnerable devices on a separate network segment is itself a specific technical form of encrypting the patient data these devices generate and transmit",
   "Penetration testing — placing the vulnerable devices on a separate restricted network segment is itself considered a form of authorised, simulated attack against the hospital's own systems"
 ],
 "answer": 0,
 "explanation": "When a root-cause fix (patching or replacing vulnerable devices) isn't immediately feasible, layered compensating controls like network segmentation reduce exposure and limit potential damage in the meantime — a practical real-world illustration of 'defence in depth': not relying on any single control being perfect."
},
{
 "q": "A newly hired employee is given access only to the specific systems and data genuinely required for their particular job role, rather than broad access to everything in the company by default. What security principle does this reflect, and what risk does it directly reduce?",
 "options": [
   "The principle of least privilege — granting only the minimum access necessary for a role, which limits both the potential damage from a compromised account and the scope of an insider threat",
   "Zero-trust security — granting broad access by default to every new employee, which is specifically what the zero-trust model requires organisations to do for all newly hired staff members",
   "Network segmentation — a principle that applies exclusively to dividing physical network infrastructure into isolated zones, with no meaningful application to how individual employee accounts are configured",
   "Two-factor authentication — a principle that applies exclusively to how a single employee logs into any individual system, with no meaningful connection to how broad or narrow their overall access is"
 ],
 "answer": 0,
 "explanation": "The principle of least privilege limits each account to only the access genuinely needed for its role — directly reducing both the potential damage if that specific account is compromised externally, and the scope of what an insider could misuse, since neither an attacker nor a rogue employee can reach systems the account was never granted access to in the first place."
},
{
 "q": "A retailer's point-of-sale systems were breached, and investigators later find the attackers first gained access through a much less secure, internet-connected HVAC (heating and cooling) contractor's system that had a trusted network connection into the retailer's broader systems. What lesson does this real pattern reinforce about supply chain and third-party risk?",
 "options": [
   "An organisation's overall security is only as strong as its weakest connected third party, so vetting and restricting the access of vendors and contractors is a genuine part of an organisation's own security posture",
   "HVAC systems are the single most common and by far the most dangerous entry point for cyberattacks against retailers specifically, more so than any other possible category of third-party vendor or contractor",
   "This kind of breach could only ever happen to a retailer specifically, since heating and cooling contractors are never granted any form of network access by companies operating in any other industry",
   "Third-party vendor access has no meaningful bearing on an organisation's own security, since responsibility for a breach originating through a vendor's system always rests entirely with that vendor alone"
 ],
 "answer": 0,
 "explanation": "This reflects a real, well-documented pattern (echoing the 2013 Target breach): attackers often look for the weakest link in a connected ecosystem, and a trusted but poorly secured third-party connection can become the actual entry point into an otherwise well-defended primary target — which is why vendor security vetting is a genuine, necessary part of an organisation's own risk management."
},
{
 "q": "A company detects a breach at 2am, and its documented incident response plan specifies exact steps: isolate affected systems, preserve evidence, notify a specific response team, assess scope, and only then begin recovery — rather than staff improvising a response in the moment. What is the main benefit of having this plan prepared in advance?",
 "options": [
   "It enables a faster, more consistent, and less error-prone response under real pressure, reducing both the technical damage and the risk of destroying evidence needed to understand and fully remediate the breach",
   "It has no genuine practical benefit at all beyond satisfying a purely bureaucratic paperwork requirement, and companies without such a plan generally respond to breaches equally well in practice",
   "It guarantees that no breach will ever cause any actual damage whatsoever, regardless of how severe, sophisticated, or fast-moving the specific attack in question happens to be",
   "It exists purely to assign formal blame to specific individual staff members after a breach has occurred, rather than to actually guide any part of the technical response itself"
 ],
 "answer": 0,
 "explanation": "A pre-documented incident response plan means critical steps (isolation, evidence preservation, notification, scoping) happen in a considered, consistent order under real time pressure, rather than being improvised in a moment of panic — reducing both the technical damage from a slow or chaotic response and the risk of destroying evidence needed to fully understand what happened."
},
{
 "q": "A piece of malicious software spreads automatically from computer to computer across a network with no human action required, unlike a virus which typically needs a user to open an infected file to spread. What type of malware does this describe?",
 "options": [
   "A worm — self-replicating malware that spreads across networks autonomously, without requiring a human to open or execute an infected file the way a traditional virus generally does",
   "A trojan — malware disguised as legitimate software that a user is specifically tricked into willingly installing themselves, which by definition requires that direct human action to spread at all",
   "Ransomware — malware that specifically encrypts a victim's files and demands payment for their release, a behaviour unrelated to whether the malware requires human action in order to initially spread",
   "Spyware — malware designed specifically to covertly monitor and collect a user's activity and personal information, a behaviour unrelated to whether the malware needs human action to spread"
 ],
 "answer": 0,
 "explanation": "A worm is specifically defined by its ability to self-replicate and spread across a network autonomously, without needing a human to open a file or click anything — a meaningfully different propagation method from a virus (needs an infected file opened) or a trojan (needs a user tricked into installing it)."
},
{
 "q": "An attacker steals the small text file a website uses to remember that a user is already logged in, and uses it on their own browser to impersonate that logged-in user without ever needing the actual password. What is this attack called?",
 "options": [
   "Session hijacking — stealing or forging a valid session token (like a login cookie) to impersonate an already-authenticated user, bypassing the need to know their actual password at all",
   "SQL injection — inserting malicious database commands directly into the website's login form, which is the specific technique required in order to steal another user's session cookie",
   "A brute-force attack — systematically trying every possible password combination against the website's login form, until eventually one combination matches the targeted user's actual password",
   "A supply chain attack — compromising a trusted third-party vendor connected to the website first, which is the specific technique required in order to steal another user's active session cookie"
 ],
 "answer": 0,
 "explanation": "Session hijacking targets the token proving a user is already authenticated, rather than their credentials — if an attacker obtains a valid session cookie, they can impersonate that logged-in user directly, entirely bypassing the login process and the password itself."
},
{
 "q": "A hospital keeps daily backups of its patient records on a separate system, so that even if ransomware encrypts the primary database, the hospital can restore from a recent backup without paying the ransom. Which security property does a solid backup strategy most directly protect, and why is it not a complete substitute for actual malware prevention?",
 "options": [
   "Availability — backups directly protect against data becoming inaccessible, but they don't prevent the initial breach or stop attackers from also having read or copied sensitive data before encrypting it",
   "Confidentiality — backups directly ensure that ransomware attackers are physically unable to read or copy any sensitive patient data at any point, which is the primary property backups are designed to protect",
   "Integrity — backups directly guarantee that no attacker can ever alter or corrupt the hospital's original patient records, which is the primary property that a solid backup strategy is designed to protect",
   "Backups provide no meaningful security benefit at all in a ransomware scenario, since ransomware is specifically designed to also permanently corrupt and encrypt any and all connected backup systems"
 ],
 "answer": 0,
 "explanation": "Backups are primarily an Availability safeguard — letting an organisation recover access without paying a ransom — but they don't address Confidentiality (if data was also exfiltrated and threatened with public release, a real modern ransomware tactic) or prevent the initial breach itself, which is why prevention and backups are complementary, not substitutes for each other."
},
{
 "q": "Two encryption approaches exist: one where the sender and receiver share the exact same secret key for both locking and unlocking a message, and another where a public key locks a message that only a separate, mathematically related private key can unlock. What is the second approach called, and why does it solve a key-distribution problem the first approach has?",
 "options": [
   "Public-key (asymmetric) encryption — anyone can use a recipient's freely published public key to encrypt a message, but only the recipient's private key can decrypt it, avoiding the need to secretly share a single shared key in advance",
   "Symmetric encryption — anyone can use a recipient's freely published public key to encrypt a message, and that exact same key can also then be used by anyone at all to decrypt that same message afterward",
   "Hashing — a one-way mathematical process that scrambles data irreversibly, which serves as a full and direct substitute for actually encrypting and later decrypting any real message content at all",
   "End-to-end encryption is simply a different, unrelated name that refers to this exact same underlying single-shared-key process rather than to any separate genuinely distinct encryption approach"
 ],
 "answer": 0,
 "explanation": "Public-key (asymmetric) cryptography uses a mathematically linked key pair — a public key anyone can use to encrypt, and a private key only the recipient holds to decrypt — which elegantly solves the problem symmetric encryption has: how do two parties who've never met securely agree on one shared secret key in the first place?"
},
{
 "q": "A document is digitally signed by its author using their private key, and anyone can verify the signature is genuine using the author's public key. If even one character of the document is altered after signing, the signature verification fails. What does a valid digital signature actually prove?",
 "options": [
   "That the document was signed by whoever holds the corresponding private key, and that the document has not been altered since it was signed — providing both authenticity and integrity assurances",
   "That the document's content is factually accurate and true, since a valid digital signature is specifically designed to mathematically verify the truthfulness of whatever claims the document contains",
   "That the document has been encrypted and is therefore unreadable to anyone except the original author, which is the sole and complete purpose that a digital signature is designed to serve",
   "That the document was created using a specific software application, since digital signatures work by mathematically embedding the identity of the exact program used to originally create the file"
 ],
 "answer": 0,
 "explanation": "A digital signature proves two distinct things: authenticity (only the private-key holder could have produced this signature) and integrity (any alteration after signing breaks the signature). It says nothing about whether the document's actual content is factually true, and it isn't the same thing as encrypting the document for confidentiality."
},
{
 "q": "A home WiFi router still using an old, weak WiFi security protocol from the early 2000s is far easier for a nearby attacker to break into than one using a modern protocol. What does upgrading to a modern WiFi security protocol most directly protect against?",
 "options": [
   "Unauthorised users on the physical wireless network being able to intercept traffic or gain network access, since weaker older protocols have well-known, publicly documented cryptographic weaknesses that can be exploited",
   "Phishing emails being sent to any device that happens to connect to the home WiFi network, since WiFi protocol strength is what directly determines whether phishing emails can reach connected devices",
   "Ransomware being installed on any device that connects to the network, since the specific WiFi security protocol in use is what technically determines whether ransomware can run on a connected device",
   "SQL injection attacks being carried out against any website visited by a device connected to the home network, since WiFi protocol strength is the specific factor that prevents this class of attack"
 ],
 "answer": 0,
 "explanation": "WiFi security protocols specifically protect the wireless link itself — who can join the network and whether traffic on it can be eavesdropped or manipulated. Older protocols have well-documented cryptographic weaknesses that let a nearby attacker break in relatively easily; it's a distinct layer from application-level threats like phishing, ransomware, or SQL injection, which operate independently of WiFi protocol strength."
},
{
 "q": "A company migrates its data storage to a major cloud provider and assumes the provider is now fully responsible for all security, including how the company's own staff configure access permissions. Months later, a misconfigured storage bucket left publicly accessible online causes a major data leak. What does this scenario illustrate?",
 "options": [
   "The shared responsibility model — cloud providers generally secure the underlying infrastructure, but the customer remains responsible for correctly configuring their own access controls and settings on top of it",
   "A supply chain attack — the cloud provider itself was directly compromised by an external attacker, which is the only possible explanation for how the storage bucket became publicly accessible online",
   "A zero-day vulnerability — a previously unknown flaw in the cloud provider's own underlying infrastructure that the company had no realistic way of detecting or preventing through any of its own actions",
   "Ransomware-as-a-service — a criminal platform was used to rent the exact attack technique that caused the storage bucket to become misconfigured and publicly accessible in this specific incident"
 ],
 "answer": 0,
 "explanation": "Cloud security typically follows a shared responsibility model: the provider secures the underlying infrastructure (physical data centres, hypervisor, base network), but the customer remains responsible for correctly configuring access controls, permissions, and settings on top of it — misconfigured storage buckets left publicly accessible are one of the most common real-world causes of cloud data leaks, and they're a customer-side failure, not a provider breach."
},
{
 "q": "A company keeps a detailed, tamper-resistant record of who accessed which systems and files, and when, across their entire network. Months after a breach, investigators use this record to reconstruct exactly how the attacker moved through the network. What is this kind of record called, and why does it matter even when nothing seems wrong?",
 "options": [
   "An audit log (or logging/monitoring system) — a record of system activity that, even when nothing appears wrong day to day, becomes essential for reconstructing what happened during an incident investigation",
   "A honeypot — a deliberately exposed decoy system, which by definition cannot also serve as a genuine record of legitimate system activity across a company's real, non-decoy production network",
   "A firewall — a network security barrier that filters incoming and outgoing traffic, which does not itself create or maintain any lasting historical record of past user or system activity over time",
   "A digital signature — a cryptographic proof of who authored and signed a specific document, which has no meaningful application to tracking or recording general ongoing system access activity"
 ],
 "answer": 0,
 "explanation": "Audit logs and monitoring systems record activity continuously, and their value often only becomes obvious after the fact — without them, reconstructing exactly how an attacker moved through a network during a past breach becomes far harder or even impossible, which is why logging is considered a foundational security control even when nothing currently seems wrong."
},
{
 "q": "An attacker uses AI voice-cloning technology to imitate a company's CEO's voice closely enough to convincingly call the finance department and urgently request an emergency wire transfer. What established attack category does this represent, updated with a new technological capability?",
 "options": [
   "Social engineering — this is a modern, AI-enabled variant of impersonation-based social engineering, exploiting trust in a recognised voice and urgency, the same underlying psychological levers as older phone-based scams",
   "SQL injection — the AI-generated voice call is inserting malicious database commands directly into the finance department's phone system, which is the specific technique enabling the fraudulent transfer",
   "A zero-day exploit — the attacker is exploiting a previously undiscovered software vulnerability specifically within the AI voice-cloning tool itself, unrelated to any psychological manipulation of a human being",
   "A supply chain attack — the attacker first compromised a trusted third-party vendor connected to the finance department's systems, which is the specific technique required to imitate the CEO's voice convincingly"
 ],
 "answer": 0,
 "explanation": "This is social engineering with an AI-powered upgrade: the underlying manipulation — impersonating a trusted authority figure to create urgency and bypass normal verification — is identical to classic phone-based fraud, but voice-cloning technology makes the impersonation itself far more convincing, which is why many organisations are updating verification procedures (like requiring a callback to a known number) in response."
},
{
 "q": "A company grants every employee broad access to every internal system 'just in case they need it someday', rather than reviewing and adjusting access based on actual current job needs. An employee who left the finance team for marketing eight months ago still has full access to sensitive payroll systems. What security gap does this illustrate?",
 "options": [
   "A failure to enforce least privilege combined with a lack of periodic access review — access rights should be reviewed and adjusted as roles change, not granted broadly once and left unmanaged indefinitely",
   "A zero-day vulnerability specific to the payroll system's own underlying software, which is unrelated to how the company manages or reviews individual employee access permissions over time",
   "A supply chain attack, since the employee's continued unnecessary access to payroll systems was caused by a compromised third-party vendor rather than by the company's own internal access management process",
   "End-to-end encryption failure, since encrypting the payroll data itself would have been sufficient to fully prevent the employee's continued unnecessary access to sensitive payroll information"
 ],
 "answer": 0,
 "explanation": "Least privilege isn't a one-time setup — it requires ongoing review as people change roles, since access that made sense in an old role can become an unnecessary, unmonitored risk in a new one. Periodic access reviews (revoking or adjusting permissions as roles change) are a standard, practical control for exactly this kind of gap."
},
{
 "q": "A security researcher who discovers a serious vulnerability in a company's product reports it privately to the company first, giving them time to fix it before any public disclosure, and receives a cash reward for the responsible report. What is this practice called, and what incentive problem does it solve?",
 "options": [
   "A bug bounty programme — paying independent researchers for responsibly disclosed vulnerabilities, which gives skilled researchers a legitimate, paid incentive to report flaws to the company rather than sell or exploit them elsewhere",
   "Penetration testing — a bug bounty programme is simply a different name for the exact same practice as hiring one specific, single outside firm to conduct an internal security test of the company's product",
   "A honeypot — the researcher was actually interacting with a deliberately exposed, fake decoy version of the company's real product, rather than genuinely reporting a vulnerability in the actual live product",
   "DevSecOps — a bug bounty programme is simply one specific automated security scanning step that occurs during a company's own internal software development and code review pipeline"
 ],
 "answer": 0,
 "explanation": "Bug bounty programmes create a legitimate financial incentive for security researchers to report vulnerabilities responsibly to the company rather than sell them on a criminal market or exploit them directly — a complement to, not a replacement for, an organisation's own internal penetration testing and security review processes."
},
{
 "q": "A company designs a new mobile app so that it collects only the specific personal data genuinely required for the app to function, rather than requesting broad access to contacts, location, and photos 'in case it's useful later'. What principle does this reflect, and why does it also reduce security risk, not just privacy risk?",
 "options": [
   "Privacy by design combined with data minimisation — collecting less unnecessary personal data directly shrinks what could be exposed or misused if the app or its backend is ever breached",
   "Zero-trust security — collecting only the minimum necessary personal data is considered one of the specific, defining technical requirements of implementing a zero-trust security architecture for any mobile app",
   "The principle of least privilege applies exclusively to internal employee system access and has no meaningful application whatsoever to how a mobile app collects or handles data from its own end users",
   "Network segmentation, since limiting what personal data a mobile app collects is functionally equivalent to dividing a company's internal network into separate, access-restricted zones"
 ],
 "answer": 0,
 "explanation": "Privacy by design and data minimisation are related but distinct from network-level controls: by deliberately not collecting data the app doesn't actually need, there's simply less sensitive data available to expose if a breach ever does happen — reducing both privacy risk and the practical severity of any future security incident."
},
{
 "q": "A malicious app disguises itself as a simple flashlight utility but, once installed, secretly records every key a user types, including banking passwords, and sends that data to a remote attacker. What is this specific category of malware called?",
 "options": [
   "A keylogger — malware that secretly records keystrokes to capture sensitive information like passwords, often bundled inside another seemingly harmless or useful application to trick users into installing it",
   "A worm — malware that spreads autonomously across a network without requiring any human action, a propagation method unrelated to the specific keystroke-recording behaviour described in this particular scenario",
   "Ransomware — malware that specifically encrypts a victim's files and demands a payment for their release, a behaviour unrelated to the specific keystroke-recording activity described in this particular scenario",
   "A zero-day exploit — a previously undiscovered software vulnerability being actively exploited, which is a category describing a type of flaw rather than a category describing a type of malware behaviour"
 ],
 "answer": 0,
 "explanation": "A keylogger specifically captures keystrokes to harvest sensitive information like passwords, often disguised inside or bundled with an unrelated, seemingly harmless app (a trojan-style delivery method) — a distinct malware behaviour from a self-spreading worm or file-encrypting ransomware."
},
{
 "q": "A company's mobile device management (MDM) system allows IT staff to remotely wipe all company data from an employee's phone the moment it's reported lost or stolen, without affecting the employee's own personal photos and apps on a separate profile. What security goal does this capability most directly serve?",
 "options": [
   "Limiting the exposure of sensitive company data if a device falls into the wrong hands, while still respecting the boundary between company-managed data and the employee's own personal information",
   "Preventing the employee's phone from ever being physically lost or stolen in the first place, since MDM software is specifically designed to make theft of an enrolled device technically impossible",
   "Automatically and permanently encrypting all of the employee's personal photos and apps stored outside of the company-managed profile, in addition to remotely wiping the separate company data",
   "Replacing the need for the employee to use a screen-lock passcode at all, since MDM's remote-wipe capability is considered a full substitute for any device-level access control on the phone itself"
 ],
 "answer": 0,
 "explanation": "MDM's remote-wipe capability is a damage-limitation control for a device that's already lost or stolen — reducing exposure of sensitive company data — while typically respecting a separation between company-managed and personal data on a personally-owned device, rather than preventing loss/theft itself or replacing basic device-level protections like a passcode."
},
{
 "q": "An attacker compromises a website that employees of a specific target company regularly and legitimately visit (like an industry news site), and quietly plants malware that only activates for visitors coming from that target company's network. What is this targeted attack technique called?",
 "options": [
   "A watering hole attack — compromising a website the intended victims are known to visit regularly, rather than attacking the target organisation's own systems directly",
   "SQL injection — inserting malicious database commands directly into the target company's own internal systems, rather than compromising any separate, unrelated third-party website the employees happen to visit",
   "A brute-force attack — systematically trying every possible password combination against the target company's own login systems, rather than compromising any unrelated third-party website they happen to visit",
   "Ransomware-as-a-service — renting ready-made ransomware tools from a criminal platform specifically to encrypt the industry news website's own files, rather than to actually target the intended company at all"
 ],
 "answer": 0,
 "explanation": "A watering hole attack targets a trusted site the intended victims are known to frequent (like predators waiting near a watering hole animals visit), rather than attacking the actual target organisation head-on — an indirect approach that can bypass defences the target's own systems would otherwise have caught."
},
{
 "q": "A malicious webpage is designed to visually overlay a fake 'Play Video' button directly on top of an invisible real 'Confirm Purchase' button, so that a user thinks they're clicking one thing but are actually clicking another. What is this deceptive UI technique called?",
 "options": [
   "Clickjacking — tricking a user into clicking something different from what they perceive by visually layering deceptive content over a hidden, real interactive element",
   "SQL injection — inserting malicious database commands directly into the webpage's visible 'Play Video' button, which is the specific technique responsible for making the underlying purchase button invisible",
   "A brute-force attack — systematically trying every possible visual button placement combination until one happens to successfully trick the user into clicking the hidden real purchase button underneath",
   "A zero-day exploit — taking advantage of a previously undiscovered flaw specific to how video-playback buttons are rendered by web browsers, unrelated to any deliberate deceptive layering of interface elements"
 ],
 "answer": 0,
 "explanation": "Clickjacking deceives users into clicking something other than what they perceive, typically by layering an invisible legitimate control beneath a visible decoy — a UI-level deception technique, distinct from attacks that exploit a database query (SQL injection) or a software vulnerability (zero-day)."
},
{
 "q": "A large e-commerce site uses behavioural analysis (mouse movement patterns, request timing, and browsing patterns) alongside a CAPTCHA to distinguish real shoppers from automated bots trying to buy up all the limited-stock items instantly for resale. Why might behavioural analysis alone sometimes catch bots that a simple CAPTCHA misses?",
 "options": [
   "Sophisticated bots can sometimes be built or trained specifically to solve common CAPTCHA challenges, while genuinely humanlike variability in timing and interaction patterns remains comparatively harder for automated scripts to convincingly fake at scale",
   "CAPTCHAs and behavioural analysis are functionally identical techniques that always produce exactly the same detection results, so using both together provides no additional benefit over using either one alone",
   "Behavioural analysis works by directly and permanently blocking every visitor's access to the website the moment any bot-like activity is detected anywhere on the platform, regardless of that specific visitor's actual behaviour",
   "Bots are physically incapable of ever completing an online purchase under any circumstances, which is the specific and complete reason any additional bot-detection layer beyond a basic CAPTCHA would ever be necessary"
 ],
 "answer": 0,
 "explanation": "As CAPTCHA-solving bots and services have become more sophisticated, additional layers like behavioural analysis (timing patterns, mouse movement, interaction rhythm) provide a complementary signal that's harder for automated scripts to convincingly fake at scale — which is why many high-value targets like limited-stock sales use multiple overlapping bot-detection layers rather than relying on a CAPTCHA alone."
},
{
 "q": "A company's security policy requires that any software vulnerability rated 'critical' must be patched within 48 hours of a fix becoming available, while 'low severity' issues can wait for the next scheduled monthly update. What does this tiered approach reflect about practical vulnerability management?",
 "options": [
   "Not all vulnerabilities carry equal risk, so prioritising patching effort by actual severity and exploitability lets a security team focus limited time and resources where the real danger is greatest",
   "This kind of tiered patching policy provides no real security benefit compared to patching every single vulnerability, regardless of its severity rating, at exactly the same fixed monthly schedule",
   "Critical vulnerabilities patched within 48 hours are mathematically guaranteed to never be exploited by any attacker during that 48-hour window, making the specific deadline itself the primary source of protection",
   "Low-severity vulnerabilities pose no risk whatsoever to any organisation under any circumstances, which is the actual reason they are deliberately left unpatched until the next scheduled monthly update"
 ],
 "answer": 0,
 "explanation": "Vulnerability management in practice requires prioritisation, since patching everything instantly and equally often isn't realistic — tiering by actual severity and exploitability lets limited security resources focus on the highest-risk issues fastest, while still ensuring lower-risk issues get addressed on a reasonable, if slower, schedule."
},
{
 "q": "A company discovers that an attacker had quiet, undetected access to their network for eleven months before finally being noticed, during which time the attacker slowly mapped internal systems and exfiltrated data in small, hard-to-detect increments. What does this long undetected duration primarily highlight the importance of?",
 "options": [
   "Ongoing monitoring and anomaly detection, since a single point-in-time defence isn't enough — attackers who evade initial detection can operate for extended periods unless activity is continuously watched for unusual patterns",
   "Password strength specifically, since eleven months of undetected access can only be explained by the attacker having originally guessed an unusually weak initial password to gain their first entry point",
   "Physical building security specifically, since undetected network access lasting this long is only possible if the attacker also gained physical, in-person entry to the company's actual office premises",
   "The company's cyber insurance policy specifically, since the length of an attacker's undetected access has a direct and primary bearing only on how large the resulting insurance payout will eventually be"
 ],
 "answer": 0,
 "explanation": "Long-dwelling, undetected intrusions ('advanced persistent threats' in security terminology) highlight why ongoing monitoring and anomaly detection matter as much as strong perimeter defences — an attacker who gets past initial defences and evades detection can operate for months, which is why continuous, not just point-in-time, security matters."
},
{
 "q": "A regulator fines a European company millions of euros under GDPR for mishandling customer data, while a comparable Nigerian company faces enforcement action from NITDA/the NDPR authorities for a similar violation. What does the existence of both frameworks illustrate about data protection regulation globally?",
 "options": [
   "Data protection regulation has become a genuine global trend, with different jurisdictions (the EU's GDPR, Nigeria's NDPR, and others) independently establishing legal consequences for how organisations handle personal data",
   "GDPR and the NDPR are legally and technically identical frameworks that apply uniformly and interchangeably to any company anywhere in the world, regardless of where that company or its customers are actually located",
   "Only European companies can realistically ever face meaningful fines for data protection violations, since Nigeria's NDPR framework carries no genuine legal enforcement mechanism or regulatory authority behind it",
   "Data protection fines of this kind only ever apply to extremely large multinational technology corporations, and have no realistic practical relevance to a smaller company operating only within Nigeria"
 ],
 "answer": 0,
 "explanation": "Data protection regulation has genuinely globalised over the past decade — GDPR, the NDPR, and comparable frameworks in other countries each independently establish real legal consequences for mishandling personal data, reflecting a broader international trend rather than one region acting alone, though the specific requirements and enforcement mechanisms differ meaningfully between jurisdictions."
},
{
 "q": "Which of the following are genuine, practical benefits of network segmentation as a security control? Select all that apply.",
 "options": [
   "It limits how far an attacker can move after compromising one part of the network",
   "It allows sensitive systems to be isolated with stricter access controls than the general network",
   "It guarantees that no successful cyberattack of any kind can ever occur anywhere on the segmented network",
   "It can reduce the overall damage and scope of a breach by containing it within one isolated segment"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Limiting lateral movement, allowing stricter isolation for sensitive systems, and containing breach scope are all genuine, well-established benefits of network segmentation. It is not a guarantee against attacks occurring at all — it's a damage-containment and access-control strategy, not a prevention-of-all-attacks strategy."
},
{
 "q": "Which of the following are genuine differences between a virus, a worm, and a trojan, as these terms are used in cybersecurity? Select all that apply.",
 "options": [
   "A worm can spread across a network on its own, without needing a human to open an infected file",
   "A virus typically needs a host file to be opened or executed by a user in order to activate and spread",
   "A trojan disguises itself as legitimate, desirable software to trick a user into installing it voluntarily",
   "All three terms describe exactly the same underlying technical behaviour with no meaningful distinction between them"
 ],
 "answer": [0, 1, 2],
 "multi": True,
 "explanation": "Worms, viruses, and trojans are genuinely distinct malware categories defined by how they spread or gain initial access: worms self-propagate across networks, viruses need a host file activated by a user, and trojans rely on disguise and social engineering to get voluntarily installed — they are not interchangeable terms for the same thing."
},
{
 "q": "A small nonprofit with a limited budget is deciding which security investment to prioritise first: enabling two-factor authentication on all staff accounts, or purchasing an expensive dedicated intrusion detection appliance. Given typical small-organisation attack patterns, which is generally the more cost-effective first step, and why?",
 "options": [
   "Enabling two-factor authentication first, since account compromise through weak or reused passwords is one of the most common real-world attack vectors, and 2FA is comparatively cheap and directly addresses it",
   "The expensive intrusion detection appliance first, since detecting an attack after it has already begun is always considered a higher security priority than making the initial account compromise harder to achieve",
   "Neither investment matters at all for a small nonprofit specifically, since organisations of that size are never realistically targeted by any attacker under any circumstances regardless of their security posture",
   "Both should be purchased and enabled simultaneously regardless of the nonprofit's actual limited budget, since security investment prioritisation is never a genuinely meaningful consideration for any organisation"
 ],
 "answer": 0,
 "explanation": "For a resource-constrained organisation, prioritising controls that address the most common, high-impact attack vectors most cheaply makes practical sense — 2FA directly and cheaply blocks a huge share of account-compromise attempts (like credential stuffing and phishing-obtained passwords), making it a stronger first investment than a more expensive detection tool that helps mainly after a compromise has already begun."
},
{
 "q": "A free mobile game quietly tracks a user's location, browsing habits on other apps, and contact list, then sells this profile to advertisers — all technically disclosed in a lengthy terms-of-service document almost no one reads. What category of software behaviour does this describe, and why is a lengthy disclosure sometimes considered an inadequate protection on its own?",
 "options": [
   "Spyware-like data harvesting — covertly collecting and monetising user data; a technically-present but practically unreadable disclosure gives users little genuine ability to make an informed, meaningful choice about their own data",
   "A worm — the game is described as autonomously spreading itself from one user's device to another user's device across a network, which is the specific defining behaviour described in this particular scenario",
   "A zero-day exploit — the game is taking advantage of a previously undiscovered software vulnerability in the phone's operating system, unrelated to any disclosed or undisclosed data collection practice",
   "A supply chain attack — the game itself was compromised by a separate, unrelated third-party attacker, rather than being designed from the outset by its own original developer to collect and sell user data"
 ],
 "answer": 0,
 "explanation": "This describes spyware-like behaviour (sometimes bundled into 'legitimate' apps as a business model rather than classic malware): the concern isn't purely technical but also about meaningful informed consent — a disclosure buried in unreadable legal text raises real questions about whether users genuinely consented to that level of tracking, which is part of why data-minimisation and privacy-by-design principles matter."
},
{
 "q": "A bank's fraud detection system flags a transaction as suspicious because it occurred at an unusual time, from an unfamiliar location, and for an amount far larger than the customer's typical spending pattern — even though the correct card number and PIN were entered. What security principle does this illustrate?",
 "options": [
   "Behavioural/anomaly-based detection — flagging activity that deviates from an established normal pattern, which can catch fraud even when the attacker has the correct credentials, unlike checks that only verify the password or PIN itself",
   "Two-factor authentication — the fraud detection system is functioning as the required second independent verification factor, which is the only reason the suspicious transaction was flagged at all in this case",
   "End-to-end encryption — the fraud detection system works by making the specific transaction details unreadable to the attacker, which is the actual underlying mechanism responsible for flagging it as suspicious",
   "A honeypot — the flagged transaction was actually directed toward a deliberately exposed decoy account, rather than toward the customer's own real, genuine bank account and available funds"
 ],
 "answer": 0,
 "explanation": "Anomaly-based fraud detection doesn't rely solely on 'did they enter the correct credentials' — it watches for deviations from an established normal pattern (timing, location, amount), which can catch fraud even when an attacker has correctly stolen or guessed the actual card number and PIN, a genuinely different and complementary layer of defence from credential verification alone."
},
]
