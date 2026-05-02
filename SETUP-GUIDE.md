# 🤖 Outlook Email Bot - Setup Guide

## What This Bot Does

Your personal email assistant that can:
- ✅ **Organize emails** automatically into folders (Newsletters, Important, Social, Promotions, Receipts)
- ✅ **Filter newsletters** and move them to a separate folder
- ✅ **Show statistics** about your emails
- ✅ **Voice commands** - Talk to your bot!
- ✅ **Chat interface** - Type commands naturally

---

## Prerequisites

1. **Windows Computer** (required for Outlook integration)
2. **Microsoft Outlook** installed and configured with your email account
3. **Python 3.8 or higher** installed
4. **Microphone** (for voice commands)

---

## Step 1: Check Python Installation

Open Terminal (or Command Prompt) and run:

```bash
python3 --version
```

You should see something like `Python 3.x.x`. If not, download Python from [python.org](https://www.python.org/downloads/)

---

## Step 2: Install Required Libraries

Open Terminal and navigate to the bot folder:

```bash
cd Desktop/outlook-email-bot
```

Install the required libraries:

```bash
pip3 install pywin32 SpeechRecognition pyttsx3 PyAudio
```

**Note for macOS users:** This bot requires Windows because it uses Microsoft Outlook's COM interface. If you're on Mac, you'll need to:
- Use Windows via Boot Camp or Parallels
- Or use the web version of Outlook (requires different approach)

---

## Step 3: Run the Bot

Make sure Outlook is running, then:

```bash
python3 email_bot.py
```

You should see:
```
╔══════════════════════════════════════════╗
║   OUTLOOK EMAIL BOT - Phase 1           ║
║   Organize & Filter Your Emails         ║
╚══════════════════════════════════════════╝

🤖 Initializing Outlook Email Bot...
✅ Connected to Outlook successfully!
✅ Bot ready! You can type or speak commands.
```

---

## Step 4: Use the Bot

### Type Commands:

```
You: organize my emails
Bot: Organizing your emails. This may take a moment.
Bot: Done! Organized 45 emails: 12 newsletters, 5 important, 8 social, 15 promotions, 5 receipts
```

### Voice Commands:

```
You: voice
🎤 Listening... (speak now)
[Say: "organize my emails"]
Bot: Organizing your emails...
```

---

## Available Commands

| Command | What It Does |
|---------|-------------|
| `organize my emails` | Sorts all emails into category folders |
| `filter newsletters` | Moves newsletters to Newsletters folder |
| `show stats` | Shows email statistics (unread, total) |
| `help` | Shows available commands |
| `voice` | Switch to voice input mode |
| `quit` or `exit` | Close the bot |

---

## How It Works

### Email Categories:

1. **Newsletters** - Emails with "newsletter", "unsubscribe", "subscription"
2. **Important** - Emails with "urgent", "important", "ASAP"
3. **Social** - Facebook, Twitter, LinkedIn notifications
4. **Promotions** - Sales, discounts, offers
5. **Receipts** - Invoices, payment confirmations

### What Happens:

1. Bot scans your inbox (last 30 days)
2. Analyzes subject, sender, and content
3. Creates folders if they don't exist
4. Moves emails to appropriate folders
5. Keeps you updated with voice feedback

---

## Troubleshooting

### "Error connecting to Outlook"
- Make sure Outlook is running
- Check that Outlook is properly configured with your email account
- Try restarting Outlook

### "Import error" or "Module not found"
- Run: `pip3 install -r requirements.txt`
- Make sure you're in the correct folder

### Voice commands not working
- Check your microphone is connected
- Grant microphone permissions to Terminal/Python
- Speak clearly and wait for the "Listening..." prompt

### Bot is slow
- Normal! Processing many emails takes time
- First run is slower (creates folders)
- Subsequent runs are faster

---

## Tips for Best Results

1. **Run regularly** - Daily or weekly to keep inbox organized
2. **Check folders** - Review categorized emails to ensure accuracy
3. **Customize categories** - Edit `email_bot.py` to add your own keywords
4. **Start small** - Test with "filter newsletters" first
5. **Backup** - Outlook keeps emails safe, but you can export important ones

---

## Example Session

```
👤 You: organize my emails
🤖 Bot: Organizing your emails. This may take a moment.
📧 Found 127 emails to organize...
📁 Created folder: Newsletters
📁 Created folder: Promotions
🤖 Bot: Done! Organized 89 emails: 34 newsletters, 12 important, 8 social, 30 promotions, 5 receipts

👤 You: show stats
🤖 Bot: You have 15 unread emails out of 127 total emails from the last 7 days

👤 You: voice
🎤 Listening... (speak now)
👤 [Speaking: "filter newsletters"]
🤖 Bot: Filtering newsletters
🤖 Bot: Moved 34 newsletters to the Newsletters folder

👤 You: quit
🤖 Bot: Goodbye! Have a great day!
```

---

## Next Steps (Future Features)

Phase 2 will include:
- Auto-reply to specific emails
- Email summaries
- Schedule reminders
- Extract attachments
- Bulk operations

---

## Need Help?

If you encounter issues:
1. Check this guide's Troubleshooting section
2. Make sure all prerequisites are met
3. Verify Outlook is running and configured
4. Check Python and library versions

---

**Enjoy your organized inbox! 📧✨**