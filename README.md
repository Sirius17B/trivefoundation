# THRIVE Website — Developer Documentation

**Version:** 4.0  
**Last updated:** March 2026  
**Maintainer:** Chisom Okoye  
**Stack:** Pure HTML · CSS · Vanilla JavaScript (no build tools, no frameworks)

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [File Structure](#2-file-structure)
3. [How to Run Locally](#3-how-to-run-locally)
4. [Configuration — The Single Source of Truth](#4-configuration--the-single-source-of-truth)
5. [Renaming the Organisation](#5-renaming-the-organisation)
6. [Pages Reference](#6-pages-reference)
7. [JavaScript Engines](#7-javascript-engines)
8. [Admin System & CMS](#8-admin-system--cms)
9. [Quiz System](#9-quiz-system)
10. [League & Tech Leaderboards](#10-league--tech-leaderboards)
11. [Video Upload & Playback](#11-video-upload--playback)
12. [Gallery](#12-gallery)
13. [Donation System](#13-donation-system)
14. [CSS Design System](#14-css-design-system)
15. [Accessibility](#15-accessibility)
16. [Security](#16-security)
17. [Storage — How Data Persists](#17-storage--how-data-persists)
18. [How to Add a New Page](#18-how-to-add-a-new-page)
19. [How to Add a New Quiz](#19-how-to-add-a-new-quiz)
20. [How to Update the Team](#20-how-to-update-the-team)
21. [Deploying to a Live Server](#21-deploying-to-a-live-server)
22. [Known Limitations & Future Work](#22-known-limitations--future-work)
23. [Contributing Guidelines](#23-contributing-guidelines)

---

## 1. Project Overview

THRIVE is an independent youth development initiative that runs technology training, football leagues, and inspirational talks for young Nigerians. This website is its public face and operational hub.

### What the website does

- **Public pages:** Homepage, About, Activities, Gallery, Contact, Donate
- **Live leaderboards:** Football (boys + girls leagues) and Tech Rankings with real-time tables
- **Quiz Arena:** Timed, structured knowledge quizzes with a leaderboard
- **Video section:** Upload and watch programme recordings
- **Admin CMS:** Any authorised admin can log in via a PIN and edit all text, images, stats, and quiz questions directly in the browser — no server needed

### Design principles

- **Zero dependencies.** No React, no Node, no build step. Open `index.html` in any browser and it works.
- **Config-driven.** All content defaults live in `js/config.js`. Change one file, change everything.
- **Accessible.** Semantic HTML, ARIA roles, descriptive alt texts, keyboard navigation throughout.
- **Mobile-first.** Every layout is designed for phones first, then scaled up.

---

## 2. File Structure

```
thrive-website/
│
├── index.html            Homepage
├── about.html            About the organisation + team
├── activities.html       The three programme pillars
├── league.html           Football & Tech leaderboards (full admin)
├── quiz.html             Timed quiz arena
├── videos.html           Video upload & playback
├── gallery.html          Photo gallery with filters
├── donate.html           Donation tiers & bank details
├── contact.html          Contact form + volunteer/sponsor info
│
├── assets/
│   ├── tree-logo.png     The organisation logo image (replace to rebrand)
│   ├── logo.svg          Fallback SVG logo (used as favicon)
│   └── uploads/          Placeholder folder for any local assets
│
├── css/
│   └── style.css         All styles — design tokens, layout, components
│
├── js/
│   ├── config.js         ★ ALL content defaults live here — start here
│   ├── components.js     Shared nav, footer, logo, admin UI injection
│   └── main.js           All JS engines: carousel, league, CMS, quiz, video, auth
│
└── README.md             This file
```

### Load order on every page

Every HTML page loads scripts in this exact order at the bottom of `<body>`:

```html
<script src="js/config.js"></script>       <!-- 1. Content defaults -->
<script src="js/components.js"></script>   <!-- 2. Shared UI (nav, footer, admin UI) -->
<script src="js/main.js"></script>         <!-- 3. All engines -->
<script>
  /* 4. Page-specific init */
  injectNav();
  injectAdminUI();
  injectFooter();
  /* ... page logic ... */
</script>
```

---

## 3. How to Run Locally

No installation required.

```bash
# Option A — just open the file
open thrive-website/index.html

# Option B — run a local server (recommended, avoids some browser restrictions)
cd thrive-website
python3 -m http.server 8080
# Then visit http://localhost:8080
```

> **Why a server?** Some browsers block `window.storage` when files are opened directly from disk (`file://`). A local server fixes this so the CMS, quiz leaderboard, and video storage all work correctly during development.

---

## 4. Configuration — The Single Source of Truth

**`js/config.js`** is the only file you need to edit for most content changes. It exports a single global object: `window.SITE_CONFIG`.

### Full config reference

```js
window.SITE_CONFIG = {

  // ── IDENTITY ────────────────────────────────────────────
  ORG_NAME:      'THRIVE',           // Used everywhere — nav, footer, titles
  ORG_TAGLINE:   'Raising Champions',
  ORG_YEAR:      '2026',
  ORG_SEASON:    'A Time To Build',  // Hero sub-heading
  ORG_MISSION:   'Empowering youth through technology, sport, and inspiration.',
  ORG_EMAIL:     'hello@thriveng.org',
  ORG_PHONE:     '+234 800 000 0000',
  ORG_VENUE_2025:'FGC NISE, Anambra State, Nigeria', // Venue only — not owner

  // ── HERO ─────────────────────────────────────────────────
  HERO_LINE1:    'A Time',           // First line of big hero headline
  HERO_LINE2:    'To Build',         // Second line (shown in italic green)
  HERO_EYEBROW:  'Now Active · 2026 Season',
  HERO_BODY:     '...',              // Hero paragraph text

  // ── STATS BAR ────────────────────────────────────────────
  STATS: {
    youth:    { value: 120, label: 'Youth Trained',     suffix: '+' },
    hours:    { value: 48,  label: 'Event Hours',       suffix: ''  },
    partners: { value: 6,   label: 'Partners & Donors', suffix: ''  },
  },
  // Change value: to update the animated number on the homepage

  // ── DONATION TIERS ───────────────────────────────────────
  DONATION_TIERS: [
    { label: 'Seed',    amount: '₦10,000',  desc: 'Materials for one student' },
    { label: 'Sapling', amount: '₦50,000',  desc: 'Sponsor a full tech session' },
    { label: 'Tree',    amount: '₦150,000', desc: 'Fund one event day', featured: true },
    { label: 'Forest',  amount: '₦400,000', desc: 'Sponsor a school edition' },
  ],
  // featured: true makes that tier visually highlighted

  // ── BANK DETAILS ─────────────────────────────────────────
  BANK: {
    account_name: 'THRIVE Foundation',
    bank:         'First Bank of Nigeria',
    account_no:   '3012345678',
    sort_code:    '011152003',
    note:         'Use your full name as the payment reference.',
  },

  // ── GALLERY IMAGES ───────────────────────────────────────
  GALLERY: [
    {
      src:   'https://...',           // Image URL (Unsplash or your own)
      alt:   'Description for screen readers', // REQUIRED for accessibility
      label: 'Caption shown on hover',
      tag:   'football'              // 'football' | 'tech' | 'community'
    },
    // ... more items
  ],

  // ── QUIZ SETTINGS ────────────────────────────────────────
  QUIZ_SETTINGS: {
    passMark:          50,    // % score needed to pass
    showExplanations:  true,  // Show answer explanation after each question
    shuffleQuestions:  true,  // Randomise question order
    shuffleOptions:    false, // Randomise option order (A/B/C/D)
  },

  // ── QUIZZES ──────────────────────────────────────────────
  QUIZZES: [
    {
      id:          'tech-general', // Unique ID — used for leaderboard storage
      title:       'Tech Challenge',
      category:    'tech',         // 'tech' | 'football'
      timeMinutes: 20,
      description: 'Short description shown on the quiz card.',
      questions: [
        {
          q:           'Question text here?',
          options:     ['Option A', 'Option B', 'Option C', 'Option D'],
          answer:      0,           // Index of correct option (0 = A, 1 = B, etc.)
          explanation: 'Optional explanation shown after answering.'
        },
        // ... more questions
      ],
    },
    // ... more quizzes
  ],

  // ── TEAM ─────────────────────────────────────────────────
  TEAM: [
    {
      name:  'Chisom Okoye',
      role:  'Founder & Programme Director',
      color: '#0A3D2E',   // Avatar background colour (if no photo)
      photo: 'https://...' // URL to photo, or '' for initials avatar
    },
    // ... more members
  ],

  // ── HIGHLIGHTS CAROUSEL ──────────────────────────────────
  HIGHLIGHTS: [
    {
      img:      'https://...',   // Card image URL
      alt:      'Description',   // Alt text for accessibility
      tag:      'football',      // 'football' | 'tech' | 'community'
      tagLabel: 'Football',      // Display text for the tag badge
      title:    'Card headline',
      date:     'THRIVE 2025',
    },
    // ... up to ~8 items recommended
  ],
};
```

---

## 5. Renaming the Organisation

To rename from "THRIVE" to anything else:

**Step 1** — Open `js/config.js` and change:
```js
ORG_NAME: 'THRIVE',  →  ORG_NAME: 'YOUR NEW NAME',
```

**Step 2** — That's it. Every `[data-org-name]` element across the site reads from this value at runtime. The nav logo wordmark, footer copyright, page titles, and all references update automatically.

**Step 3 (optional)** — If you want to update the `<title>` tags in the HTML files too, do a find-and-replace for `THRIVE` across all `.html` files. This only affects the browser tab label before JavaScript runs.

> **Logo image:** The logo image itself (`assets/tree-logo.png`) is separate. Replace that file with a new one if you need a different icon. Keep the filename the same, or update the reference in `js/components.js` in the `LOGO_SVG()` function.

---

## 6. Pages Reference

| File | Purpose | Admin features |
|---|---|---|
| `index.html` | Homepage — hero, stats, carousel, leaderboards, activities | Inline text editing |
| `about.html` | Story, values, team | Inline text editing, team from config |
| `activities.html` | Three pillars: Tech, Football, Talks | Inline text editing |
| `league.html` | Full leaderboards + admin result/team entry | Full league admin, CMS panel |
| `quiz.html` | Quiz arena — timed tests, leaderboard | Add/edit/delete questions |
| `videos.html` | Video library | Upload, delete videos |
| `gallery.html` | Photo gallery with tag filter | Add/delete images |
| `donate.html` | Bank details, donation tiers | Inline text editing |
| `contact.html` | Contact form, volunteer/sponsor info | Inline text editing |

---

## 7. JavaScript Engines

All engines live in `js/main.js` as global objects on `window`.

### `LeagueEngine` — Football league management

```js
// Load data for a league from storage
await LeagueEngine.load('boys');   // or 'girls'

// Get current data
const data = LeagueEngine.get('boys');
// Returns: { teams: ['Team A', ...], results: [{home, away, hg, ag}, ...] }

// Add a match result
LeagueEngine.addResult('boys', 'SS3 Boys', 'JSS3 Boys', 4, 3);

// Remove a result by index
LeagueEngine.removeResult('boys', 0);

// Add / remove a team
LeagueEngine.addTeam('boys', 'New Team');
LeagueEngine.removeTeam('boys', 'New Team');

// Get sorted standings table
const table = LeagueEngine.buildTable('boys');
// Returns array of: { name, p, w, d, l, gf, ga, gd, pts, form }
// Sorted by: pts → gd → gf
```

### `TechEngine` — Tech rankings

```js
await TechEngine.load();

// Get all participants
const all = TechEngine.get().participants;

// Get top N sorted by score
const top5 = TechEngine.getTop(5);

// Add / remove participant
TechEngine.add('Amara Okafor', 'SS3', 92, 'Weather App');
TechEngine.remove(0); // by index
```

### `VideoEngine` — Video library

```js
await VideoEngine.load();

// Get all videos
const videos = VideoEngine.get();
// Each video: { title, dataUrl, type, date }

// Add a video (dataUrl from FileReader)
VideoEngine.add('Boys Final', dataUrl, 'video/mp4');

// Remove by index
VideoEngine.remove(0);
```

### `CMS` — Content management

```js
await CMS.load();   // Load saved overrides from storage

CMS.apply();        // Apply all overrides to the current DOM

CMS.get('hero_line1', 'Default text');   // Read a value
CMS.set('hero_line1', 'New text');       // Write a value (also saves)
```

**CMS keys** (what `data-cms="..."` attributes reference):

| Key | Location | Default |
|---|---|---|
| `hero_line1` | Hero headline line 1 | "A Time" |
| `hero_line2` | Hero headline line 2 | "To Build" |
| `hero_body` | Hero paragraph | config HERO_BODY |
| `hero_quote` | Parallax quote text | Van Moody quote |
| `hero_quote_cite` | Quote attribution | "— Van Moody" |
| `org_name` | Organisation name everywhere | config ORG_NAME |
| `org_tagline` | Tagline | config ORG_TAGLINE |
| `footer_tagline` | Footer brand text | "Raising the next generation..." |
| `footer_quote` | Footer italic quote | "Every living being..." |
| `stat_youth_count` | Youth trained number | config STATS.youth.value |
| `stat_hours_count` | Event hours number | config STATS.hours.value |
| `stat_partners_count` | Partners number | config STATS.partners.value |
| `donate_title` | Donate page heading | — |
| `donate_sub` | Donate page subtext | — |

### `AdminAuth` — Authentication

```js
AdminAuth.isLoggedIn();       // true/false
AdminAuth.login('2025');      // returns true, 'locked', or false
AdminAuth.logout();           // clears session

// Change the PIN:
// 1. Open js/main.js
// 2. Find the line: const _AH = btoa('thrive-2025-admin');
// 3. Replace '2025' with your new PIN
// 4. Save the file
```

> **Security note:** This is a client-side PIN for convenience — suitable for a small team's internal tool. For a public-facing admin system handling sensitive data, replace this with server-side authentication (Firebase Auth, Supabase, etc.).

### `initCarousel(selector)` — Carousel

```js
initCarousel('#main-carousel');
// Reads .c-card children inside .carousel-viewport
// Auto-plays every 4.8s, pauses on hover
// Supports touch swipe and keyboard arrow keys
// Arrow buttons + dots auto-generated
```

### `initCounters()` — Animated stats

Called once on page load. Finds all `[data-count]` elements and animates their value from 0 to the target number when they scroll into view.

```html
<span data-count="120" data-suffix="+">120+</span>
```

---

## 8. Admin System & CMS

### How to log in

1. Click the **Admin** button in the top-right of the navigation bar on any page
2. Enter the PIN (default: `2025`)
3. Click **Sign In**

### What happens after login

- The nav button turns green and says **Edit Content**
- A green toolbar appears at the bottom of every page
- Every editable text element gets a dashed green outline — **click any of them to edit directly**
- Every editable image gets an orange dashed outline — **click to replace with a new image from your device**
- Changes auto-save to browser storage as you edit
- Click **Save All Changes** in the toolbar to make sure everything is saved

### Site Settings panel

Click **Site Settings** in the toolbar to open a full settings panel with tabs:

| Tab | What you can change |
|---|---|
| **Identity** | Organisation name, tagline, mission, email |
| **Homepage** | Hero headline (both lines), body text, quote, quote author |
| **Stats** | Youth trained, event hours, partners — both number and label |
| **Donate** | Donate page title, subtitle, payment reference note |
| **Footer** | Footer tagline, footer quote |

### Logging out

Click the **Log Out** button in the bottom toolbar. The session clears and edit mode deactivates. Because the session uses `sessionStorage`, it also clears automatically when the browser tab is closed.

### Changing the admin PIN

Open `js/main.js` and find this line near line 220:

```js
const _AH = btoa('thrive-2025-admin');
```

Change `'2025'` to your new PIN:

```js
const _AH = btoa('thrive-NEWPIN-admin');
```

The format must stay as `'thrive-' + PIN + '-admin'`. Save the file and redeploy.

---

## 9. Quiz System

### How it works

1. Quizzes are defined in `js/config.js` under `QUIZZES`
2. When a user starts a quiz, questions are loaded (optionally shuffled) and a countdown timer starts
3. Each question shows 4 options (A/B/C/D). The user selects one, sees if they're right, and optionally reads an explanation
4. At the end, the score is shown and the user can optionally enter their name for the leaderboard
5. Scores are stored per-quiz in browser storage

### Adding a quiz via code

Add a new object to the `QUIZZES` array in `config.js`:

```js
{
  id:          'history-general',   // Must be unique — used as storage key
  title:       'History Quiz',
  category:    'tech',              // 'tech' | 'football' (controls badge colour)
  timeMinutes: 10,
  description: 'Test your knowledge of world history.',
  questions: [
    {
      q:           'In what year did Nigeria gain independence?',
      options:     ['1957', '1960', '1963', '1966'],
      answer:      1,               // 0=A, 1=B, 2=C, 3=D
      explanation: 'Nigeria gained independence from Britain on October 1, 1960.'
    },
  ],
}
```

### Adding questions via the admin UI

1. Log in as admin on `quiz.html`
2. Click **Show Question Editor**
3. Select the quiz from the dropdown
4. Click **+ Add Question**
5. Fill in the question, four options, correct answer, and optional explanation
6. Click **Save Question**

Admin-added questions are stored in browser storage and persist across sessions. They layer on top of (or replace) the defaults from `config.js`.

### Quiz leaderboard

Scores are stored per quiz ID. The top 20 scores per quiz are kept. The leaderboard is visible to all visitors at the bottom of `quiz.html`.

---

## 10. League & Tech Leaderboards

### Football league

The league uses a standard points system: Win = 3 pts, Draw = 1 pt, Loss = 0 pts. Tables are sorted by: Points → Goal Difference → Goals For.

**To add a result (admin):**
1. Go to `league.html`
2. Log in as admin
3. Select Boys or Girls league
4. Type the home team, home goals, away goals, away team
5. Click **Add**

The table updates instantly. Results are saved to browser storage.

**To manage teams:**
- Admin can add new teams manually, or they are auto-created when a result is entered
- Removing a team also removes all their results

### Tech rankings

Participants are scored out of 100 based on project quality.

**To add a participant (admin):**
1. Go to `league.html` → Tech Rankings tab
2. Log in as admin
3. Fill in Name, Class, Project Name, Score
4. Click **Add**

---

## 11. Video Upload & Playback

Videos are uploaded on `videos.html` by an admin and stored as base64 data URLs in browser storage.

**To upload a video:**
1. Log in as admin
2. Go to `videos.html`
3. Enter a title (optional — defaults to filename)
4. Click the upload zone or drag a video file onto it
5. A progress bar shows loading status
6. The video appears in the grid and is playable by all visitors

**File size:** Maximum 200 MB per video. This limit exists because videos are stored in browser storage — very large libraries may hit storage limits. For a production site with many videos, use an external video host (YouTube, Vimeo, Cloudflare Stream) and embed the URL instead.

**Supported formats:** MP4 (recommended), WebM, MOV, OGG

---

## 12. Gallery

Gallery images are defined in `config.js` under `GALLERY`. Each item needs:

```js
{
  src:   'https://your-image-url.jpg',
  alt:   'Descriptive text for screen readers — always required',
  label: 'Caption shown on hover',
  tag:   'football'   // 'football' | 'tech' | 'community'
}
```

To use your own photos instead of Unsplash:
1. Upload photos to a hosting service (Cloudinary, Imgur, your own server)
2. Replace the `src` URL with your image URL
3. Update the `alt` description to match the actual photo

**Adding/removing via admin:** On `gallery.html`, when logged in as admin, you'll see an **Add Image** button and a **Remove** button on each image.

---

## 13. Donation System

### Tiers

Defined in `config.js` under `DONATION_TIERS`. Four tiers by default. The `featured: true` flag highlights one tier visually.

The tiers appear in two places:
- As clickable chips on the homepage hero CTA (right panel)
- As full cards on `donate.html`

### Bank details

Defined in `config.js` under `BANK`. Shown on `donate.html` with a copy-to-clipboard button for the account number.

**To update bank details:** Edit the `BANK` object in `config.js`. You can also update some fields via Admin → Site Settings → Donate.

---

## 14. CSS Design System

All styles are in `css/style.css`. The system uses CSS custom properties (variables) defined in `:root`.

### Colour palette

```css
/* Brand greens — from the tree logo leaves */
--c-forest:   #1A3D2B   /* Dark backgrounds, nav, footer */
--c-green:    #2E7D4F   /* Primary brand green */
--c-green-lt: #3DB870   /* Hover states, accents */
--c-green-xl: #C6EDD6   /* Tinted panels */

/* Teal — secondary action colour */
--c-teal:     #1B7B78
--c-teal-lt:  #25A89F

/* Orange — call-to-action energy */
--c-orange:   #E8621A
--c-orange-lt:#F5874A

/* Amber — warmth, stats highlights */
--c-amber:    #D4940A
--c-amber-lt: #F5C842

/* Neutrals — warm to echo the logo */
--c-cream:    #F8F4EE   /* Page background */
--c-sand:     #EDE7DC   /* Card/panel backgrounds */
--c-white:    #FFFFFF
--c-text:     #1C2B1C   /* Body text */
--c-muted:    #5C6E5C   /* Placeholder / secondary text */
--c-border:   #D8E5D8

/* Dark backgrounds */
--c-dark:     #132D1F
--c-mid:      #1E4434
--c-brown:    #6B3D1E   /* Trunk accent — used sparingly */
```

### Typography

```css
--fd: 'Playfair Display', Georgia, serif    /* Display / headings */
--fb: 'DM Sans', system-ui, sans-serif      /* Body text */
```

Both fonts are loaded from Google Fonts. If offline, they fall back to Georgia and system-ui respectively.

### Spacing

```css
--pad: clamp(16px, 5vw, 60px)   /* Universal horizontal padding */
```

Used as `padding: 0 var(--pad)` on all full-width sections. Scales from 16px on small phones to 60px on wide screens.

### Border radii

```css
--r-sm: 6px
--r-md: 12px
--r-lg: 20px
--r-xl: 28px
```

### Breakpoints

| Breakpoint | Behaviour |
|---|---|
| `≥ 1440px` | Generous padding scales up |
| `≤ 960px` | Hero collapses to single column, sidebar CTA hidden |
| `≤ 640px` | Mobile nav drawer, stacked grids, smaller padding |
| `≤ 380px` | Minimum padding (12px), donation tiers stack |

### Utility classes

```css
.fade-up              /* Animates element up into view on scroll */
.text-center          /* text-align: center */
.grid-2 / .grid-3 / .grid-4   /* Responsive CSS grid shortcuts */
.overflow-x-auto      /* Horizontal scroll wrapper */
.btn                  /* Base button styles */
.btn-primary          /* Orange CTA button */
.btn-green            /* Green action button */
.btn-teal             /* Teal secondary button */
.btn-outline          /* Transparent with border */
.btn-sm               /* Smaller button */
.btn-full             /* Full width button */
.fi                   /* Form input field */
.admin-only           /* Hidden by default, shown when admin is logged in */
.eyebrow              /* Small all-caps label above headings */
.lead                 /* Larger intro paragraph */
```

---

## 15. Accessibility

This site follows WCAG 2.1 AA guidance:

- All images have descriptive `alt` attributes (or `alt=""` for decorative images with `aria-hidden="true"`)
- Semantic HTML: `<header>`, `<main>`, `<nav>`, `<section>`, `<article>`, `<footer>`
- ARIA roles and labels on interactive elements (`role="dialog"`, `aria-modal`, `aria-label`)
- Colour contrast ratios meet AA standards
- Focus management: modals trap focus when open
- Keyboard navigation: all interactive elements reachable by Tab, Enter, Space, Escape
- Skip-to-content link on homepage
- Live regions (`aria-live="polite"`) on toast notifications and error messages
- Form labels associated with their inputs

**When adding new content**, always:
- Add `alt` text to every `<img>` (describe what's in the image)
- Use heading levels in order (h1 → h2 → h3, never skip)
- Add `aria-label` to icon-only buttons
- Test keyboard navigation — can you use the feature without a mouse?

---

## 16. Security

- **X-Frame-Options:** Set via meta tag to prevent clickjacking
- **X-Content-Type-Options:** Prevents MIME sniffing
- **Referrer-Policy:** Limits referrer data sent to third parties
- **Input sanitisation:** All user input passes through `sanitize()` before being inserted into the DOM as HTML, preventing XSS
- **Admin PIN:** Hashed with `btoa()` and compared — protects against casual snooping in source code, though not cryptographically strong. See note in [Admin System](#8-admin-system--cms)
- **Rate limiting:** 5 failed login attempts locks the login form for 60 seconds
- **No third-party trackers:** No Google Analytics, Facebook Pixel, or other tracking scripts

---

## 17. Storage — How Data Persists

This site uses `window.storage` (provided by the Claude.ai hosting environment). It works like a simple key-value store:

```js
await window.storage.set('my-key', 'my-value');
const result = await window.storage.get('my-key');
console.log(result.value); // 'my-value'
```

**What is stored:**

| Storage key | Contents |
|---|---|
| `thrive_league_v3_boys` | Boys league teams and results |
| `thrive_league_v3_girls` | Girls league teams and results |
| `thrive_tech_v2_` | Tech rankings participants |
| `thrive_videos_v1_list` | Uploaded video data |
| `thrive_cms_v1_data` | Admin CMS overrides |
| `thrive_quizzes_v1` | Admin-edited quiz questions |
| `thrive_quiz_lb_v1` | Quiz leaderboard scores |

**If deployed outside Claude.ai:** Replace `window.storage` with your own backend or `localStorage`. The simplest swap:

```js
// Drop this in before config.js loads:
window.storage = {
  async get(key) { const v = localStorage.getItem(key); return v ? {value:v} : null; },
  async set(key, value) { localStorage.setItem(key, value); return {value}; },
  async delete(key) { localStorage.removeItem(key); return {deleted:true}; },
  async list(prefix) { const keys = Object.keys(localStorage).filter(k=>k.startsWith(prefix||'')); return {keys}; },
};
```

---

## 18. How to Manage the News & Stories Feed

The Activities page has a live news feed showing the latest programme stories. Stories appear newest-first, with the top story shown as the main featured article.

### Adding a story via admin UI

1. Go to `activities.html`, log in as admin
2. Click **Add Story**
3. Fill in: headline, date, category (Announcement/Tech/Football/Event), image URL (optional), and story body
4. Click **Save Story**

The new story is added to the top of the list automatically.

### Editing or reordering stories

When logged in as admin, every story has an **Edit this story** button on the featured panel, and the editor panel at the bottom shows all stories with **↑ ↓** buttons to change order.

### Adding a story via config.js (bulk/developer)

Add objects to the `STORIES` array in `js/config.js`. Newest entries should be **first** in the array:

```js
STORIES: [
  {
    id:       'story-2026-04',     // Unique — no spaces
    date:     'April 2026',
    headline: 'THRIVE Expands to Lagos',
    category: 'Announcement',      // Announcement | Tech | Football | Event
    body:     'Full story text…',
    image:    'https://…',         // Optional image URL
    imageAlt: 'Description for screen readers',
    featured: false,
  },
  // … older stories follow
]
```

---

## 19. How to Add a New Page

1. Copy the structure from a simple page like `about.html`
2. Update the `<title>` and `<meta name="description">`
3. Keep the same script loading order at the bottom
4. Call `injectNav()`, `injectAdminUI()`, `injectFooter()` in your init script
5. Add your page content between `<main>` and `</main>`
6. Add a nav link in `js/components.js` — find the `injectNav` function and add:
   ```html
   <a href="your-page.html" class="nav-link">Your Page</a>
   ```
   Add it in both the desktop `nav-links` and the mobile hamburger menu sections.

---

## 20. How to Add a New Quiz

**Via code (recommended for bulk questions):**

Add a new object to `QUIZZES` in `js/config.js`:

```js
{
  id:          'science-basics',    // Unique — no spaces
  title:       'Science Quiz',
  category:    'tech',             // Controls badge colour
  timeMinutes: 15,
  description: 'Test your knowledge of basic science.',
  questions: [
    {
      q:       'What planet is closest to the Sun?',
      options: ['Venus', 'Earth', 'Mercury', 'Mars'],
      answer:  2,          // Mercury = index 2
      explanation: 'Mercury is the closest planet to the Sun.'
    },
    // Add as many questions as needed
  ],
}
```

**Via the admin UI:**

1. Go to `quiz.html`, log in as admin
2. Click **Show Question Editor**
3. Use the dropdown to pick a quiz, or add to any existing quiz
4. Click **+ Add Question** to add questions one at a time

---

## 21. How to Update the Team

Edit the `TEAM` array in `js/config.js`:

```js
TEAM: [
  {
    name:  'Full Name',
    role:  'Their Role',
    color: '#0A3D2E',    // Hex colour for initials avatar background
    photo: 'https://...' // Leave as '' to use initials avatar instead
  },
]
```

The team renders automatically on `about.html`. No HTML changes needed.

---

## 22. Deploying to a Live Server

This site is fully static — it can be hosted anywhere that serves HTML files.

### Option A — Netlify (free, recommended)

1. Create a free account at [netlify.com](https://netlify.com)
2. Drag and drop the `thrive-website/` folder onto the Netlify dashboard
3. Your site is live instantly at a `*.netlify.app` URL
4. To connect a custom domain: Site settings → Domain management

### Option B — GitHub Pages (free, see GitHub guide below)

See the GitHub section at the end of this document.

### Option C — Any web host (cPanel, etc.)

Upload all files to the `public_html` folder via FTP or the file manager. The entry point is `index.html`.

### After deploying

If you deploy outside Claude.ai, `window.storage` will not exist. Add the `localStorage` shim from [Section 17](#17-storage--how-data-persists) to make all data persistence work.

---

## 23. Known Limitations & Future Work

| Limitation | Details | Suggested fix |
|---|---|---|
| **Client-side admin PIN** | The PIN is a light convenience lock, not cryptographic security | Migrate to Firebase Auth or Supabase |
| **Video storage size** | Videos stored as base64 in browser storage — large libraries will hit limits | Host videos on YouTube/Vimeo, embed by URL |
| **No email on contact form** | Contact form has client-side validation but no backend | Add Netlify Forms or Formspree action |
| **No real-time multi-user** | Two admins editing at the same time will overwrite each other | Add a backend (Firebase Firestore, etc.) |
| **Quiz: no per-user accounts** | Leaderboard names are self-reported | Add authentication for verified scores |
| **Images are Unsplash URLs** | External URLs could break if Unsplash changes | Upload real photos and host them locally |

---

## 24. Contributing Guidelines

### Getting the code

```bash
git clone https://github.com/YOUR-USERNAME/thrive-website.git
cd thrive-website
```

### Making changes

There is no build step. Edit the files directly.

```
js/config.js       → Content changes (text, images, team, quiz questions)
css/style.css      → Visual/design changes
js/components.js   → Nav, footer, admin modal
js/main.js         → Feature logic (carousel, engines, auth)
*.html             → Page structure
```

### Before submitting a change

- [ ] Test in Chrome and Firefox
- [ ] Test on a phone (or use browser dev tools → mobile emulation)
- [ ] Check that the admin login still works and CMS saves/loads correctly
- [ ] Make sure all images have `alt` text
- [ ] Check that the JavaScript `sanitize()` function wraps any user-supplied content before it touches the DOM
- [ ] Run a bracket balance check: `python3 -c "s=open('js/main.js').read(); print(s.count('{') - s.count('}'))"`  — should print `0`

### Code style

- Use `'use strict'` at the top of every script block
- Sanitise all user input with `window.sanitize()` before DOM insertion
- Keep functions focused — one job each
- Add a comment above any function that isn't immediately obvious
- CSS: add new component styles before the `/* ── RESPONSIVE ── */` block, not after it

### Commit message format

```
fix: carousel arrows overlapping on small screens
feat: add Science quiz to config
content: update bank account number
style: adjust hero heading size on mobile
docs: update README contributing section
```

---

*This documentation was written for THRIVE v4.0. If you make significant structural changes, please update the relevant sections.*
