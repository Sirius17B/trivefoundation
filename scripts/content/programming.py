# Programming & Web Systems — 121 questions, applied-reasoning style.
# Covers programming fundamentals, web development, databases, and DevOps
# infrastructure — the largest single topic bucket in the tech quiz.
QUESTIONS = [
{
 "q": "A function that calculates a factorial calls itself with a smaller input each time until it reaches a base case of 1, at which point it stops calling itself and starts returning results back up the chain. What programming technique does this describe?",
 "options": [
   "Recursion — a function solving a problem by calling itself on a smaller version of the same problem, with a base case that stops the chain of calls from continuing indefinitely",
   "Iteration — repeating a block of code a fixed number of times using a loop construct, without the function ever calling itself again from within its own function body",
   "Polymorphism — allowing different object types to respond differently to the exact same method call, a concept unrelated to a function repeatedly calling a smaller version of itself",
   "Inheritance — one class acquiring the properties and behaviours of another parent class, a concept unrelated to a function that repeatedly calls a smaller version of itself"
 ],
 "answer": 0,
 "explanation": "Recursion solves a problem by having a function call itself on a smaller sub-problem, relying on a base case to eventually stop the chain — factorial, tree traversal, and many divide-and-conquer algorithms are classic examples, distinct from simple iteration, which loops without the function calling itself."
},
{
 "q": "Two developers write functions that both sort a list of one million numbers. Function A takes roughly twice as long when the list doubles in size. Function B takes roughly four times as long when the list doubles. Which function scales better for very large inputs, and what is this kind of comparison called?",
 "options": [
   "Function A scales better; this kind of comparison of how running time grows with input size is called time complexity, often expressed using Big O notation",
   "Function B scales better, since a function that takes proportionally longer as input grows is always considered the more efficient and higher-quality algorithm by any standard measure",
   "Neither function's actual real-world scaling behaviour can be meaningfully compared in any way without first knowing the specific programming language each one happens to be written in",
   "This kind of comparison is called object-oriented programming, a term referring specifically to organising running-time comparisons between two different sorting functions of any kind"
 ],
 "answer": 0,
 "explanation": "Time complexity describes how an algorithm's running time grows as input size increases, commonly expressed in Big O notation. Function A growing linearly (roughly doubling time for doubling input) scales far better for very large inputs than Function B growing quadratically (roughly quadrupling time for doubling input) — a genuinely practical distinction once data sizes get large."
},
{
 "q": "A class called `Animal` has a method `makeSound()`. Separate classes `Dog` and `Cat` both inherit from `Animal` but each provides its own specific version of `makeSound()`, so calling the same method name produces a bark or a meow depending on which object it's called on. What object-oriented principle does this illustrate?",
 "options": [
   "Polymorphism — the same method name behaving differently depending on the specific object it's called on, allowing code to treat different related object types through one consistent interface",
   "Encapsulation — bundling an object's internal data and the methods that operate on it together, while restricting direct outside access to that data, a concept unrelated to one method name behaving differently per object type",
   "Recursion — a function or method calling itself repeatedly on a smaller version of the same problem, a concept unrelated to different classes each providing their own version of a shared method name",
   "Abstraction — hiding complex implementation details behind a simpler, more general interface, a concept unrelated specifically to one shared method name producing different behaviour per object type"
 ],
 "answer": 0,
 "explanation": "Polymorphism lets different object types respond to the same method call in their own specific way — code that calls `makeSound()` doesn't need to know or care whether it's dealing with a Dog or a Cat, which is a core part of what makes object-oriented design flexible and extensible."
},
{
 "q": "A team's codebase has the exact same date-formatting logic copy-pasted into fifteen different files. When a bug is found in that logic, they have to remember to fix it in all fifteen places, and inevitably miss one. What principle would have prevented this, and what does it recommend instead?",
 "options": [
   "DRY (Don't Repeat Yourself) — extracting the shared logic into a single reusable function that all fifteen places call, so a fix in one place automatically applies everywhere it's used",
   "KISS (Keep It Simple) — the principle specifically recommends copy-pasting logic into as many separate files as needed, rather than consolidating shared logic into any single reusable function",
   "Encapsulation — the principle specifically recommends duplicating logic across many files so that each file's internal implementation remains fully independent of every other file in the codebase",
   "Recursion — the principle recommends restructuring the date-formatting logic so that it repeatedly calls itself, rather than addressing the actual underlying problem of duplicated code across files"
 ],
 "answer": 0,
 "explanation": "DRY specifically targets this exact failure mode: duplicated logic scattered across a codebase means every future fix has to be remembered and applied everywhere it was copied, which is exactly the kind of error-prone maintenance burden that consolidating shared logic into one reusable function eliminates."
},
{
 "q": "A developer writes automated tests that check individual functions in isolation, a smaller number of tests that check how several components work together, and only a handful of tests that check the entire application end-to-end through the actual user interface. What is this layered testing structure commonly called?",
 "options": [
   "The testing pyramid — favouring many fast, cheap unit tests at the base, fewer integration tests in the middle, and very few slow, expensive end-to-end tests at the top",
   "Recursion — the layered structure of unit, integration, and end-to-end tests is itself considered a specific practical example of a function repeatedly calling a smaller version of itself",
   "The CAP theorem — a principle describing an unavoidable tradeoff between Consistency, Availability, and Partition tolerance in distributed systems, unrelated to how automated tests are structured",
   "Polymorphism — writing different types of automated tests that each respond differently to the exact same underlying test command, depending on which specific component is actually being tested"
 ],
 "answer": 0,
 "explanation": "The testing pyramid recommends many fast, cheap unit tests forming a broad base, fewer integration tests in the middle, and very few slow, expensive full end-to-end tests at the top — balancing test coverage against the cost and fragility of tests that exercise the whole system through the actual interface."
},
{
 "q": "A team maintains an old, business-critical system that's too risky to rewrite all at once, so instead they gradually build a new system alongside it, slowly rerouting individual pieces of functionality to the new system over many months until the old one can finally be retired. What is this migration strategy called?",
 "options": [
   "The strangler fig pattern — gradually replacing a legacy system piece by piece by routing functionality to a new system over time, rather than attempting a risky, all-at-once full rewrite",
   "The testing pyramid — a strategy specifically describing how to structure automated tests, rather than describing any strategy for gradually migrating away from an old legacy software system",
   "DRY (Don't Repeat Yourself) — a principle specifically about avoiding duplicated code within a single codebase, rather than describing any strategy for migrating between two separate systems",
   "Polymorphism — an object-oriented programming concept about a shared method name behaving differently per object type, unrelated to any strategy for migrating away from a legacy system"
 ],
 "answer": 0,
 "explanation": "The strangler fig pattern (named after a vine that gradually envelops and eventually replaces its host tree) describes incrementally migrating functionality from an old system to a new one piece by piece, letting the new system gradually 'strangle' and replace the old one — a much lower-risk approach than a single risky full rewrite for a critical system."
},
{
 "q": "A team stores their entire server configuration — which software is installed, what settings are applied, how many servers exist — as version-controlled code files, rather than manually clicking through a control panel each time a new server is needed. What is this practice called?",
 "options": [
   "Infrastructure as code — defining and managing infrastructure through machine-readable configuration files, enabling consistent, repeatable, and version-controlled environment setup rather than manual, error-prone configuration",
   "Object-oriented programming — a programming paradigm organising code into classes and objects, unrelated to whether a team's server configuration is stored as version-controlled files or set up manually",
   "The testing pyramid — a strategy for structuring a team's automated tests into layers, unrelated to whether a team's actual server configuration is stored as code or configured manually by hand",
   "Recursion — a programming technique where a function calls itself, unrelated to whether a team's server configuration is stored as version-controlled code or configured manually through a control panel"
 ],
 "answer": 0,
 "explanation": "Infrastructure as code (IaC) treats server and environment configuration as version-controlled, machine-readable files rather than manual, one-off setup — making environments consistent, repeatable, and auditable, and letting a new server be provisioned identically to an existing one just by running the same code."
},
{
 "q": "A large monolithic e-commerce application is split into separate, independently deployable services — one for payments, one for inventory, one for user accounts — each communicating over the network rather than all running as one single program. What architecture does this describe, and what is a key tradeoff?",
 "options": [
   "Microservices — independently deployable services communicating over a network; this enables independent scaling and deployment per service, at the cost of added complexity in coordinating and monitoring many separate moving parts",
   "Object-oriented programming — organising the entire application's internal code into classes and objects, a concept describing internal code structure rather than how services are physically deployed or communicate",
   "Infrastructure as code — managing server configuration through version-controlled files, a concept unrelated to whether an application is split into multiple independently deployable network services",
   "The testing pyramid — a strategy for structuring an application's automated tests into layers, a concept unrelated to whether the application itself is split into multiple independently deployable services"
 ],
 "answer": 0,
 "explanation": "Microservices architecture splits a system into independently deployable, separately scalable services communicating over a network — offering real flexibility (deploy and scale the payments service without touching inventory) at the real cost of added operational complexity: network calls can fail, and coordinating many moving parts requires more sophisticated monitoring than one single monolithic program."
},
{
 "q": "A company runs code that automatically executes in response to specific events (like a file upload), paying only for the exact compute time used, with no server that they themselves have to provision, patch, or manage sitting idle between events. What is this computing model called?",
 "options": [
   "Serverless computing — running code in response to events without provisioning or managing dedicated servers directly, paying only for actual execution time rather than for constantly-running idle capacity",
   "Microservices — splitting an application into many independently deployable services, a concept describing how an application's overall architecture is divided rather than how its infrastructure is billed or managed",
   "Infrastructure as code — managing server configuration through version-controlled files, a concept describing how infrastructure is defined rather than whether any server needs to be actively managed at all",
   "The CAP theorem — a principle describing an unavoidable tradeoff between Consistency, Availability, and Partition tolerance, unrelated to whether an application runs on dedicated managed servers or event-triggered functions"
 ],
 "answer": 0,
 "explanation": "Serverless computing (despite the name, servers still exist, just managed entirely by the cloud provider) runs code in response to specific triggering events, billing only for actual execution time — well suited to unpredictable or bursty workloads where paying for constantly-running idle server capacity would be wasteful."
},
{
 "q": "A team notices their production environment behaves subtly differently from their local development environment — a library version mismatch causes a bug that only appears after deployment, never during local testing. Which practice most directly addresses this class of problem?",
 "options": [
   "Environment parity (keeping development, staging, and production environments as close to identical as possible), often achieved using tools like containerisation to package the exact same runtime environment everywhere",
   "The testing pyramid, since writing more unit tests that check individual functions in isolation is specifically designed to catch environment-configuration mismatches between development and production",
   "Recursion, since restructuring the application's code to call itself repeatedly is specifically the standard technique used to eliminate differences between a development and a production environment",
   "Polymorphism, since making the same method name behave differently depending on which specific object it's called on is specifically the standard fix for development-versus-production environment mismatches"
 ],
 "answer": 0,
 "explanation": "Environment parity — keeping development, staging, and production as close to identical as realistically possible, often via containerisation — directly targets 'works on my machine' bugs caused by subtle configuration or dependency-version differences between environments, which unit testing alone doesn't catch since the tests themselves run in yet another environment."
},
{
 "q": "A developer packages an application together with its exact runtime environment — specific library versions, configuration, dependencies — into a single portable unit that runs identically on a laptop, a testing server, and a production server. What technology enables this, and what classic problem does it solve?",
 "options": [
   "Containerisation (like Docker) — packaging an application with its exact dependencies into a portable unit that runs consistently anywhere, solving the classic 'it works on my machine but not in production' problem",
   "Recursion — a programming technique where a function calls itself, a concept describing a function's internal control flow rather than how an application's runtime environment is packaged and deployed",
   "The CAP theorem — a principle describing tradeoffs in distributed databases specifically, unrelated to how an application and its dependencies are packaged into a portable, consistently runnable unit",
   "Polymorphism — an object-oriented programming concept about shared method names behaving differently per object, unrelated to how an application and its runtime dependencies are packaged for deployment"
 ],
 "answer": 0,
 "explanation": "Containerisation packages an application together with its exact runtime environment — dependencies, configuration, library versions — into one portable, consistent unit, directly solving the classic problem of code that works locally but breaks in a differently-configured production environment."
},
{
 "q": "A company runs hundreds of containers across many servers and needs something to automatically restart any container that crashes, distribute incoming traffic evenly, and roll out updates without downtime. What category of tool is designed specifically for this, and why is it needed beyond containerisation alone?",
 "options": [
   "A container orchestration platform (like Kubernetes) — containerisation packages an application consistently, but managing hundreds of running containers across many servers reliably requires a separate, dedicated orchestration layer",
   "A CAP theorem implementation — a container orchestration platform is essentially just a practical implementation of the CAP theorem's Consistency, Availability, and Partition tolerance tradeoff applied to running containers",
   "A testing pyramid tool — container orchestration platforms exist specifically to automatically generate the unit, integration, and end-to-end tests needed to properly test hundreds of separately running containers",
   "An infrastructure-as-code alternative — container orchestration platforms exist specifically to replace the need for defining server configuration as version-controlled code, rather than to manage already-running containers"
 ],
 "answer": 0,
 "explanation": "Containerisation solves 'package consistently'; orchestration (Kubernetes being the dominant example) solves the separate problem of reliably running, scaling, healing, and updating potentially hundreds of containers across many servers — auto-restarting crashed containers, load balancing traffic, and rolling out updates without downtime, none of which containerisation alone provides."
},
{
 "q": "A team's deployment process used to involve manually copying files to a server late at night, hoping nothing broke. They switch to a system where every code change is automatically tested, and if it passes, automatically deployed to production within minutes. What is this practice called, and what specific benefit does 'automatically tested on every change' provide?",
 "options": [
   "Continuous integration/continuous deployment (CI/CD) — automatically building, testing, and deploying every code change; testing on every change catches integration problems within minutes rather than discovering them weeks later",
   "Infrastructure as code — a practice specifically about defining server configuration as version-controlled files, rather than about automatically testing and deploying code changes as they are made",
   "Object-oriented programming — a programming paradigm organising code into classes and objects, unrelated to whether a team's code changes are automatically tested and deployed rather than manually copied to a server",
   "The strangler fig pattern — a strategy specifically for gradually migrating away from a legacy system, rather than a practice describing how code changes are automatically tested and deployed to production"
 ],
 "answer": 0,
 "explanation": "CI/CD automates building, testing, and deploying code, catching problems (like a change that breaks another part of the system) within minutes of being introduced rather than being discovered much later — and CD (continuous deployment) extends this to automatically ship passing changes to production, enabling teams to release reliably many times a day."
},
{
 "q": "A popular website suddenly gets ten times its normal traffic during a viral moment. Instead of the site crashing, incoming requests are automatically distributed across many identical servers, and new servers are spun up as demand grows, then shut down again afterward. What two related concepts does this describe?",
 "options": [
   "Load balancing and auto-scaling — distributing traffic across multiple servers, combined with automatically adding or removing server capacity based on real-time demand, together handling large or unpredictable traffic spikes",
   "Recursion and polymorphism — a function repeatedly calling itself, combined with the same method name behaving differently depending on the object it's called on, together explaining how a website absorbs a traffic spike",
   "The testing pyramid and DRY — structuring automated tests into layers, combined with avoiding duplicated code, together explaining how a website automatically absorbs and survives a sudden large traffic spike",
   "Infrastructure as code and the CAP theorem — defining server configuration as version-controlled files, combined with a database consistency-versus-availability tradeoff, together explaining a website's traffic-spike behaviour"
 ],
 "answer": 0,
 "explanation": "Load balancing distributes incoming requests across multiple servers so no single one becomes a bottleneck, while auto-scaling automatically adjusts how many servers exist based on real-time demand — together, exactly the combination needed to absorb a sudden, large, unpredictable traffic spike without manual intervention or an outage."
},
{
 "q": "A company deploys a new version of their app to just 5% of users first, closely monitoring for errors, before gradually rolling it out to everyone if nothing goes wrong. What deployment strategy is this, and what problem does it primarily reduce?",
 "options": [
   "A canary release (gradual rollout) — deploying a change to a small subset of users first, which limits the blast radius if the new version has an undiscovered bug, compared to deploying to 100% of users at once",
   "Continuous integration — a practice specifically about automatically testing every code change as it's committed, unrelated to whether a deployment is gradually rolled out to a small percentage of users first",
   "Infrastructure as code — a practice specifically about defining server configuration as version-controlled files, unrelated to whether a new app version is deployed gradually to a small subset of users first",
   "Containerisation — a technology specifically about packaging an application with its exact dependencies, unrelated to whether that packaged application is gradually rolled out to a small subset of users first"
 ],
 "answer": 0,
 "explanation": "A canary release limits exposure to a new, potentially buggy version by rolling it out to a small fraction of real users first — if something breaks, the blast radius is contained to that small group rather than every user at once, and the rollout can be paused or reverted before wider damage happens."
},
{
 "q": "A company's monitoring dashboard shows real-time graphs of server response times, error rates, and resource usage, plus detailed logs of every request, letting engineers quickly diagnose why a specific user's request failed at 3am without needing to manually reproduce the issue. What is this overall practice called?",
 "options": [
   "Observability (logging, metrics, and monitoring) — instrumenting a system so its internal state and behaviour can be understood externally, critical for diagnosing issues in complex, distributed production systems",
   "The testing pyramid — a strategy for structuring automated tests into layers of unit, integration, and end-to-end tests, unrelated to real-time monitoring of a live, already-deployed production system's behaviour",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, unrelated to real-time monitoring and diagnosis of a live, already-deployed production system",
   "Polymorphism — an object-oriented programming concept about shared method names behaving differently per object, unrelated to real-time monitoring and diagnosis of a live, already-deployed production system"
 ],
 "answer": 0,
 "explanation": "Observability — combining logs, metrics, and monitoring dashboards — lets engineers understand what's actually happening inside a complex, live production system without needing to manually reproduce every issue, which becomes essential once a system is too complex or distributed to reason about by just reading its source code."
},
{
 "q": "A software team uses feature flags to ship a new checkout flow to production code, but keep it switched off for all real users until it's ready, then turn it on instantly for everyone without needing a new deployment. What is the main practical benefit of this approach?",
 "options": [
   "It decouples deploying code from releasing a feature to users, letting the team ship code safely ahead of time and enable or disable the feature instantly, without needing a new deployment or risking a rollback",
   "It eliminates the need for the team to write any automated tests at all for the new checkout flow, since feature flags are specifically designed to replace the entire need for a testing pyramid",
   "It guarantees the new checkout flow will have zero bugs once switched on, since feature-flagged code is mathematically verified to be defect-free before it is ever allowed to be deployed to production",
   "It permanently prevents the team from ever needing to deploy any further code changes to the checkout flow again, since a feature flag is designed to be the very last deployment that flow will ever need"
 ],
 "answer": 0,
 "explanation": "Feature flags separate 'is this code deployed' from 'is this feature turned on for users', letting a team deploy code safely ahead of a launch and toggle it on or off instantly without a new deployment — useful for controlled rollouts, quick rollback if something goes wrong, and testing in production with a limited audience."
},
{
 "q": "A user's browser sends a GET request to fetch a webpage, and later sends a POST request to submit a login form. What is the fundamental difference in intent between these two HTTP methods?",
 "options": [
   "GET is intended for retrieving data without changing anything on the server, while POST is intended for submitting data that typically creates or changes something on the server",
   "GET is intended for submitting data that changes something on the server, while POST is intended purely for retrieving data without changing anything on the server, the exact reverse of their actual standard usage",
   "GET and POST are functionally and semantically identical in every meaningful respect, and the specific choice between them is purely a matter of arbitrary developer preference with no practical implications",
   "GET is used exclusively for images and other binary files, while POST is used exclusively for plain text content, with the distinction based entirely on the specific type of content being transferred"
 ],
 "answer": 0,
 "explanation": "HTTP methods carry semantic meaning: GET requests are meant to safely retrieve data without side effects (which is why a browser can safely cache or retry them), while POST is meant for submitting data that typically changes server-side state, like creating an account or logging in — a distinction that matters for caching, security, and how browsers and servers are expected to behave."
},
{
 "q": "A user tries to load a webpage and instead sees '404 Not Found', while a different request returns '500 Internal Server Error'. What is the key practical difference between these two HTTP status codes for someone debugging the issue?",
 "options": [
   "404 means the requested resource genuinely doesn't exist at that address, while 500 means something went wrong on the server itself while trying to process an otherwise valid request — pointing to different places to look for the bug",
   "404 and 500 both mean exactly the same thing — that the server is completely offline and unreachable — and the specific numeric code returned is essentially arbitrary and carries no diagnostic meaning",
   "404 means the user's own internet connection has failed, while 500 means the user's specific web browser itself has crashed, with neither status code actually originating from the server being contacted",
   "404 indicates a successful request, while 500 indicates the request was blocked entirely by the user's own local firewall before it could ever actually reach the target server for processing"
 ],
 "answer": 0,
 "explanation": "HTTP status codes are grouped meaningfully: 4xx codes (like 404) indicate a problem with the request itself — often that the resource doesn't exist at that address — while 5xx codes (like 500) indicate the server received a valid request but failed while processing it, which points a debugging developer toward very different places to investigate."
},
{
 "q": "A mobile app and a web app both need to fetch a user's order history from the same backend, without either client needing to know how the data is actually stored in the database. What architectural pattern commonly provides this kind of consistent, structured access to data over HTTP?",
 "options": [
   "A REST API — a set of conventions for exposing data and operations over HTTP using consistent URLs and methods, letting multiple different client applications interact with the same backend consistently",
   "Containerisation — a technology for packaging an application with its exact runtime dependencies, unrelated to how multiple different client applications retrieve structured data from a shared backend system",
   "The testing pyramid — a strategy for structuring a team's automated tests into layers, unrelated to how multiple different client applications actually retrieve data from a shared backend over HTTP",
   "Infrastructure as code — a practice for defining server configuration as version-controlled files, unrelated to how multiple different client applications retrieve structured data from a shared backend system"
 ],
 "answer": 0,
 "explanation": "A REST API exposes data and operations through a consistent set of URL and HTTP-method conventions, letting different client applications (mobile, web, or anything else) interact with the same backend the same predictable way, without needing any direct knowledge of how the data is actually stored underneath."
},
{
 "q": "A small startup's mobile app queries their GraphQL API and specifies exactly which fields it needs (just the user's name and avatar), while their admin dashboard queries the exact same API but requests many more fields for the same underlying data. How does this differ from a typical REST API in practice?",
 "options": [
   "GraphQL lets each client specify exactly which fields it needs in a single request, whereas a typical REST endpoint usually returns a fixed set of fields, sometimes requiring multiple separate requests to gather everything a client actually needs",
   "GraphQL and REST are functionally and technically identical approaches to API design, and the specific choice between them makes no practical difference whatsoever to how a client actually requests data",
   "GraphQL only works for mobile applications specifically, while REST only works for web-based dashboard applications specifically, making the choice between the two purely dependent on client platform type",
   "GraphQL eliminates the need for any backend server at all, since a GraphQL API is defined as a system where the client application directly queries the database without any server layer in between"
 ],
 "answer": 0,
 "explanation": "GraphQL's core design lets each client precisely specify which fields it needs in a single flexible query, addressing a common REST pain point — either over-fetching unused fields or under-fetching and needing multiple round trips — though REST remains simpler to cache and reason about for many typical use cases, which is why both approaches coexist in practice."
},
{
 "q": "A user logs into a website, and on every subsequent page they visit, the site remembers they're logged in without asking for their password again. What mechanism commonly enables a website to 'remember' a user across multiple separate page requests, given that HTTP itself doesn't inherently track state between requests?",
 "options": [
   "Cookies or tokens (like session cookies or JWTs) — a small piece of data stored by the browser and sent with each subsequent request, letting the server recognise the same user across otherwise stateless HTTP requests",
   "GraphQL — a query language for APIs that lets a client specify exactly which fields it needs, a concept unrelated to how a website recognises the same logged-in user across separate page requests",
   "Containerisation — packaging an application with its exact runtime dependencies into a portable unit, a concept unrelated to how a website recognises the same logged-in user across separate page requests",
   "Load balancing — distributing incoming requests across multiple servers, a concept unrelated to how a specific individual website visitor is recognised as the same logged-in user across separate requests"
 ],
 "answer": 0,
 "explanation": "HTTP is fundamentally stateless — each request is independent by default. Cookies (or token-based approaches like JWTs) work around this by having the browser store a small piece of identifying data and automatically send it with every subsequent request, letting the server recognise 'this is the same logged-in user' across an otherwise stateless protocol."
},
{
 "q": "A news website is fully readable and navigable using only a keyboard, includes descriptive alt text for images, and uses proper heading structure so a screen reader can announce the page's layout to a blind visitor. What practice does this reflect, and why does it matter beyond serving users with disabilities?",
 "options": [
   "Web accessibility — designing so people with a range of abilities can use a site; it also tends to improve usability more broadly (clear structure helps everyone) and is often a genuine legal requirement in many jurisdictions",
   "Responsive design — designing so a website's layout adapts to different screen sizes, a concept specifically about screen size adaptation rather than about screen readers, alt text, or keyboard navigation",
   "Search engine optimisation — designing a website's content and structure to rank higher in search engine results, a concept unrelated to whether the site can actually be used by a blind visitor with a screen reader",
   "Progressive enhancement — building a baseline experience that works everywhere and enhancing it for more capable browsers, a concept describing a general build strategy rather than accessibility specifically"
 ],
 "answer": 0,
 "explanation": "Web accessibility (often shortened to a11y) covers exactly this: keyboard navigability, alt text, and proper semantic structure for screen readers. It genuinely matters beyond serving users with disabilities — clear, well-structured content tends to be more usable for everyone, and in many jurisdictions accessibility compliance is also a real legal requirement, not just a nicety."
},
{
 "q": "A retailer's website loads noticeably faster for a repeat visitor than for a first-time visitor, because images and other static assets are stored locally in the browser after the first visit and reused rather than re-downloaded. What is this mechanism called?",
 "options": [
   "Browser caching — storing copies of static assets locally after they're first downloaded, so subsequent visits can reuse them instead of re-downloading identical content from the server every time",
   "Load balancing — distributing incoming requests across multiple servers, a concept unrelated to whether a specific individual visitor's browser stores and reuses assets from a previous visit to the same site",
   "GraphQL — a query language letting a client specify exactly which data fields it needs from an API, a concept unrelated to whether a browser stores and reuses static assets across multiple separate visits",
   "Containerisation — packaging an application with its exact runtime dependencies into a portable unit, a concept unrelated to whether a specific visitor's browser stores and reuses assets from a previous visit"
 ],
 "answer": 0,
 "explanation": "Browser caching stores copies of static assets (images, stylesheets, scripts) locally after the first download, letting a returning visitor's browser reuse them instead of re-fetching identical content from the server — directly improving load speed for repeat visits without changing anything about the underlying content itself."
},
{
 "q": "A single-page application (SPA) loads once and then dynamically updates content on the page as the user navigates, without full page reloads, unlike a traditional multi-page site where every navigation triggers a fresh full-page reload from the server. What is the main practical tradeoff of this approach?",
 "options": [
   "SPAs often feel faster and smoother for in-app navigation after the initial load, but require more careful handling for things like search engine indexing and initial load performance, which traditional server-rendered pages handle more naturally",
   "SPAs are strictly and unconditionally better than traditional multi-page sites in absolutely every practical respect, with no meaningful downside of any kind for any type of website or web application",
   "SPAs cannot ever be indexed by any search engine under any circumstances, making them categorically unsuitable for use in literally any type of website, including private, login-only internal company tools",
   "SPAs and traditional multi-page sites are technically identical in how they load and render content, differing only in superficial visual styling choices made by the specific development team involved"
 ],
 "answer": 0,
 "explanation": "SPAs can feel notably smoother once loaded, since navigation doesn't require full page reloads — but the initial load can be heavier, and search engine indexing and other concerns that traditional server-rendered pages handle naturally often require extra deliberate engineering effort in an SPA, which is a real, practical tradeoff development teams weigh based on the specific type of site being built."
},
{
 "q": "A browser blocks a webpage's JavaScript from making a request to a different domain's API unless that API explicitly allows it via specific response headers. What security mechanism is this, and what problem is it trying to prevent?",
 "options": [
   "CORS (Cross-Origin Resource Sharing) — a browser security mechanism that restricts webpages from making requests to a different domain unless explicitly permitted, helping prevent malicious sites from silently making unauthorised requests on a user's behalf",
   "A REST API convention — a set of URL and HTTP method conventions for exposing data over HTTP, a concept unrelated to whether a browser allows or blocks a webpage's JavaScript from calling a different domain's API",
   "Browser caching — storing copies of static assets locally after they're first downloaded, a concept unrelated to whether a browser allows or blocks a webpage's JavaScript from calling a different domain's API",
   "Load balancing — distributing incoming server requests across multiple servers, a concept unrelated to whether a browser allows or blocks a specific webpage's JavaScript from calling a different domain's API"
 ],
 "answer": 0,
 "explanation": "CORS is a browser-enforced security mechanism restricting cross-domain requests by default, requiring the target API to explicitly opt in via response headers — a defence against a malicious webpage silently using a logged-in user's browser to make unauthorised requests to another site on their behalf."
},
{
 "q": "A team building a chat application needs the server to push new messages to connected users instantly, rather than having each user's browser repeatedly ask 'any new messages yet?' every few seconds. What web technology is specifically designed for this kind of persistent, two-way, real-time connection?",
 "options": [
   "WebSockets — a protocol enabling a persistent, two-way connection between browser and server, letting the server push updates instantly rather than requiring the client to repeatedly poll for new data",
   "REST API — a set of conventions for exposing data over HTTP using standard request-response cycles, which is specifically well suited to instant, persistent, two-way real-time communication like a live chat feed",
   "CORS — a browser security mechanism restricting cross-domain requests by default, a concept unrelated to whether a chat application can push new messages to connected users instantly and continuously",
   "Browser caching — storing copies of static assets locally in a user's browser, a concept unrelated to whether a chat application's server can push new messages to connected users instantly and continuously"
 ],
 "answer": 0,
 "explanation": "WebSockets establish a persistent, two-way connection, letting a server push data to a connected client the moment it's available — well suited to real-time features like chat, live notifications, or live dashboards, unlike a standard REST request-response cycle, which requires the client to initiate every exchange."
},
{
 "q": "A team wants their web app to work offline, feel like a native app when added to a phone's home screen, and still be accessible through a normal browser URL. What category of web application is specifically designed to achieve this combination?",
 "options": [
   "A progressive web app (PWA) — a web application built to work offline, be installable to a device's home screen, and still remain accessible through a standard browser, blending web reach with native-app-like capability",
   "A single-page application (SPA) — a web application that updates content dynamically without full page reloads, a concept describing in-app navigation behaviour rather than offline support or home-screen installability",
   "A REST API — a set of conventions for exposing data over HTTP, a concept describing how a backend serves data rather than whether a specific web application can work offline or be added to a home screen",
   "A microservice — an independently deployable backend service communicating over a network, a concept about backend architecture rather than about a specific web application's offline or installability features"
 ],
 "answer": 0,
 "explanation": "Progressive web apps specifically combine offline capability (through techniques like service workers caching content), home-screen installability, and continued accessibility via a normal URL — aiming to blend the reach of the web with capabilities traditionally associated with native mobile apps."
},
{
 "q": "A junior developer asks why their team bothers using a package manager instead of just manually downloading and copying library files into the project folder. What is the strongest practical argument for using a package manager?",
 "options": [
   "It automatically tracks exact dependency versions, resolves compatibility between multiple dependencies, and makes it far easier to update, share, and reproduce a project's exact set of dependencies across different machines and team members",
   "Package managers exist purely as a formal industry convention with no genuine technical benefit, and manually downloading and copying library files achieves exactly the same practical outcome with no meaningful tradeoff",
   "Package managers are required specifically because it is technically impossible for any browser or server to ever run code that was manually copied into a project folder rather than installed through a package manager",
   "Package managers exist solely to prevent other developers on the same team from ever being able to see or read which specific external libraries a project is actually using in its source code"
 ],
 "answer": 0,
 "explanation": "A package manager tracks exact versions, automatically resolves compatibility between many interdependent libraries, and makes a project's dependencies easy to reproduce consistently across different developers' machines and environments — a manually maintained folder of copied files quickly becomes error-prone and hard to keep consistent as a project and its dependencies grow."
},
{
 "q": "A frontend project uses a bundler to combine dozens of separate JavaScript source files, along with their many external library dependencies, into a small number of optimised files actually sent to the browser. What is the primary practical benefit of this build step?",
 "options": [
   "It reduces the number of separate files and total amount of code a browser needs to download and parse, generally improving load performance compared to shipping dozens of unbundled, unoptimised individual files",
   "It is required because browsers are technically incapable of ever loading more than exactly one single JavaScript file at a time, regardless of how that file's content is written or structured",
   "It permanently and irreversibly changes the underlying programming language the application's source code is written in, converting all of its logic from JavaScript into an entirely different language",
   "It exists solely so that other developers cannot read or understand a project's original, unbundled source code, functioning purely as an intentional code-obfuscation and secrecy technique"
 ],
 "answer": 0,
 "explanation": "Bundling combines many source files and dependencies into fewer, often smaller and optimised files, reducing the number of separate downloads and the total amount of code the browser needs to fetch and parse — a genuine performance optimisation for real-world load times, not a technical necessity or a deliberate obfuscation technique."
},
{
 "q": "A team stores their database password and API keys in environment variables rather than directly typing them into the application's source code files that get committed to version control. What is the main security reasoning behind this practice?",
 "options": [
   "Keeping secrets out of source code prevents them from being exposed if the code repository is ever leaked, shared publicly, or accessed by someone who shouldn't see production credentials, and allows different environments to use different secrets safely",
   "Environment variables are required because it is technically impossible for any application's source code file to ever contain a text string representing a password or an API key of any kind whatsoever",
   "This practice exists purely as an arbitrary stylistic coding convention with no actual underlying security benefit, and hardcoding secrets directly into committed source code files carries no meaningfully greater risk",
   "Environment variables automatically and permanently encrypt any secret value stored inside them, making this the only technically viable way to ever protect a password or API key from ever being accidentally exposed"
 ],
 "answer": 0,
 "explanation": "Hardcoded secrets in source code end up in version control history, potentially exposed if the repository is ever leaked, made public, or accessed by someone who shouldn't have production credentials. Environment variables keep secrets out of the codebase entirely and let different environments (development, staging, production) safely use different actual secret values without changing any code."
},
{
 "q": "A backend service automatically limits any single user or API client to a maximum of 100 requests per minute, returning an error if that limit is exceeded. What is this practice called, and what does it primarily protect against?",
 "options": [
   "Rate limiting — restricting how many requests a client can make in a given time window, protecting a backend service from being overwhelmed by excessive traffic, whether from a bug, abuse, or a deliberate attack",
   "Load balancing — distributing incoming requests across multiple servers, a concept about spreading traffic across infrastructure rather than about capping how many requests any single client is permitted to send",
   "CORS — a browser security mechanism restricting cross-domain JavaScript requests by default, a concept unrelated to how many total requests any individual client is permitted to send to a backend service",
   "Browser caching — storing copies of static assets locally in a user's browser, a concept unrelated to how many total requests any individual client is permitted to send to a backend service in a given period"
 ],
 "answer": 0,
 "explanation": "Rate limiting caps how many requests a given client can make in a time window, protecting a backend from being overwhelmed — whether the excessive traffic comes from a genuine bug in a client's code, deliberate abuse, or an attempted denial-of-service attack — while still allowing normal, well-behaved usage to function properly."
},
{
 "q": "A user's data is stored across two related database tables — one for customers and one for their orders, linked by a customer ID — rather than repeating every customer's full details inside every single order record. What is the primary benefit of structuring data this way?",
 "options": [
   "It avoids data duplication and the inconsistency risk that comes with it — updating a customer's details in one place keeps every order correctly linked to current information, rather than needing to update the same details in every order record",
   "It is required because it is technically impossible for any database table to ever store more than one single piece of information about any given customer within a single, unified table structure",
   "It guarantees the database will never experience any downtime, since normalising data into linked tables is defined as the specific technique that makes any database's uptime mathematically guaranteed",
   "It has no meaningful practical benefit over storing full customer details inside every individual order record, and both approaches are considered functionally and practically equivalent by database designers"
 ],
 "answer": 0,
 "explanation": "This reflects database normalisation: separating data into related tables avoids duplicating the same customer details across every order, which both saves storage and — more importantly — avoids the inconsistency risk of updating a customer's address in one place while stale copies linger unchanged in old order records elsewhere."
},
{
 "q": "A bank's database guarantees that a money transfer either fully completes (both the sender's balance decreases and the receiver's balance increases) or doesn't happen at all — never leaving the transfer half-done even if the system crashes mid-transfer. What database property ensures this?",
 "options": [
   "Transactions (specifically the Atomicity guarantee, part of ACID properties) — ensuring a group of operations either all succeed together or all fail together, with no partial, inconsistent state ever left behind",
   "Database indexing — creating a data structure that speeds up how quickly specific records can be looked up, a concept unrelated to whether a multi-step transfer completes fully or not at all if a crash occurs",
   "Load balancing — distributing incoming requests across multiple database servers, a concept unrelated to whether a specific multi-step transfer completes fully or not at all if the system crashes mid-transfer",
   "GraphQL — a query language letting a client specify exactly which fields it needs from an API, a concept unrelated to whether a bank's multi-step money transfer completes fully or not at all if a crash occurs"
 ],
 "answer": 0,
 "explanation": "This is the Atomicity guarantee within the ACID properties (Atomicity, Consistency, Isolation, Durability) that relational databases aim to provide for transactions: a group of operations is treated as a single indivisible unit, either fully completing or fully rolling back, which is exactly what prevents a crash from leaving a bank transfer half-completed."
},
{
 "q": "A search feature that used to take three seconds to find a customer by their phone number now returns results in ten milliseconds, after a database administrator adds a specific structure that lets the database jump directly to matching rows instead of scanning every row in the table. What did they most likely add?",
 "options": [
   "A database index — a data structure that allows the database to look up matching rows quickly, similar to a book's index letting a reader find a topic without reading every page",
   "A REST API — a set of conventions for exposing data and operations over HTTP, a concept about how external clients access data over a network rather than about how a database internally speeds up its own lookups",
   "A load balancer — a component that distributes incoming requests across multiple servers, a concept about spreading traffic across infrastructure rather than about how quickly a single database can look up matching rows",
   "A container — a portable unit packaging an application with its exact runtime dependencies, a concept unrelated to how quickly a database can look up rows matching a specific search query like a phone number"
 ],
 "answer": 0,
 "explanation": "A database index is built specifically to speed up lookups on a particular column, letting the database jump directly to matching rows rather than scanning the entire table one row at a time — the same principle as a book's index letting a reader jump straight to a topic instead of reading cover to cover, at the cost of some extra storage and slightly slower writes."
},
{
 "q": "A company chooses a relational (SQL) database for their strictly structured financial transaction records, but chooses a NoSQL document database for their rapidly evolving, loosely structured product catalogue with wildly different fields per product category. What is the reasoning behind using two different database types for two different parts of the same system?",
 "options": [
   "Different data shapes and consistency needs suit different database types — rigid, relationship-heavy structured data (like financial transactions) often fits relational databases well, while flexible, varied-shape data (like a diverse product catalogue) often fits document databases better",
   "This reasoning is fundamentally flawed, since any well-designed company should always use exactly one single database technology consistently across every single part of their system without any exception",
   "SQL databases are technically incapable of storing any product information whatsoever, which is the sole reason a completely separate NoSQL database technology is required for the product catalogue specifically",
   "NoSQL databases are, without exception, strictly and unconditionally faster than any SQL database for every possible type of query or data structure, which is the sole reason for choosing NoSQL for the catalogue"
 ],
 "answer": 0,
 "explanation": "Choosing between SQL and NoSQL isn't about one being universally better — it's about matching database structure to data shape and consistency requirements: rigid, relationship-heavy data with strict consistency needs (like financial transactions) commonly suits relational databases, while flexible, varied-shape data (like products with wildly different attributes per category) commonly suits document-style NoSQL databases, and many real systems genuinely use both for different parts of the same product."
},
{
 "q": "A popular website keeps three synchronised copies of its database on servers in different regions, so that if one server fails or a whole region loses power, the site keeps running using one of the other copies. What is this practice called?",
 "options": [
   "Database replication — maintaining multiple synchronised copies of a database across different servers or locations, improving both fault tolerance (surviving a server failure) and, often, read performance for geographically distributed users",
   "Database indexing — creating a data structure that speeds up how quickly specific records can be looked up within a single database, a concept unrelated to maintaining multiple synchronised copies across different servers",
   "Database normalisation — organising data into related tables to avoid duplication and inconsistency, a concept about a single database's internal table structure rather than about maintaining multiple copies across servers",
   "A REST API — a set of conventions for exposing data and operations over HTTP, a concept about how external clients access data rather than about maintaining multiple synchronised copies of a database across servers"
 ],
 "answer": 0,
 "explanation": "Database replication keeps synchronised copies of data across multiple servers or regions, which directly improves fault tolerance (the system survives a single server or region failing) and often improves read performance for users closer to a given replica — a distinct concept from indexing (speeding up lookups within one database) or normalisation (organising a single database's table structure)."
},
{
 "q": "A social media platform has hundreds of millions of users, and their user data is split across many separate database servers, with each server holding only a subset of users (say, based on user ID ranges), rather than one server trying to hold everyone. What is this technique called, and what problem does it primarily solve?",
 "options": [
   "Sharding — splitting a dataset across multiple database servers, primarily solving the scalability problem of a dataset growing too large or a workload too heavy for any single database server to handle efficiently",
   "Database indexing — creating a data structure that speeds up lookups within a single database server, a concept unrelated to splitting an entire dataset across many separate database servers based on user ID ranges",
   "Database normalisation — organising a single database's tables to avoid data duplication and inconsistency, a concept unrelated to splitting an entire dataset across many separate physical database servers",
   "Containerisation — packaging an application with its exact runtime dependencies into a portable unit, a concept unrelated to splitting a large dataset across many separate physical database servers"
 ],
 "answer": 0,
 "explanation": "Sharding splits a dataset across multiple database servers (each holding a subset, often by some key like user ID range), directly addressing the scalability problem of a dataset or workload becoming too large for any single server to handle efficiently — a different technique from replication (multiple full copies for fault tolerance) though the two are sometimes combined."
},
{
 "q": "A distributed database serving users worldwide must choose its behaviour during a network partition (when some servers temporarily can't communicate with others): either keep serving requests with possibly slightly outdated data, or refuse requests until the servers can fully resync. This forced tradeoff is described by which principle?",
 "options": [
   "The CAP theorem — stating that a distributed system experiencing a network partition must choose between Consistency (always correct, up-to-date data) and Availability (always responding to requests), since guaranteeing both simultaneously during a partition is not possible",
   "The testing pyramid — a strategy for structuring a system's automated tests into layers of unit, integration, and end-to-end tests, unrelated to how a distributed database behaves during an actual network partition",
   "DRY (Don't Repeat Yourself) — a principle about avoiding duplicated code within a codebase, unrelated to how a distributed database handles the specific tradeoff between consistency and availability during a partition",
   "Recursion — a programming technique where a function calls itself on a smaller version of a problem, unrelated to how a distributed database handles a tradeoff between consistency and availability during a partition"
 ],
 "answer": 0,
 "explanation": "The CAP theorem describes a real, unavoidable tradeoff for distributed systems during a network partition: they can prioritise Consistency (every read reflects the latest write, even if that means refusing some requests) or Availability (always responding, even if some responses might be slightly stale) — but not perfectly guarantee both at the same time under partition conditions."
},
{
 "q": "A developer accidentally deletes an important production database table with a single mistyped command. The company recovers all the lost data within the hour from an automated daily copy stored separately from the live database. What practice made this recovery possible?",
 "options": [
   "Regular database backups — maintaining periodic, separately stored copies of data specifically so it can be restored after accidental deletion, corruption, or other data loss, independent of the live database's own current state",
   "Database sharding — splitting a dataset across multiple servers based on some key like user ID range, a technique focused on scalability for large datasets rather than on recovering from an accidental data deletion",
   "Database indexing — creating a data structure that speeds up lookups within a database, a technique focused on query performance rather than on recovering data that has already been accidentally deleted",
   "The CAP theorem — a principle describing an unavoidable tradeoff in distributed systems during a network partition, unrelated to whether a company can actually recover data after an accidental deletion mistake"
 ],
 "answer": 0,
 "explanation": "Regular backups — separately stored, periodic copies of data — exist specifically to recover from scenarios like accidental deletion, corruption, or ransomware, independent of whatever state the live database is currently in. Without them, a single mistaken command with no other safeguard could mean genuinely permanent, unrecoverable data loss."
},
{
 "q": "A junior developer is told their new feature 'passed code review' only after two senior teammates read through the actual proposed code changes, asked clarifying questions, and suggested specific improvements before it was allowed to be merged into the shared codebase. What is the primary purpose of this process?",
 "options": [
   "Catching bugs, design issues, and knowledge gaps before code reaches production, while also spreading understanding of the codebase across the team rather than concentrating it in just the original author",
   "Code review exists purely as a bureaucratic formality required for legal compliance reasons, with no genuine connection to catching bugs or improving the actual quality of the code being reviewed",
   "Code review's sole purpose is to slow down the pace of a team's overall development process, deliberately introducing unnecessary friction and delay into the process of building new features",
   "Code review is required specifically because junior developers are, by definition, mathematically guaranteed to write buggy code, an assumption that does not apply to code written by senior developers"
 ],
 "answer": 0,
 "explanation": "Code review serves multiple genuine purposes at once: catching bugs and design problems before they reach production, sharing knowledge of the codebase across the team rather than isolating it with one person, and mentoring — none of which are specific to junior versus senior authorship, since even experienced developers benefit from a second set of eyes."
},
{
 "q": "A team decides to skip writing proper tests and documentation for a new feature to hit a tight deadline, planning to 'come back and fix it properly later.' Six months later, that shortcut is still causing bugs and slowing down every new feature built near that part of the codebase. What concept describes this situation?",
 "options": [
   "Technical debt — shortcuts taken for short-term speed that create ongoing, compounding costs later, similar to financial debt accumulating interest the longer it goes unpaid",
   "The CAP theorem — a principle describing an unavoidable tradeoff in distributed systems between consistency and availability during a network partition, unrelated to the consequences of skipping tests and documentation",
   "Database sharding — a technique for splitting a large dataset across multiple database servers, unrelated to the consequences of a development team skipping proper tests and documentation to meet a deadline",
   "Polymorphism — an object-oriented programming concept about shared method names behaving differently per object type, unrelated to the long-term consequences of a team skipping tests and documentation"
 ],
 "answer": 0,
 "explanation": "Technical debt is a deliberate (or sometimes accidental) shortcut that trades short-term speed for longer-term cost — exactly like financial debt, the longer it goes unaddressed, the more it tends to compound, slowing down future work and increasing bug risk in the affected area of the codebase, which is why teams generally try to track and periodically pay it down rather than let it accumulate indefinitely."
},
{
 "q": "A tech company operating across multiple African countries hires developers who work fully remotely from their home cities, connected to distributed teams and clients around the world, rather than all working from one physical office. This model, associated with organisations like Andela, has been significant for African tech talent primarily because:",
 "options": [
   "It connects skilled developers in African countries to global job opportunities and market-rate compensation without requiring physical relocation, helping address a real gap between local talent supply and local job availability",
   "It is the only way software can technically be built at all, since it is fundamentally impossible for any group of developers working in the exact same physical office to ever successfully build any software product",
   "It eliminates any need for developers to have internet access, since remote work by definition means working entirely offline without any connection to distributed teams, clients, or shared code repositories",
   "It guarantees every participating developer an identical salary regardless of experience level, project complexity, or employer, since remote work is defined by a single fixed, universal global pay rate"
 ],
 "answer": 0,
 "explanation": "The distributed/remote-work model connects skilled developers to a much larger global market of opportunities and compensation without requiring relocation — genuinely significant given that local job markets don't always match local talent supply, and it's part of why organisations built around this model have been influential in African tech employment specifically."
},
{
 "q": "A startup builds the absolute simplest working version of their product — just enough to test their core idea with real users — before investing in a fully-featured, polished version. What is this approach called, and what is its main purpose?",
 "options": [
   "A minimum viable product (MVP) — building the smallest functional version of a product to test core assumptions with real users before investing heavily in features that might turn out to be unwanted or wrong",
   "The testing pyramid — a strategy for structuring a team's automated tests into layers, unrelated to the broader business strategy of building a minimal product to first validate an idea with real users",
   "Technical debt — deliberately taking on shortcuts for short-term speed at the cost of increased long-term maintenance burden, a concept distinct from the specific product strategy of building a minimal viable product",
   "Infrastructure as code — a practice for defining server configuration as version-controlled files, unrelated to the broader business and product strategy of building a minimal version of a product to test an idea"
 ],
 "answer": 0,
 "explanation": "A minimum viable product is built specifically to test whether a core idea actually resonates with real users before committing significant resources to fully building it out — a risk-reduction strategy from lean startup thinking, distinct from technical debt (which is about code-quality shortcuts) or infrastructure practices."
},
{
 "q": "A program needs to store a list of student names where fast access by position (get the 5th name) matters more than frequent insertion or removal from the middle of the list. Which basic data structure is generally best suited to this specific access pattern?",
 "options": [
   "An array — stores elements in contiguous, indexed positions, giving fast constant-time access by position, though inserting or removing an element from the middle requires shifting other elements",
   "A linked list — stores elements as a chain of nodes each pointing to the next, giving fast insertion or removal at any point, but requiring a slower step-by-step walk through the chain to reach a specific position",
   "A hash table — stores elements as key-value pairs for fast lookup by a specific key, a structure not organised around accessing elements by their numeric position in a sequential ordered list",
   "Arrays and linked lists offer functionally identical performance characteristics for every possible access pattern, making the specific choice between them purely a matter of arbitrary developer preference"
 ],
 "answer": 0,
 "explanation": "Arrays store elements in contiguous memory with direct index-based access, making 'get the 5th element' a fast, constant-time operation — the right tradeoff when positional access matters more than frequent middle insertion/removal, which is comparatively expensive for arrays but cheap for a linked list, illustrating why data structure choice should match actual access patterns."
},
{
 "q": "A program needs to quickly check whether a given username is already taken, out of millions of registered usernames, without scanning the entire list each time. Which data structure is specifically designed to make this kind of lookup very fast on average?",
 "options": [
   "A hash table — maps each key (like a username) to a value using a hash function, enabling average constant-time lookups without needing to scan through every stored entry",
   "A linked list — stores elements as a chain of nodes, each requiring a step-by-step walk through the chain to find a specific value, generally making a full username lookup slower on average than a hash table",
   "An array sorted alphabetically would always be strictly faster than a hash table for this specific username-lookup task, regardless of how many millions of usernames are actually stored",
   "This kind of fast lookup task is fundamentally impossible for any data structure to perform without physically scanning through every single one of the millions of stored usernames one at a time"
 ],
 "answer": 0,
 "explanation": "Hash tables map keys to values using a hash function, giving average constant-time lookups regardless of how many entries are stored — exactly the right structure for 'is this username taken' checks against a huge collection, versus a linked list or unsorted array, which would require scanning through entries one by one in the worst case."
},
{
 "q": "A file system's folder structure — folders containing files and other folders, which can themselves contain more folders — is naturally represented in code using which fundamental data structure?",
 "options": [
   "A tree — a hierarchical structure where each node can have multiple child nodes, naturally matching nested, branching relationships like folders containing subfolders",
   "A hash table — a structure mapping keys directly to values for fast lookup, a shape that doesn't naturally represent hierarchical, nested parent-child folder relationships the way a tree structure does",
   "An array — a structure storing elements in a single, flat, contiguous, indexed sequence, a shape that doesn't naturally represent nested, branching parent-child folder relationships the way a tree structure does",
   "A linked list — a structure storing elements as a single flat chain of nodes each pointing only to the next one, a shape that doesn't naturally represent branching, nested folder relationships"
 ],
 "answer": 0,
 "explanation": "Tree structures represent hierarchical, branching relationships naturally, where each node can have multiple children — a file system's nested folder structure is a textbook real-world example, distinct from flat linear structures like arrays and linked lists, or key-value structures like hash tables."
},
{
 "q": "A 'undo' feature in a text editor needs to reverse the most recently made change first, then the one before that, and so on — always undoing in the exact reverse order actions were taken. Which basic data structure naturally models this 'last action taken, first action undone' behaviour?",
 "options": [
   "A stack — a Last-In-First-Out (LIFO) structure where the most recently added item is the first one removed, naturally matching an undo feature's need to reverse the most recent action first",
   "A queue — a First-In-First-Out (FIFO) structure where the earliest added item is the first one removed, which would undo the very first action taken rather than the most recently made change",
   "A hash table — a structure mapping keys to values for fast lookup by key, a shape not organised around any particular strict ordering of insertion or removal like a true undo history requires",
   "An array and a stack are functionally and technically identical structures with no meaningful behavioural difference whatsoever regarding the specific order in which their elements can be added or removed"
 ],
 "answer": 0,
 "explanation": "A stack's Last-In-First-Out behaviour exactly matches undo functionality: the most recently performed action is the first one reversed. A queue's First-In-First-Out behaviour would do the opposite — undo the oldest action first — which is why undo features are built on stacks, not queues."
},
{
 "q": "A support ticketing system processes customer tickets strictly in the order they arrived — the very first ticket submitted is the very first one handled, no matter how many new tickets have arrived since. Which basic data structure naturally models this behaviour?",
 "options": [
   "A queue — a First-In-First-Out (FIFO) structure where the earliest added item is the first one removed, naturally matching a support system that must handle the oldest ticket first",
   "A stack — a Last-In-First-Out (LIFO) structure where the most recently added item is the first one removed, which would handle the newest ticket first rather than the oldest one",
   "A hash table — a structure mapping keys to values for fast lookup by a specific key, a shape not organised around any strict first-arrived, first-handled ordering the way a ticketing queue requires",
   "A tree — a hierarchical structure where each node can have multiple child nodes, a shape not organised around any strict linear, sequential first-arrived, first-handled processing order"
 ],
 "answer": 0,
 "explanation": "A queue's First-In-First-Out behaviour exactly matches a fair support-ticket system: the oldest waiting ticket is always handled first, regardless of how many newer tickets have since arrived — the direct opposite ordering behaviour from a stack, which would prioritise the most recently added item instead."
},
{
 "q": "A developer accidentally writes `let x = 5; x = 'hello';` in a language that allows a variable's type to freely change at runtime, versus a different language that would immediately throw a compile-time error for the exact same code. What distinction does this illustrate?",
 "options": [
   "Dynamic versus static typing — dynamically typed languages allow a variable's type to change freely at runtime, while statically typed languages check and enforce types before the program even runs, catching this kind of mismatch earlier",
   "Compiled versus interpreted languages — a distinction about whether source code is translated to machine code ahead of time or executed line-by-line at runtime, unrelated to whether a variable's type can change after being assigned",
   "Recursion versus iteration — a distinction about whether a function calls itself or repeats using a loop construct, unrelated to whether a given programming language allows a variable's assigned type to change freely",
   "Object-oriented versus functional programming — a distinction about two different overall programming paradigms, unrelated specifically to whether a given language allows a single variable's type to change at runtime"
 ],
 "answer": 0,
 "explanation": "Dynamic typing (as in JavaScript or Python) lets a variable hold any type and change type freely at runtime — flexible, but errors like this one only surface when that specific line actually runs. Static typing (as in Java or TypeScript) checks types before the program runs at all, catching this exact kind of mismatch earlier, as a compile-time error rather than a runtime surprise."
},
{
 "q": "One programming language translates an entire program's source code into machine code all at once before it can be run, producing an executable file. A different language reads and executes source code line by line each time the program runs, without a separate translation step first. What distinction is this?",
 "options": [
   "Compiled versus interpreted languages — a compiled language is translated to machine code ahead of time into a standalone executable, while an interpreted language is read and executed line by line each time it runs",
   "Static versus dynamic typing — a distinction about whether a variable's type is checked before the program runs or allowed to change freely at runtime, unrelated to how or when source code is translated into machine code",
   "Recursion versus iteration — a distinction about a function calling itself versus repeating using a loop construct, unrelated to whether a language's source code is translated ahead of time or executed line by line",
   "Object-oriented versus functional programming — a distinction between two different overall programming paradigms, unrelated specifically to whether a language's source code is compiled ahead of time or interpreted at runtime"
 ],
 "answer": 0,
 "explanation": "Compiled languages translate the full program to machine code ahead of time, producing a standalone executable that can run without the original compiler present; interpreted languages read and execute source code line by line each time, generally trading some raw execution speed for faster iteration and not needing a separate build step — a real, practical tradeoff influencing language choice for different kinds of projects."
},
{
 "q": "Two parts of a program running at the same time both try to update the same shared variable, and depending on the exact, unpredictable timing of each operation, the final result sometimes comes out different across separate runs of the identical code. What is this problem called?",
 "options": [
   "A race condition — a bug where the outcome depends on the unpredictable relative timing of concurrent operations accessing shared state, often fixed using synchronisation mechanisms like locks",
   "A memory leak — a bug where a program fails to release memory it no longer needs, causing memory usage to grow over time, a problem unrelated to unpredictable timing between concurrently running operations",
   "Technical debt — a buildup of shortcuts taken for short-term speed that create ongoing, compounding maintenance costs later, a concept unrelated to the specific unpredictable-timing bug being described here",
   "A zero-day vulnerability — a security flaw unknown to a software's own vendor, with no patch yet available, a concept from cybersecurity unrelated to unpredictable timing between two concurrently running program operations"
 ],
 "answer": 0,
 "explanation": "A race condition occurs when the correctness of a program depends on the unpredictable relative timing of concurrent operations touching shared state — a notoriously hard class of bug to reproduce and debug precisely because it may not show up consistently, and is typically addressed using synchronisation mechanisms like locks or atomic operations to control access to shared state."
},
{
 "q": "A long-running program's memory usage steadily climbs hour after hour even though the actual amount of data it's working with stays roughly constant, eventually causing it to crash. What is this problem generally called, and what typically causes it in languages without automatic memory management?",
 "options": [
   "A memory leak — memory that's allocated but never released after it's no longer needed, gradually accumulating over time; in languages without automatic garbage collection, this often happens when a programmer forgets to explicitly free memory they allocated",
   "A race condition — a bug where the outcome of concurrent operations depends on unpredictable timing, a concept about timing-dependent correctness rather than about steadily accumulating, un-released memory over a long period",
   "Technical debt — a buildup of shortcuts taken for short-term development speed, a broader software-engineering concept rather than a specific, low-level technical description of gradually accumulating unreleased memory",
   "A zero-day vulnerability — a previously unknown security flaw a vendor hasn't yet patched, a cybersecurity concept unrelated to a long-running program's memory usage steadily and gradually climbing over time"
 ],
 "answer": 0,
 "explanation": "A memory leak happens when a program allocates memory but never releases it once it's no longer needed, so usage climbs steadily even though actual working data stays constant. Languages with automatic garbage collection (like Python or JavaScript) reduce but don't fully eliminate this risk; languages requiring manual memory management (like C) put this responsibility squarely on the programmer, where a forgotten deallocation is a classic cause."
},
{
 "q": "Two developers working on the same file both make different changes to the exact same line of code, and when one of them tries to merge their changes into the shared codebase, the version control system flags the file and asks a human to decide which change should win. What is this situation called?",
 "options": [
   "A merge conflict — occurring when version control can't automatically reconcile two sets of changes that both touch the same part of a file, requiring a human to manually decide how to resolve the conflicting versions",
   "A race condition — a bug where the outcome of concurrently running program operations depends on unpredictable timing, a concept about a running program's behaviour rather than about reconciling two developers' code changes",
   "Technical debt — a buildup of shortcuts taken for short-term development speed that create ongoing maintenance costs, a broader concept distinct from the specific, immediate act of manually resolving conflicting file changes",
   "A memory leak — memory that is allocated but never properly released by a running program, a concept about a program's runtime memory behaviour rather than about two developers' conflicting code changes to one file"
 ],
 "answer": 0,
 "explanation": "A merge conflict happens when version control can't automatically combine two sets of changes that touch the same part of a file — it's a routine, expected part of collaborative development using tools like Git, resolved by a human explicitly choosing (or combining) which version of that specific section should be kept."
},
{
 "q": "A developer wraps a piece of code that might fail (like reading a file that may not exist) in a block that catches any resulting error and shows the user a friendly message, instead of letting the whole program crash. What is this practice called?",
 "options": [
   "Error handling (using try/catch or similar constructs) — anticipating that certain operations might fail and defining a controlled response, rather than letting an unhandled failure crash the entire program",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept unrelated to how a program responds when a specific operation like a file read unexpectedly fails",
   "Polymorphism — an object-oriented concept where the same method name behaves differently depending on the specific object it's called on, a concept unrelated to how a program responds to an operation that fails",
   "A design pattern specifically and exclusively called the 'observer pattern', which happens to be the sole and only recognised technique used across all programming languages for handling operations that might fail"
 ],
 "answer": 0,
 "explanation": "Error handling anticipates that certain operations can fail (a missing file, a broken network connection, invalid user input) and defines what should happen in that case, rather than letting an unhandled failure crash the whole program — a fundamental defensive programming practice distinct from unrelated concepts like recursion or polymorphism."
},
{
 "q": "A team building a large application repeatedly encounters the same recurring design problem — coordinating updates when one part of the system changes and several other parts need to react — and adopts a well-known, named, reusable solution structure other developers would immediately recognise. What is this kind of reusable solution generally called?",
 "options": [
   "A design pattern — a general, reusable, well-documented solution to a commonly recurring software design problem, giving developers a shared vocabulary and a battle-tested structure rather than reinventing a solution from scratch each time",
   "A data structure — a specific way of organising and storing data, like an array or a hash table, a concept about data organisation rather than about a general, reusable solution to a recurring design coordination problem",
   "Technical debt — a buildup of shortcuts taken for short-term development speed, a concept describing an accumulating cost rather than a deliberate, well-documented, reusable solution to a recurring design problem",
   "A REST API — a set of conventions for exposing data and operations over HTTP, a specific web-development concept rather than a general, reusable solution to a recurring internal software design coordination problem"
 ],
 "answer": 0,
 "explanation": "A design pattern is a general, reusable, well-documented solution to a commonly recurring design problem (the scenario described — one part changing and others needing to react — is the classic 'observer pattern') — giving developers shared vocabulary and a proven structure rather than reinventing a solution independently each time the same problem arises."
},
{
 "q": "A public API changes how one of its endpoints returns data, breaking every existing application built against the old format overnight, with no warning. What practice would have let the API evolve without breaking every existing integration immediately?",
 "options": [
   "API versioning — maintaining multiple, distinctly labelled versions of an API simultaneously (like /v1/ and /v2/), letting existing integrations keep working against the old version while new integrations adopt the new one",
   "Load balancing — distributing incoming requests across multiple servers, a concept about spreading traffic across infrastructure rather than about managing breaking changes to an API's data format over time",
   "Database sharding — splitting a large dataset across multiple database servers, a concept about data storage scalability rather than about managing breaking changes to an API's external data format over time",
   "Containerisation — packaging an application with its exact runtime dependencies into a portable unit, a concept about deployment packaging rather than about managing breaking changes to an API's external data format"
 ],
 "answer": 0,
 "explanation": "API versioning lets a provider introduce breaking changes in a new, separately labelled version while keeping the old version running unchanged for existing integrations — giving consumers time to migrate deliberately, rather than having every dependent application break simultaneously and without warning the moment something changes."
},
{
 "q": "A team practising agile/scrum development breaks their work into short, fixed-length cycles (say, two weeks), at the end of which they demo working software and adjust priorities based on feedback, rather than planning the entire year of work upfront and only showing results at the very end. What is the main reasoning behind this approach?",
 "options": [
   "Shorter feedback cycles let a team catch misunderstandings, changing requirements, or wrong assumptions early and cheaply, rather than discovering a fundamental problem only after months of work built on a flawed initial plan",
   "This approach exists purely to make a development team's overall work appear busier and more active to company management, with no genuine connection to actual software quality or project outcomes",
   "Agile/scrum development guarantees that a project will always be completed by its very first originally planned deadline, regardless of any requirement changes or unexpected complications discovered along the way",
   "Breaking work into short, fixed-length cycles has no meaningful practical difference from planning an entire year of work upfront, and both approaches are considered functionally equivalent by most software teams"
 ],
 "answer": 0,
 "explanation": "The core rationale behind agile, iterative development is cheap, early feedback: by regularly demoing working software and reassessing priorities in short cycles, a team can catch a wrong assumption or a changed requirement within weeks rather than only discovering it after months of work already built on a now-outdated upfront plan."
},
{
 "q": "A new developer joins a team and spends their first week almost entirely reading a well-maintained internal wiki explaining the codebase's architecture, deployment process, and team conventions, getting productive far faster than a previous hire who joined a team with no such documentation. What does this illustrate about documentation's practical value?",
 "options": [
   "Good documentation reduces the time and effort required to bring new team members up to speed, and also reduces a team's dependence on any single person's memory of how and why a system was built the way it was",
   "Documentation exists purely as a bureaucratic formality with no genuine practical benefit to a development team's actual day-to-day productivity or its ability to onboard and train new hires effectively",
   "Well-documented codebases are always mathematically guaranteed to contain fewer bugs than poorly documented ones, since the mere presence of documentation is what directly and solely determines a codebase's bug rate",
   "This scenario proves that documentation is only ever useful for genuinely new hires specifically, and provides no ongoing practical value whatsoever to experienced team members who already know the codebase well"
 ],
 "answer": 0,
 "explanation": "Documentation's practical value shows up clearly in onboarding speed and in reducing a team's dependence on any one person's memory (what happens when that person leaves or is simply unavailable) — a real, measurable difference in productivity and resilience, not merely a bureaucratic checkbox, even though it doesn't directly determine bug rates on its own."
},
{
 "q": "A small business owner with no coding background builds a working internal inventory-tracking tool by dragging and connecting visual blocks in a platform, rather than writing traditional code by hand. What is this category of tool called, and what is its main tradeoff compared to traditional custom-coded software?",
 "options": [
   "Low-code/no-code platforms — letting people build functional applications through visual tools rather than hand-written code, trading some flexibility and fine-grained control for dramatically faster development and a much lower skill barrier to entry",
   "Infrastructure as code — a practice specifically about defining server configuration through version-controlled text files, a concept distinct from visual, drag-and-drop application-building tools aimed at non-programmers",
   "A REST API — a set of conventions for exposing data and operations over HTTP, a concept about how software systems communicate with each other rather than about how an individual application is actually built",
   "Containerisation — a technology for packaging an application with its exact runtime dependencies into a portable unit, a concept about deployment rather than about how an application is originally built or designed"
 ],
 "answer": 0,
 "explanation": "Low-code/no-code platforms let people build functional software through visual tools rather than hand-written code, dramatically lowering the barrier to entry and speeding up development for many common use cases — at the real cost of less fine-grained control and flexibility compared to fully custom-coded software, which matters once requirements get sufficiently complex or unusual."
},
{
 "q": "A developer contributes a bug fix to a widely used open-source JavaScript library, and after review by the project's maintainers, it's merged and becomes available to every project depending on that library worldwide. What does this illustrate about the open-source development model?",
 "options": [
   "Contributions from outside the original core team can improve software used by a huge number of downstream projects, and a maintainer review process still exists to check quality and correctness before changes are accepted",
   "Anyone can submit any code to any open-source project and have it automatically and immediately merged into the shared codebase, with no review, approval, or quality-checking process of any kind involved",
   "Open-source software, by definition, cannot legally be used inside any commercial, for-profit company or product, making this bug fix's real-world downstream impact limited exclusively to non-commercial projects",
   "This kind of external contribution is only theoretically possible in principle and essentially never actually happens in practice on any real, actively maintained widely used open-source software project"
 ],
 "answer": 0,
 "explanation": "Open-source development genuinely allows contributions from outside a project's core team, and a real fix from an outside contributor can end up benefiting a huge number of downstream projects — but nearly all serious open-source projects still maintain a review process to check quality and correctness before merging, rather than accepting any submitted code automatically."
},
{
 "q": "A company deciding on a technology stack for a new product weighs factors like their existing team's skills, the size and health of each option's developer community, long-term maintenance costs, and how well each option fits their specific performance needs — rather than simply picking whatever technology is currently most talked about online. What does this decision-making approach illustrate?",
 "options": [
   "Good technology choices are driven by a project's actual specific context and constraints, not by hype or popularity alone, since the 'best' stack genuinely depends on team skills, community support, and the product's real requirements",
   "Technology stack choice has no meaningful long-term consequences for a company whatsoever, since any technology option will always perform identically regardless of the team's skills or the community supporting it",
   "The single most popular and most talked-about technology option is always guaranteed to be the objectively correct choice for literally any company or project, regardless of that specific team's own particular skills or context",
   "This kind of careful, multi-factor decision-making approach to choosing a technology stack is considered an outdated practice that experienced modern engineering teams have now completely abandoned in every case"
 ],
 "answer": 0,
 "explanation": "Sound technology stack decisions weigh real, project-specific factors — team familiarity, community and ecosystem health, long-term maintenance burden, and actual performance needs — rather than defaulting to whatever's most hyped at the moment, since a technology that's a great fit for one team and product can be a poor fit for another with different skills, scale, or requirements."
},
{
 "q": "Which of the following are genuine, well-established benefits of using version control (like Git) for a software project? Select all that apply.",
 "options": [
   "Tracking a full history of every change, including who made it and when",
   "Allowing multiple developers to work on different features simultaneously without directly overwriting each other's work",
   "Guaranteeing that a project's code will never contain any bugs once it is placed under version control",
   "Making it possible to revert to a previous working version if a recent change introduces a serious problem"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Change history tracking, safe parallel collaboration, and the ability to revert to a previous working state are all genuine, core benefits of version control. It does not and cannot guarantee bug-free code — version control tracks and manages changes; it has no bearing on whether the code within those changes is actually correct."
},
{
 "q": "Which of the following are genuine reasons a development team might choose a microservices architecture over a single monolithic application? Select all that apply.",
 "options": [
   "The ability to scale one specific part of the system (like the payments service) independently of other parts",
   "The ability to deploy an update to one service without needing to redeploy the entire application",
   "Microservices architecture guarantees zero operational complexity and completely eliminates the need for any monitoring or coordination between services",
   "Different teams can work on and independently deploy different services using different technology choices suited to each service's needs"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Independent scaling, independent deployment, and technology flexibility per service are all genuine, commonly cited benefits of microservices. The claim about zero operational complexity is false and is actually the opposite of a well-known real tradeoff — microservices generally increase operational complexity (more moving parts, network calls, and coordination needed), which is exactly why the architecture isn't automatically the right choice for every project."
},
{
 "q": "A website lets users 'Sign in with Google' instead of creating a new username and password just for that site. Behind the scenes, the site never sees or stores the user's actual Google password. What authentication approach makes this possible?",
 "options": [
   "OAuth — a protocol that lets a user grant one application limited access to their account on another service (like Google) without ever sharing their actual password with the requesting application",
   "A REST API — a set of conventions for exposing data and operations over HTTP, a general concept about API design rather than the specific mechanism that lets one service authenticate a user via another service",
   "CORS — a browser security mechanism restricting cross-domain JavaScript requests by default, a browser-security concept unrelated to how a 'Sign in with Google' authentication flow actually works",
   "A REST API and OAuth are simply two different names referring to the exact same identical underlying technical protocol, with no meaningful distinction between how each one actually works in practice"
 ],
 "answer": 0,
 "explanation": "OAuth is specifically designed to let a user grant one application limited, scoped access to their account on another service without ever handing over their actual password to the requesting application — the standard mechanism behind 'Sign in with Google/Facebook/GitHub' style authentication flows used across the web."
},
{
 "q": "A signup form immediately shows an error message under the email field the moment a user types something that isn't a validly formatted email address, before they even try to submit the form. What is this practice called, and why is it usually paired with a second check on the server as well?",
 "options": [
   "Form validation (client-side and server-side) — checking input immediately in the browser gives fast feedback, but a server-side check is still needed because client-side checks can be bypassed by a user directly sending a request",
   "CORS — a browser security mechanism restricting cross-domain JavaScript requests by default, a concept about cross-origin request permissions rather than about checking whether a user's typed input is correctly formatted",
   "Rate limiting — restricting how many requests a client can make within a given time window, a concept about request volume rather than about checking whether a specific piece of user-typed input is validly formatted",
   "Only client-side validation in the browser is ever needed for a form like this, since it is technically impossible for any user to submit data to a server without going through the browser's own visible form fields"
 ],
 "answer": 0,
 "explanation": "Client-side validation gives immediate, responsive feedback without a round trip to the server, but it can always be bypassed by someone sending a request directly (not through the actual form), so server-side validation remains necessary as the real, trustworthy check — client-side is a UX improvement, not a security guarantee on its own."
},
{
 "q": "A news website's article pages are structured with clear heading tags, descriptive page titles, and clean URLs, and the site loads quickly on mobile devices. A competing site with similar content but messy structure, slow load times, and generic titles ranks lower in search results for the same topics. What practice does the first site's approach reflect?",
 "options": [
   "Search engine optimisation (SEO) — structuring and building a site in ways that help search engines understand and favourably rank its content, alongside genuinely serving readers well through clear structure and fast loading",
   "Web accessibility — designing so people with a range of abilities can use a site, a related but distinct practice focused specifically on usability for people with disabilities rather than on search engine ranking",
   "CORS — a browser security mechanism restricting cross-domain JavaScript requests by default, a concept entirely unrelated to how a website's structure or load speed might affect its search engine ranking",
   "Browser caching — storing copies of static assets locally in a visitor's browser after a first visit, a concept about repeat-visit load speed rather than about a site's overall structure or its search engine ranking"
 ],
 "answer": 0,
 "explanation": "SEO covers exactly this combination — clear structure, descriptive titles, clean URLs, and fast load times — which search engines use as signals to understand and rank content, and which also happen to genuinely improve the experience for real human readers, making good SEO and good usability substantially overlapping goals rather than competing ones."
},
{
 "q": "A user's browser stores a small piece of data locally that persists even after the browser is fully closed and reopened days later, used by a website to remember a user's preferred theme (dark or light mode) without needing to ask every single visit. Compared to a typical session cookie that expires when the browser closes, what does this describe?",
 "options": [
   "Persistent local storage (like localStorage) — data that remains stored in the browser across sessions until explicitly cleared, well suited to remembering long-lived preferences rather than short-lived, per-session state",
   "CORS — a browser security mechanism restricting cross-domain JavaScript requests by default, a concept about cross-origin request permissions rather than about how long a specific piece of browser-stored data persists",
   "A REST API — a set of conventions for exposing data and operations over HTTP between a client and a server, a concept unrelated to how long a specific piece of data is stored locally within a user's own browser",
   "Server-side rendering — generating a webpage's HTML on the server before sending it to the browser, a concept about page generation rather than about how long browser-stored preference data persists between visits"
 ],
 "answer": 0,
 "explanation": "Persistent browser storage mechanisms (like localStorage) keep data available across sessions until explicitly cleared, which suits a long-lived preference like a theme choice — different from a typical session cookie's shorter, per-visit lifetime, and a genuinely different tool for a genuinely different kind of state to remember."
},
{
 "q": "When a user types a website's name into their browser, a system translates that human-readable name into the numeric address actually needed to locate the correct server on the internet. What is this translation system called?",
 "options": [
   "DNS (Domain Name System) — translating human-readable domain names into the numeric IP addresses computers use to locate and communicate with the correct server on the internet",
   "CORS — a browser security mechanism restricting cross-domain JavaScript requests by default, a concept about cross-origin request permissions rather than about translating a domain name into a numeric server address",
   "A REST API — a set of conventions for exposing data and operations over HTTP, a concept about how a client and server exchange data rather than about translating a domain name into a numeric server address",
   "Browser caching — storing copies of static assets locally in a visitor's browser, a concept about reusing previously downloaded content rather than about translating a domain name into a numeric server address"
 ],
 "answer": 0,
 "explanation": "DNS acts as the internet's naming directory, translating human-friendly domain names into the numeric IP addresses that actually route network traffic to the correct server — a foundational, invisible step that happens before a browser can even begin requesting the actual webpage content."
},
{
 "q": "A website serving users worldwide stores copies of its images and static files on servers physically distributed across many countries, so a visitor in Lagos loads those files from a nearby server rather than one located on another continent. What is this network of distributed servers called, and what problem does it solve?",
 "options": [
   "A CDN (Content Delivery Network) — a geographically distributed set of servers caching static content close to users, reducing load times by shortening the physical and network distance data has to travel",
   "DNS (Domain Name System) — a system for translating human-readable domain names into numeric IP addresses, a concept about name resolution rather than about physically distributing copies of static content globally",
   "A REST API — a set of conventions for exposing data and operations over HTTP, a concept about how a client and server exchange structured data rather than about physically distributing static content globally",
   "Load balancing — distributing incoming requests across multiple servers typically within one data centre or region, a concept distinct from geographically distributing cached static content across the whole world"
 ],
 "answer": 0,
 "explanation": "A CDN caches static content (images, stylesheets, scripts) on servers distributed across many geographic locations, so a user's request is served by a nearby server rather than travelling to one central, possibly distant server — directly reducing load times by shortening the physical and network distance the data has to travel."
},
{
 "q": "A payment processor's system automatically sends a notification to a merchant's server the moment a payment succeeds, rather than requiring the merchant's server to repeatedly ask 'has the payment gone through yet?' every few seconds. What is this pattern called?",
 "options": [
   "A webhook — a mechanism where one system automatically sends a notification (an HTTP request) to another system the moment a specific event occurs, rather than requiring the second system to repeatedly poll for updates",
   "A REST API — a set of general conventions for exposing data and operations over HTTP, a broader concept describing how data is generally structured and requested rather than the specific event-driven notification pattern here",
   "CORS — a browser security mechanism restricting cross-domain JavaScript requests by default, a browser-specific security concept unrelated to how one backend server notifies another backend server about an event",
   "DNS — a system for translating human-readable domain names into numeric IP addresses, a naming-resolution concept entirely unrelated to how one system might automatically notify another about a completed event"
 ],
 "answer": 0,
 "explanation": "A webhook flips the usual request direction: instead of a client repeatedly polling a server asking whether something has happened, the server proactively sends a notification the moment the event actually occurs — more efficient than polling, and a standard pattern for integrating systems like payment processors with merchant applications."
},
{
 "q": "A blog built with a static site generator produces plain HTML files ahead of time that are simply served as-is to every visitor, while a dynamic site regenerates and customises its HTML on the server for each individual request. What is a key practical tradeoff between these two approaches?",
 "options": [
   "Static sites are typically faster to serve and simpler to host securely, since there's no server-side logic processing each request, but they can't easily show personalised or frequently changing content without extra tooling",
   "Static and dynamic sites are functionally and technically identical in every practical respect, and the specific choice between them makes no meaningful difference to a site's performance, security, or personalisation ability",
   "Dynamic sites are always strictly faster to load for every single visitor than any static site, regardless of that specific site's actual content, personalisation needs, or overall server configuration",
   "Static sites are fundamentally incapable of being hosted on the actual public internet, and can technically only ever be viewed by opening the raw HTML file directly on the specific computer that originally created it"
 ],
 "answer": 0,
 "explanation": "Static sites serve pre-built HTML with no per-request server processing, which tends to make them fast and simple to host securely — but showing personalised, frequently changing, or per-user content requires extra tooling (client-side JavaScript fetching data, or partial regeneration), which a dynamic, server-rendered site handles more naturally at the cost of needing server-side processing for every request."
},
{
 "q": "A team rolls out a new version of their application by deploying it fully to an entirely separate, identical set of servers first, testing it there, then instantly switching all live traffic over to the new servers — keeping the old servers running and ready in case they need to switch back immediately. What deployment strategy is this?",
 "options": [
   "Blue-green deployment — running two identical production environments, deploying and testing a new version on the idle one, then switching traffic over instantly, with the old environment kept ready for an immediate rollback if needed",
   "A canary release — gradually rolling a new version out to a small percentage of users first before expanding to everyone, a related but distinct strategy from switching 100% of traffic between two complete environments at once",
   "Continuous integration — automatically building and testing every code change as it's committed, a practice about the build/test pipeline rather than about how traffic is switched between two live production environments",
   "Infrastructure as code — defining server configuration as version-controlled files, a practice about how infrastructure is defined and provisioned rather than about how live traffic is switched between two environments"
 ],
 "answer": 0,
 "explanation": "Blue-green deployment keeps two complete, identical production environments, deploying and verifying the new version on the currently idle one before switching all traffic over instantly — offering a very fast rollback (just switch traffic back) if something goes wrong, a different risk-management strategy from a gradual canary rollout to a subset of users."
},
{
 "q": "A large system made of many microservices adds a dedicated infrastructure layer that automatically handles retries, encryption, and monitoring for all the network calls between services, without each individual service needing to implement that logic itself. What is this infrastructure layer generally called?",
 "options": [
   "A service mesh — a dedicated infrastructure layer handling cross-cutting concerns like retries, encryption, and monitoring for service-to-service communication, so individual services don't each need to implement this logic themselves",
   "An API gateway — a single entry point that routes external client requests to the appropriate backend service, a related but distinct concept focused on external-facing traffic rather than internal service-to-service communication",
   "A load balancer — a component distributing incoming requests across multiple servers, a narrower concept about traffic distribution rather than about handling retries, encryption, and monitoring for internal service communication",
   "A CDN — a geographically distributed network of servers caching static content close to users, a concept about serving static content quickly rather than about managing internal communication between backend microservices"
 ],
 "answer": 0,
 "explanation": "A service mesh specifically handles cross-cutting service-to-service communication concerns — retries, encryption, monitoring, traffic routing between internal services — centrally, so individual microservices don't each need to reimplement that logic, which becomes increasingly valuable as the number of services (and the complexity of their interactions) grows."
},
{
 "q": "A company's system has a single, well-defined entry point that all external client requests pass through first, which handles authentication, routes each request to the correct backend microservice, and can apply rate limiting consistently across all of them. What is this component called?",
 "options": [
   "An API gateway — a single entry point that handles concerns like authentication, request routing, and rate limiting for external client requests before they reach the appropriate backend microservice",
   "A service mesh — an infrastructure layer specifically focused on handling communication concerns between internal backend services, a related but distinct concept from managing external client-facing request entry",
   "DNS — a system for translating human-readable domain names into numeric IP addresses, a naming-resolution concept unrelated to authenticating, routing, and rate-limiting incoming external client requests",
   "A CDN — a geographically distributed network of servers caching static content close to users, a concept about serving cached static content quickly rather than about authenticating and routing dynamic API requests"
 ],
 "answer": 0,
 "explanation": "An API gateway sits at the external-facing edge of a system, giving one consistent place to handle authentication, routing to the right backend service, and rate limiting — distinct from a service mesh, which handles the internal communication between backend services after a request has already been routed inside the system."
},
{
 "q": "A load balancer periodically sends a small test request to each server in its pool and automatically stops routing traffic to any server that fails to respond correctly, until that server recovers. What is this periodic check called, and why does it matter?",
 "options": [
   "A health check — a periodic automated check confirming a server is actually working correctly, letting infrastructure automatically route traffic away from failing servers rather than continuing to send real user requests to something broken",
   "A merge conflict — a situation where version control can't automatically reconcile two developers' changes to the same file, a concept about source code collaboration rather than about ongoing server-availability monitoring",
   "A race condition — a bug where the outcome of concurrently running operations depends on unpredictable timing, a concept about a running program's internal correctness rather than about ongoing server-availability monitoring",
   "A merge conflict and a health check are simply two different names for exactly the same underlying technical concept, with no meaningful distinction between what each one actually describes or checks"
 ],
 "answer": 0,
 "explanation": "Health checks let infrastructure automatically detect a failing or unresponsive server and stop routing real user traffic to it, rather than users experiencing errors while an operator manually notices and intervenes — a foundational, largely invisible piece of what keeps a system reliable even when individual servers occasionally fail."
},
{
 "q": "A production system logs messages at different severity levels — DEBUG for fine-grained development detail, INFO for normal operation, WARNING for concerning-but-not-broken situations, and ERROR for actual failures — and in production, only WARNING and above are actually stored and reviewed. What is the reasoning behind filtering by severity level like this?",
 "options": [
   "It keeps log volume manageable and lets engineers focus on genuinely important signals in production, while still allowing DEBUG-level detail to be temporarily enabled when actively investigating a specific issue",
   "Log severity levels have no genuine practical purpose beyond an arbitrary labelling convention, and filtering logs by severity provides no real benefit to how efficiently a production issue can actually be diagnosed",
   "DEBUG-level logs are technically impossible to generate at all once an application has been deployed to a real production environment, which is the actual underlying reason only higher severity levels are ever stored there",
   "Severity-level filtering exists solely to satisfy a formal legal or regulatory record-keeping requirement, with no genuine connection to how efficiently a real production issue can actually be found and diagnosed"
 ],
 "answer": 0,
 "explanation": "Filtering by severity keeps log volume manageable in production, where storing every fine-grained DEBUG message from a busy live system would be both expensive and would bury genuinely important signals — while still allowing that finer detail to be temporarily enabled specifically when actively debugging a particular issue that needs it."
},
{
 "q": "A team stores their database credentials and API keys in a dedicated secrets-management tool rather than in environment variables set directly on each server, gaining the ability to rotate a leaked credential instantly across every service using it, and to audit exactly which service accessed which secret and when. What does this additional layer provide beyond basic environment variables?",
 "options": [
   "Centralised control, auditability, and easier rotation of sensitive credentials across many services, compared to secrets scattered as environment variables across many individually configured servers",
   "Centralised secrets management provides no genuine practical benefit whatsoever over environment variables, and the two approaches are considered functionally and practically identical by security-conscious engineering teams",
   "It makes it technically impossible for any credential to ever be leaked or compromised under any circumstances, since dedicated secrets-management tools are mathematically guaranteed to be completely unbreachable",
   "It eliminates the need for any service to ever authenticate to a database at all, since secrets-management tools are specifically designed to remove the requirement for any credential to exist anywhere in the system"
 ],
 "answer": 0,
 "explanation": "Dedicated secrets management adds centralised control, auditability (who accessed what secret, when), and much faster rotation when a credential does leak — genuine practical advantages over environment variables scattered individually across many servers, though no tool makes a system unbreachable or removes the fundamental need for credentials to exist somewhere."
},
{
 "q": "An automated tool scans a project's dependencies and flags that a library three levels deep in the project's dependency tree has a known, publicly disclosed security vulnerability, even though the development team never directly chose to include that specific library themselves. What does this illustrate about modern software dependency risk?",
 "options": [
   "Modern applications often depend on many indirect (transitive) dependencies beyond what a team directly chose, so a vulnerability deep in that dependency tree can affect a project the team never even knew was using that specific library",
   "This kind of automated dependency scanning is purely theoretical and does not reflect any genuine real-world risk, since a vulnerability in an indirectly included library can never actually affect an application using it",
   "Only libraries a development team directly and explicitly chose to include in their project can ever realistically pose any security risk, making indirect, transitive dependencies inherently safe by default in every case",
   "This scenario proves that using any external library at all, whether direct or indirect, is always a fundamentally worse security choice than writing every single piece of functionality entirely from scratch in-house"
 ],
 "answer": 0,
 "explanation": "Modern software commonly depends on a large, often surprisingly deep tree of indirect (transitive) dependencies beyond what a team explicitly chose — a vulnerability anywhere in that tree can genuinely affect the final application, which is exactly why automated dependency scanning tools have become a standard, practical part of many teams' security practice, rather than a purely theoretical concern."
},
{
 "q": "A team building an internal admin tool used only by twelve trusted employees, versus a team building a public-facing e-commerce checkout used by millions of anonymous strangers, would reasonably apply very different levels of security rigor and different priorities. What does this illustrate about how security and engineering decisions should generally be made?",
 "options": [
   "Sound engineering and security decisions should be proportionate to actual risk and context, since the same level of investment that's appropriate for a public system handling millions of strangers' payment details may be genuinely excessive for a small internal tool",
   "Every single software system, regardless of its actual number of users, its exposure to the public internet, or the sensitivity of the data involved, should always be built to exactly the same fixed, universal standard of rigor",
   "Internal tools used by a small number of trusted employees should always receive strictly greater security investment than any public-facing system, since employees are inherently more likely to misuse a system than any random stranger",
   "Security and engineering rigor should be determined entirely at random for any given project, since there is no genuine, meaningful relationship between a system's actual risk profile and how much investment it reasonably deserves"
 ],
 "answer": 0,
 "explanation": "Proportionate, risk-based decision-making is a core practical engineering principle: the appropriate level of security investment, testing rigor, and infrastructure complexity genuinely depends on context — user count, exposure, and data sensitivity — rather than applying one fixed universal standard regardless of what's actually at stake for that specific system."
},
{
 "q": "A junior developer wonders whether to pursue a traditional computer science degree or an intensive coding bootcamp to break into the tech industry. What is the most balanced, accurate way to frame the real tradeoff between these two paths?",
 "options": [
   "A CS degree typically offers deeper theoretical grounding over a longer time and cost, while a bootcamp typically offers faster, more focused practical skills for a narrower target role — neither path guarantees success, and many successful developers come from each",
   "A coding bootcamp is always strictly and unconditionally superior to a traditional computer science degree in every practical respect, for literally any specific career path or role within the entire tech industry",
   "A traditional computer science degree is always strictly and unconditionally superior to any coding bootcamp in every practical respect, for literally any specific career path or role within the entire tech industry",
   "Neither a computer science degree nor a coding bootcamp has ever produced a single successful, employed professional software developer, making both paths considered equally and completely nonviable by the industry"
 ],
 "answer": 0,
 "explanation": "The honest framing is a genuine tradeoff rather than one path being universally superior: a CS degree generally offers deeper theoretical foundations over more time and cost, while a bootcamp generally offers faster, narrower, practically-focused skills — the right choice depends on an individual's goals, circumstances, and target role, and real successful developers come from both paths, as well as from self-teaching."
},
{
 "q": "A database schema change (adding a new required column to an existing table with millions of rows) is written as a versioned, repeatable script that can be run automatically and consistently across every environment — development, staging, and production — rather than someone manually running SQL commands by hand in each place separately. What is this practice called?",
 "options": [
   "Database migrations — versioned, repeatable scripts that apply schema changes consistently and automatically across environments, avoiding the risk and inconsistency of manually applying the same change by hand in each place",
   "Database sharding — splitting a large dataset across multiple database servers, a technique about horizontal scalability rather than about how a schema change itself is applied consistently across different environments",
   "Database replication — maintaining multiple synchronised copies of a database across servers or regions, a technique about fault tolerance and read performance rather than about how a schema change is initially applied",
   "Database indexing — creating a data structure that speeds up lookups within a database, a technique about query performance rather than about how a structural schema change is applied consistently across environments"
 ],
 "answer": 0,
 "explanation": "Database migrations are versioned, repeatable scripts specifically designed to apply schema changes consistently and automatically across every environment, avoiding both the risk of manual human error and the inconsistency of someone running slightly different commands by hand in development versus production."
},
{
 "q": "A developer writes application code that works with data as regular objects (like a `User` object with a `.save()` method), while a separate library automatically translates those object operations into the actual SQL queries needed to read from and write to the underlying relational database. What is this kind of library called?",
 "options": [
   "An ORM (Object-Relational Mapper) — a library that translates between an application's object-oriented code and a relational database's table-based structure, letting developers work with familiar objects instead of writing raw SQL by hand",
   "A CDN — a geographically distributed network of servers caching static content close to users, a concept about serving cached content quickly rather than about translating object code into database queries",
   "A service mesh — an infrastructure layer handling communication concerns between internal backend services, a concept about network-level service communication rather than about object-to-database translation",
   "A load balancer — a component distributing incoming requests across multiple servers, a concept about spreading network traffic rather than about translating application objects into the equivalent underlying SQL queries"
 ],
 "answer": 0,
 "explanation": "An ORM bridges the gap between an application's object-oriented code and a relational database's table-based structure, automatically translating operations like `.save()` on a `User` object into the equivalent SQL — genuinely convenient for common cases, though understanding the underlying SQL still matters for performance-sensitive or unusual queries an ORM might handle inefficiently."
},
{
 "q": "A developer chooses variable names like `daysUntilExpiry` and `calculateMonthlyInterest()` instead of vague names like `x` and `doStuff()`, even though both would technically run identically. What is the primary practical benefit of this choice?",
 "options": [
   "Readable, descriptive naming makes code significantly easier for other developers (and the original author, months later) to understand, maintain, and safely modify, even though it has no effect on how the code actually executes",
   "Descriptive variable and function names make a program run measurably faster at runtime, since the computer itself is able to process shorter, more meaningful names more efficiently than longer, vaguer ones",
   "This naming choice is purely a matter of arbitrary personal aesthetic preference with absolutely no practical, measurable impact whatsoever on how maintainable, readable, or safely modifiable any codebase actually is",
   "Using descriptive names like this is technically required by every programming language's compiler or interpreter, and code using vague names like `x` will simply fail to run or compile in any language at all"
 ],
 "answer": 0,
 "explanation": "Descriptive naming has no effect on runtime execution — the computer doesn't care whether a variable is called `x` or `daysUntilExpiry` — but it has a very real effect on human readability and maintainability, which matters enormously given how much more time is typically spent reading and modifying existing code than writing new code from scratch."
},
{
 "q": "A team writing a complex algorithm first sketches out its logic in plain, structured, informal language — 'for each item in the list, if the price is above the threshold, add it to the results' — before translating it into actual code in their chosen programming language. What is this informal planning step called?",
 "options": [
   "Pseudocode — an informal, structured way of describing an algorithm's logic in plain language before (or instead of) writing it in an actual programming language's precise syntax",
   "A design pattern — a general, reusable, well-documented solution to a commonly recurring software design problem, a broader architectural concept rather than a specific informal step-by-step description of one algorithm's logic",
   "A merge conflict — a situation where version control can't automatically reconcile two developers' changes to the same file, a concept about source-code collaboration rather than about planning an algorithm's logic informally",
   "Technical debt — a buildup of shortcuts taken for short-term development speed, a concept about accumulating long-term cost rather than about informally planning an algorithm's logic before writing actual code"
 ],
 "answer": 0,
 "explanation": "Pseudocode lets a developer plan and reason about an algorithm's logic in plain, structured language before committing to a specific programming language's exact syntax — useful for catching logical errors early, communicating an approach to others, and separating 'what should this do' from 'how do I write this in this specific language'."
},
{
 "q": "A program running on a computer with multiple CPU cores splits a large image-processing task into four independent pieces and processes all four simultaneously on separate cores, finishing roughly four times faster than processing them one after another. What does this illustrate?",
 "options": [
   "Parallelism — genuinely executing multiple independent pieces of work at the exact same time using multiple processing cores, distinct from concurrency, which can interleave multiple tasks on a single core without true simultaneous execution",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept about a single function's control flow rather than about distributing independent work across multiple CPU cores",
   "A race condition — a bug where the outcome of concurrently running operations depends on unpredictable timing, a description of an unintended bug rather than of a deliberate, correctly designed performance optimisation",
   "A memory leak — memory that is allocated but never properly released by a running program, a concept about a program's memory management rather than about deliberately splitting work across multiple CPU cores for speed"
 ],
 "answer": 0,
 "explanation": "True parallelism means multiple independent pieces of work genuinely execute at the same time across multiple processing cores — a meaningfully different concept from concurrency, which can make progress on multiple tasks by interleaving them even on a single core without literal simultaneous execution, though the two are often discussed together and can be combined."
},
{
 "q": "A team building a healthcare scheduling app for a rural Nigerian clinic with unreliable internet designs the app to keep working with locally cached data when the connection drops, syncing changes once connectivity returns, rather than simply showing an error and becoming unusable offline. What does this design choice reflect about building software for real-world African contexts?",
 "options": [
   "Designing for actual local constraints (like unreliable connectivity) rather than assuming ideal, always-on conditions leads to software that's genuinely usable by its real intended users, not just usable in a well-connected demo environment",
   "This kind of offline-tolerant design is purely a theoretical best practice with no genuine real-world relevance to how software is actually built and deployed for use in African markets specifically",
   "Building for unreliable connectivity conditions is technically impossible for any software application to achieve, regardless of how much deliberate engineering effort a development team invests in the attempt",
   "Rural clinics in Nigeria specifically have no meaningful practical need for any digital scheduling software at all, making this entire hypothetical design scenario fundamentally irrelevant to real healthcare delivery"
 ],
 "answer": 0,
 "explanation": "Designing for the actual conditions users will really experience — like unreliable connectivity, common in many real deployment contexts including rural Nigerian clinics — rather than assuming ideal always-on conditions, is what makes the difference between software that only works in a comfortable demo and software that's genuinely usable and valuable for its real intended users."
},
{
 "q": "Which of the following are genuine, practical benefits of writing automated tests for a codebase? Select all that apply.",
 "options": [
   "Catching a regression (a previously working feature breaking) automatically when a new change is introduced",
   "Giving developers more confidence to refactor or restructure code, since tests will flag if the refactor breaks existing behaviour",
   "Guaranteeing that a tested codebase will never contain any bugs whatsoever, under any possible circumstance",
   "Serving as a form of executable documentation showing how a piece of code is actually expected to behave"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Catching regressions, enabling more confident refactoring, and serving as executable documentation are all genuine, well-established benefits of automated testing. The claim about guaranteeing zero bugs is false — tests only check what they were actually written to check, and a codebase can still contain bugs in scenarios its test suite simply never covers."
},
{
 "q": "Which of the following would count as genuinely reducing 'technical debt' in a codebase, as the term is generally used in software engineering? Select all that apply.",
 "options": [
   "Refactoring a confusing, hastily-written module into cleaner, better-structured code without changing its external behaviour",
   "Writing tests for a critical piece of previously untested code, so future changes to it are safer",
   "Adding a brand new, unrelated feature to the product that has no connection to any existing shortcut or quality issue",
   "Updating an outdated dependency that's been causing recurring integration problems across the team"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "Refactoring messy code, adding tests to risky untested areas, and updating a problematic outdated dependency are all genuine examples of paying down technical debt — improving the underlying quality or safety of existing code. Adding an unrelated new feature doesn't address any existing shortcut or quality issue, so it doesn't reduce technical debt even though it's valuable work in its own right."
},
{
 "q": "A function always returns the exact same output for the exact same input, and never modifies any data outside itself (no changing a global variable, no writing to a file). What is this kind of function called, and why do many developers consider it easier to reason about?",
 "options": [
   "A pure function — given the same input, it always produces the same output with no side effects, making it easier to test, predict, and reason about in isolation from the rest of the program's state",
   "A recursive function — a function that calls itself on a smaller version of the same problem, a concept about a function's internal control flow rather than about whether it has side effects or predictable output",
   "An asynchronous function — a function whose execution can pause and resume without blocking the rest of the program, a concept about timing and execution order rather than about side effects or output predictability",
   "A pure function and a recursive function are simply two different names referring to the exact same underlying programming concept, with no meaningful distinction between the two terms"
 ],
 "answer": 0,
 "explanation": "Pure functions — same input always produces the same output, with no side effects on anything outside the function — are easier to test in isolation and reason about, since understanding their behaviour doesn't require tracking the broader, potentially changing state of the rest of the program the way a function with side effects does."
},
{
 "q": "A function called `applyDiscount` takes another function as one of its arguments, letting the caller plug in different discount logic (10% off, flat ₦500 off, buy-one-get-one) without `applyDiscount` itself needing to know the specific details of each discount type. What is this pattern called?",
 "options": [
   "A higher-order function — a function that takes another function as an argument (or returns one), enabling flexible, reusable logic without the outer function needing to know the specific details of the behaviour passed in",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept about a function calling itself rather than about a function accepting another function as an argument",
   "Polymorphism — an object-oriented programming concept where the same method name behaves differently depending on the specific object it's called on, a concept from a different programming paradigm than this scenario describes",
   "A pure function — a function that always produces the same output for the same input with no side effects, a concept about output predictability rather than specifically about accepting another function as an argument"
 ],
 "answer": 0,
 "explanation": "Higher-order functions accept other functions as arguments (or return functions), which lets code like `applyDiscount` stay generic and reusable — the caller supplies the specific discount logic as a plugged-in function, without the outer function needing to hardcode or know about every possible discount type in advance."
},
{
 "q": "A function defined inside another function 'remembers' a variable from its enclosing function's scope even after that outer function has already finished running and returned. What is this behaviour called?",
 "options": [
   "A closure — an inner function retaining access to variables from its enclosing function's scope, even after the outer function has finished executing, letting that inner function 'carry' state along with it",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept about repeated self-calling rather than about an inner function remembering an outer function's variables",
   "A pure function — a function that always produces the same output for a given input with no side effects, a concept about output predictability rather than about retaining access to an outer function's variables after it returns",
   "Polymorphism — an object-oriented concept where the same method name behaves differently depending on the specific object it's called on, a concept unrelated to an inner function retaining access to an outer function's variables"
 ],
 "answer": 0,
 "explanation": "A closure is created when an inner function retains access to variables from its enclosing (outer) function's scope, even after that outer function has already returned — a powerful and common pattern used for things like maintaining private state, creating specialised functions on the fly, and callback-based event handling."
},
{
 "q": "A web page attaches a function to run automatically whenever a specific button is clicked, rather than the page checking every fraction of a second whether the button has been clicked. What programming style does this reflect, and what is the attached function commonly called?",
 "options": [
   "Event-driven programming — code reacts to specific triggering events (like a click) rather than continuously polling for them; the attached function that runs in response is commonly called a callback (or event handler)",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept about self-calling functions rather than about code reacting automatically to a triggering user event",
   "Object-oriented programming — a programming paradigm organising code into classes and objects, a broader structural paradigm distinct specifically from the practice of reacting automatically to a triggering event like a click",
   "A pure function — a function that always produces the same output for a given input with no side effects, a concept about output predictability rather than about code that reacts automatically to a triggering user event"
 ],
 "answer": 0,
 "explanation": "Event-driven programming structures code around reacting to events (clicks, key presses, network responses) as they happen, rather than continuously checking in a loop whether something has occurred — the function attached to respond to a specific event is commonly called a callback or event handler, a foundational pattern in interactive web development."
},
{
 "q": "A function fetching data from a slow external API doesn't freeze the rest of the web page while waiting for the response — the page stays fully interactive, and the fetched data is handled once it actually arrives. What programming concept enables this kind of non-blocking behaviour?",
 "options": [
   "Asynchronous programming (using constructs like promises or async/await) — letting a slow operation run in the background without freezing the rest of the program, with a defined way to handle the result once it's ready",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept about repeated self-calling rather than about a slow operation running without freezing the rest of a program",
   "Polymorphism — an object-oriented concept where the same method name behaves differently depending on the specific object it's called on, a concept unrelated to how a program handles a slow, non-blocking network operation",
   "A pure function — a function that always produces the same output for a given input with no side effects, a concept about output predictability rather than about non-blocking handling of a slow external operation"
 ],
 "answer": 0,
 "explanation": "Asynchronous programming lets a slow operation (like a network request) proceed in the background without blocking the rest of the program, with promises or async/await providing a structured way to define what should happen once the result actually becomes available — essential for keeping an interface responsive while waiting on inherently slow operations like network calls."
},
{
 "q": "A search algorithm looking for a specific name in an already-sorted list of a million names repeatedly checks the middle element and discards half the remaining list each time, finding the target in about 20 comparisons instead of potentially a million. What algorithm is this, and what does it require of the input?",
 "options": [
   "Binary search — repeatedly halving the search space by checking the middle element, achieving far fewer comparisons than checking every element one by one, but it specifically requires the input list to already be sorted",
   "A hash table lookup — mapping a key directly to a value using a hash function, a genuinely different technique that doesn't rely on repeatedly halving a sorted list's remaining search space at each comparison step",
   "Bubble sort — an algorithm for putting an unsorted list into order by repeatedly comparing and swapping adjacent elements, a sorting algorithm rather than a search algorithm for finding one specific target value",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a general technique that could implement binary search but isn't itself the name of the search algorithm"
 ],
 "answer": 0,
 "explanation": "Binary search dramatically reduces the number of comparisons needed by repeatedly halving the remaining search space — but this only works because the list is already sorted, letting the algorithm safely discard half the remaining elements at each step based on a single comparison with the middle element."
},
{
 "q": "A developer optimises a rarely-used, non-performance-critical part of an application, spending a full week making it marginally faster, while a genuinely slow, frequently-used core feature remains unoptimised. What common software engineering pitfall does this illustrate?",
 "options": [
   "Premature (or misdirected) optimisation — spending effort optimising something that doesn't meaningfully matter for real-world performance, rather than first identifying and focusing on the areas that actually affect users most",
   "Technical debt — a buildup of shortcuts taken for short-term development speed that create ongoing maintenance costs, a distinct concept about accumulated shortcuts rather than about misdirected optimisation effort",
   "A race condition — a bug where the outcome of concurrently running operations depends on unpredictable timing, a concept about program correctness rather than about how a developer chooses to spend their optimisation effort",
   "A merge conflict — a situation where version control can't automatically reconcile two developers' changes to the same file, a concept about source-code collaboration rather than about how optimisation effort is prioritised"
 ],
 "answer": 0,
 "explanation": "This illustrates the classic pitfall of premature or misdirected optimisation — investing real effort into speeding up something that doesn't actually matter much for real-world performance, instead of first measuring (profiling) to find out where the genuine bottlenecks actually are, which is usually a small, frequently-used part of the system rather than an obscure corner."
},
{
 "q": "A team debates whether to build a highly configurable, general-purpose reporting engine 'in case we need it someday', versus building just the specific report their current customers are actually asking for right now. Which principle argues for building only what's currently needed?",
 "options": [
   "YAGNI ('You Aren't Gonna Need It') — a principle advising against building speculative functionality for hypothetical future needs, since that effort often turns out to be wasted or built in the wrong shape once the real need actually arrives",
   "DRY (Don't Repeat Yourself) — a principle specifically about avoiding duplicated code within a single codebase, a distinct concept from whether a team should build speculative, general-purpose functionality ahead of actual need",
   "The testing pyramid — a strategy for structuring a team's automated tests into layers of unit, integration, and end-to-end tests, a concept unrelated to whether a team should build speculative functionality ahead of actual need",
   "Technical debt — a buildup of shortcuts taken for short-term development speed, a concept about accumulated shortcuts rather than about a deliberate choice to avoid building speculative, not-yet-needed functionality"
 ],
 "answer": 0,
 "explanation": "YAGNI specifically cautions against building speculative functionality for imagined future needs, since that effort is often wasted — either the imagined need never actually materialises, or when it does, the real requirements turn out different enough that the speculative work built earlier doesn't even fit well, making 'build what's actually needed now' the generally safer default."
},
{
 "q": "Two developers sit together at one computer, one actively writing code while the other reviews each line in real time, watches for mistakes, and thinks about edge cases — then they periodically swap roles. What is this practice called, and what is its main benefit over one person coding entirely alone?",
 "options": [
   "Pair programming — two developers actively collaborating on the same code in real time, catching mistakes and design issues immediately as they're introduced, rather than only later during a separate, delayed code review",
   "Code review — a process where completed, already-written code changes are reviewed asynchronously after the fact, a related but distinct practice from two developers actively writing code together in real time on one machine",
   "The testing pyramid — a strategy for structuring a team's automated tests into layers of unit, integration, and end-to-end tests, a concept unrelated to two developers actively collaborating on the same code together in real time",
   "A merge conflict — a situation where version control can't automatically reconcile two developers' separately made changes to the same file, a concept unrelated to two developers deliberately writing the exact same code together"
 ],
 "answer": 0,
 "explanation": "Pair programming catches mistakes and design issues in real time, as code is actually being written, rather than discovering them later in a separate, delayed code review — a genuinely different practice from asynchronous code review, though both share the underlying goal of catching problems before they reach production."
},
{
 "q": "After a major outage, instead of simply fixing the immediate symptom and moving on, a team holds a structured meeting to trace the failure back through every contributing factor — the original code change, the missing test, the alert that didn't fire — and documents what will change to prevent a similar failure in the future. What is this process called?",
 "options": [
   "A postmortem (or root cause analysis) — systematically tracing an incident back to its true underlying contributing causes, rather than only fixing the immediate visible symptom, so similar failures can genuinely be prevented in future",
   "A code review — a process where completed code changes are reviewed by teammates before being merged, a distinct practice focused on reviewing new code rather than on analysing the causes of a past incident that already occurred",
   "A canary release — gradually rolling a new version out to a small percentage of users first, a deployment strategy rather than a structured process for retrospectively analysing the causes of a past incident that already occurred",
   "A merge conflict — a situation where version control can't automatically reconcile two developers' changes to the same file, a routine source-control situation rather than a structured process for analysing a major past incident"
 ],
 "answer": 0,
 "explanation": "A postmortem (or root cause analysis) deliberately looks past the immediate symptom to trace the full chain of contributing factors behind an incident, aiming to genuinely prevent recurrence rather than just patching what broke this one time — a practice increasingly treated as blameless (focused on systemic fixes, not individual blame) in mature engineering teams."
},
{
 "q": "A daily 15-minute team meeting has each person briefly answer three questions: what did I do yesterday, what will I do today, and is anything blocking me. What is this short meeting called, and what is its primary purpose?",
 "options": [
   "A daily standup — a brief, regular check-in surfacing progress and blockers quickly, helping the team stay coordinated and catch problems early, without requiring a long, formal status meeting",
   "A postmortem — a structured, in-depth meeting for tracing a past incident back to its true root causes, a fundamentally different kind of meeting from a brief, daily, forward-looking progress check-in",
   "A code review — a process where a teammate reads through completed proposed code changes before they are merged, a distinct activity from a brief, verbal, daily team progress and blockers check-in meeting",
   "A canary release — a deployment strategy for gradually rolling a new software version out to a small percentage of users first, a technical deployment concept entirely unrelated to any kind of team meeting"
 ],
 "answer": 0,
 "explanation": "A daily standup is a short, focused check-in meant to surface progress and blockers quickly across a team, helping coordination and catching problems (like someone being stuck) early — deliberately kept brief to avoid becoming a long, unfocused status meeting that eats into actual working time."
},
{
 "q": "A class's internal implementation detail — like exactly how it stores a list of items internally — is hidden from other code, which can only interact with it through a defined set of public methods, regardless of how the internal storage might change later. What object-oriented principle does this describe?",
 "options": [
   "Encapsulation — bundling data and the methods that operate on it together while restricting direct outside access to internal details, letting the internal implementation change freely without breaking code that only uses the public methods",
   "Polymorphism — the same method name behaving differently depending on the specific object it's called on, a concept about method behaviour varying by object type rather than about hiding a class's internal implementation details",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept unrelated to whether a class's internal implementation details are hidden from other code",
   "Inheritance — one class acquiring the properties and behaviours of another parent class, a concept about class relationships rather than specifically about hiding a class's own internal implementation details from outside code"
 ],
 "answer": 0,
 "explanation": "Encapsulation hides a class's internal implementation details behind a defined public interface, which means the internal storage or logic can change later without breaking any other code that only ever interacted with the public methods — a key reason well-encapsulated code tends to be easier to safely modify and maintain over time."
},
{
 "q": "A `Car` class inherits from a more general `Vehicle` class, automatically gaining shared properties like `speed` and methods like `accelerate()`, while adding car-specific details like `numberOfDoors` on top. What object-oriented principle does this relationship describe, and what is one commonly cited risk of overusing it?",
 "options": [
   "Inheritance — a class acquiring properties and behaviours from a more general parent class; overused or deeply nested inheritance hierarchies can become rigid and hard to safely modify as a codebase grows more complex",
   "Encapsulation — bundling a class's data and methods together while restricting direct outside access, a concept about hiding internal details rather than about one class acquiring shared properties from a more general parent class",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept unrelated to how one class might acquire shared properties and behaviours from a more general parent class",
   "A pure function — a function that always produces the same output for the same input with no side effects, a concept about function behaviour rather than about a relationship between two related classes like Car and Vehicle"
 ],
 "answer": 0,
 "explanation": "Inheritance lets a class reuse and extend a more general parent class's properties and behaviours — genuinely useful for avoiding duplication, but a commonly cited real risk is that deep or overused inheritance hierarchies can become rigid and fragile, which is part of why many modern designs favour composition (combining smaller, focused pieces) over deep inheritance in many situations."
},
{
 "q": "A payment-processing function needs access to a database connection, but instead of creating that connection itself inside the function, the connection is created elsewhere and passed in as a parameter when the function is called. What design principle does this illustrate, and what is its main benefit for testing?",
 "options": [
   "Dependency injection — supplying a component's dependencies from outside rather than having it create them internally, which makes it far easier to substitute a fake or mock dependency during automated testing",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept unrelated to whether a function's dependencies are created internally or supplied from outside",
   "Polymorphism — an object-oriented concept where the same method name behaves differently depending on the specific object it's called on, a concept unrelated to how a function's dependencies are supplied to it",
   "A pure function — a function that always produces the same output for the same input with no side effects, a concept about output predictability rather than about how a function's dependencies are supplied to it"
 ],
 "answer": 0,
 "explanation": "Dependency injection supplies a component's dependencies (like a database connection) from outside rather than having the component create them internally, which makes automated testing much easier — a test can inject a fake, controllable database connection instead of needing a real one, letting the payment logic be tested in isolation."
},
{
 "q": "A large e-commerce site's homepage takes noticeably longer to become visually complete and interactive than a competitor's homepage with similar content, and an engineer traces the delay to render-blocking scripts loaded in the page's head section before any visible content appears. What browser concept is this engineer investigating?",
 "options": [
   "The critical rendering path — the sequence of steps a browser takes to convert HTML, CSS, and JavaScript into visible pixels on screen, where render-blocking resources loaded early can delay when a page first becomes visible",
   "CORS — a browser security mechanism restricting cross-domain JavaScript requests by default, a security-focused concept unrelated to how quickly a page's visible content actually renders on screen after loading begins",
   "DNS — a system for translating human-readable domain names into numeric IP addresses, a naming-resolution concept that happens before a page begins loading at all, unrelated to render-blocking scripts within the page itself",
   "A webhook — a mechanism for one system to automatically notify another the moment a specific event occurs, a backend integration concept unrelated to how quickly a webpage's own visible content renders in a user's browser"
 ],
 "answer": 0,
 "explanation": "The critical rendering path describes the specific sequence a browser follows to turn HTML, CSS, and JavaScript into visible content — resources that block this path (like large scripts loaded before any content, without a non-blocking attribute) directly delay when a user first sees anything, which is exactly the kind of performance issue front-end engineers specifically optimise for."
},
{
 "q": "A team estimates a new feature will take roughly one week based on a similar feature they built previously, but they explicitly note the estimate assumes no major surprises in an unfamiliar part of the codebase they haven't touched before. Three weeks later, they're still finishing it. What does this illustrate about software estimation in general?",
 "options": [
   "Software estimation is inherently uncertain, especially for unfamiliar territory, since unknowns (hidden complexity, unexpected edge cases, unfamiliar code) are, by definition, hard to fully anticipate in advance — a well-documented, common pattern across the industry",
   "This specific team must simply be unusually bad at estimating, since accurate, reliable software estimation is generally a fully solved, entirely predictable problem for any reasonably competent development team",
   "Software estimates should never include any explicit caveats or stated assumptions, since caveats themselves are what directly causes an estimate to end up being inaccurate later on",
   "The three-week actual duration definitively proves the original one-week estimate must have been made completely carelessly, with no genuine underlying reasoning or comparison to any previous similar feature at all"
 ],
 "answer": 0,
 "explanation": "Software estimation is famously and genuinely difficult, especially for work touching unfamiliar territory — unknowns are, almost by definition, hard to fully anticipate before actually encountering them, which is why 'estimates were wrong for unfamiliar work' is such a widely recognised industry pattern rather than a sign of one specific team's unusual incompetence."
},
{
 "q": "A mobile app displays cached data instantly when opened, then quietly fetches the latest data in the background and updates the screen if anything has changed, rather than showing a blank loading screen every single time the app opens. What does this design prioritise for the user, and what is the general pattern called?",
 "options": [
   "Stale-while-revalidate — showing potentially slightly outdated cached data immediately for a fast, responsive feel, while fetching fresh data in the background to update the view once it actually arrives",
   "A race condition — a bug where the outcome of concurrently running operations depends on unpredictable timing, a description of an unintended flaw rather than a deliberately designed, intentional user-experience pattern",
   "A merge conflict — a situation where version control can't automatically reconcile two developers' changes to the same file, a source-control concept entirely unrelated to how a mobile app chooses to display cached versus fresh data",
   "Technical debt — a buildup of shortcuts taken for short-term development speed, a concept about accumulated code-quality cost rather than about a deliberate, intentional strategy for displaying cached versus freshly fetched data"
 ],
 "answer": 0,
 "explanation": "The stale-while-revalidate pattern deliberately trades a small chance of showing briefly outdated data for a much more responsive, instant-feeling experience — showing cached data immediately while quietly fetching and applying fresh data in the background, rather than making every user wait through a loading screen on every single app open."
},
{
 "q": "A backend developer designs an API so that calling the same 'delete user' request multiple times in a row (say, due to a network retry) has the exact same end result as calling it once — the user is deleted, and repeating the call simply confirms they're still gone rather than causing an error or unexpected side effect. What property does this API design have?",
 "options": [
   "Idempotency — an operation that produces the same end result no matter how many times it's repeated with the same input, which matters a great deal for safely handling network retries without unintended side effects",
   "Polymorphism — an object-oriented concept where the same method name behaves differently depending on the specific object it's called on, a concept unrelated to whether repeating the exact same API call causes the same result",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept unrelated to whether repeating the exact same API request produces the same end result each time",
   "A race condition — a bug where the outcome of concurrently running operations depends on unpredictable timing, a description of an unintended flaw rather than a deliberately designed, desirable API safety property"
 ],
 "answer": 0,
 "explanation": "Idempotency means an operation can be safely repeated with the same input without causing unintended additional effects — genuinely important for network reliability, since a client that doesn't receive a response (due to a dropped connection) often has to retry, and an idempotent API ensures that retry doesn't accidentally cause harm, like trying to delete an already-deleted user causing an error."
},
{
 "q": "A developer building a form for Nigerian users specifically supports phone number formats starting with +234 and validates local formatting conventions, rather than only supporting the international format most common in the country the original development team happens to be based in. What practice does this reflect?",
 "options": [
   "Localisation — adapting software to genuinely fit the specific conventions, formats, and expectations of a particular target audience or region, rather than assuming one region's defaults apply universally to every user everywhere",
   "Load balancing — distributing incoming requests across multiple servers, a backend infrastructure concept entirely unrelated to whether a form's phone number validation logic actually fits a specific target user population",
   "Database sharding — splitting a large dataset across multiple database servers, a data-scalability concept entirely unrelated to whether a form's phone number validation logic fits a specific target user population",
   "Containerisation — packaging an application with its exact runtime dependencies into a portable unit, a deployment-packaging concept entirely unrelated to whether a form's validation logic fits a specific target user population"
 ],
 "answer": 0,
 "explanation": "Localisation means genuinely adapting software to fit a specific target audience's real conventions — formats, languages, expectations — rather than assuming the original development team's own regional defaults apply everywhere, which matters a great deal for software that's actually meant to serve users outside wherever it happened to originally be built."
},
{
 "q": "Which of the following are genuine examples of higher-order functions, as the term is used in programming? Select all that apply.",
 "options": [
   "A `filter` function that takes a list and a separate test function, returning only the items for which that test function returns true",
   "A `map` function that takes a list and a separate transformation function, applying that function to every item and returning the transformed results",
   "A function that adds two plain numbers together and returns their sum, taking no other function as an argument at all",
   "A function that returns a brand new function, customised based on a configuration value that was passed into it as an argument"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "`filter` and `map` are classic higher-order functions because they accept another function as an argument, and a function that returns a new customised function also qualifies (higher-order functions can take a function as an argument, return one, or both). A plain function that just adds two numbers, with no function passed in or returned, doesn't meet the definition."
},
{
 "q": "Which of the following are genuine, well-recognised reasons a development team might deliberately choose NOT to add a speculative, general-purpose configuration option 'just in case it's needed later'? Select all that apply.",
 "options": [
   "The extra flexibility adds code complexity and more surface area for bugs, even if it's never actually used",
   "Building the wrong speculative version of a feature can waste time compared to waiting for a real, concrete requirement",
   "Unused speculative code still needs to be maintained and can confuse future developers reading the codebase",
   "It is technically impossible for any codebase to ever contain an unused configuration option under any circumstances"
 ],
 "answer": [0, 1, 2],
 "multi": True,
 "explanation": "Added complexity, the risk of building the wrong speculative thing, and ongoing maintenance burden on unused code are all genuine, commonly cited reasons behind the YAGNI principle. The claim that it's technically impossible for a codebase to contain unused configuration is simply false — unused speculative code accumulating in real codebases is a well-documented, common occurrence, which is precisely the problem YAGNI is trying to prevent."
},
{
 "q": "A data object passed into a function cannot be modified by that function at all — any 'change' actually produces a brand new object, leaving the original completely untouched. What property does this data have, and why might a team deliberately design their data this way?",
 "options": [
   "Immutability — data that cannot be changed after creation; it helps prevent a whole class of bugs where one part of a program unexpectedly modifies data that another part of the program still depends on",
   "Polymorphism — an object-oriented concept where the same method name behaves differently depending on the specific object it's called on, a concept about method behaviour rather than about whether data can be modified after creation",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept about a function's control flow rather than about whether the data it receives can be modified",
   "A race condition — a bug where the outcome of concurrently running operations depends on unpredictable timing, a description of an unintended flaw rather than a deliberately chosen data-design property"
 ],
 "answer": 0,
 "explanation": "Immutable data cannot be changed after creation — any operation that looks like a modification actually produces a new object instead, leaving the original untouched. This deliberately prevents a common class of bugs where one part of a program unexpectedly changes shared data that another part still relies on being unchanged, which becomes especially valuable in concurrent or complex applications."
},
{
 "q": "A team building a job board for Nigerian tech freelancers debates whether to price their premium subscription in Naira or US Dollars, given currency volatility and their target users' actual earning currency. What does this decision primarily illustrate about building products for a specific real market?",
 "options": [
   "Pricing and payment decisions need to reflect the actual economic reality of the target users, not just an arbitrary default, since currency choice genuinely affects both perceived affordability and practical payment friction",
   "Currency choice for a product's pricing has no meaningful effect whatsoever on user adoption or perceived affordability, making this entire consideration essentially irrelevant to the product's actual real-world success",
   "Every digital product aimed at any market anywhere in the world should always be priced in US Dollars by default, regardless of that specific target market's own local currency or actual economic conditions",
   "This kind of pricing and currency decision is purely a legal compliance formality, with no genuine connection to how affordable or accessible real users will actually perceive the resulting product to be"
 ],
 "answer": 0,
 "explanation": "Pricing and currency decisions are a genuine product design choice with real consequences — they affect perceived affordability, payment friction, and trust, and getting them wrong for a specific target market (ignoring local currency reality and volatility) can meaningfully hurt adoption, which is why this kind of decision deserves deliberate consideration rather than defaulting to whatever's most common globally."
},
{
 "q": "A function is written to accept a `Shape` type as a parameter and calls a `.area()` method on it, working correctly whether it's actually given a `Circle`, `Square`, or `Triangle` object, as long as each of those types implements its own `.area()` method. What principle allows this same function to work correctly across genuinely different object types?",
 "options": [
   "Polymorphism — the same method call (`.area()`) behaving correctly across different underlying object types, letting shared code work generically without needing to know the specific concrete type it's dealing with",
   "Recursion — a programming technique where a function calls itself on a smaller version of the same problem, a concept about a function calling itself repeatedly rather than about writing generic code that works across different object types",
   "A race condition — a bug where the outcome of concurrently running operations depends on unpredictable timing, a description of an unintended flaw rather than a deliberately designed feature that lets generic code work across types",
   "A memory leak — memory that is allocated but never properly released by a running program, a concept about a program's memory management rather than about writing generic code that works correctly across different object types"
 ],
 "answer": 0,
 "explanation": "This is polymorphism in action: the function written against the general `Shape` type doesn't need to know or care whether it's actually handling a Circle, Square, or Triangle — as long as each concrete type correctly implements `.area()`, the same generic calling code works correctly across all of them, which is a core reason polymorphism makes code more flexible and extensible."
},
{
 "q": "A developer profiling a slow web page discovers that a single unoptimised database query, run on every page load, accounts for 90% of the page's total load time — everything else combined accounts for the remaining 10%. What does this finding most directly justify?",
 "options": [
   "Focusing optimisation effort specifically on that one slow query first, since fixing the single largest bottleneck will have far more real-world impact than spreading effort evenly across many smaller, less significant factors",
   "Spending equal optimisation effort across every single part of the page equally, since the specific finding that one query accounts for 90% of load time has no real bearing on how effort should actually be prioritised",
   "Rewriting the entire page completely from scratch in a different programming language, since a single slow database query can only ever realistically be fixed by discarding and completely rebuilding the whole page",
   "Concluding that database queries in general are always inherently the single biggest performance bottleneck for absolutely any web page, universally, regardless of that specific page's own actual profiling results"
 ],
 "answer": 0,
 "explanation": "This is the practical payoff of profiling before optimising: once you've measured and found that one specific bottleneck accounts for the vast majority of the slowdown, focusing effort there delivers far more real-world benefit than spreading optimisation effort evenly — a direct, evidence-based application of prioritising the biggest actual impact rather than guessing."
},
{
 "q": "A startup's engineering lead insists every new hire spend their first two days simply reading through and running the existing codebase locally, asking questions, before writing a single line of production code. What is the primary reasoning behind this onboarding approach?",
 "options": [
   "Understanding the existing system's structure, conventions, and reasoning before making changes reduces the risk of a new hire unknowingly introducing bugs or violating established patterns they didn't yet know existed",
   "This approach exists purely as an arbitrary company ritual with no genuine underlying reasoning connected to actually improving a new hire's ability to safely and effectively contribute to the codebase",
   "New hires are, without exception, incapable of contributing any genuinely useful code during their first month at any company, regardless of how much or how little onboarding time they are actually given",
   "Reading through existing code for two full days is required specifically because it is technically impossible to safely and correctly run any codebase locally without having first read through every single line of it"
 ],
 "answer": 0,
 "explanation": "Time spent understanding an existing system's structure and conventions before making changes reduces the real risk of a new hire unknowingly introducing a bug or violating an established pattern they simply didn't know about yet — a genuine, practical tradeoff between a slightly slower initial ramp-up and a meaningfully lower risk of costly early mistakes."
},
{
 "q": "A web application stores a user's authentication token in browser `localStorage`, while a security-conscious alternative implementation stores the same kind of token in an `HttpOnly` cookie that JavaScript running on the page cannot directly read or access at all. Why might the second approach be considered more secure against a certain class of attack?",
 "options": [
   "An HttpOnly cookie can't be read by JavaScript running on the page, meaning malicious JavaScript injected through a cross-site scripting vulnerability can't simply steal the token directly, unlike a token sitting in localStorage",
   "Both approaches are functionally and technically identical from a security standpoint, and the specific choice between storing a token in localStorage versus an HttpOnly cookie makes no meaningful difference whatsoever",
   "localStorage is technically incapable of ever storing any kind of text string, including an authentication token, making the entire premise of storing a token there technically impossible in the first place",
   "HttpOnly cookies are exclusively supported by one single specific web browser, making this security approach entirely impractical and unusable for any application intended to be used by the general public"
 ],
 "answer": 0,
 "explanation": "This is a genuine, practical security distinction: a token in localStorage is directly readable by any JavaScript running on the page, including malicious injected script from a cross-site scripting vulnerability, while an HttpOnly cookie is specifically inaccessible to JavaScript, closing off that particular avenue for a token to be stolen — one real reason security-conscious applications often favour HttpOnly cookies for sensitive session tokens."
},
{
 "q": "A team notices that HTTP/2, unlike the older HTTP/1.1, can send multiple requests over a single connection simultaneously rather than needing a separate connection (or waiting in a queue) for each one. What practical benefit does this multiplexing capability provide for a webpage loading many small resources?",
 "options": [
   "It reduces the overhead and delay associated with opening many separate connections, generally improving load performance for pages that need to fetch many small files like images, stylesheets, and scripts",
   "It has no meaningful practical effect whatsoever on real-world page load performance, and the specific choice between HTTP/1.1 and HTTP/2 makes no measurable difference to how quickly a typical webpage actually loads",
   "It requires every website using it to be rebuilt entirely from scratch using a completely different programming language, since HTTP/2 support cannot technically be added to an already-existing website's backend",
   "It works by physically compressing every image and video file down to a smaller file size, which is the actual specific underlying mechanism by which HTTP/2's multiplexing capability improves page load times"
 ],
 "answer": 0,
 "explanation": "HTTP/2's multiplexing lets many requests share a single connection rather than each needing its own (or waiting behind others in a queue), reducing the overhead of opening and managing many separate connections — a genuine, measurable performance improvement for typical modern pages that load many small resources, distinct from and unrelated to file compression."
},
{
 "q": "A junior developer is confused about the difference between a 'thread' and a 'process' when their senior colleague explains that a web browser typically runs each open tab as a separate process, but within a single tab, multiple threads might handle different tasks concurrently. What is the key distinction being described?",
 "options": [
   "A process has its own isolated memory space (so one tab crashing generally doesn't crash the others), while threads within the same process share that same memory space, making them lighter-weight but requiring more careful coordination",
   "There is no genuine technical distinction between a thread and a process, and browser vendors use the two terms completely interchangeably with no actual difference in how tabs or their internal tasks are structured",
   "A thread always requires significantly more memory and system resources than an entire separate process, which is the specific reason a browser deliberately gives each individual open tab its own dedicated thread instead",
   "Processes can only ever run one single task at any given time under any circumstances, while threads are specifically and exclusively designed to run an unlimited number of tasks fully simultaneously with no limit"
 ],
 "answer": 0,
 "explanation": "A process has its own isolated memory space — which is exactly why one browser tab crashing typically doesn't take down the others — while threads within the same process share that memory space, making them lighter-weight and faster to create, but requiring more careful coordination to avoid issues like race conditions when they access shared data."
},
{
 "q": "A backend engineer decides that a specific internal microservice, used only by two other trusted internal services and never exposed to the public internet, doesn't need the same level of authentication rigor as their public-facing customer API. What principle from earlier discussions about proportionate security also applies directly here?",
 "options": [
   "Security and engineering investment should be proportionate to actual exposure and risk, so a genuinely internal, non-public-facing service reasonably warrants a different (though not necessarily zero) level of rigor than a public API handling untrusted external traffic",
   "Every single internal and external service in a company's entire system must always be secured to the exact identical fixed standard, with absolutely no consideration given to that specific service's actual real-world exposure",
   "Internal services that are never exposed directly to the public internet can safely and reasonably have no authentication requirements of any kind whatsoever, since only genuinely trusted internal services would ever call them",
   "This kind of risk-based reasoning about proportionate security investment is considered an outdated, deprecated engineering practice that modern, well-run engineering teams have now universally abandoned in every case"
 ],
 "answer": 0,
 "explanation": "Proportionate, risk-based security thinking applies here too: a genuinely internal service not exposed to untrusted public traffic reasonably warrants different (generally lighter, though rarely zero, given the reality of insider threats and lateral movement risk) authentication rigor than a public-facing API handling arbitrary external requests — the same underlying principle of matching investment to actual risk, applied to a specific internal-versus-external context."
},
{
 "q": "A team building a Nigerian ride-hailing app needs their route-calculation feature to work reasonably well even when a driver's phone briefly loses signal in an area with patchy network coverage, rather than the whole app becoming unusable. Which combination of concepts discussed earlier would most directly help address this specific requirement? Select all that apply.",
 "options": [
   "Designing for actual local connectivity constraints rather than assuming ideal, always-on conditions",
   "Caching relevant data locally so the app can continue functioning with reasonably current information during a brief connectivity gap",
   "Increasing the app's overall bundle size significantly, since a larger downloaded app is what directly determines whether it can function without a network connection",
   "Relying entirely and exclusively on a live, constantly-connected WebSocket connection for absolutely every single piece of functionality in the app, with no other fallback of any kind"
 ],
 "answer": [0, 1],
 "multi": True,
 "explanation": "Designing deliberately for real local connectivity constraints, combined with local caching to bridge brief connectivity gaps, are genuine, practical approaches to this problem. Bundle size has no direct bearing on offline resilience, and relying entirely on one constantly-connected mechanism with no fallback would make the app more fragile to connectivity gaps, not less."
},
{
 "q": "A responsive website's layout automatically rearranges from a three-column grid on a desktop screen to a single stacked column on a narrow mobile phone screen, using CSS rules that apply different styles depending on the screen's width. What is this technique called?",
 "options": [
   "Responsive design (using media queries) — CSS rules that apply different styling based on characteristics like screen width, letting one single codebase adapt its layout appropriately across a wide range of device sizes",
   "Progressive enhancement — building a baseline experience that works everywhere and layering on enhancements for more capable browsers, a related but distinct concept from specifically adapting a layout's structure to screen width",
   "A CDN — a geographically distributed network of servers caching static content close to users, a concept about serving content quickly from nearby servers rather than about how a page's layout itself adapts to screen size",
   "Server-side rendering — generating a webpage's HTML on the server before sending it to the browser, a concept about where and how HTML is generated rather than about how that page's layout adapts to different screen widths"
 ],
 "answer": 0,
 "explanation": "Responsive design uses techniques like media queries to apply different CSS styling based on characteristics such as screen width, letting a single website codebase automatically adapt its layout appropriately whether it's viewed on a wide desktop monitor or a narrow mobile phone screen, rather than needing entirely separate desktop and mobile versions."
},
]
