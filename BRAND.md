# Trivefoundation — Brand Guide

**Version 1.1 · October 2026**
The single reference for how Trivefoundation looks and sounds on the website, in letters and on printed material.
The values here are the same ones in `css/style.css` (token block at the top). If you change one, change the other.

---

## 1. Names

| Use this | For | Never |
|---|---|---|
| **Trivefoundation** (one word, capital T only) | The organisation (who signs letters, owns the website, receives donations) | "Trive Foundation", "TriveFoundation", "THRIVE Foundation" |
| **THRIVE 2.0** (then 3.0, 4.0 …) | The yearly programme / edition. 2026 is THRIVE 2.0, themed "A Time To Build" | "Trivefoundation 2026" for an edition |
| **THRIVE** | The programme in general ("the THRIVE quiz", "THRIVE participants") | — |

- The 2025 event is "the maiden edition of THRIVE (2025)".
- Trivefoundation is independent. Venues host an edition; they do not own it, and a venue is **never** the organisation's address. 2025: FGC Nise. 2026: Union Secondary School, Amichi, Anambra State, for both categories (Tech & Innovation in the ICT Laboratory, football at the same school).
- The logo stacks the name as TRIVE over "foundation"; in running text it is always the single word Trivefoundation.
- Trivefoundation has no official email address or postal address yet. Do not print a personal email on the letterhead; add the official one when it exists.
- The two programme categories are **Tech & Innovation** and **Football**. Inspiration talks close each edition.
- Tech & Innovation always reads: *Artificial Intelligence, Introduction to Robotics, Machine Learning, Software Programming & Applications* — not "HTML/CSS".
- Bank account name "TRIVE CARE SERVICES" is a legal account name. Do not restyle or rename it.

`scripts/static_checks.py` fails the build if a page contains one of the wrong spellings.

---

## 2. Logo

The logo is the word **TRIVE** with the letter I replaced by a figure with raised arms (a person, and a growing leaf), over the word **foundation**.

### Files (`assets/`)

| File | Use |
|---|---|
| `logo.svg` | Default. Full colour, on white / off-white / mint / sky |
| `logo-white.svg` | On navy. White lettering, lighter greens |
| `logo-mono-navy.svg`, `logo-mono-white.svg` | One-colour printing, stamps, embossing, fax |
| `logo-wordmark.svg`, `logo-wordmark-white.svg` | TRIVE without "foundation" — only when the logo is under 90 px wide |
| `logo-mark.svg`, `logo-mark-white.svg` | The figure alone — watermark, avatar, bullet |
| `favicon.svg`, `apple-touch-icon.png`, `icon-512.png` | Browser tab / home-screen icon (figure on a navy tile) |
| `logo-1600.png`, `logo-white-1600.png` | Transparent PNGs for Word, PowerPoint, WhatsApp, social |

All files have a **transparent background**. Never place the logo on a white box over a coloured background — use the white version instead.

### Rules

- **Clear space:** keep a margin equal to the height of the figure's head (about one third of the T's height) free on all sides.
- **Minimum size:** full logo 90 px / 24 mm wide. Below that use the wordmark; below 48 px use the mark.
- **Backgrounds:** `logo.svg` on white, paper, mint, sky. `logo-white.svg` on navy or on a dark photo. Do not put the colour logo on green or on a busy photo.
- **Don't:** stretch, rotate, recolour, add shadows or outlines, retype the name in another font, or rearrange the figure.

### How the logo was built (and how to rebuild it)

The supplied logo was a raster image. It was redrawn as vector paths:

- **TRIVE** — outlines from the open-source font Fredoka (weight 700, width 106), corners rounded a further 24 units to match the supplied artwork.
- **foundation** — outlines from the open-source font Quicksand (weight 700), letter-spaced to the width of TRIVE.
- **Figure** — hand-drawn curves traced from the supplied artwork. Head and lower leaf in Trive Green, arms and body in Leaf Green.
- A 9-unit gap is cut out of the R and the V so the figure never touches the letters and the logo stays transparent.

These are deliberate small changes from the supplied image: slightly lighter letter weight, a cleaner gap around the figure, a little more space above "foundation". Everything is parameterised in `scripts/brand/build_logo.py`:

```bash
pip install fonttools brotli shapely skia-pathops cairosvg pillow
python3 scripts/brand/build_logo.py assets      # rewrites every logo file
```

Useful knobs at the top of that file: `NAVY`, `GREEN`, `LEAF` (colours), `WG`/`WD` (letter weight/width), `ROUND` (corner rounding), `SLOT` (space for the figure), `KNOCK` (gap around the figure), `FW` (weight of "foundation").
Both fonts are under the SIL Open Font License, which allows use in a logo; the logo files contain shapes, not font data.

---

## 3. Colour

White or off-white backgrounds, navy for structure and text, green for action. Navy areas are limited to the footer, the support/bank cards and photo bands.

### Brand colours (sampled from the logo)

| Token | Hex | Name | Use |
|---|---|---|---|
| `--navy` | `#08365B` | Trive Navy | Wordmark, headings, navy cards, secondary buttons |
| `--navy-deep` | `#062845` | Deep Navy | Footer, hover on navy |
| `--green` | `#1C854B` | Trive Green | Primary buttons, the figure's head and leaf, large display text |
| `--green-deep` | `#17713F` | Deep Green | Green **text** and links on light backgrounds, button hover |
| `--leaf` | `#45A24A` | Leaf Green | The figure's body, decorative lines. **Not for text on white** (3.2:1) |
| `--leaf-lt` | `#7DD181` | Light Leaf | Green text and accents **on navy** |

### Surfaces and text

| Token | Hex | Use |
|---|---|---|
| `--white` | `#FFFFFF` | Cards, nav, alternate sections |
| `--paper` | `#F7FAF7` | Default page background (off-white with a hint of green) |
| `--mint` | `#E8F4EA` | Tinted band, tech tags, success |
| `--sky` | `#EAF1F6` | Tinted panel, football tags, image placeholders |
| `--line` | `#D5DEE6` | Borders, dividers |
| `--ink` | `#10283C` | Body text |
| `--muted` | `#4A6072` | Secondary text, captions |

### Accent and status — use sparingly

| Token | Hex | Use |
|---|---|---|
| `--sun` | `#F2A91E` | One warm accent: medals, "talks" pillar, focus ring, a highlighted score. Navy text on it. Never a page background |
| `--sun-tint` / `--sun-ink` | `#FDF3DC` / `#7A4F00` | Tag background / tag text |
| `--danger` / `--danger-tint` | `#B42318` / `#FEECEB` | Errors, delete actions |

`--sun` is optional. If the Foundation prefers a strict two-colour identity, set `--sun` to `--leaf` and `--sun-ink` to `--green-deep` in `style.css`; nothing else needs to change.

### Contrast (WCAG 2.1; body text needs 4.5:1, large text 3:1)

| Pair | Ratio | OK for |
|---|---|---|
| Ink on white / paper | 15.1 / 14.4 | all text |
| Muted on white / paper / mint | 6.6 / 6.2 / 5.8 | all text |
| Navy on white / mint / sky | 12.4 / 11.0 / 10.9 | all text |
| Deep Green on white / paper / mint | 6.1 / 5.8 / 5.4 | all text |
| White on Trive Green (buttons) | 4.7 | all text |
| Trive Green on paper (hero headline) | 4.4 | large text only |
| White on navy | 12.4 | all text |
| Light Leaf on navy / deep navy | 6.7 / 8.1 | all text |
| Sun on navy, navy on sun | 6.2 | all text |
| Sun-ink on sun-tint | 6.5 | all text |
| Leaf Green on white | 3.2 | decoration and large shapes only |

### Colour coding of the pillars

Tech & Innovation = green · Football = navy · Inspiration talks = sun. Classes: `.ico-tech`, `.ico-football`, `.ico-talks`, `.bar-*`, `.tag-*`.

---

## 4. Typography

| Where | Headings | Body |
|---|---|---|
| Website | **Fredoka** 600 (700 for the hero headline) — the same family the logo lettering comes from | **Lexend** 400 (300 for lead paragraphs, 500–600 for labels and buttons) |
| Letters, Word, PowerPoint | **Calibri** bold, navy | **Calibri** 11 pt, ink |
| If neither is available | Trebuchet MS / Arial | Arial |

- Web fonts are self-hosted in `assets/fonts/` (variable woff2). No Google Fonts request; the site's Content-Security-Policy only allows fonts from the site itself.
- Headings are navy. Eyebrow labels (small caps above a heading) are Deep Green, 0.72 rem, letter-spaced 0.14 em, uppercase.
- No italics in Fredoka (it has none). For emphasis use weight or colour.
- Letters do not use Fredoka: recipients will not have it installed, and Calibri reads as more formal.

---

## 5. Layout and components (website)

- **Backgrounds:** alternate `--paper` and `--white`; one `--mint` band per page for the closing call to action. Use the band classes (`.band-white`, `.band-paper`, `.band-mint`, `.band-sky`, `.band-navy`) instead of inline colours.
- **Navy is an accent surface:** footer, the hero "Support the mission" card, the bank-details card, photo bands. Not page backgrounds.
- **Width:** content is capped at 1200 px (`--maxw`) and centred; side padding `--pad` scales from 16 px to 60 px.
- **Buttons:** pill-shaped. Green = main action (`.btn-primary`). Navy = secondary (`.btn-teal`). Outline/ghost for quiet actions on light. `.btn-secondary` only on navy.
- **Cards:** white, 1 px `--line` border, 18 px radius, soft navy-tinted shadow.
- **Icons:** simple line icons (stroke 2, `currentColor`). **No emoji as icons.**
- **Photos:** real programme photos first. Stock photos must show Black / African young people, and every image needs descriptive `alt` text. Photo bands carry a navy overlay so white text stays readable.
- **Focus ring:** 3 px `--sun` outline on every focusable element. Do not remove it.
- **Motion:** short (0.2 s) and optional; `prefers-reduced-motion` is respected.

---

## 6. Letterhead and documents

Files: `Trivefoundation_Letterhead.docx` (blank) and the letter build scripts in the brand kit (`letters/`).

- A4, 2 cm side margins.
- **Header:** colour logo left (about 4.7 cm wide); right-aligned block: "Tech | Innovation | Football" (Deep Green, bold), website, telephone. No email or postal address until official ones exist. Under it a two-line rule: navy (thick) over Leaf Green (thin).
- **Footer:** hairline; "Trivefoundation · Equipping young Nigerians through technology, sport and inspiration" left, "Page X of Y" right, 8 pt muted.
- **Body:** Calibri 11 pt, ink, left-aligned, 1.2 line spacing. Reference and date on one line (ref left, date right). Subject line in bold navy capitals with a navy underline rule. Numbered section headings in bold navy.
- **Sign-off:** "Yours faithfully," — signature space — NAME (bold navy) — position — "For: Trivefoundation" (italic) — phone.
- **Tone:** professional, respectful, cordial, human. Short paragraphs. One request per letter, stated plainly, with an easy way to respond.

---

## 7. Voice

- Plain, warm, confident. Say what the programme does; avoid slogans stacked on slogans.
- Do not publish numbers, dates, venues or partner names that have not been confirmed.
- Spelling: the website uses British spelling ("programme", "organisation"); the supplied letters use American ("program", "finalize"). **Pick one** — see HANDOVER.md, open questions.
