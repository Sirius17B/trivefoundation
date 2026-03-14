# GitHub Guide — Upload, Share & Collaborate

This guide explains how to put the THRIVE website on GitHub so your collaborators can review and edit the code. You do not need to know Git deeply to follow these steps.

---

## Part 1 — Create a GitHub Account

If you don't have one already:

1. Go to [github.com](https://github.com)
2. Click **Sign up**
3. Choose a username (e.g. `chisom-thrive`), enter your email and a password
4. Verify your email address

---

## Part 2 — Create the Repository

A repository (repo) is where your project lives on GitHub.

1. After logging in, click the **+** icon in the top-right corner → **New repository**
2. Fill in the form:
   - **Repository name:** `thrive-website`
   - **Description:** `THRIVE youth development website`
   - **Public** (so your friend can see it without needing a GitHub account) or **Private** (only invited people can see it)
   - **Do NOT** tick "Add a README file" — you already have one
3. Click **Create repository**
4. GitHub will show you a page with setup instructions — keep this tab open

---

## Part 3 — Install Git on Your Computer

Git is the tool that sends your files to GitHub.

**On Windows:**
1. Go to [git-scm.com/download/win](https://git-scm.com/download/win)
2. Download and run the installer — click Next through all screens, defaults are fine
3. When done, open **Git Bash** from your Start menu

**On Mac:**
Open **Terminal** (search for it with Cmd+Space) and run:
```bash
git --version
```
If Git is not installed, macOS will prompt you to install it automatically.

**On Linux:**
```bash
sudo apt install git    # Ubuntu/Debian
sudo dnf install git    # Fedora
```

---

## Part 4 — Upload Your Files

Open Terminal (Mac/Linux) or Git Bash (Windows). Navigate to your project folder, then run these commands one at a time:

```bash
# 1. Go into your website folder
cd path/to/thrive-website
# Example on Mac:    cd ~/Downloads/thrive-website
# Example on Windows: cd C:/Users/YourName/Downloads/thrive-website

# 2. Tell Git who you are (only need to do this once per computer)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# 3. Initialise Git in the folder
git init

# 4. Stage all the files for upload
git add .

# 5. Create the first commit (a snapshot of your files)
git commit -m "Initial upload — THRIVE website v4"

# 6. Connect to your GitHub repository
#    Replace YOUR-USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR-USERNAME/thrive-website.git

# 7. Set the main branch name
git branch -M main

# 8. Push (upload) the files to GitHub
git push -u origin main
```

GitHub will ask for your username and password. For the password, use a **Personal Access Token** (not your actual password — see note below).

### Getting a Personal Access Token

GitHub no longer accepts passwords for pushes. Here's how to get a token:

1. Go to GitHub → Click your profile photo (top-right) → **Settings**
2. Scroll to the bottom of the left sidebar → **Developer settings**
3. **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)**
4. Give it a name like "thrive-website upload"
5. Set expiration to 90 days (or no expiration if you prefer)
6. Tick the **repo** checkbox
7. Click **Generate token**
8. Copy the token immediately — it only shows once
9. Use this token as your password when Git asks

---

## Part 5 — Enable GitHub Pages (Free Hosting)

Once your files are on GitHub, you can make the website live in one click:

1. Go to your repository on GitHub: `github.com/YOUR-USERNAME/thrive-website`
2. Click **Settings** (tab at the top of the repository page)
3. In the left sidebar, click **Pages**
4. Under **Source**, choose **Deploy from a branch**
5. Under **Branch**, select `main` and `/ (root)` → click **Save**
6. Wait about 60 seconds, then refresh the page
7. A green box will appear: **Your site is published at `https://YOUR-USERNAME.github.io/thrive-website/`**

> **Important:** Because the site is in a subfolder (`/thrive-website/`), the asset paths should still work — all internal links are relative (`href="about.html"`, `src="css/style.css"`), so they work from any subfolder automatically.

---

## Part 6 — Invite Your Friend to Collaborate

### If the repository is Private:

1. Go to your repository → **Settings** → **Collaborators** (left sidebar)
2. Click **Add people**
3. Search for your friend's GitHub username or email
4. Click **Add [username]** → they receive an email invitation
5. They accept the invitation and can now push changes

### If the repository is Public:

Your friend can see the code without an invitation. But to make edits, they still need to be a collaborator (follow the steps above) or they can use a **Fork & Pull Request** workflow (explained below).

---

## Part 7 — Your Friend's Workflow (Making Edits)

Once your friend is a collaborator, here's how they work on the project:

### First time — Clone the repository

```bash
# Download a copy of the code to their computer
git clone https://github.com/YOUR-USERNAME/thrive-website.git
cd thrive-website
```

### Making a change — Step by step

```bash
# 1. Always get the latest version before starting work
git pull origin main

# 2. Create a new branch for the change (keeps main clean)
git checkout -b fix/carousel-arrows
# Name format: fix/description or feat/description or content/description

# 3. Make their edits in the files...

# 4. See what changed
git status
git diff

# 5. Stage and commit the changes
git add .
git commit -m "fix: carousel arrows no longer overlap on mobile"

# 6. Push the branch to GitHub
git push origin fix/carousel-arrows
```

### Opening a Pull Request (asking you to review)

1. Go to `github.com/YOUR-USERNAME/thrive-website`
2. GitHub will show a banner: **"fix/carousel-arrows had recent pushes"** → click **Compare & pull request**
3. Write a short description of what changed and why
4. Click **Create pull request**
5. You get notified, review the changes, leave comments, and click **Merge pull request** when happy

### Updating main after a merge

```bash
git checkout main
git pull origin main
```

---

## Part 8 — Everyday Commands Cheat Sheet

```bash
# Download latest changes from GitHub
git pull origin main

# See what files have changed
git status

# See what's different in the files
git diff

# Stage all changes
git add .

# Stage one specific file
git add js/config.js

# Commit with a message
git commit -m "content: update donation tier amounts"

# Push to GitHub
git push origin main

# Create and switch to a new branch
git checkout -b feat/new-quiz

# Switch back to main
git checkout main

# See all branches
git branch -a

# Delete a branch after it's merged
git branch -d feat/new-quiz
```

---

## Part 9 — Recommended Branch Strategy

For a small team, this simple approach works well:

```
main          → Always working, deployed code. Never commit directly.
feat/...      → New features (feat/science-quiz)
fix/...       → Bug fixes (fix/mobile-nav-overlap)
content/...   → Text/image updates (content/update-team-page)
```

**Rule:** Never push directly to `main`. Always use a branch and a Pull Request so your collaborator can review before anything goes live.

---

## Part 10 — Keeping GitHub Pages Up to Date

Every time you merge a Pull Request into `main`, GitHub Pages automatically rebuilds and deploys within ~60 seconds. You don't need to do anything — the live website updates itself.

---

## Quick Reference — Who Does What

| Task | Who | How |
|---|---|---|
| Change organisation name | You or collaborator | Edit `ORG_NAME` in `js/config.js` |
| Update stats numbers | You or collaborator | Edit `STATS` in `js/config.js` |
| Add a quiz question | Admin (browser) | Log in → `quiz.html` → Question Editor |
| Add a quiz question (bulk) | Developer | Edit `QUIZZES` in `js/config.js` |
| Update bank details | Developer | Edit `BANK` in `js/config.js` |
| Change text on any page | Admin (browser) | Log in → click text → type → Save |
| Add a new page | Developer | Copy a page, add nav link in `components.js` |
| Change colours | Developer | Edit `:root` variables in `css/style.css` |
| Replace the logo | Developer | Replace `assets/tree-logo.png` |
| Upload a video | Admin (browser) | Log in → `videos.html` → upload zone |
| Add gallery photos | Admin (browser) | Log in → `gallery.html` → Add Image |

---

*This guide is written for the THRIVE website v4. For technical questions about the codebase, refer to `README.md`.*
