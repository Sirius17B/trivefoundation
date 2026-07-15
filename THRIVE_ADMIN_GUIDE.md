# THRIVE Website — Admin Access Guide

## Admin PIN
**PIN: 2025**

## How to Access the Admin Panel

1. Open the THRIVE website in your browser
2. Scroll to the bottom of any page — look for a small **Admin** link in the footer
   - Or navigate directly to: `your-site-url.com/index.html` and look for the admin link
3. Click **Admin**
4. Enter PIN: **2025**
5. You are now in the admin panel

## What You Can Do as Admin

| Section | What You Can Manage |
|---------|---------------------|
| **League Management** | Add teams, record match results, update standings |
| **CMS** | Edit page content, hero text, announcements |
| **Video Management** | Add/remove video links for the inspiration section |
| **Quiz Admin** | View quiz statistics and reset scores |

## Admin PIN Technical Details

The PIN is stored encoded in `js/main.js`:
```javascript
// The PIN "2025" is verified against:
btoa('thrive-2025-admin') === "dGhyaXZlLTIwMjUtYWRtaW4="
```

If you ever need to change the PIN, open `js/main.js` and update the `_AH` constant.

## Browser Storage (localStorage) Keys

If you need to debug or reset data manually using browser DevTools (F12 → Application → Local Storage):

| Key Prefix | What It Stores |
|------------|----------------|
| `thrive_v5_league_*` | Football league data (teams, fixtures, results) |
| `thrive_v5_tech_*` | Tech quiz scores and progress |
| `thrive_v5_cms_*` | CMS content (page text, announcements) |
| `thrive_v5_videos_*` | Video links for the inspiration section |

## To Reset All Admin Data

Open browser DevTools (F12) → Console → type:
```javascript
Object.keys(localStorage)
  .filter(k => k.startsWith('thrive_v5_'))
  .forEach(k => localStorage.removeItem(k));
location.reload();
```

## Deployment (GitHub → Netlify)

After making changes, push to GitHub and Netlify auto-deploys:
```bash
git add js/quiz-bank.js quiz.html QUIZ_TOPIC_REFERENCE.md
git commit -m "feat: quiz bank v5.3 — 532 total (373 tech 70% / 159 football 30%)"
git push origin main
```

Verify deployment: open the site → browser console (F12) → should show:
`THRIVE Quiz Bank v5.3 loaded — Tech: 373 (70%) | Football: 159 (30%) | Total: 532`
