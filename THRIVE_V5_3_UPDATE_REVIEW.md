# THRIVE Website v5.3 — Complete Update Review Script

**Prepared by:** Claude (AI assistant)
**Original version:** v5.2
**Updated version:** v5.3
**Review date:** July 2025

---

## Executive Summary

This document summarises every upgrade made to the THRIVE website from v5.2 to v5.3 across five areas: Quiz Bank, Quiz Engine, Website UX/Aesthetics, Study Book, and Documentation. Each section states what existed before, what was changed, and why.

---

## 1. QUIZ BANK — `js/quiz-bank.js`

### Before (v5.2)
| Metric | Value |
|--------|-------|
| Total questions | 230 |
| Tech questions | 71 (31%) |
| Football questions | 159 (69%) |
| Tech session size | Hardcoded 30 in quiz.html |
| Football session size | Hardcoded 30 in quiz.html |
| Version string | `THRIVE Quiz Bank v5.2` |

### After (v5.3)
| Metric | Value |
|--------|-------|
| Total questions | **532** |
| Tech questions | **373 (70%)** |
| Football questions | **159 (30%)** |
| Tech session size | **50** (stored in quiz config `sessionSize` property) |
| Football session size | **25** (stored in quiz config `sessionSize` property) |
| Version string | `THRIVE Quiz Bank v5.3` |

### New Tech Question Topics Added

**Batch 1 — 91 questions added (Advanced AI & ML Theory)**
- Recurrent neural networks (RNN) and LSTMs — how they process sequences and why transformers replaced them
- Word embeddings and Word2Vec — semantic arithmetic between word vectors
- BERT vs GPT architectures — encoder-only vs decoder-only transformer designs
- Tokenisation — how LLMs process text as sub-word units, not whole words
- Multihead attention — how transformers attend to different aspects of input simultaneously
- AI alignment techniques — RLHF vs DPO vs Constitutional AI
- Prompt injection — security attacks on AI agents via environmental instructions
- Grounding and hallucination mitigation — RAG, fact-checking, uncertainty expression
- Reinforcement learning in game playing — AlphaGo, AlphaZero, self-play
- Object detection vs image segmentation — bounding boxes vs pixel-level classification
- Face recognition — capabilities, accuracy disparities, and controversial applications
- Neural architecture search (NAS) — automated discovery of optimal architectures
- Multimodal learning — video, medical imaging, autonomous driving sensor fusion
- Catastrophic forgetting — elastic weight consolidation (EWC) as a solution
- Meta-learning (learning to learn) — MAML and few-shot generalisation
- Knowledge graphs — entity-relationship triples, semantic reasoning
- Online vs offline (batch) learning — data streams vs full dataset training
- Semantic similarity — cosine similarity between embeddings for search and matching
- Anomaly detection — predictive maintenance, fraud detection, cybersecurity
- Causal AI — Pearl's do-calculus, intervention vs observation, counterfactuals
- Data poisoning attacks — backdoor triggers in training data
- Model stealing attacks — cloning commercial models via API queries
- Differential privacy — formal mathematical privacy guarantees in AI training
- Adversarial examples — imperceptible pixel perturbations causing misclassification
- Model interpretability vs explainability — LIME, SHAP, post-hoc methods
- Model calibration — confidence scores that actually reflect accuracy rates
- Weak supervision — Snorkel, label functions, noisy label generation at scale
- Self-supervised pre-training — predicting next tokens vs supervised fine-tuning
- The lottery ticket hypothesis — winning subnetworks within large models
- Teacher-student training — Alpaca, GPT-4-generated instruction datasets
- Instruction tuning — how raw language models become useful assistants
- Embeddings in modern systems — recommendation engines, vector databases
- AI red teaming — adversarial safety testing for frontier AI models
- Model merging — combining fine-tuned models without retraining
- RLHF vs DPO — two alignment approaches compared with trade-offs
- Tool use and function calling — how LLMs take real-world actions through APIs
- Sparse attention — Longformer, BigBird, efficient long-context processing
- Continual pre-training — domain adaptation before fine-tuning
- Prompt caching — KV cache reuse for cost reduction on large contexts
- AI watermarking — SynthID, Maryland algorithm, robustness challenges
- AI for code generation — GitHub Copilot, copyright concerns, security risks
- Reasoning vs memorisation in LLMs — what chain-of-thought reveals about LLMs
- AI for drug discovery — Insilico Medicine, BenevolentAI, AlphaFold beyond proteins
- The bitter lesson (Richard Sutton) — scale beating hand-crafted domain knowledge
- AI in Africa — Masakhane, NCAIR, Ubenwa, Google DeepMind Africa
- Federated learning at scale — statistical heterogeneity, communication overhead
- AI regulation in Africa — Nigeria's National AI Policy Framework, NCAIR
- AI consciousness — why this is an unresolved philosophical and scientific question
- The paperclip maximiser thought experiment — why goal specification matters
- Multiagent AI — AlphaStar, OpenAI Five, traffic coordination, supply chains
- Neuromorphic computing — IBM NorthPole, brain-like efficiency vs GPU
- Model collapse — degradation from training on AI-generated data
- Graph neural networks (GNN) — molecular property prediction, fraud detection, social graphs
- AutoML — automated feature engineering, model selection, and hyperparameter tuning
- AI for climate change — DeepMind cooling, materials discovery, deforestation monitoring
- Surveillance capitalism (Shoshana Zuboff) — behavioural data as a commercial product
- AI and employment — Acemoglu, McKinsey, WEF Future of Jobs research
- Privacy by design — GDPR Article 25, Ann Cavoukian's framework
- The right to be forgotten — Google Spain v AEPD, NDPR individual rights
- AI in education — personalised learning, intelligent tutoring, academic dishonesty risks
- Responsible scaling policy (RSP) — Anthropic's Preparedness Framework
- AI safety vs AI ethics — different time horizons and risk categories
- RAG limitations — chunking strategies, retrieval quality, faithfulness issues
- Chain-of-thought vs tree-of-thought — linear vs branching reasoning exploration
- AI for satellite imagery analysis — deforestation, informal settlements, crop monitoring
- Model cards — standardised transparency documentation for AI systems
- AI agent safety — irreversible actions, prompt injection from environment, permission scoping
- The transformer attention mechanism — Query, Key, Value as soft database lookup
- Vision Transformer (ViT) — patches as tokens, unifying vision and language architectures
- AI governance in practice — conformity assessments, auditing, redress mechanisms
- Synthetic data — when to use it over real data, strengths and limitations
- AI and national security — autonomous weapons, disinformation, surveillance exports to Africa
- Human-in-the-loop AI — when legally required, when beneficial, implementation approaches
- AI for biodiversity and conservation — WildBook, BirdNET, camera trap classification
- AI for financial inclusion in Nigeria — alternative credit scoring, OPay, Carbon, FairMoney
- The alignment problem — outer alignment, inner alignment, specification gaming
- Retrieval-Augmented Generation in practice — engineering challenges, failure modes
- Bayesian inference — uncertainty quantification, Gaussian processes, variational inference
- AI winter history — two AI winters, why the current period is different
- AI for agriculture in Africa — PlantVillage, Hello Tractor, Babban Gona
- The Chinchilla scaling paper — optimal compute allocation, training data vs model size
- AI hallucination mitigation — RAG, self-consistency, retrieval + faithfulness training
- AI in Nigeria's healthcare system — realistic potential, CHW augmentation model
- AI and language preservation — Masakhane, Mozilla Common Voice, Lacuna Fund
- Explainable AI in healthcare — saliency maps, SHAP for clinical decision support
- The digital divide in AI — data, compute, talent, language, product, and benefit divides
- AI model robustness — distribution shift in African deployment contexts
- AI for social good in Africa — Ubenwa birth asphyxia, Zipline, Peek Vision

**Batch 2 — 118 questions added (Systems, Cloud, Data Engineering, Programming, Nigeria Tech)**
- Hash tables — O(1) average lookup, collision handling, load factor
- Binary search trees — O(log n) search, self-balancing trees (AVL, Red-Black)
- Dynamic programming vs greedy algorithms — coin change problem, when each applies
- Graph data structures — adjacency matrix vs adjacency list, BFS, Dijkstra
- Dijkstra's algorithm — priority queue, O((V+E) log V), A* extension
- SQL vs NoSQL — selection criteria based on data structure and access patterns
- ACID properties — atomicity, consistency, isolation, durability in financial systems
- Database sharding — horizontal partitioning for billion-user scale
- TCP vs UDP — reliability vs speed trade-off, application-level examples
- JWT authentication — stateless auth, signature verification, refresh tokens
- OAuth 2.0 — authorisation (not authentication), OpenID Connect distinction
- The N+1 query problem — eager loading as the solution, ORM tools
- Caching strategies — Cache-Aside, Write-Through, Write-Behind, Read-Through
- Horizontal vs vertical scaling — statelessness requirement, load balancers
- SOLID principles — five OOP design principles with practical examples
- Dependency injection — testability, loose coupling, DI containers (Spring, Angular)
- Garbage collection types — reference counting, mark-and-sweep, generational GC
- The actor model — Erlang/Elixir, WhatsApp's architecture, fault isolation
- Debouncing vs throttling — search autocomplete vs scroll event handling
- Lazy loading vs eager loading — code splitting, image lazy loading
- Immutable infrastructure — Phoenix server pattern, Docker + Kubernetes
- Twelve-factor app methodology — twelve principles for cloud-native applications
- Distributed tracing — trace IDs, Jaeger, Zipkin, diagnosing slow microservices
- Feature flags — gradual rollouts, kill switches, LaunchDarkly
- Chaos engineering — Netflix Simian Army, Chaos Monkey, blameless postmortem
- Blue-green vs canary deployment — instant vs gradual traffic switching
- Circuit breaker pattern — preventing cascading failures in microservices
- Saga pattern — compensating transactions for distributed transactions
- API versioning — URL versioning, header versioning, deprecation periods
- Event sourcing — immutable event log vs mutable CRUD state
- Repository pattern — abstracting the data access layer for testability
- Monorepo vs multi-repo — Google's monorepo, Nx/Bazel tooling, when to use each
- Principle of least privilege — AWS IAM, blast radius limitation, real breach examples
- Load testing — k6, JMeter, Gatling, stress/soak/spike test types
- Shared responsibility model in cloud — what AWS secures vs what you secure
- Shift left in security and testing — cost multiplier for late defect discovery
- Service mesh technology — Istio, Envoy sidecar, mTLS, observable networking
- Pyramid of testing — unit/integration/E2E, the ice cream cone antipattern
- GitOps — ArgoCD, Flux, Git as the single source of truth for infrastructure
- CQRS pattern — separating read models from write models
- Strangler fig pattern — incremental legacy migration without big bang rewrites
- Two-generals problem — why exactly-once delivery is theoretically impossible
- Message queuing (Kafka vs RabbitMQ) — retention, offset tracking, consumer groups
- Test coverage — why 100% coverage is not sufficient, mutation testing
- Cloud service models (IaaS/PaaS/SaaS) — what each level manages
- Serverless computing — AWS Lambda, cold starts, provisioned concurrency
- Infrastructure as code — Terraform, CloudFormation, Ansible
- SLO/SLA/SLI — error budget concept, how they relate to each other
- DORA metrics — deployment frequency, lead time, change failure rate, MTTR
- Continuous Integration vs Delivery vs Deployment — manual approval distinction
- Container orchestration (Kubernetes) — scheduling, self-healing, rolling updates
- SRE on-call culture — blameless postmortem, blame vs systemic thinking
- Golden signals — latency, traffic, errors, saturation (Google SRE framework)
- Observability vs monitoring — why novel failures require exploratory analysis
- eBPF — sandboxed kernel programs, Cilium, zero-overhead production profiling
- MTTR vs MTBF — why optimising recovery often beats preventing failures
- Infrastructure drift — snowflake servers, Terraform plan for detection
- Content delivery network (CDN) — African CDN coverage gap, Lagos nodes
- DNS resolution — recursive resolver, root nameservers, TLD, TTL
- Process vs thread vs coroutine — Python GIL, goroutines, async I/O model
- ETL pipeline — extract, transform, load; foundational data engineering pattern
- Data warehouse — columnar storage, BigQuery, Redshift, Snowflake
- Apache Spark — in-memory vs MapReduce, lazy evaluation, PySpark
- Apache Kafka — commit log, consumer offsets, retention, partitioning
- dbt (data build tool) — SQL transformations with software engineering practices
- OLTP vs OLAP — why you need both, the risk of running analytics on production
- Change data capture (CDC) — Debezium, WAL reading, real-time sync
- Medallion architecture — Bronze/Silver/Gold zones in data lakes
- Stream vs batch processing — Flink, Spark Structured Streaming, Lambda architecture
- Apache Airflow — DAGs, task dependencies, retry logic, web UI
- Data governance and NDPR — Nigeria's data protection obligations
- Data lake vs lake house — Delta Lake, Apache Iceberg, schema enforcement
- Data mesh — domain ownership of data products, decentralisation
- Data quality — Great Expectations, data contracts, observability tools
- Data lineage — impact analysis, debugging, GDPR deletion compliance
- Data-driven decision making — A/B testing, avoiding metric fixation
- Python — NumPy/Pandas/scikit-learn ecosystem, GIL limitation
- JavaScript — browser ubiquity, event loop, Node.js
- TypeScript — gradual static typing, compile-time error catching
- Rust — ownership system, memory safety without GC, zero-overhead
- Go — goroutines (2KB stack), channels, Docker/Kubernetes/Terraform ecosystem
- Java — JVM, Spring Boot, Kotlin and Scala as JVM alternatives
- Python GIL — why Python threads cannot parallelise CPU-bound work
- Async/await programming — event loop, non-blocking I/O, concurrent requests
- Memory safety — 70% of Chrome/Microsoft security vulnerabilities, Rust adoption
- Functional vs imperative programming — immutability, pure functions, React
- WebAssembly — Figma, AutoCAD Web, Cloudflare Workers, near-native speed
- Decorator pattern — @login_required, @cache, cross-cutting concerns
- Halting problem — undecidability, implications for static analysis
- Static vs dynamic typing — compile-time vs runtime type checking
- Prototype chain in JavaScript — how inheritance works under class syntax
- Kubernetes vs Docker Compose — local dev vs multi-server production
- Reactive programming — RxJS, streams, debounce, merge, cancel
- Tail call optimisation (TCO) — Scheme guarantee, Python lack of TCO
- Command pattern — undo/redo, command history, Photoshop history panel
- Observer vs pub-sub pattern — tight coupling vs message broker decoupling
- Eventual consistency — e-commerce checkout example, compensation transactions
- Nigerian startup ecosystem — Flutterwave, Paystack, Andela, Kuda
- Paystack acquisition significance — first major Nigerian exit, VC confidence
- Andela's talent marketplace — connecting African engineers to global companies
- Interswitch ecosystem — Quickteller, Verve card, foundational payment infrastructure
- Flutterwave's achievements — Rave API, 30+ African countries, unicorn status
- CBN's role in Nigeria's digital economy — cashless policy, eNaira, FX policy
- Lagos as a tech hub — Yabacon Valley, CcHub, subsea cables, IXPN
- NITDA's role — NDPR enforcement, local content policy, NITDEF
- Subsea cable infrastructure — WACS, ACE, MainOne, Equiano
- Nigerian fintech regulation landscape — CBN, SEC, NAICOM, NCC overlap
- Mobile money in Nigeria vs Kenya — M-Pesa model, 2021 CBN regulatory shift
- eNaira and CBDC experience — low adoption lessons, existing alternatives
- Nigerian tech talent — brain drain, Japa wave, Andela marketplace, bootcamps
- African tech investment landscape — $6.5B peak (2022), leading sectors
- Diaspora role in African tech — remittances, knowledge transfer, return migration
- NDPR individual rights — access, rectification, erasure, portability
- Open source in Africa — Masakhane, OpenMRS, iHRIS, individual contributions

---

## 2. QUIZ ENGINE — `quiz.html`

### Before (v5.2)
- Session size hardcoded: `const SESSION_Q = 30;` — both tech and football got 30 questions
- No per-quiz session size configuration

### After (v5.3)
- `SESSION_Q = 50` as fallback default
- Quiz runner now reads `quiz.sessionSize` from the QUIZZES config object first:
  ```javascript
  // Before
  const selected = buildQuestionSet(quiz.questions, SESSION_Q);

  // After
  const selected = buildQuestionSet(quiz.questions, quiz.sessionSize || SESSION_Q);
  ```
- Tech quiz: 50 questions per session (stored as `sessionSize: 50` in quiz-bank.js)
- Football quiz: 25 questions per session (stored as `sessionSize: 25` in quiz-bank.js)
- Session size is now config-driven — change it in quiz-bank.js without touching quiz.html

---

## 3. WEBSITE UX & AESTHETICS — `css/style.css`

### Before (v5.2)
- Size: ~42 KB
- Basic card and button styles
- No hover animations on quiz answer options
- No quiz answer feedback animations
- Minimal table styling
- No loading states

### After (v5.3)
- Size: **~53 KB** (7,143 characters of new styles added)

**New UX features added:**

| Feature | Implementation |
|---------|---------------|
| Smooth scroll | `html { scroll-behavior: smooth; }` |
| Selection colour | Green brand highlight on text selection |
| Focus-visible ring | Accessible keyboard navigation indicator (2px green ring) |
| Card hover lift | `translateY(-3px)` + `var(--sh-lg)` on all card types |
| Button active scale | `scale(.97)` on click press for tactile feel |
| Button shadow glow | Green glow on primary buttons, orange glow on CTA buttons |
| Button ripple | White `::after` pseudo-element flash on click |
| Answer option slide | `translateX(4px)` + green border on hover |
| Correct answer pulse | `@keyframes correctPulse` — gentle scale bounce |
| Incorrect answer shake | `@keyframes shake` — horizontal shake animation |
| Explanation fade-in | `@keyframes fadeSlideIn` — slide up from below |
| Toast notification | `@keyframes toastIn` — scale+fade-in from below |
| Loading skeleton | Shimmer gradient animation for async loading states |
| Table polish | Styled `thead`, hover rows, `last-child` no border |
| Leaderboard podium | Gold/silver/bronze colours for rank 1/2/3 |
| Score badge | Colour-coded (green/amber/red) for high/mid/low scores |
| Quiz progress bar | Green gradient fill with smooth width transition |
| Question number chip | Circular green chip beside question numbers |
| Section labels | Small-caps uppercase green labels |
| Stat numbers | Clamp-scaled display numbers for hero stats |
| Empty state | Centred placeholder with opacity-reduced icon |
| Mobile hide utility | `.hide-mobile` class for responsive column control |
| Mobile button stack | `width: 100%` on buttons below 480px |
| Stat grid mobile | 2-column grid on small screens |
| Print styles | Hides nav, footer, buttons; avoids breaking quiz cards |

---

## 4. CONTENT — `index.html`

### Before (v5.2)
- Displayed "500+ quiz questions" (inaccurate)
- Version references to v5.2

### After (v5.3)
- Updated to display **"532 quiz questions"** (accurate)
- Version updated to v5.3 where referenced

---

## 5. STUDY BOOK — `QUIZ_TOPIC_REFERENCE.md` + `THRIVE_Study_Book.docx`

### Before (v5.2)
- 873 lines
- 8 tech chapters + 5 football chapters
- Practice questions at end of each chapter
- **No answer key** — questions had no marked correct answers

### After (v5.3)
- **1,211 lines** (+338 lines)
- **10 tech chapters** + 5 football chapters (added Chapter 9: Cloud/DevOps/SRE and Chapter 10: Data Engineering)
- **75 practice questions** (5 per chapter) — all 4 answer options written out
- **Correct answers marked with ✓** inline within each chapter
- **Appendix A: Complete Answer Key** — tabular quick-reference for all 75 answers (A/B/C/D) plus detailed explanations for tricky questions across all chapters
- **Appendix B: Key Terms Glossary** — 40+ defined terms alphabetically

**New chapters added:**

**Chapter 9 — Cloud, DevOps, and Systems Engineering**
- Cloud service models (IaaS/PaaS/SaaS)
- SLI/SLO/SLA and the error budget concept
- CI vs Continuous Delivery vs Continuous Deployment
- DORA metrics framework
- SRE on-call culture and blameless postmortems
- Chaos engineering philosophy

**Chapter 10 — Data Engineering**
- ETL and ELT patterns
- Data warehouse vs data lake vs lake house
- Medallion architecture (Bronze/Silver/Gold)
- Apache Spark, Kafka, dbt, and Airflow
- Stream vs batch processing
- OLTP vs OLAP and why systems specialise

**Word Document (`THRIVE_Study_Book.docx`)**
- Regenerated from updated markdown
- 15-chapter structure
- All practice questions formatted with green highlighting on correct answers
- Appendices included

---

## 6. NEW DOCUMENTATION FILES

### `THRIVE_ADMIN_GUIDE.md` (NEW)

A standalone, clear admin access reference covering:
- **Admin PIN: 2025** — prominently displayed
- Step-by-step admin panel access instructions
- Table of what each admin section manages (League, CMS, Video, Quiz)
- Technical detail on how the PIN is stored (`btoa('thrive-2025-admin')`)
- Full table of localStorage keys (`thrive_v5_league_*`, `thrive_v5_tech_*`, `thrive_v5_cms_*`, `thrive_v5_videos_*`)
- Browser console command to reset all admin data
- Verification steps after Netlify deployment

### `GITHUB_UPDATE_GUIDE.md` (UPDATED)

Updated from v5.2 to reflect:
- New files changed (6 files vs 3 previously)
- Updated commit message with correct question counts
- Updated verification instructions (532 total, Tech=50, Football=25)
- Quick admin reference added at bottom

---

## 7. QUIZ BANK VERSION LOG (inside `quiz-bank.js`)

```javascript
// Before
console.log('THRIVE Quiz Bank v5.2 loaded — Tech: 71, Football: 159, Total: 230');

// After
console.log('THRIVE Quiz Bank v5.3 loaded — Tech: 373, Football: 159, Total: 532');
```

The version log string outputs to the browser console on page load — this is the primary verification signal for confirming a successful deployment.

---

## 8. SUMMARY TABLE

| Area | v5.2 | v5.3 | Change |
|------|------|------|--------|
| Total quiz questions | 230 | **532** | +302 (+131%) |
| Tech questions | 71 (31%) | **373 (70%)** | +302 |
| Football questions | 159 (69%) | **159 (30%)** | unchanged |
| Tech session size | 30 (hardcoded) | **50** (config-driven) | +20 questions per session |
| Football session size | 30 (hardcoded) | **25** (config-driven) | adjusted |
| Study book chapters | 13 | **15** | +2 new chapters |
| Study book lines | 873 | **1,211** | +338 lines |
| Practice questions | 65 (no answers) | **75 (with answers + key)** | +10 + full answer key |
| CSS file size | ~42 KB | **~53 KB** | +7 KB of UX enhancements |
| New CSS animations | 0 | **8 @keyframes** | correctPulse, shake, fadeSlideIn, toastIn, skeleton-shimmer, etc. |
| Admin guide | Not documented | **Standalone file** | PIN, access steps, localStorage keys |
| Quiz engine | Hardcoded 30 | **Config-driven sessionSize** | Tech=50, Football=25 |

---

## 9. FILES CHANGED

```
thrive-v5/
├── js/
│   └── quiz-bank.js          ← UPDATED (230 → 532 questions, sessionSize added)
├── css/
│   └── style.css             ← UPDATED (42KB → 53KB, UX enhancements)
├── quiz.html                 ← UPDATED (hardcoded 30 → quiz.sessionSize)
├── index.html                ← UPDATED (question count string)
├── QUIZ_TOPIC_REFERENCE.md   ← UPDATED (873 → 1,211 lines, answers added)
└── THRIVE_ADMIN_GUIDE.md     ← NEW (admin PIN, access guide, localStorage keys)

outputs/
├── thrive-v5.zip             ← REGENERATED (complete site package)
├── THRIVE_Study_Book.docx    ← REGENERATED (from updated markdown)
├── GITHUB_UPDATE_GUIDE.md    ← UPDATED
└── THRIVE_ADMIN_GUIDE.md     ← NEW
```

---

## 10. DEPLOYMENT VERIFICATION CHECKLIST

After pushing to GitHub and Netlify redeploys, confirm the following:

- [ ] Browser console shows: `THRIVE Quiz Bank v5.3 loaded — Tech: 373 (70%) | Football: 159 (30%) | Total: 532`
- [ ] Starting a Tech quiz presents exactly **50 questions**
- [ ] Starting a Football quiz presents exactly **25 questions**
- [ ] Quiz answer options show a green pulse animation on correct selection
- [ ] Quiz answer options show a red shake animation on incorrect selection
- [ ] Explanation text fades in smoothly after answering
- [ ] Cards lift visually on hover (3px upward + shadow deepens)
- [ ] Admin panel accessible via footer Admin link with PIN **2025**
- [ ] League Management, CMS, Video, and Quiz Admin sections all load in admin panel
- [ ] Site displays "532 quiz questions" in any hero/stats section
- [ ] Mobile view: buttons stack to full width below 480px

---

*End of review document.*
*THRIVE — Technology, Hard work, Resilience, Innovation, Vision, and Excellence*
