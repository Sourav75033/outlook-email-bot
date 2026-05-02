# 🤖 AI Features Guide - Smart Inbox Analysis & VIP Management

## New Advanced Features

Your Outlook Email Bot now has AI-powered features to help you work smarter!

---

## 1. 📊 Smart Inbox Analysis

### What It Does
Analyzes your inbox (last 3 months) and suggests:
- Custom categories based on your email patterns
- VIP contacts (frequent senders)
- Common keywords in your emails
- Top domains you receive emails from

### How to Use

**Type or Say:**
```
analyze my inbox
```

**What You'll See:**
```
📊 Analyzing 450 emails...

👥 Top 10 Email Senders:
  45 emails from john@company.com
  32 emails from team@project.com
  28 emails from newsletter@tech.com
  ...

🌐 Top 10 Domains:
  78 emails from @company.com
  45 emails from @github.com
  32 emails from @linkedin.com
  ...

🔑 Top 20 Keywords in Subjects:
  45 times: project
  32 times: meeting
  28 times: report
  ...

💡 SUGGESTED CATEGORIES:
  • Category 'Company' with keywords: company.com
  • Category 'Work' with keywords: project, meeting, deadline
  • Category 'Finance' with keywords: invoice, payment, bill
  ...

⭐ SUGGESTED VIPs (frequent senders):
  • john@company.com (45 emails)
  • team@project.com (32 emails)
  ...
```

### Use the Suggestions

After analysis, you can:
```
add category Work with keywords project, meeting, deadline
add vip john@company.com
organize my emails
```

---

## 2. ⭐ VIP Management

### What It Does
Mark important people, emails, or domains as VIPs. Get instant notifications when they email you!

### Add VIPs

**By Email:**
```
add vip john@company.com
```

**By Name:**
```
add vip John Smith
```

**By Domain (all emails from a company):**
```
add vip company.com
```

### Remove VIPs

```
remove vip john@company.com
```

### List All VIPs

```
list vips
```

**Output:**
```
You have 8 VIPs

📧 VIP Emails:
  • john@company.com
  • boss@work.com
  • client@important.com

👤 VIP Names:
  • John Smith
  • Sarah Johnson

🌐 VIP Domains:
  • company.com
  • important-client.com
```

---

## 3. 🔔 Real-Time Email Notifications

### What It Does
Monitors your inbox and shows pop-up notifications when VIPs email you!

### Start Monitoring

**Monitor for 1 hour (default):**
```
monitor inbox
```

**Monitor for specific duration:**
```
monitor inbox for 30 minutes
monitor inbox for 120 minutes
```

### What Happens

```
🔍 Monitoring inbox for VIP emails...
⏰ Will monitor for 60 minutes
💡 Press Ctrl+C to stop monitoring

[When VIP email arrives]
🔔 NOTIFICATION: VIP Email from John Smith
   Subject: Urgent: Project Update Needed

🤖 Bot: New VIP email from John Smith
```

**On macOS:** You'll see a system notification with sound!

### Stop Monitoring

Press `Ctrl+C` to stop monitoring anytime.

---

## 4. 🎯 Complete Workflow Examples

### Example 1: Set Up Work Email Management

```
Step 1: Analyze inbox
You: analyze my inbox

Step 2: Add suggested VIPs
You: add vip boss@company.com
You: add vip john@company.com

Step 3: Create work category
You: add category Work with keywords project, meeting, deadline, report

Step 4: Organize emails
You: organize my emails

Step 5: Start monitoring
You: monitor inbox for 480 minutes
(Monitors for 8 hours - your work day!)
```

### Example 2: Manage Client Emails

```
Step 1: Add important clients as VIPs
You: add vip client1@important.com
You: add vip client2@vip.com
You: add vip important-client.com

Step 2: Create Clients category
You: add category Clients with keywords invoice, proposal, contract, quote

Step 3: Organize client emails
You: organize to folder Clients with keywords invoice, proposal, contract

Step 4: Get notified of new client emails
You: monitor inbox for 240 minutes
```

### Example 3: Personal Email Organization

```
Step 1: Analyze to find patterns
You: analyze my inbox

Step 2: Add family as VIPs
You: add vip mom@email.com
You: add vip dad@email.com
You: add vip Family

Step 3: Create categories
You: add category Family with keywords mom, dad, sister, family
You: add category Finance with keywords bank, credit card, payment

Step 4: Organize
You: organize my emails

Step 5: Monitor for important emails
You: monitor inbox for 60 minutes
```

---

## 5. 💡 Pro Tips

### Tip 1: Run Analysis Regularly
```
# Run once a month to discover new patterns
analyze my inbox
```

### Tip 2: Use Domain VIPs for Companies
```
# Get notified for ALL emails from a company
add vip company.com
```

### Tip 3: Combine with Categories
```
# VIPs for notifications, categories for organization
add vip boss@company.com
add category Work with keywords project, meeting
monitor inbox for 480 minutes
```

### Tip 4: Monitor During Work Hours
```
# Start monitoring when you begin work
monitor inbox for 480 minutes

# Stop with Ctrl+C when done
```

### Tip 5: Use Name VIPs for Flexibility
```
# Catches emails even if they use different email addresses
add vip John Smith
```

---

## 6. 🎤 Voice Command Examples

### Analysis
```
You: voice
🎤 Listening...
[Say: "analyze my inbox"]
```

### VIP Management
```
You: voice
🎤 Listening...
[Say: "add VIP john at company dot com"]
[Say: "list my VIPs"]
[Say: "remove VIP john at company dot com"]
```

### Monitoring
```
You: voice
🎤 Listening...
[Say: "monitor inbox for sixty minutes"]
[Say: "start monitoring"]
```

---

## 7. ⚙️ Technical Details

### VIP Storage
- VIPs are saved in `vip_list.json`
- Persists between bot sessions
- Can be edited manually if needed

### Notification System
- **macOS**: Uses AppleScript for native notifications
- **Windows**: Falls back to console notifications
- **Sound**: "Glass" sound on macOS

### Monitoring Frequency
- Checks inbox every 30 seconds
- Minimal impact on Outlook performance
- Can run in background

### Analysis Scope
- Analyzes last 90 days (3 months) of emails
- Processes subject, sender, and email body
- Identifies patterns and frequencies

---

## 8. 🔧 Customization

### Adjust Monitoring Interval
Edit `email_bot.py`, line ~492:
```python
time.sleep(30)  # Change 30 to desired seconds
```

### Change Analysis Period
Edit `email_bot.py`, line ~352:
```python
emails = self.get_emails(days=90)  # Change 90 to desired days
```

### Customize Notification Sound (macOS)
Edit `email_bot.py`, line ~337:
```python
sound name "Glass"  # Change to: Basso, Blow, Bottle, Frog, Funk, etc.
```

---

## 9. 📋 Command Reference

| Command | What It Does | Example |
|---------|--------------|---------|
| `analyze my inbox` | Smart analysis & suggestions | `analyze my inbox` |
| `add vip EMAIL` | Add VIP by email | `add vip john@company.com` |
| `add vip NAME` | Add VIP by name | `add vip John Smith` |
| `add vip DOMAIN` | Add VIP by domain | `add vip company.com` |
| `remove vip IDENTIFIER` | Remove VIP | `remove vip john@company.com` |
| `list vips` | Show all VIPs | `list vips` |
| `monitor inbox` | Start monitoring (60 min) | `monitor inbox` |
| `monitor inbox for N minutes` | Monitor for N minutes | `monitor inbox for 120 minutes` |

---

## 10. ❓ FAQ

**Q: How often should I run analysis?**
A: Once a month, or when your email patterns change significantly.

**Q: Can I have multiple VIPs from the same domain?**
A: Yes! You can add specific emails AND the domain.

**Q: Will monitoring drain my battery?**
A: Minimal impact - checks every 30 seconds, very lightweight.

**Q: Can I monitor overnight?**
A: Yes! Use `monitor inbox for 480 minutes` (8 hours) or more.

**Q: What if I close the bot while monitoring?**
A: Monitoring stops. Restart bot and run monitor command again.

**Q: Can I export my VIP list?**
A: Yes! The `vip_list.json` file contains all VIPs in JSON format.

---

**Enjoy your AI-powered email assistant! 🚀**