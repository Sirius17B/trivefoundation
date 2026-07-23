# GitHub Guide — Commit, Push & Deploy THRIVE v5

This guide walks you through putting the website on GitHub, keeping it updated, and deploying it live for free.

---

## Step 1 — Create a GitHub Account (if you don't have one)

1. Go to [github.com](https://github.com) → **Sign up**
2. Choose a username (e.g. `chisom-okoye`), enter your email and password
3. Verify your email address

---

## Step 2 — Create the Repository

1. After logging in, click **+** (top right) → **New repository**
2. Fill in:
   - **Repository name:** `thrive-website`
   - **Description:** `THRIVE youth development website v5`
   - **Visibility:** Public (for free GitHub Pages hosting) or Private (for invited collaborators only)
   - **Do NOT** tick "Add a README file" — you already have one
3. Click **Create repository**
4. Keep this page open — you'll need the repository URL

---

## Step 3 — Install Git on Your Computer

**Windows:**
- Download from [git-scm.com/download/win](https://git-scm.com/download/win)
- Run the installer (click Next through all defaults)
- Open **Git Bash** from your Start menu

**Mac:**
```bash
git --version
# If not installed, macOS will prompt you to install it automatically
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt install git
```

---

## Step 4 — First-Time Upload

Open Terminal (Mac/Linux) or Git Bash (Windows).

```bash
# 1. Navigate to the thrive-v5 folder
#    Replace the path with wherever you saved the folder
cd path/to/thrive-v5
# Mac example:    cd ~/Downloads/thrive-v5
# Windows example: cd C:/Users/YourName/Downloads/thrive-v5

# 2. Tell Git who you are (only once per computer)
git config --global user.name "Chisom Okoye"
git config --global user.email "your@email.com"

# 3. Initialise Git in the folder
git init

# 4. Stage all files for upload
git add .

# 5. Create the first commit (snapshot)
git commit -m "feat: THRIVE website v5 — full rebuild"

# 6. Connect to your GitHub repository
#    Replace YOUR-USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR-USERNAME/thrive-website.git

# 7. Set the main branch name
git branch -M main

# 8. Push (upload) everything to GitHub
git push -u origin main
```

GitHub will ask for your username and a **Personal Access Token** (not your password).

### Getting a Personal Access Token (PAT)

1. Go to GitHub → Click your profile photo → **Settings**
2. Scroll to the bottom left → **Developer settings**
3. **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)**
4. Name it: `thrive-website`
5. Set expiration: 90 days (or No expiration)
6. Tick the **repo** checkbox
7. Click **Generate token**
8. **Copy it immediately** — it only shows once
9. Use this token when Git asks for your password

---

## Step 5 — Enable GitHub Pages (Free Hosting)

Once files are on GitHub:

1. Go to `https://github.com/YOUR-USERNAME/thrive-website`
2. Click **Settings** tab (at the top of the repository)
3. In the left sidebar → **Pages**
4. Under **Source** → **Deploy from a branch**
5. Under **Branch** → select `main` and `/ (root)` → click **Save**
6. Wait ~60 seconds → refresh the page
7. A green box appears: **Your site is published at `https://YOUR-USERNAME.github.io/thrive-website/`**

> **Note:** All internal links are relative (`href="about.html"`) so they work correctly whether hosted at a root domain or in a subfolder.

---

## Step 6 — Making Updates (Day-to-Day Workflow)

Every time you edit files and want to push updates to GitHub:

```bash
# 1. Make sure you're in the project folder
cd path/to/thrive-v5

# 2. Check what's changed
git status
git diff

# 3. Stage the changed files
git add .
# Or stage specific files:
git add js/config.js

# 4. Commit with a descriptive message
git commit -m "content: update bank account details"

# 5. Push to GitHub
git push origin main
```

GitHub Pages automatically rebuilds and deploys within ~60 seconds after every push. No extra steps needed.

---

## Step 7 — Invite a Collaborator

If someone else needs to make edits:

### For a Private repository:
1. Repository → **Settings** → **Collaborators** (left sidebar)
2. Click **Add people** → search by GitHub username or email
3. They'll receive an email invitation to accept

### For a Public repository:
Anyone can see the code. But to push changes, they still need to be a collaborator (follow the steps above).

---

## Step 8 — Collaborator Workflow (Making Edits Safely)

Once added as a collaborator, your colleague follows this pattern:

```bash
# First time: download a copy of the code
git clone https://github.com/YOUR-USERNAME/thrive-website.git
cd thrive-website

# Every time before starting work: get the latest version
git pull origin main

# Create a branch for the change (keeps main clean)
git checkout -b fix/quiz-question-typo
# Branch naming: fix/..., feat/..., content/...

# Make edits to the files...

# Stage, commit, push the branch
git add .
git commit -m "fix: correct answer for HTML question #3"
git push origin fix/quiz-question-typo
```

Then on GitHub, they open a **Pull Request** for you to review before merging.

---

## Step 9 — Commit Message Convention

Use this format for clear history:

```
feat: add new quiz questions on networking
fix: correct offside rule explanation
content: update 2026 season dates
style: improve mobile nav spacing
docs: update GitHub guide
```

---

## Step 10 — Everyday Commands Reference

```bash
# Check what's changed
git status

# See exact changes
git diff

# Stage everything
git add .

# Stage one file
git add js/config.js

# Commit
git commit -m "your message here"

# Push to GitHub
git push origin main

# Get latest from GitHub
git pull origin main

# Create a new branch
git checkout -b feat/new-feature

# Switch back to main
git checkout main

# List all branches
git branch -a

# Delete a branch after it's merged
git branch -d feat/new-feature

# View commit history
git log --oneline

# Undo unstaged changes to a file
git checkout -- js/config.js

# Undo the last commit (but keep the changes)
git reset --soft HEAD~1
```

---

## Step 11 — Custom Domain (Optional)

To use `thrivefoundation.org` instead of `github.io`:

1. Buy the domain from a registrar (Namecheap, Cloudflare Domains, etc.)
2. In your domain's DNS settings, add:
   - **A records** pointing to GitHub Pages IPs:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
   - OR a **CNAME record**: `www → YOUR-USERNAME.github.io`
3. In GitHub → Settings → Pages → **Custom domain** → enter your domain → Save
4. Tick **Enforce HTTPS** once the certificate is issued (takes up to 24 hours)

---

## Step 12 — Merging a Pull Request

When a collaborator opens a Pull Request:

1. Go to the Pull Request on GitHub
2. Review the **Files changed** tab
3. Leave comments if needed
4. Click **Merge pull request** → **Confirm merge**
5. GitHub Pages redeploys automatically

---

## Quick Reference — Who Does What

| Task | How |
|---|---|
| Change org name | Edit `ORG_NAME` in `js/config.js` → commit & push |
| Update stats | Edit `STATS` in `js/config.js` → commit & push |
| Add a quiz question (bulk) | Edit `QUIZZES` in `js/quiz-bank.js` → commit & push |
| Add a quiz question (live) | Admin login → Quiz page → Question Editor |
| Update bank details | Edit `BANK` in `js/config.js` → commit & push (or Admin → Donate page) |
| Change colours | Edit `:root` variables in `css/style.css` → commit & push |
| Change fonts | Edit `@import` in `css/style.css` and `--font-head`/`--font-body` variables |
| Add gallery photos | Admin login → Gallery page → Add Image |
| Add league results | Admin login → League page → Add Match Result |
| Edit page text | Admin login → click highlighted text → type → Save All |
| Add a new page | Copy a page, update nav in `js/components.js` → `injectNav()` function |
| Run QA checks | `python3 scripts/static_checks.py` |

---

## REBRAND CHECKLIST

When the organisation name changes from THRIVE to something else:

- [ ] `js/config.js` → change `ORG_NAME`, `ORG_TAGLINE`, `ORG_EMAIL`
- [ ] `js/config.js` → change `BANK.account_name`
- [ ] All `.html` files → change `<title>` tags (find & replace "THRIVE")
- [ ] `sitemap.xml` → update domain URL
- [ ] `_headers` → update CSP if domain changes
- [ ] `.well-known/security.txt` → update contact email and policy URL
- [ ] `robots.txt` → update sitemap URL
- [ ] `package.json` → update `"name"` field (optional)
- [ ] Assets → replace `assets/tree-logo.png` and `assets/logo.svg` with new logo

Everything else (nav, footer, page headings, meta descriptions) updates automatically from `config.js`.

---

*Guide written for THRIVE website v5. For technical questions, refer to README.md.*
