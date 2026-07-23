# THRIVE Website — Handoff Brief for Claude Code
## Context: Continuing work started in Claude.ai Chat

---

## Who I Am and What This Project Is

**Client:** Chisom Okoye — Environmental engineer based in Copenhagen, Denmark. Founder of THRIVE, a youth development initiative based in Nigeria.

**THRIVE** runs three programmes for young Nigerians:
1. **Tech Challenge** — AI, ML, robotics, cybersecurity, data science, programming quiz
2. **Football Arena** — Laws of the Game, tactics, world/Nigerian football quiz
3. **Inspiration Talks** — motivational video content

The website is a static site (HTML/CSS/JavaScript, no backend framework) deployed via **GitHub → Netlify auto-deploy**.

---

## What Claude.ai Chat Built (v5.2 → v5.3)

The original v5.2 site had a working quiz engine, league management, CMS, and video management — all powered by vanilla JS with localStorage for persistence. The original quiz bank had 230 questions (71 tech / 159 football). The client asked for a series of upgrades. Here is everything that was completed:

### 1. Quiz Bank (`js/quiz-bank.js`) — MAJOR EXPANSION

**Before:** 230 questions (71 tech 31% / 159 football 69%)
**After:** 532 questions (373 tech 70% / 159 football 30%)

The file is 472KB and contains two arrays — `techQ` and `footballQ` — inside an IIFE that registers them on `window.SITE_CONFIG.QUIZZES`.

**Structure of each question:**
```javascript
{
  q: 'Question text here',
  options: ['Option A', 'Option B', 'Option C', 'Option D'],
  answer: 1,        // 0-indexed correct answer
  explanation: 'Why this answer is correct'
}
```

**`SITE_CONFIG.QUIZZES` array structure:**
```javascript
window.SITE_CONFIG.QUIZZES = [
  {
    id: 'tech-challenge',
    title: 'Tech Challenge',
    category: 'tech',
    description: 'AI, machine learning, robotics, cybersecurity, data science...',
    questions: techQ,
    sessionSize: 50,   // ← ADDED in v5.3 — questions drawn per session
  },
  {
    id: 'football-arena',
    title: 'Football Arena',
    category: 'football',
    description: 'Laws of the Game, tactics, world football history...',
    questions: footballQ,
    sessionSize: 25,   // ← ADDED in v5.3 — questions drawn per session
  },
];
```

**Tech topics covered** (373 questions across):
- AI Foundations (narrow AI, supervised/unsupervised/reinforcement learning, overfitting, transfer learning, Turing test, hallucination, bias)
- LLMs and Generative AI (transformer architecture, prompt engineering, context window, RAG, fine-tuning, RLHF, DPO, Constitutional AI, GANs, diffusion models, zero-shot, in-context learning, scaling laws)
- Advanced AI/ML Theory (RNNs, LSTMs, BERT vs GPT, tokenisation, multihead attention, word embeddings, causal AI, adversarial examples, differential privacy, data poisoning, model stealing, federated learning, knowledge distillation, instruction tuning, tool use/function calling, prompt injection, AI red teaming, model collapse, GNNs, AutoML, neuromorphic computing)
- Robotics (Moravec's paradox, SLAM, cobots, sim-to-real, digital twins, soft robotics, swarm robotics, teleoperation, path planning, uncanny valley, robot grasping)
- Cybersecurity and Networks (CIA triad, zero-trust, E2EE, social engineering, SQL injection, zero-day, supply chain attacks, 2FA, TLS/HTTPS, OAuth 2.0, JWT, rate limiting, DevSecOps)
- Data Science and Analytics (EDA, feature engineering, xG, random forest, gradient boosting, bias-variance tradeoff, k-means clustering, dimensionality reduction, time series forecasting, A/B testing, feature importance)
- Emerging Technology and Society (5G, IoT, blockchain, precision agriculture, edge AI, digital inequality, algorithmic accountability, AI bias as social justice, responsible AI, climate AI, AI governance, future of work, digital literacy, data sovereignty, surveillance capitalism)
- Programming and CS Concepts (Big O notation, OOP, recursion, dynamic programming, version control/Git, TDD, hash tables, BSTs, graphs, Dijkstra, SOLID principles, dependency injection, garbage collection, actor model, debouncing/throttling, lazy loading, immutable infrastructure, twelve-factor app)
- Cloud / DevOps / SRE (cloud service models, serverless, IaC/Terraform, SLO/SLA/SLI, DORA metrics, CI/CD, Kubernetes, container orchestration, SRE blameless postmortem, golden signals, observability vs monitoring, eBPF, MTTR/MTBF, GitOps, chaos engineering, blue-green/canary deployment, circuit breaker, saga pattern, CQRS, strangler fig, feature flags, load testing, shared responsibility model, shift left)
- Data Engineering (ETL/ELT, data warehouse, Apache Spark, Apache Kafka, dbt, OLTP vs OLAP, CDC, medallion architecture, stream vs batch, Apache Airflow, data governance/NDPR, data lake/lake house, data mesh, data lineage, data quality)
- Systems Design (SQL vs NoSQL, ACID, sharding, horizontal vs vertical scaling, caching strategies, N+1 query problem, TCP vs UDP, JWT/OAuth 2.0, message queuing/Kafka vs RabbitMQ, event sourcing, repository pattern, CQRS, API versioning, distributed tracing, idempotency)
- Programming Languages (Python, JavaScript, TypeScript, Rust, Go, Java, Python GIL, async/await, memory safety, functional vs imperative, WebAssembly, decorator pattern, halting problem, static vs dynamic typing, prototype chain)
- Nigeria/Africa Tech Ecosystem (Flutterwave, Paystack acquisition, Andela, Interswitch, Kuda, OPay, CBN role, Lagos as tech hub, NITDA, NDPR, subsea cables, eNaira/CBDC, mobile money, African VC landscape, diaspora role, AfCFTA)

**Football topics covered** (159 questions — unchanged from v5.2):
- Laws of the Game (offside, VAR four situations, direct vs indirect free kicks, back-pass rule, 2019 goal kick change, penalty rules)
- Tactics (pressing, gegenpress, formations 4-3-3/4-2-3-1/3-5-2, false nine, inverted wingers, tiki-taka, positional play, xG as a tactical tool)
- World Football History (FIFA founding, World Cup history/winners, Bosman ruling, total football, Miracle of Istanbul, Hand of God)
- Nigerian and African Football (Super Eagles, Jay-Jay Okocha, Nwankwo Kanu, Rashidi Yekini, Stephen Keshi, Victor Osimhen, Asisat Oshoala, Enyimba CAF Champions League 2003/2004, AFCON history, George Weah)
- Positions and Statistics (xG, PPDA, progressive passes, goalkeeper evolution, false 9, inverted wingers, number 10 significance)

**Validation command** (run in the repo root):
```bash
node -e "
const fs=require('fs');
const code=fs.readFileSync('js/quiz-bank.js','utf8');
const vm=require('vm');
const ctx={window:{},console:{log:m=>console.log(m)}};
vm.createContext(ctx);
try {
  vm.runInContext(code,ctx);
  const q=ctx.window.SITE_CONFIG.QUIZZES;
  const t=q[0].questions.length,f=q[1].questions.length,tot=t+f;
  console.log('Tech:',t,'('+Math.round(t/tot*100)+'%) | Football:',f,'('+Math.round(f/tot*100)+'%) | Total:',tot);
  console.log('Sessions: Tech='+q[0].sessionSize+' Football='+q[1].sessionSize);
  let bad=0;
  [...q[0].questions,...q[1].questions].forEach((qq,i)=>{
    if(!qq||!qq.q||!qq.options||qq.options.length!==4||qq.answer===undefined||!qq.explanation) bad++;
  });
  console.log(bad===0?'ALL QUESTIONS VALID':'ISSUES: '+bad);
} catch(e) { console.log('ERR:',e.message); }
"
```
Expected output: `Tech: 373 (70%) | Football: 159 (30%) | Total: 532 | Sessions: Tech=50 Football=25 | ALL QUESTIONS VALID`

---

### 2. Quiz Engine (`quiz.html`) — SESSION SIZE FIX

**The problem:** Session size was hardcoded as `const SESSION_Q = 30;` — both quizzes delivered 30 questions regardless of quiz type.

**The fix:**
```javascript
// Before
const selected = buildQuestionSet(quiz.questions, SESSION_Q);

// After
const selected = buildQuestionSet(quiz.questions, quiz.sessionSize || SESSION_Q);
```

Also updated `SESSION_Q` fallback from 30 to 50:
```javascript
const SESSION_Q = 50; // fallback — overridden per quiz by quiz.sessionSize
```

Result: Tech quiz draws 50 random questions per session. Football quiz draws 25.

---

### 3. CSS UX Enhancements (`css/style.css`)

**Before:** 42KB — basic layout, card styles, colour palette
**After:** 53KB — added 7KB of UX/animation enhancements at the bottom of the file

**Additions (appended, non-destructive):**
- `html { scroll-behavior: smooth; }` + `::selection` brand colour
- `:focus-visible` accessible keyboard ring
- Card hover lift: `translateY(-3px)` + deeper shadow on `.card`, `.quiz-card`, `.activity-card`
- Button active: `scale(.97)` press + `::after` ripple flash
- Button hover glow: green shadow on `.btn-primary`, orange on `.btn-cta`
- Quiz answer option slide: `translateX(4px)` + green border on hover
- `@keyframes correctPulse` — gentle scale bounce for correct answers
- `@keyframes shake` — horizontal shake for incorrect answers
- `@keyframes fadeSlideIn` — explanation box fade-up after answering
- `@keyframes toastIn` — toast notification scale+fade entrance
- `@keyframes skeleton-shimmer` — loading placeholder animation
- `.explanation-box` — left-bordered green explanation panel style
- `.toast` styles (success, error, info variants)
- `.quiz-progress` + `.quiz-progress-fill` — session progress bar
- `.score-badge` (high/mid/low colour variants)
- `.q-chip` — circular question number indicator
- `.stat-number` + `.stat-label` — hero stat display styles
- `.section-label` — small-caps uppercase section headers
- `.empty-state` — centred placeholder for empty lists
- Table styles: styled `thead`, hover rows, last-child border removal
- Leaderboard `.rank-1/.rank-2/.rank-3` gold/silver/bronze
- Mobile utilities: `.hide-mobile`, button full-width below 480px, 2-col stat grid
- Print styles: hides nav/footer/buttons, preserves quiz card layout

---

### 4. Study Book (`QUIZ_TOPIC_REFERENCE.md` + `THRIVE_Study_Book.docx`)

**Before:** 873 lines, 13 chapters, practice questions with no marked answers
**After:** 1,211 lines, 15 chapters, 75 practice questions with answers + full answer key

**New chapters:**
- Chapter 9: Cloud, DevOps, and Systems Engineering
- Chapter 10: Data Engineering

**Appendix A** — Quick-reference answer key (all 75 questions, A/B/C/D) + detailed explanations for questions that are likely to trip up students.

**Appendix B** — 40+ term glossary.

**Word doc** regenerated using the `docx` npm package.

---

### 5. Admin Access Documentation (`THRIVE_ADMIN_GUIDE.md`) — NEW FILE

**Admin PIN:** `2025`

How it's stored in `js/main.js`:
```javascript
// The encoded check value
const _AH = btoa('thrive-2025-admin'); // = "dGhyaXZlLTIwMjUtYWRtaW4="
// PIN "2025" is verified against this on the admin login form
```

**Access:** Footer → Admin link → enter `2025`

**Admin sections:** League Management, CMS, Video Management, Quiz Admin

**localStorage keys:**
| Key prefix | Contents |
|------------|----------|
| `thrive_v5_league_*` | Football league data |
| `thrive_v5_tech_*` | Tech quiz scores |
| `thrive_v5_cms_*` | CMS content |
| `thrive_v5_videos_*` | Video links |

---

## File Structure

```
thrive-v5/                      ← complete deployable site
├── index.html                  ← homepage (updated: shows 532 questions)
├── quiz.html                   ← quiz engine (updated: config-driven sessionSize)
├── about.html
├── activities.html
├── QUIZ_TOPIC_REFERENCE.md     ← study book (updated: 15 chapters, answers)
├── THRIVE_ADMIN_GUIDE.md       ← NEW: admin PIN + access guide
├── css/
│   └── style.css               ← updated: +7KB UX enhancements
├── js/
│   ├── quiz-bank.js            ← MAIN CHANGE: 230→532 questions
│   ├── main.js                 ← unchanged: admin PIN, localStorage, UI
│   ├── config.js               ← unchanged: site config, ORG_NAME
│   └── components.js           ← unchanged: reusable UI components
├── assets/
└── ...
```

---

## What Has NOT Been Done (potential next tasks)

1. **Push to GitHub** — the client needs to copy updated files from the downloaded zip and push. The GitHub Update Guide (`GITHUB_UPDATE_GUIDE.md`) has the exact commands.

2. **Backend/server** — there is none. All data is in localStorage. If the client wants persistent server-side storage (scores across devices, real user accounts), that would require building a backend (Supabase/Firebase would be the lightest lift for a static site).

3. **Nigerian language support** — quiz questions are English only. Adding Yoruba, Hausa, or Igbo translations would significantly expand THRIVE's reach.

4. **Quiz timer** — no per-question or per-session timer exists. Could be added to `quiz.html`.

5. **PDF export of results** — after completing a quiz, participants cannot export their results. Could be implemented with `window.print()` or a PDF library.

6. **Admin analytics dashboard** — the admin panel lets you manage content but has no aggregate quiz performance stats (average score, most-missed questions, question difficulty ratings).

7. **More football questions** — football is currently 159 questions (30%). If the client wants to go back to 50/50, approximately 215 more football questions are needed.

8. **PWA (Progressive Web App)** — adding a service worker and manifest would allow the site to work offline and be installed on phones. Particularly valuable for Nigerian users with unreliable connectivity.

---

## Tech Stack Summary

| Concern | Implementation |
|---------|---------------|
| HTML | Vanilla HTML5, semantic elements |
| CSS | Custom CSS with CSS variables (`--green-600`, `--font-head`, etc.) |
| JavaScript | Vanilla ES6+ IIFE modules, no framework |
| Fonts | Sora (headings) + Inter (body) via Google Fonts |
| Icons | Likely inline SVG or a small icon library (check `components.js`) |
| Storage | Browser `localStorage` — all data lives in the browser |
| Deployment | GitHub repository → Netlify auto-deploy on push to `main` |
| No build step | Pure static files — no webpack, no npm required for the site itself |

---

## Key Design Decisions to Preserve

1. **No dependencies on `node_modules` for the running site** — the site is pure static HTML/CSS/JS. npm/node is only used for generating the study book docx and running validation scripts.

2. **Quiz bank is a single self-contained IIFE** — `quiz-bank.js` wraps everything in `(function(){ ... })()` and attaches to `window.SITE_CONFIG`. Do not break this structure — `quiz.html` reads from `window.SITE_CONFIG.QUIZZES`.

3. **All question data lives in `quiz-bank.js`** — there is no separate JSON file, no API call. The file is loaded as a `<script>` tag in `quiz.html` and `index.html`.

4. **localStorage keys are namespaced** with `thrive_v5_` prefix — any new persistent data should follow this convention.

5. **CSS variables are defined in `:root`** and should be used for all colours, spacing, and typography — do not hardcode `#218F52` etc. directly.

6. **Admin PIN** is stored as `btoa('thrive-2025-admin')` in `js/main.js`. Do not move or expose this in plaintext.

---

## Quick Validation After Any Changes

```bash
# 1. Validate quiz bank (from repo root)
node -e "
const fs=require('fs');
const code=fs.readFileSync('js/quiz-bank.js','utf8');
const vm=require('vm');
const ctx={window:{},console:{log:m=>console.log(m)}};
vm.createContext(ctx);
vm.runInContext(code,ctx);
const q=ctx.window.SITE_CONFIG.QUIZZES;
const t=q[0].questions.length,f=q[1].questions.length,tot=t+f;
console.log('Tech:',t,'('+Math.round(t/tot*100)+'%) | Football:',f,'('+Math.round(f/tot*100)+'%) | Total:',tot);
console.log('Sessions: Tech='+q[0].sessionSize+' Football='+q[1].sessionSize);
let bad=0;
[...q[0].questions,...q[1].questions].forEach(qq=>{
  if(!qq||!qq.q||!qq.options||qq.options.length!==4||qq.answer===undefined||!qq.explanation) bad++;
});
console.log(bad===0?'ALL VALID':'ISSUES: '+bad);
"

# 2. Check CSS is not broken (just a syntax check via Node)
node -e "
const css=require('fs').readFileSync('css/style.css','utf8');
const opens=css.split('{').length-1;
const closes=css.split('}').length-1;
console.log(opens===closes?'CSS brackets balanced':'MISMATCH: '+opens+' opens vs '+closes+' closes');
"

# 3. Deploy
git add js/quiz-bank.js quiz.html css/style.css index.html QUIZ_TOPIC_REFERENCE.md THRIVE_ADMIN_GUIDE.md
git commit -m "feat: v5.3 — 532 questions (373 tech 70% / 159 football 30%), enhanced UX, study book with answers"
git push origin main
```

---

## Deliverables Available for Download

| File | Description |
|------|-------------|
| `thrive-v5.zip` | Complete deployable site package — extract and push to GitHub |
| `THRIVE_ADMIN_GUIDE.md` | Admin PIN, access steps, localStorage key reference |
| `THRIVE_Study_Book.docx` | 15-chapter study book as Word document |
| `QUIZ_TOPIC_REFERENCE.md` | Same study book as markdown |
| `GITHUB_UPDATE_GUIDE.md` | Exact git commands to deploy |
| `THRIVE_V5_3_UPDATE_REVIEW.md` | Full technical review of every change made |

---

*Prepared for handoff from Claude.ai Chat → Claude Code*
*THRIVE — Technology, Hard work, Resilience, Innovation, Vision, and Excellence*
