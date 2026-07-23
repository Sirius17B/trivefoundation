# THRIVE Website — v5

**Stack:** Pure HTML · CSS (custom design system) · Vanilla JavaScript  
**No build tools. No frameworks. Open `index.html` in any browser.**

---

## Quick Start

```bash
cd thrive-v5
python3 -m http.server 8080
# Open http://localhost:8080
```

## Rebrand in 60 seconds

Open `js/config.js` and change:
```js
ORG_NAME:    'THRIVE',       // → 'Your New Name'
ORG_TAGLINE: 'Raising Champions',
ORG_EMAIL:   'hello@thrivefoundation.org',
```
Every page — nav, footer, titles, leaderboards — updates automatically.

## Admin PIN

Default PIN: `2025`  
To change: open `js/main.js`, replace `btoa('thrive-2025-admin')` with `btoa('thrive-NEWPIN-admin')`.

## File Structure

```
thrive-v5/
├── index.html          Homepage
├── about.html          About + team
├── activities.html     Pillars, news feed, hub links
├── league.html         Football leagues + tech rankings
├── quiz.html           Quiz arena + leaderboard
├── gallery.html        Photos + videos
├── donate.html         Donation tiers + bank details
├── contact.html        Contact form
├── privacy.html        Privacy policy
├── terms.html          Terms & guidelines
├── videos.html         Redirect → gallery.html#videos
│
├── js/
│   ├── config.js       ★ All content defaults — start here
│   ├── quiz-bank.js    60 tech + 60 football curriculum questions
│   ├── components.js   Nav, footer, admin UI
│   └── main.js         Engines: league, tech, video, CMS, auth, carousel
│
├── css/
│   └── style.css       Design system (white/light theme, Sora + Inter)
│
├── assets/             Logo files
├── netlify/functions/  contact.js + donor-confirmation.js
├── scripts/            static_checks.py
└── tests/              Playwright smoke tests (scaffold)
```

## QA

```bash
python3 scripts/static_checks.py
```

Checks: one `<title>` per page, one meta description, one canonical, no broken internal links, no missing image alt attributes, required files present.

## Deploy

- **Netlify:** Drag-and-drop the folder at netlify.com → live instantly
- **GitHub Pages:** See `GITHUB_GUIDE.md`
- **Any static host:** Upload all files; entry point is `index.html`

## Storage

Uses `window.storage` (Claude.ai hosting). For external deployment, add this shim before `config.js`:

```js
window.storage = {
  async get(key)      { const v=localStorage.getItem(key); return v?{value:v}:null; },
  async set(key,val)  { localStorage.setItem(key,val); return {value:val}; },
  async delete(key)   { localStorage.removeItem(key); return {deleted:true}; },
  async list(prefix)  { const k=Object.keys(localStorage).filter(k=>k.startsWith(prefix||'')); return {keys:k}; },
};
```

## Documents

| File | Purpose |
|---|---|
| `GITHUB_GUIDE.md` | Step-by-step: push to GitHub, deploy, collaborate, rebrand |
| `QUIZ_TOPIC_REFERENCE.md` | Study guide covering all 120 quiz questions by topic |
| `BACKEND_DONOR_PRIVACY.md` | Architecture guide for production backend |
