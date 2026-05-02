# ⚡ Quick Start - Get Running in 5 Minutes!

## Step 1: Install Python Libraries (2 minutes)

Open Terminal and run:

```bash
cd Desktop/outlook-email-bot
pip3 install -r requirements.txt
```

Wait for installation to complete. You'll see:
```
Successfully installed pywin32-305 SpeechRecognition-3.10.0 pyttsx3-2.90 PyAudio-0.2.13
```

---

## Step 2: Make Sure Outlook is Running (30 seconds)

1. Open Microsoft Outlook
2. Make sure you're logged into your email account
3. Keep Outlook open in the background

---

## Step 3: Run the Bot (30 seconds)

In Terminal, run:

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

🤖 Bot: Hello! I'm your Outlook Email Assistant. How can I help you today?

==================================================
Type a command or say 'voice' to use voice input
==================================================
👤 You: 
```

---

## Step 4: Try Your First Command (1 minute)

### Option A: Type a Command

Type: `organize my emails` and press Enter

The bot will:
- Scan your inbox
- Create folders (Newsletters, Important, Social, Promotions, Receipts)
- Move emails to appropriate folders
- Tell you what it did

### Option B: Use Voice

1. Type: `voice` and press Enter
2. Wait for "🎤 Listening..."
3. Say: "organize my emails"
4. Bot will process your command

---

## Step 5: Check Your Results (1 minute)

Open Outlook and look at your inbox. You should see new folders:
- 📁 Newsletters
- 📁 Important
- 📁 Social
- 📁 Promotions
- 📁 Receipts

Your emails are now organized! 🎉

---

## Common Commands

| Type This | What Happens |
|-----------|--------------|
| `organize my emails` | Sorts all emails into folders |
| `filter newsletters` | Moves only newsletters |
| `show stats` | Shows email statistics |
| `help` | Lists all commands |
| `voice` | Switch to voice mode |
| `quit` | Exit the bot |

---

## Troubleshooting

### "Error connecting to Outlook"
→ Make sure Outlook is running and you're logged in

### "Module not found" error
→ Run: `pip3 install -r requirements.txt` again

### Voice not working
→ Check microphone permissions in System Preferences

### Bot is slow
→ Normal! First run takes longer (creating folders)

---

## What's Next?

1. **Customize keywords** - Edit `config.py` to add your own categories
2. **Run regularly** - Use daily to keep inbox organized
3. **Try voice commands** - More natural and hands-free
4. **Check folders** - Review categorized emails

---

## Need More Help?

See [SETUP-GUIDE.md](SETUP-GUIDE.md) for detailed documentation.

---

**That's it! You're ready to manage your emails like a pro! 🚀**