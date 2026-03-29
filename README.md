# Mail Cleaner 🧹

A simple Python script I built to automatically clean my Gmail inbox by deleting promotional and junk emails that I don't need anymore.

## Why I built this

My inbox had over 1000 unread emails — mostly job alert spam, newsletters, shopping promotions and Reddit notifications. It was getting hard to find important emails. So I built this script to automatically find and delete all the useless ones in one go.

It deleted 333+ emails in the first run itself!

## What it does

- Scans your Gmail inbox
- Finds emails from promotional senders (LinkedIn job alerts, H&M, Unstop, Reddit notifications, etc.)
- Moves them all to trash automatically
- Keeps important emails safe (security alerts, newsletters you actually read, etc.)

## Technologies used

- Python
- Gmail API (Google Cloud)
- OAuth 2.0 authentication

## How to set it up

**Step 1 — Install Python**

Download from python.org and install it. Make sure to check "Add Python to PATH" during installation.

**Step 2 — Install required libraries**

Open CMD and run:
```
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

**Step 3 — Set up Gmail API**

1. Go to console.cloud.google.com
2. Create a new project
3. Enable the Gmail API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download the credentials file and rename it to `credentials.json`
6. Place it in the same folder as the script

**Step 4 — Run the script**

```
python gmail_cleanup.py
```

A browser window will open asking you to sign in to Gmail and give permission. After that, it will start deleting automatically.

Next time you run it, it won't even ask for login — it remembers your session.

## How to use the one-click shortcut

Just double-click `run.bat` — it opens CMD automatically and runs the script. No typing needed.

## What gets deleted

- LinkedIn job alert emails
- Unstop promotional emails
- H&M newsletter emails
- Reddit notification emails
- edX promotional emails
- UNiDAYS emails
- Instagram notification emails
- Steam promotional emails

## What gets kept

- Security alerts (Google, Facebook)
- Newsletters I actually read (Zerodha Daily Brief, etc.)
- College related emails
- Any important account emails

## Note

Don't upload your `credentials.json` or `token.pickle` files to GitHub — they contain your personal Google account access and should stay private on your computer only.

## Result

Deleted 333+ junk emails automatically in the first run on an inbox that had 1000+ unread emails.
