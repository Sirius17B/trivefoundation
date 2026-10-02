# Handover — Trivefoundation brand refresh (October 2026)

**Purpose of this file.** A complete, honest record of what was changed, why, what was checked and what is still open, written so that another reviewer (a person, ChatGPT or any other assistant) can audit the work and improve it without having to rediscover anything.

**Base:** repository `Sirius17B/trivefoundation`, commit `57b9f51` ("Show a page-1 preview thumbnail for uploaded PDFs…"), live at `trivefoundation.netlify.app`.
**State of this work:** committed on the branch `brand-refresh-2026`. Not merged into `main`, not deployed.
**Companion files:** `BRAND.md` (the rules), `README.md` (developer documentation, sections 5 and 13 updated).

---

## 1. The brief

1. Take the new logo (TRIVE with a raised-arms figure as the I, "foundation" beneath; small changes to font/size/shape allowed) and build a consistent brand around it. Colours were undecided.
2. Apply it to the website: white or off-white background with the Trivefoundation theme colours.
3. Redesign the letterhead, and improve the school invitation letter so it is more official and better organised, adding the confirmed venue from the venue letter.
4. Document everything for review.

Standing rules carried over from earlier work: the organisation is **Trivefoundation**, the yearly programme is **THRIVE 2.0 / 3.0 …**; the Tech curriculum reads AI, Introduction to Robotics, Machine Learning, Software Programming & Applications; the organisation is independent of any venue; no emoji as icons; every image has alt text; stock photos show Black / African young people; the codebase stays simple (plain HTML/CSS/JS, no build step); the signature block of letters is kept as supplied.

---

## 2. Decisions, in one table

| Topic | Decision | Reason |
|---|---|---|
| Palette | Navy `#08365B`, green `#1C854B`, leaf `#45A24A`, sampled from the logo. Deep variants for text. Off-white `#F7FAF7`. One optional warm accent, sun `#F2A91E` | The logo already defines two colours; the brand should not add a third identity colour. Sun is confined to medals, the "talks" pillar and the focus ring, and can be switched off in one line (BRAND.md §3) |
| Dark vs light | Light everywhere. Navy only for the footer, the hero support card, the bank card, photo bands | The brief asked for white / off-white. The previous site was dark green with white text |
| Logo | Redrawn as vector paths with a transparent background. Lettering from Fredoka (TRIVE) and Quicksand (foundation); figure hand-traced | The supplied file was a raster image on white; a brand needs scalable, transparent, one-colour and reversed versions |
| Web fonts | Fredoka (headings) + Lexend (body), self-hosted | Fredoka ties headings to the logo. Self-hosting removes the Google Fonts dependency and lets the CSP tighten to `font-src 'self'` |
| Letter font | Calibri | Installed on recipients' machines; reads as formal |
| Organisation name spelling | "Trivefoundation" — one word, capital T only | Confirmed by the founder on 2 October 2026. The logo stacks it as TRIVE / foundation; running text is always one word. The site previously said "TriveFoundation" and the supplied letters "Trive Foundation" |
| Content width | Capped at 1200 px | Earlier instruction: follow layout best practice for line length |
| Pillar colours | Tech = green, Football = navy, Talks = sun | Replaces the previous teal / orange / purple |
| Old CSS variable names | Kept as aliases pointing to the new tokens | Avoids rewriting every page-level style block; nothing silently breaks |

---

## 3. What changed, file by file

### New files
| Path | What it is |
|---|---|
| `BRAND.md` | Brand guide |
| `HANDOVER.md` | This file |
| `assets/logo.svg`, `logo-white.svg`, `favicon.svg` | **Replaced** with the new logo (same filenames) |
| `assets/logo-mono-navy.svg`, `logo-mono-white.svg`, `logo-wordmark*.svg`, `logo-mark*.svg` | Extra logo variants |
| `assets/apple-touch-icon.png`, `icon-512.png`, `logo-1600.png`, `logo-white-1600.png` | PNG exports |
| `assets/fonts/fredoka-latin-wght.woff2`, `lexend-latin-wght.woff2`, `OFL.txt` | Self-hosted fonts and their licence text |
| `scripts/brand/build_logo.py`, `glyphs.py`, `fonts/*.woff2` | Script that regenerates every logo file; it reproduces `assets/logo.svg` byte for byte |

### Removed
- `assets/tree-logo.png` (old tree logo, 480 KB). No page references it any more.
- All `<meta http-equiv="X-Frame-Options">` tags. Browsers ignore that header in a meta tag and log a console error on every page (which also makes `tests/smoke.spec.js` fail). The real header is still sent from `_headers`.

### `css/style.css` — rewritten (580 → 558 lines)
- New token block (brand, surfaces, text, accent) and a "Legacy aliases" block mapping every old variable (`--c-forest`, `--c-teal`, `--ink-900`, `--green-600` …) to a brand token. `--c-ink`, which `resources.html` used but nobody defined, now exists.
- `@font-face` for the two self-hosted fonts; the Google Fonts `@import` is gone.
- Every component restyled for light backgrounds: nav (solid white, navy links, green Donate pill), hero (off-white; the photo now sits on the right and fades into the page; headline navy + green), stats (white card with coloured top ticks), carousel, leaderboards, activity cards, league tables, page headers (mint-to-paper gradient with a faint figure watermark), gallery, donate tiers, bank card, forms, modals, admin toolbar, buttons, footer (deep navy), toast.
- New utility classes: `.band-white/-paper/-mint/-sky/-navy`, `.ico-tech/-football/-talks`, `.bar-*`, `.value-card`, `.hero-note`, `.lb-empty`, `.link`, `.btn-ghost` (was used by the quiz pages but never defined), `.btn-danger`, `.cms-toolbar`.
- The duplicated "2026 holistic visual refresh" override block at the end of the old file was folded into the main rules.
- Mobile menu breakpoint raised from 640 px to 860 px (seven links did not fit on small tablets).
- Leaderboard strip on desktop: 2 columns from 1024 px, 4 from 1240 px (it was 3 columns for 4 boards).
- Print rules hide nav, footer and admin toolbar.

### `js/components.js`
- `LOGO_SVG()` now returns an `<img>` of `assets/logo.svg` (light) or `logo-white.svg` (navy) instead of the tree PNG plus a Georgia wordmark.
- Nav uses the colour logo; `id="nav-menu"` added so the hamburger's `aria-controls` points at something real.
- Admin login, edit toolbar and Site Settings panel recoloured through classes/tokens; behaviour unchanged.
- Footer: white logo, default tagline changed to "Equipping young Nigerians through technology, sport and inspiration." (the old line repeated the 2025 theme).
- Removed the hard-coded `document.title.replace(/TriveFoundation/…)`; `CMS.apply()` now does it.

### `js/main.js`
- `CMS.apply()`: the page title used to be patched with `replace(/THRIVE/g, name)`, which no longer matched any title. It now replaces the default organisation name with the current one, once per change, and updates the logo's alt text. No other logic touched (storage, league, quiz, auth are as they were).

### `js/config.js`
- `ORG_NAME` → `'Trivefoundation'`; `ORG_TAGLINE` → `'Tech · Innovation · Football'`; `HERO_EYEBROW` → `'THRIVE 2.0 · 2026 Edition'`; added `ORG_VENUE_2026`.
- `STORIES`: programme editions are now called THRIVE; the announcement story was rewritten (it claimed an expansion to "three schools across the FCT", which is not where the programme runs) and now states the confirmed venue. **Bank details, donation tiers, quiz settings and team names/roles are untouched.**
- `TEAM`: initials-badge colours changed to brand navy/green. The founder entry pointed at a stock-photo face; that URL was removed so an initials badge shows until a real photo is uploaded through the admin.
- Header comment documents the naming rule.

### HTML pages (all twelve)
- Inline dark-theme colours removed (white text, `#3DD68C`, `#FBBF24`, `#7C3AED`, dark gradients) in favour of classes and tokens. What remains hard-coded in the pages is small and intentional: `theme-color`, white text on navy/overlay elements, translucent navy modal backdrops and two error tints (about 30 literals, down from about 140).
- Titles and descriptions say "Trivefoundation" (one word); `theme-color` and `apple-touch-icon` added.
- `index.html`: hero eyebrow "THRIVE 2.0 · 2026 Edition"; pillar chips and activity cards use the new curriculum wording; closing call-to-action is a mint band; emoji removed from leaderboard tabs; "expand across the FCT" replaced with "reach more schools in Anambra State and beyond".
- `about.html`: values section converted from a dark band to white cards; story paragraph 3 explains organisation vs programme.
- `activities.html`: Tech pillar rewritten (Artificial Intelligence, Introduction to Robotics, Machine Learning, Software Programming & Applications; capstone + written quiz + panel presentation); category tags recoloured; sticky hub menu follows the new nav height; a phone-width overflow (the page scrolled sideways to 1156 px) fixed with `minmax(0,1fr)`.
- `contact.html`: venue block now shows the 2026 venue (Union Secondary School, Amichi, Anambra State — Tech & Innovation in the ICT Laboratory, football at the same school), says plainly that it is the host venue for this year and not the organisation's address, and notes the 2025 host. The CMS keys for this block were **renamed** (`contact_venue_label`, `contact_venue_2026`, `contact_venue_note`) so a previously saved "FGC NISE" override cannot hide the new venue.
- `donate.html`: bank card navy; no change to the account data or the confirmation form logic.
- `quiz.html`: dark hero replaced by the standard page header; content constrained to the site width.
- `quiz-play.html`: results header uses the new logo; correct/wrong/skipped states use brand green, danger red, sun.
- `resources.html`: emoji document icons replaced by a line icon plus the existing type badge.
- `league.html`: emoji removed from the Football tab; spacing under the header reduced.

### Other
- `_headers`: CSP `style-src` and `font-src` no longer allow Google Fonts (`font-src 'self'`).
- `scripts/static_checks.py`: now also fails when a brand asset is missing, when a page uses a wrong spelling of the organisation name (the two-word and camel-case forms), or when a Google Fonts URL reappears.
- `README.md`: intro note, file tree, section 5 (renaming) and section 13 (design system) rewritten. `GITHUB_GUIDE.md`: one line about the logo file. `package.json`: version 5.0.0.

### Deliberately not changed
- Netlify Functions, storage keys, admin PIN hash, quiz bank, league/quiz engines.
- `scripts/build_study_pdfs.py` and the generated study books: still use the old tree mark and green/orange palette, and rely on Windows fonts, so the script could not be run here. Follow-up item.
- The stock photographs themselves (URLs unchanged apart from the one removed above).

---

## 4. Letterhead and invitation letter (delivered outside this repository)

Kept out of the repo on purpose: Netlify publishes the repository root, so anything committed here is public.

- **Letterhead** (`Trivefoundation_Letterhead.docx`): colour logo left; right-aligned "Tech | Innovation | Football", website, telephone; navy-over-green double rule; footer with the organisation line and "Page X of Y". Spec in BRAND.md §6.
- **Invitation** (`THRIVE_2.0_Invitation_001_….docx`, 3 pages): reference and date line; addressee; subject line; two opening paragraphs; a "Program at a glance" table (program and organizer, categories, venue, schedule, cost, reply); numbered sections — 1 Tech & Innovation, 2 Football, 3 Venue and Schedule, 4 Confirmation of Participation; closing; signature block as supplied; enclosure note; page 3 is a boxed School Participation Confirmation form.
- **Content changes from the supplied draft:** the organisation is written "Trivefoundation" throughout, including the "For:" line of the signature (the draft had "THRIVE Foundation" once and "Trive Foundation" elsewhere); **five (5)** students per school for Tech & Innovation (the draft said 6, the venue letter 10 — the founder confirmed 5); the sentence "specific dates and venue arrangements will be confirmed" replaced by the confirmed host venue for **both** categories (Union Secondary School, Amichi, Anambra State; Tech & Innovation in the ICT Laboratory, football at the same school; afternoon sessions 3:00–5:30 PM, taken from the venue letter), worded so it cannot be mistaken for the organisation's address; a gentle reply window ("within one week of receiving this letter", with an invitation to call if more time is needed); a statement that participation is free and that there are prizes to be won; capstone/quiz/panel sentence de-duplicated (it appeared twice); the four tick-boxes including "Both" became three with "tick all that apply"; a School Address row and a "for Trivefoundation use only" line were added to the form; a reference number was added.
- **Sending to several schools:** five to seven schools are expected. Each letter needs its own addressee block, school name in the first paragraph and reference number (`…/INV/001`, `002`, …). `build_invitation.js` takes a list of schools and writes one file per school.
- **Build:** `letters/letterhead.js` (shared header/footer/styles), `letters/build_invitation.js` (add each school to the `SCHOOLS` list; one file per school), `letters/build_letterhead.js`. Run with `node` and the `docx` npm package.

---

## 5. What was checked, and how

| Check | Result |
|---|---|
| `python3 scripts/static_checks.py` (titles, descriptions, canonicals, internal links, alt text, required files, brand guardrails) | Pass |
| Headless Chromium over all 12 pages: no JavaScript exceptions, no console errors other than unreachable network calls, exactly one title, logo image loads, both fonts load | Pass |
| The two behavioural tests from `tests/smoke.spec.js` (skip link receives first Tab; donor form refuses submit without consent) | Pass |
| Horizontal overflow at 390 px on every page | None (one found on Activities and fixed) |
| Visual review of screenshots at 390, 1366, 1600 and 1920 px: home, about, activities, contact, donate, league, quiz, gallery, resources, privacy; mobile menu open | Done |
| Contrast ratios for every text/background pair in the palette | Table in BRAND.md §3 |
| Word files: schema validation, then rendered to PDF and inspected page by page | Pass |
| Logo script reproduces the shipped `logo.svg` | Identical |

### Not verified — please test before or right after deploying
1. **Photographs.** The build environment cannot reach `images.unsplash.com`, so layouts were checked with a placeholder image. Look at the hero (photo on the right, fading into the page) and the two photo bands with the real pictures.
2. **Netlify Functions.** Admin login, inline editing, saving, gallery/resource uploads, quiz codes and leaderboards need the deployed backend. The code paths were not modified, but they were not exercised.
3. **Saved admin content.** Text saved through the admin (Netlify Blobs key `thrive_cms_v1_data`) overrides the defaults in the HTML and `config.js`. If someone previously saved the organisation name, hero text, footer tagline or activity text, the **old wording will still show** until it is edited or cleared in Admin → Site Settings. The same applies to stories (`thrive_stories_v1`).
4. **Microsoft Word.** The letters were rendered with LibreOffice, which substitutes a metric-compatible font for Calibri. Page breaks should match, but open the files in Word once before printing.
5. **Real devices and other browsers** (Safari on iPhone in particular).
6. **`npm test`** with the repo's own Playwright runner was not run (the package is not installed here); an equivalent script was used.

---

## 6. Confirmed by the founder (2 October 2026)

- The organisation's name is **Trivefoundation**, one word.
- **Five** students per school for Tech & Innovation.
- **Football is at the same venue** as Tech & Innovation this year: Union Secondary School, Amichi, Anambra State.
- That school is the **host venue for this year's events only**. It is not Trivefoundation's official address and must never be presented as one.
- Schools get about **one week** to reply; the wording must stay friendly, not pressuring.
- The reference-number scheme `TF/THRIVE-2.0/INV/001…` is accepted; five to seven schools will be invited.
- There is **no official email address yet**; one is planned. Until then the letterhead carries website and telephone only.
- **Participation is free** for schools and students, and **there are prizes to be won**. The invitation says so in the opening, in the at-a-glance table ("Cost") and for the top three Tech students.

### Assumptions that still stand
- 3:00 PM – 5:30 PM afternoon sessions, taken from the venue letter.
- American spelling ("program", "finalize") was kept in the letter because the supplied draft used it.

---

## 7. Open questions for the Foundation

1. **Dates** for THRIVE 2.0 (training week, football fixtures, closing ceremony).
2. **What the prizes are**, and whether football teams win prizes too. The letter only says there are prizes to be won.
3. **Official contact details.** No official email or postal address yet. The website shows a personal Gmail address and a placeholder phone number in `config.js` (`ORG_PHONE`, unused). Add the official email to the letterhead (`letterhead.js`, `ORG` block) and to the site (Admin → Site Settings → Identity) when it exists.
4. **Unverified website content** inherited from earlier versions: the impact numbers (120+ youth, 48 hours, 6 partners), "100% objectives met", "3–5 schools in 2026", the dates and details in the sample stories, and "50 questions" in the quiz description. Confirm or edit them in the admin.
5. **Spelling convention:** British on the website, American in the letters. Choose one.
6. **Keep the sun accent?** See BRAND.md §3 for the one-line switch.
7. **Photos.** All photographs are stock. Real photos from the 2025 edition would do more for credibility than any design change.
8. **The venue letter** to Union Secondary School says ten students per school; the invitation now says five. If the host school needs the corrected number, tell them.

---

## 8. Suggested review checklist (for ChatGPT or any reviewer)

- Does the redrawn logo keep the character of the supplied one? Compare letter weight, the figure's proportions and the gap around it. Tuning knobs are listed in BRAND.md §2.
- Is navy + green + off-white enough, or does the identity need the warm accent more (or less)?
- Is Fredoka right for headings on a site that also has to look serious to principals and sponsors? Swapping is one line (`--fd` in `style.css`); Lexend for headings is the conservative option.
- Read every page for wording that still mixes up the organisation and the programme.
- Check the hero on a real phone and a wide monitor with the real photo.
- Read the invitation as a school principal would: is anything missing that they need in order to say yes (cost, dates, supervision, transport, consent, contact person)?
- Accessibility pass with a screen reader on the nav, the quiz and the donate form; the palette was checked for contrast, the interaction was not.
- Remaining clean-up candidates: page-level `<style>` blocks in `activities.html`, `quiz.html`, `quiz-play.html`, `resources.html` could move into `style.css`; `league.html` carries its own copy of the admin modal; inline `style=""` attributes remain for spacing; the study-book PDF script needs the new palette and logo.

---

## 9. Running and deploying

```bash
python3 -m http.server 8080        # then open http://localhost:8080  (backend calls will 404 locally — expected)
python3 scripts/static_checks.py   # must print "Static checks passed."
npm install && npm test            # repo's own Playwright smoke tests
```

To publish: open a pull request from `brand-refresh-2026` into `main`, let Netlify build a deploy preview, review the preview (section 5, "Not verified"), then merge.
