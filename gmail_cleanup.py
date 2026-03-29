#!/usr/bin/env python3
"""
Gmail Inbox Cleaner for Asis Sharma
====================================
This script will automatically delete:
- LinkedIn job alert emails
- Unstop promotional emails
- H&M newsletter emails
- Reddit notification emails
- edX promotional emails
- UNiDAYS emails
- Instagram notification emails
- Steam promotional emails

It will KEEP:
- Zerodha Daily Brief
- FIC Ramjas Finance Daily
- Google security alerts
- Facebook security alerts
- Reddit account/password emails
- Coursera, Oracle, Apify emails
- All other important emails
"""

import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# --- WHAT TO DELETE ---
SENDERS_TO_DELETE = [
    "jobalerts-noreply@linkedin.com",       # LinkedIn job alerts
    "jobs-noreply@linkedin.com",            # LinkedIn job digests
    "noreply@dare2compete.news",            # Unstop job alerts
    "noreply@unstop.news",                  # Unstop promotions
    "newsletter@email.hm.com",             # H&M newsletter
    "noreply@redditmail.com",              # Reddit notifications
    "news@sfmc.edx.org",                   # edX promotions
    "hello@info.myunidays.com",            # UNiDAYS
    "posts-recap@mail.instagram.com",      # Instagram recap
    "notification@priority.instagram.com", # Instagram notifications
    "noreply@steampowered.com",            # Steam promotions
    "notifications-noreply@linkedin.com",  # LinkedIn general notifications
]

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate():
    """Login to your Gmail account."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def trash_messages(service, query):
    """Move all messages matching query to trash."""
    trashed = 0
    page_token = None

    while True:
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=500,
            pageToken=page_token
        ).execute()

        messages = results.get('messages', [])
        if not messages:
            break

        for msg in messages:
            service.users().messages().trash(userId='me', id=msg['id']).execute()
            trashed += 1
            print(f"  🗑️  Deleted email #{trashed}...")

        page_token = results.get('nextPageToken')
        if not page_token:
            break

    return trashed

def main():
    print("\n🚀 Gmail Inbox Cleaner Starting...")
    print("=" * 45)

    service = authenticate()
    print("✅ Successfully logged into Gmail!\n")

    total_deleted = 0

    for sender in SENDERS_TO_DELETE:
        print(f"\n📧 Cleaning emails from: {sender}")
        query = f"from:{sender}"
        count = trash_messages(service, query)
        print(f"   ✅ Deleted {count} emails")
        total_deleted += count

    print("\n" + "=" * 45)
    print(f"🎉 DONE! Total emails deleted: {total_deleted}")
    print("Your inbox is now clean!")
    print("\nNote: Deleted emails are in Trash.")
    print("Gmail auto-empties Trash after 30 days.")
    print("Or open Gmail > More > Trash > Empty Trash now.")

if __name__ == '__main__':
    main()
