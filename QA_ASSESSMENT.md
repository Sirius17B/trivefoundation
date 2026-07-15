# TriveFoundation Website QA Assessment & Test Plan

**Assessment date:** 2026-06-14  
**Assessed build:** Current repository branch, served locally at `http://localhost:8080`  
**Website URL supplied:** `[INSERT YOUR WEBSITE URL HERE]` was not replaced, so this assessment targets the static site in this repository.  
**Main purpose inferred:** Public nonprofit/youth-development website for TriveFoundation, promoting technology training, football leagues, inspirational talks, gallery/media, donations, contact/volunteer/sponsor outreach, quizzes, and admin-managed content.  
**Primary user flows inferred:**

1. Visitor lands on homepage → explores programme pillars → opens Activities.
2. Visitor views Activities → reads stories → opens league/quiz hubs.
3. Visitor views Gallery → filters images → watches videos.
4. Supporter opens Donate → reviews tiers/account details → contacts team for in-kind support.
5. Sponsor/volunteer opens Contact → submits contact form.
6. Participant opens Quiz Arena → selects quiz → completes timed quiz → score is saved to local leaderboard.
7. Admin opens admin login → authenticates with PIN → edits CMS content, gallery/video, quiz, and leaderboard data.



## Remediation update — 2026-07-15

A fresh QA pass found no unresolved Git conflict markers in the tracked website source, and the static QA parser passes. Admin access was made discoverable from the shared navigation instead of being hidden for anonymous sessions, while still requiring the existing authorized PIN. The league page now declares its custom admin UI to avoid duplicate global login/CMS modal injection and keeps its Admin Login control visible. The design system received a holistic 2026 refresh with layered warm backgrounds, stronger nav/hero treatment, improved card depth, hover motion, form focus visibility, and mobile admin-button handling. Playwright browser QA remains blocked in this environment because the Chromium binary is missing and the Playwright CDN download returns HTTP 403.

## Remediation update — 2026-06-14

The highest-impact static-site issues identified in this assessment have now been addressed in the codebase: `videos.html` is a clean redirect page with one title and one meta description, all public HTML pages have meta descriptions and canonical links, duplicate homepage CTA copy was removed, privacy and terms pages were added, `robots.txt` and `sitemap.xml` were added, and `scripts/static_checks.py` now guards against duplicate titles, missing metadata, broken internal links, missing image alt attributes, and missing standards files. Donor identity protection still requires a real backend before production collection of private donor confirmations; see `BACKEND_DONOR_PRIVACY.md` for the recommended architecture and controls.

## 1. Executive Summary

### Overall health

The site is visually polished and covers the core nonprofit flows, but it has several risks typical of vibe-coded/static AI-generated sites: duplicated/obsolete pages, client-side-only admin/security controls, local-storage persistence for operational data, placeholder organization/bank/contact details, inconsistent metadata, and insufficient automated regression coverage.

### Critical issues to address first

| Priority | Issue | Why it matters | Recommended action |
|---|---|---|---|
| High | Admin/CMS appears entirely client-side with PIN and local storage | Anyone with browser/devtools access can inspect or bypass client-side controls; content edits are device-local and not durable across users | Move admin authentication and writes to a server/API with proper auth, authorization, audit logs, and backups |
| High | Donation details and contact data may be placeholders | Donor trust and money movement depend on accuracy | Verify all bank, email, phone, and organization details before production |
| High | `videos.html` contains duplicate `<title>` tags and both redirect + legacy page content | SEO, browser behavior, analytics, and user expectations can be inconsistent | Replace with a clean redirect page or restore it as a real page, not both |
| High | No backend for contact form/payment confirmation | Users may believe submissions or donations are processed when they are not | Wire forms to tested endpoints and show durable confirmation/error states |
| High | Missing meta descriptions on most pages | Reduces SEO quality and share/search result quality | Add unique descriptions to every public page |
| Medium | Multiple duplicate navigation/CTA labels and redirect-era text | Feels unprofessional and vibe-coded | Remove duplicate CTAs, stale copy, and old page remnants |

## 2. Detailed Findings by Category

Status legend: **Pass** = observed acceptable in static/code review; **Fail** = confirmed problem; **Blocked** = requires live URL, credentials, browser matrix, or production services; **Not Run** = recommended test not executed in this pass.

### 2.1 Functional Testing

| Test ID | Description | Steps | Expected / Pass Criteria | Actual | Status | Priority | Tools / Methods | Vibe-coded pitfalls to watch |
|---|---|---|---|---|---|---|---|---|
| FUNC-001 | Homepage loads | Serve repo with `python3 -m http.server 8080`; open `/index.html` | Page returns 200, no blank screen, hero and nav render | Local server responded for `index.html` | Pass | High | Browser, curl | JS assumes globals exist and can blank the page if load order changes |
| FUNC-002 | Internal link integrity | Parse all local HTML anchors excluding external/mail/tel/hash links | All internal files exist | No broken file targets found in static parse | Pass | High | Python HTML parser | AI-generated nav often references deleted pages |
| FUNC-003 | Navigation routes | Click Home, About, Activities, Gallery, Contact, Donate | Correct page loads, active nav state is accurate, no duplicate nav entries | Needs browser verification beyond static route existence | Not Run | High | Playwright/Cypress/manual | Injected nav can diverge from static page content |
| FUNC-004 | Homepage CTAs | Click Explore Programme, chips, Donate, Volunteer | User reaches expected destination/anchor | Static hrefs exist; browser anchor behavior not fully verified | Not Run | High | Browser/manual | Duplicate CTAs or stale anchors after page consolidation |
| FUNC-005 | Activities story feed | Load Activities, select story cards/categories if available | Featured story updates, no layout break, images have fallback | Requires browser interaction | Not Run | Medium | Browser/manual | Dynamic story rendering can fail when config items miss fields |
| FUNC-006 | Gallery filters | Click All/Football/Tech/Community | Only matching images show, active filter state updates | Requires browser interaction | Not Run | Medium | Browser/manual | Inline `onclick` handlers break silently if functions are renamed |
| FUNC-007 | Gallery admin add image | Login as admin, add image URL/caption/alt/category | Item persists according to defined storage behavior and is sanitized | Blocked without authorized PIN and storage spec | Blocked | High | Manual with credentials | Missing alt validation and unsanitized labels are common |
| FUNC-008 | Donation tiers render | Open Donate | Config tiers render exactly once, featured/amount labels display correctly | Needs browser render check | Not Run | High | Browser/manual | Currency formatting/placeholder bank data can be overlooked |
| FUNC-009 | Custom donation amount | Enter invalid, zero, decimal, very large, valid amount | Validation rejects invalid values and explains next step | Needs browser/manual; no payment flow observed in static review | Not Run | High | Browser/manual | Number inputs alone are not sufficient validation |
| FUNC-010 | Contact form happy path | Complete required fields and submit | User receives success state and submission reaches backend/inbox | Backend not evident in static review | Blocked | High | Browser + network inspector | Forms often show fake success without sending data |
| FUNC-011 | Contact form negative cases | Submit empty, malformed email, long text, script payload | Inline errors, no XSS, no fake success | Needs browser + backend verification | Not Run | High | Browser, security payloads | Missing server-side validation |
| FUNC-012 | Quiz selection and timer | Open Quiz Arena, start each quiz, answer questions, timeout | Timer works, progress/score accurate, no skipped state corruption | Needs browser interaction | Not Run | High | Browser/manual/Playwright | State machines generated by AI often fail on back/refresh/timeouts |
| FUNC-013 | Quiz leaderboard persistence | Finish quiz twice, refresh, clear storage | Leaderboard behavior matches product spec and handles storage errors | Requires browser storage testing | Not Run | Medium | Browser devtools | Local-only leaderboard can mislead users as “live” |
| FUNC-014 | League tabs/standings | Switch boys/girls/tech tabs | Correct standings show and remain responsive | Requires browser interaction | Not Run | Medium | Browser/manual | Duplicate tab IDs or stale copied labels |
| FUNC-015 | Video redirect | Open `/videos.html` | Clean redirect or clear landing page, not mixed content | Static review found redirect plus legacy content and duplicate titles | Fail | High | Static HTML parser/manual | Old content left behind after moving videos into Gallery |
| FUNC-016 | Error handling/offline | Load with JS disabled, blocked images, slow network | Core content remains understandable; errors are graceful | Not run | Not Run | Medium | DevTools throttling, disable JS | Static sites often depend on JS for core nav/footer |

### 2.2 Usability & User Experience

| Test ID | Description | Steps | Expected / Pass Criteria | Actual | Status | Priority | Tools / Methods | Vibe-coded pitfalls to watch |
|---|---|---|---|---|---|---|---|---|
| UX-001 | First-impression clarity | Review homepage above the fold | Purpose, audience, and primary CTA obvious in under 5 seconds | Static copy is clear; visual confirmation recommended | Pass | High | Heuristic review | Pretty hero with vague mission copy |
| UX-002 | CTA hierarchy | Identify primary CTA per page | One primary action per viewport; secondary actions visually distinct | Homepage contains multiple similar programme/gallery/league CTAs; one duplicate “Open Activities hubs”/“League & Quiz hubs” pattern observed in code | Fail | Medium | Heuristic review | AI adds extra buttons without removing older copy |
| UX-003 | Mobile navigation | Test 320, 375, 390, 768 px | Hamburger works, links reachable, no horizontal scroll | Not run | Not Run | High | Chrome DevTools, real devices | Fixed/absolute elements overlapping on small screens |
| UX-004 | Donation trust | Review Donate page | Bank details, impact explanation, and contact path are credible and verified | Values appear configurable and may be placeholder; verification needed | Blocked | High | Content review with stakeholder | Placeholder financial data accidentally shipped |
| UX-005 | Content consistency | Scan organization naming, year, venue, programme claims | Naming, dates, and facts are consistent across pages | Potential inconsistent “THRIVE” comments and TriveFoundation branding; README mentions placeholder-like docs | Not Run | Medium | Content QA | Mixed names from earlier prompts/rebrands |
| UX-006 | Loading and feedback | Trigger dynamic operations: forms, uploads, quiz submission | Clear loading, success, and error states | Needs browser interaction | Not Run | Medium | Manual/browser | Silent failure on client-side-only features |
| UX-007 | Think-aloud support flow | Simulate donor: homepage → donate → account/contact | Donor knows how to give and what happens next | Need live/manual test | Not Run | High | Moderated/unmoderated test | Missing confirmation step causes uncertainty |
| UX-008 | Think-aloud participant flow | Simulate student: activities → quiz → results | Student can start and complete without help | Need live/manual test | Not Run | High | Manual | Timed overlays can trap users or lose state |

### 2.3 Accessibility — WCAG 2.2 AA

| Test ID | Description | Steps | Expected / Pass Criteria | Actual | Status | Priority | Tools / Methods | Vibe-coded pitfalls to watch |
|---|---|---|---|---|---|---|---|---|
| A11Y-001 | Images have alt attributes | Parse static `<img>` tags | Informative images have descriptive alt; decorative images have empty alt and hidden if needed | Static parse found no `<img>` missing `alt` | Pass | High | Python parser, axe | AI images with vague or duplicate alt text |
| A11Y-002 | Keyboard navigation | Tab through all pages and modals | Visible focus, logical order, no keyboard traps | Not run | Not Run | High | Keyboard-only manual, axe | Custom carousels/modals often trap focus incorrectly |
| A11Y-003 | Modal accessibility | Open admin/login/CMS/quiz overlays | Focus moves into modal, Escape closes if appropriate, background inert | Not run | Not Run | High | Manual + screen reader | `role=dialog` without focus management |
| A11Y-004 | Color contrast | Check text/buttons/links in all themes | Normal text ≥ 4.5:1, large text ≥ 3:1, focus ≥ visible | Not run | Not Run | High | axe, Lighthouse, Colour Contrast Analyser | Random gradients and low-opacity text fail contrast |
| A11Y-005 | Semantic headings | Inspect heading order | One meaningful H1 per page, no skipped confusing hierarchy | Not run | Not Run | Medium | axe, manual | AI-generated sections often overuse H2/H3 for styling |
| A11Y-006 | ARIA correctness | Inspect tabs/carousels/filter groups | ARIA roles match keyboard behavior | Not run | Not Run | Medium | axe, manual | ARIA added visually but not functionally |
| A11Y-007 | Reduced motion | Enable prefers-reduced-motion | Animations/carousels respect user preference | Not run | Not Run | Medium | DevTools rendering emulation | Infinite/auto animations ignore motion sensitivity |
| A11Y-008 | Screen reader labels | Review nav, buttons, form labels | Controls have accessible names and error announcements | Some labels/ARIA exist in code; full screen reader pass still needed | Not Run | High | NVDA/VoiceOver | Icon-only buttons without labels |

### 2.4 Cross-Browser & Device Compatibility

| Test ID | Description | Steps | Expected / Pass Criteria | Actual | Status | Priority | Tools / Methods | Vibe-coded pitfalls to watch |
|---|---|---|---|---|---|---|---|---|
| COMPAT-001 | Latest Chrome | Run smoke suite | No layout/JS errors | Not run | Not Run | High | BrowserStack/local | Chrome-only testing hides Safari issues |
| COMPAT-002 | Latest Firefox | Run smoke suite | Same behavior as Chrome | Not run | Not Run | High | BrowserStack/local | CSS features differ subtly |
| COMPAT-003 | Latest Safari/iOS Safari | Run smoke suite | No broken sticky/fixed elements, media works | Not run | Not Run | High | BrowserStack/real iPhone | `100vh`, file inputs, storage quirks |
| COMPAT-004 | Latest Edge | Run smoke suite | Same behavior as Chrome | Not run | Not Run | Medium | BrowserStack/local | Enterprise Edge tracking/security settings |
| COMPAT-005 | One older major version | Run high-priority flows | Graceful degradation | Not run | Not Run | Medium | BrowserStack | Modern CSS/JS unsupported without fallback |
| COMPAT-006 | Responsive widths | Test 320, 360, 390, 414, 768, 1024, 1366, 1440 | No horizontal scroll, no overlap, CTAs reachable | Not run | Not Run | High | DevTools, Playwright screenshots | Grid/card layouts overflow on narrow phones |
| COMPAT-007 | Touch interactions | Swipe carousel, tap filters/nav | No accidental double actions; hit targets ≥ 44px | Not run | Not Run | Medium | Real device | Hover-dependent UI unusable on touch |

### 2.5 Performance & Load

| Test ID | Description | Steps | Expected / Pass Criteria | Actual | Status | Priority | Tools / Methods | Vibe-coded pitfalls to watch |
|---|---|---|---|---|---|---|---|---|
| PERF-001 | Lighthouse baseline | Run Lighthouse mobile and desktop for key pages | Performance ≥ 85, A11y ≥ 90, Best Practices ≥ 90, SEO ≥ 90 | Not run | Not Run | High | Lighthouse/PageSpeed | Pretty image-heavy pages score poorly |
| PERF-002 | Load time | Cold load on simulated Fast 3G/4G | Main pages usable < 3s target where feasible | Not run | Not Run | High | Lighthouse, WebPageTest | Unsplash remote images delay LCP |
| PERF-003 | LCP image optimization | Inspect hero/gallery images | Correct dimensions, compressed, responsive `srcset`, lazy loading below fold | Hero/background images are remote Unsplash URLs and may lack local optimization | Fail | Medium | DevTools Network | AI sites use large remote stock images everywhere |
| PERF-004 | CLS | Record page load and image rendering | CLS < 0.1 | Not run | Not Run | Medium | Lighthouse | Dynamic injected nav/footer shifts layout |
| PERF-005 | JS/CSS weight | Inspect unused JS/CSS | Minimal unused code, no duplicate legacy blocks | Single large `main.js`; old videos page content indicates cleanup needed | Not Run | Medium | Coverage tab | “One big JS file” grows with unused features |
| PERF-006 | Load under concurrency | Simulate 50/100/250 users for static assets | Static server/CDN remains responsive | Not run | Not Run | Low/Medium | k6, Artillery | Static hosting usually fine; third-party images can bottleneck |
| PERF-007 | CPU/memory | Interact with carousels/quiz/gallery for 10 minutes | No leaks or excessive timers | Not run | Not Run | Medium | Performance profiler | Intervals/listeners not cleaned up |

### 2.6 Security

| Test ID | Description | Steps | Expected / Pass Criteria | Actual | Status | Priority | Tools / Methods | Vibe-coded pitfalls to watch |
|---|---|---|---|---|---|---|---|---|
| SEC-001 | Admin authentication model | Inspect and attempt login/bypass | Auth enforced server-side; no hardcoded client secrets | Client-side admin/PIN model is indicated by static code/docs and should not be treated as secure | Fail | High | Code review, DevTools | “Hidden admin” in frontend only |
| SEC-002 | Input sanitization/XSS | Submit `<script>`, event handlers, SVG payloads in CMS/contact/gallery/quiz | Payload is stored/rendered safely as text | Not fully run; sanitizer exists but all sinks must be verified | Not Run | High | Manual payloads, ZAP | Sanitizer exists but not consistently applied |
| SEC-003 | CSRF | Submit state-changing admin/contact actions cross-site | Protected by same-site cookies/tokens or not exposed | No backend observed; future backend must include CSRF protection | Blocked | High | ZAP/manual | AI backends omit CSRF |
| SEC-004 | Secrets scan | Search repo for tokens/API keys/PINs | No real secrets committed | Not run in this pass | Not Run | High | Gitleaks, trufflehog, `rg` | Hardcoded keys in config files |
| SEC-005 | Headers | Check production headers | HTTPS, HSTS, CSP, X-Content-Type-Options, frame policy/referrer policy | Static HTML includes some meta equivalents, but real HTTP headers/CSP/HSTS require hosting config | Blocked | High | SecurityHeaders.com, curl | Meta tags are not substitutes for all headers |
| SEC-006 | Dependency vulnerabilities | Audit dependencies | No critical/high vulnerabilities | No package manifest/build dependency detected in quick repo check | Pass | Medium | `npm audit` if deps exist | Hidden CDN/dependency references still need review |
| SEC-007 | Rate limiting/abuse | Repeated login/contact/quiz submissions | Rate limits, lockouts, abuse logs | Client-only login lockout appears easily bypassed on refresh/devtools | Fail | High | Manual/DevTools | Frontend-only rate limiting |
| SEC-008 | Data exposure | Inspect local storage/session storage | No sensitive data stored client-side | Needs browser inspection | Not Run | High | DevTools Application tab | Storing admin/content/user data in local storage |
| SEC-009 | Upload security | Upload invalid/large/malicious video | Type/size checks server-side; malware scanning if stored | Static/local upload behavior cannot be production-safe alone | Blocked | High | Manual, backend review | Client-only accept attributes are bypassable |

### 2.7 SEO & Content Quality

| Test ID | Description | Steps | Expected / Pass Criteria | Actual | Status | Priority | Tools / Methods | Vibe-coded pitfalls to watch |
|---|---|---|---|---|---|---|---|---|
| SEO-001 | Unique title tag | Parse all HTML pages | Exactly one descriptive `<title>` per page | `videos.html` has two title tags | Fail | High | Python HTML parser | Old titles remain after page refactors |
| SEO-002 | Meta descriptions | Parse all HTML pages | Every public page has unique meta description | Missing on `about.html`, `videos.html`, `gallery.html`, `donate.html`, `league.html`, and `contact.html` | Fail | High | Python HTML parser | AI skips metadata except homepage |
| SEO-003 | Open Graph/Twitter tags | Inspect key pages | Correct title, description, image, canonical URL | Only partial OG found on homepage in quick static review | Not Run | Medium | SEO crawler | Social shares look generic or wrong |
| SEO-004 | Heading structure | Crawl pages | Logical H1/H2/H3 hierarchy | Not run | Not Run | Medium | Screaming Frog, axe | Multiple H1s in legacy content pages |
| SEO-005 | Crawlability | Check robots, sitemap, canonical links | Sitemap/robots present for production | Not observed in quick file list | Fail | Medium | Static file check | Static projects omit sitemap/robots |
| SEO-006 | Content accuracy | Verify programme claims, dates, venue, stats, bank details | All claims validated by stakeholder/source | Requires stakeholder confirmation | Blocked | High | Content audit | AI hallucinated facts/testimonials |
| SEO-007 | Duplicate/stale content | Search for moved/legacy pages and duplicate text | No contradictory “moved” and active content on same page | `videos.html` mixes moved notice and legacy media content | Fail | Medium | Static review | AI preserves old sections after redesign |

### 2.8 Technical & Code Quality — Vibe-Specific

| Test ID | Description | Steps | Expected / Pass Criteria | Actual | Status | Priority | Tools / Methods | Vibe-coded pitfalls to watch |
|---|---|---|---|---|---|---|---|---|
| TECH-001 | Browser console | Open each page and interact | No errors, no uncaught promise rejections, warnings understood | Not run | Not Run | High | DevTools, Playwright console listener | Missing function names from inline handlers |
| TECH-002 | Static HTML sanity | Parse pages for duplicate titles, broken links, missing img alt | No critical static issues | Found duplicate title on `videos.html`; no broken internal links/missing img alt in parser | Fail | High | Python HTML parser | HTML copied/pasted into invalid final state |
| TECH-003 | JS architecture | Review modularity | Feature code modularized/testable, low coupling | Large all-in-one `main.js` architecture increases regression risk | Fail | Medium | Code review | “Mega file” generated by AI |
| TECH-004 | Inline styles/handlers | Inspect pages | Styles and behavior centralized where practical | Many inline styles and `onclick` handlers exist | Fail | Medium | Code review | Hard to maintain, test, and lint |
| TECH-005 | Content source of truth | Verify config-driven content | Content is centralized and defaults can be safely overridden | Config exists; pages still contain substantial hardcoded copy | Not Run | Medium | Code review | Partial config-driven migration |
| TECH-006 | Automated tests | Check for test framework/scripts | Smoke/a11y/link tests exist in CI | No test harness observed in quick repo check | Fail | High | File/package review | Vibe-coded sites often lack regression tests |
| TECH-007 | HTML/CSS validation | Run W3C/Stylelint | No invalid markup or CSS issues | Not run | Not Run | Medium | W3C validator, stylelint | Invalid nesting/duplicate attributes |
| TECH-008 | Dynamic content resilience | Remove optional fields from config in test branch | UI falls back gracefully without crashing | Not run | Not Run | Medium | Unit/manual | Assumes every config field exists |

### 2.9 Other: Analytics, Legal, i18n, Edge Cases

| Test ID | Description | Steps | Expected / Pass Criteria | Actual | Status | Priority | Tools / Methods | Vibe-coded pitfalls to watch |
|---|---|---|---|---|---|---|---|---|
| OTHER-001 | Analytics | Verify GA/analytics events for key flows | Page views and donation/contact/quiz events tracked with consent where required | Not observed in quick static review | Not Run | Medium | Tag Assistant, network tab | Tracking added without consent or not at all |
| OTHER-002 | Privacy policy | Locate privacy policy | Clear privacy policy covering forms, analytics, local storage, uploads | Not observed in quick file list | Fail | High | Content review | Legal pages forgotten |
| OTHER-003 | Terms/acceptable use | Locate terms | Terms or participation rules available if quizzes/uploads/admin content exist | Not observed in quick file list | Fail | Medium | Content review | User-generated/upload features without rules |
| OTHER-004 | Cookie/consent | Check cookies/tracking | Consent banner if non-essential cookies are used | Needs production/tracking review | Blocked | Medium | Browser devtools | Consent missing when analytics added later |
| OTHER-005 | Internationalization | Test text expansion, locale, currency/phone/date | Works for target Nigerian audience; formats intentional | Not run | Low/Medium | Manual | Hardcoded strings block future localization |
| OTHER-006 | RTL/language support | If applicable, test RTL/language switch | No layout break | Not applicable unless multilingual scope is added | Not Run | Low | Browser/manual | AI layouts assume LTR |
| OTHER-007 | Slow network/offline | Throttle/offline refresh | Graceful messaging and no corrupted state | Not run | Medium | DevTools | Dynamic remote images/API fail silently |
| OTHER-008 | High traffic | Static host/CDN test | CDN handles bursts and cache headers are correct | Blocked until hosting is known | Blocked | Medium | k6/WebPageTest | Third-party assets dominate reliability |

## 3. Prioritized Bug / Issue List

| ID | Priority | Issue | Reproduction / Evidence | Impact | Recommended fix |
|---|---|---|---|---|---|
| BUG-001 | High | `videos.html` has duplicate `<title>` tags and mixed redirect/legacy content | Static parser reported `videos.html: 2 title tags`; file has meta refresh redirect plus old video page sections | SEO confusion, stale content, possible weird browser titles/analytics | Make `videos.html` a minimal redirect page with one title and canonical link, or fully restore as a standalone page |
| BUG-002 | High | Most pages lack meta descriptions | Static parser warned for About, Videos, Gallery, Donate, League, Contact | Poor search snippets and lower SEO quality | Add unique meta descriptions to every page |
| BUG-003 | High | Admin security is client-side | Docs/code describe browser PIN and local storage admin CMS | Content and admin controls are not production-secure | Implement backend auth, roles, rate limits, audit logs, secure sessions |
| BUG-004 | High | Donation/contact details may be placeholders | Config contains generic phone/bank-like values and no verified production URL was supplied | Donor trust and payment risk | Stakeholder verification checklist before launch; add last-verified date internally |
| BUG-005 | High | Contact/donation actions may not submit to a real backend | Static site architecture has no evident server endpoint | Users may think they completed an action when nothing was received | Add tested backend/form service and end-to-end tests |
| BUG-006 | Medium | Duplicated/stale CTA copy on homepage | Homepage leaderboard header includes two similar Activity/League hub links in code | Unprofessional feel and diluted CTA | Remove the duplicate or clarify separate destinations |
| BUG-007 | Medium | Remote stock images used heavily | Unsplash URLs are used for hero/gallery/content images | Performance, reliability, and brand authenticity risks | Host optimized images locally/CDN, use `srcset`, define dimensions, compress |
| BUG-008 | Medium | Large monolithic JS and inline handlers/styles | `main.js` centralizes many engines; pages contain many inline styles/onclicks | Regression risk and maintainability issues | Split modules by feature and add lint/test coverage |
| BUG-009 | Medium | Missing legal pages | No privacy/terms files observed in quick file list | Compliance/trust risk, especially with forms/uploads/analytics | Add privacy policy, terms, cookie notice if needed |
| BUG-010 | Medium | No automated QA harness observed | No package/test setup found in quick file discovery | Regressions likely after vibe-coded edits | Add Playwright smoke tests, axe checks, link checker, Lighthouse CI |

## 4. Recommendations & Fixes

### Immediate launch-blocking fixes

1. **Clean `videos.html`.** Decide whether videos live in Gallery or on a dedicated Videos page. Do not ship both a redirect and full legacy content.
2. **Add metadata.** Every page needs a unique `<title>`, meta description, canonical URL, and OG/Twitter metadata.
3. **Verify real-world details.** Confirm bank account, phone, email, venue, participant numbers, dates, and quotes with the TriveFoundation owner before publication.
4. **Secure admin features.** Treat the current browser-admin pattern as a prototype only. Move authentication and writes server-side.
5. **Connect forms.** Contact/volunteer/sponsor flows must submit to an actual endpoint with success/error states and spam protection.
6. **Add legal pages.** Add Privacy Policy and Terms/Participation/Upload rules before collecting user data or media.

### Automated QA suite to add

- **Playwright smoke tests:** load each page, assert nav/footer render, click key CTAs, monitor console errors.
- **axe-core accessibility tests:** run on every page and key modal/quiz states.
- **Static link/metadata test:** fail CI for broken internal links, duplicate titles, missing meta descriptions, missing image alt.
- **Lighthouse CI:** budget for LCP, CLS, total JS/CSS, image weight, a11y, SEO.
- **Security checks:** gitleaks/trufflehog for secrets, ZAP baseline against staging.

### AI prompt ideas for regeneration/refactor

Use targeted prompts instead of broad “make it better” prompts:

- **Videos page cleanup:** “Refactor `videos.html` into a minimal accessible redirect page to `gallery.html#videos` with exactly one title, one meta description, a canonical URL, and no legacy upload/listing sections.”
- **SEO metadata:** “For each HTML page in this static site, add a unique meta description, canonical URL placeholder, Open Graph title/description, and Twitter card tags using existing page content. Do not change visible content.”
- **Admin hardening plan:** “Convert the current client-side admin CMS into a backend-backed design. Produce API endpoints, auth/session model, role permissions, rate limiting, audit logging, and migration steps from localStorage.”
- **Accessibility pass:** “Audit all dialogs, tabs, carousels, and custom buttons for WCAG 2.2 AA. Add focus management, keyboard controls, visible focus styles, reduced-motion support, and axe-compatible ARIA.”
- **Test harness:** “Add Playwright tests for homepage, navigation, gallery filters, donation page, contact form validation, quiz start/complete, and admin login lockout. Include axe checks and console-error failure.”

## 5. Retest Plan

### Retest scope after fixes

| Area | Retest activities | Exit criteria |
|---|---|---|
| Functional smoke | Load every page, click every nav/CTA, complete donor/contact/quiz flows | No broken links, no console errors, all flows complete with durable expected outcome |
| SEO/content | Re-run metadata parser and crawl | One title and description per page; no stale/duplicate content; sitemap/robots present |
| Accessibility | Run axe plus manual keyboard/screen reader checks | No critical/serious axe issues; keyboard users can complete all core tasks |
| Security | Verify backend auth, input validation, headers, secret scans, ZAP baseline | No client-only privileged actions; no high/critical findings |
| Performance | Run Lighthouse mobile/desktop on key pages | Meets agreed budgets: LCP ≤ 2.5s target, CLS ≤ 0.1, JS/images optimized |
| Cross-browser/device | Test Chrome, Firefox, Edge, Safari and mobile/tablet/desktop sizes | No blocking layout or functional differences |
| Regression automation | Run CI test suite on every PR | Tests are deterministic and block merges on critical regressions |

### Recommended retest cadence

- **Before first production launch:** Full pass across all categories.
- **After every vibe-coded/AI-generated change:** Automated smoke + axe + link/metadata checks at minimum.
- **Before fundraising campaigns:** Donation/contact flow verification with stakeholder sign-off.
- **Monthly:** Security dependency/secret scan, analytics sanity check, content accuracy review.

## Appendix A — Commands executed during this assessment

```bash
find .. -name AGENTS.md -print
find . -maxdepth 2 -type f | sed 's#^./##' | head -100
git status --short
sed -n '1,220p' README.md
sed -n '1,200p' index.html
sed -n '1,160p' js/main.js
sed -n '1,120p' js/config.js
python3 -m http.server 8080 >/tmp/trive_http.log 2>&1 & echo $! > /tmp/trive_http.pid
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
class P(HTMLParser):
 def __init__(self): super().__init__(); self.titles=0; self.desc=False; self.links=[]; self.imgs=[]
 def handle_starttag(self, tag, attrs):
  d=dict(attrs)
  if tag=='title': self.titles+=1
  if tag=='meta' and d.get('name')=='description': self.desc=True
  if tag=='a' and 'href' in d: self.links.append(d['href'])
  if tag=='img': self.imgs.append(d)
errors=[]
for p in Path('.').glob('*.html'):
 parser=P(); parser.feed(p.read_text(errors='ignore'))
 if parser.titles!=1: errors.append(f'{p}: {parser.titles} title tags')
 if not parser.desc: print('WARN no meta description',p)
 for href in parser.links:
  if href.startswith(('http','mailto:','tel:','#','javascript:')): continue
  target=href.split('#')[0]
  if target and not Path(target).exists(): errors.append(f'{p}: broken href {href}')
 for img in parser.imgs:
  if 'alt' not in img: errors.append(f'{p}: img missing alt {img.get("src")}')
print('\n'.join(errors) or 'No internal link/alt/title errors')
PY
curl -I -s http://localhost:8080/index.html | head
```
