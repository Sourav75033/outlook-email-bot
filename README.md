# 🤖 Outlook Email Bot

Your personal AI assistant to organize and manage Outlook emails with voice commands!

## ✨ Features

### Core Features
- 🗂️ **Auto-organize emails** into folders (Newsletters, Important, Social, Promotions, Receipts)
- 🎯 **Smart filtering** based on keywords and patterns
- 🎤 **Voice commands** - Talk to your bot naturally
- 💬 **Chat interface** - Type commands in plain English
- 📊 **Email statistics** - See your inbox overview
- 🔄 **Automatic folder creation** - No manual setup needed

### Custom Organization
- ➕ **Add custom categories** - Create your own email categories with keywords
- 📁 **Use existing folders** - Organize emails to folders you already have
- 🔧 **Dynamic keyword management** - Add keywords to categories on the fly

### 🤖 AI-Powered Features (NEW!)
- 📊 **Smart Inbox Analysis** - Analyzes your emails and suggests categories
- ⭐ **VIP Management** - Mark important people/emails for priority handling
- 🔔 **Real-time Notifications** - Get instant alerts when VIPs email you
- 💡 **Pattern Recognition** - Discovers email patterns and frequent senders
- 🎯 **Intelligent Suggestions** - Recommends categories based on your email habits

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd outlook-email-bot
pip3 install -r requirements.txt
```

### 2. Run the Bot

```bash
python3 email_bot.py
```

### 3. Start Organizing!

```
You: organize my emails
Bot: Done! Organized 45 emails: 12 newsletters, 5 important, 8 social...
```

## 📖 Full Documentation

See [SETUP-GUIDE.md](SETUP-GUIDE.md) for detailed instructions.

## 🎯 Example Commands

### Basic Organization
| Say or Type | What Happens |
|-------------|--------------|
| "organize my emails" | Sorts all emails into category folders |
| "filter newsletters" | Moves newsletters to separate folder |
| "show stats" | Displays email statistics |

### Custom Categories & Folders
| Say or Type | What Happens |
|-------------|--------------|
| "list folders" | Shows all your Outlook folders |
| "list categories" | Shows configured email categories |
| "add category Work with keywords project, meeting" | Creates custom category |
| "organize to folder Work with keywords project" | Moves emails to specific folder |

### 🤖 AI Features
| Say or Type | What Happens |
|-------------|--------------|
| "analyze my inbox" | Smart analysis with category suggestions |
| "add vip john@company.com" | Mark email/person as VIP |
| "list vips" | Show all VIP contacts |
| "monitor inbox for 60 minutes" | Get alerts for VIP emails |

### Other
| Say or Type | What Happens |
|-------------|--------------|
| "voice" | Switch to voice input |
| "help" | Show all commands |

**📖 Detailed Guides:**
- [CUSTOM-CATEGORIES-GUIDE.md](CUSTOM-CATEGORIES-GUIDE.md) - Custom categories & folders
- [AI-FEATURES-GUIDE.md](AI-FEATURES-GUIDE.md) - AI analysis, VIPs & notifications

## 🔧 Requirements

- Windows OS (for Outlook COM interface)
- Microsoft Outlook installed and configured
- Python 3.8+
- Microphone (for voice commands)

## 📁 Project Structure

```
outlook-email-bot/
├── email_bot.py          # Main bot application
├── requirements.txt      # Python dependencies
├── SETUP-GUIDE.md       # Detailed setup instructions
└── README.md            # This file
```

## 🎨 How It Categorizes Emails

The bot analyzes email subject, sender, and content to categorize:

- **Newsletters**: Contains "newsletter", "unsubscribe", "subscription"
- **Important**: Contains "urgent", "important", "ASAP", "priority"
- **Social**: Facebook, Twitter, LinkedIn, Instagram notifications
- **Promotions**: Sales, discounts, offers, deals
- **Receipts**: Invoices, payment confirmations, order receipts

## 🔮 Coming Soon (Phase 2)

- ✉️ Auto-reply to specific emails
- 📝 Daily email summaries
- ⏰ Schedule email reminders
- 📎 Extract and organize attachments
- 🗑️ Bulk delete operations
- 🔍 Advanced search queries

## 🐛 Troubleshooting

**Bot won't connect to Outlook?**
- Ensure Outlook is running
- Check Outlook is configured with your email account

**Voice commands not working?**
- Check microphone permissions
- Speak clearly after "Listening..." prompt

**Import errors?**
- Run: `pip3 install -r requirements.txt`

## 💡 Tips

1. Run the bot daily to keep your inbox organized
2. Review categorized emails to ensure accuracy
3. Customize keywords in `email_bot.py` for better results
4. Start with "filter newsletters" to test functionality

## 📄 License

Free to use and modify for personal use.

## 🤝 Contributing

This is a personal project, but feel free to fork and customize for your needs!

---

**Made with ❤️ to help you achieve inbox zero!**