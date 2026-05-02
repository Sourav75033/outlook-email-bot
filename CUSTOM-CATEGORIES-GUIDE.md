# 📁 Custom Categories & Folders Guide

## New Features Added!

You can now:
1. ✅ **Add your own email categories** with custom keywords
2. ✅ **Use existing Outlook folders** to organize emails
3. ✅ **Add keywords to existing categories** to improve filtering
4. ✅ **List all your folders and categories**

---

## 🎯 Example Commands

### 1. List Your Existing Folders

**Type or Say:**
```
list folders
```

**Bot Response:**
```
You have 8 folders
📁 Your Outlook folders:
  1. Newsletters
  2. Important
  3. Social
  4. Promotions
  5. Receipts
  6. Work
  7. Personal
  8. Archive
```

---

### 2. List Configured Categories

**Type or Say:**
```
list categories
```

**Bot Response:**
```
📋 Current email categories:

  Newsletters:
    Keywords: newsletter, unsubscribe, subscription, digest, weekly update
    
  Important:
    Keywords: urgent, important, asap, priority, critical
    
  Work:
    Keywords: project, meeting, deadline, report, presentation
```

---

### 3. Add a New Category

**Type or Say:**
```
add category Work with keywords project, meeting, deadline, report
```

**Bot Response:**
```
✅ Category 'Work' configured with keywords: project, meeting, deadline, report
📁 Created folder: Work
🤖 Bot: Created new category: Work
```

**More Examples:**
- `add category Personal with keywords family, vacation, birthday`
- `add category Clients with keywords invoice, proposal, contract`
- `add category School with keywords assignment, homework, exam, class`

---

### 4. Add Keywords to Existing Category

**Type or Say:**
```
add keywords presentation, conference to category Work
```

**Bot Response:**
```
✅ Keywords added: presentation, conference
🤖 Bot: Added 2 keywords to Work
```

**More Examples:**
- `add keywords spam, junk to category Promotions`
- `add keywords bill, statement to category Receipts`

---

### 5. Organize Emails to Specific Folder

**Type or Say:**
```
organize to folder Work with keywords project, meeting
```

**Bot Response:**
```
🤖 Bot: Organizing emails to Work folder
📧 Found 127 emails to organize...
🤖 Bot: Moved 23 emails to Work folder
```

**This works with:**
- ✅ Existing folders (folders you already have in Outlook)
- ✅ New folders (bot will create them if they don't exist)

**More Examples:**
- `organize to folder Clients with keywords invoice, proposal, contract`
- `organize to folder Personal with keywords family, vacation`
- `move to folder Archive with keywords 2023, old, completed`

---

## 🎤 Voice Command Examples

### Example 1: Add Work Category
```
You: voice
🎤 Listening...
You: [Say] "add category Work with keywords project, meeting, deadline"
🤖 Bot: Created new category: Work
```

### Example 2: Organize to Existing Folder
```
You: voice
🎤 Listening...
You: [Say] "organize to folder Clients with keywords invoice, proposal"
🤖 Bot: Moved 15 emails to Clients folder
```

---

## 💡 Pro Tips

### 1. Use Existing Folders
If you already have folders in Outlook (like "Work", "Personal", "Clients"), the bot will use them automatically. No need to create new ones!

### 2. Build Custom Categories Gradually
Start with a few keywords and add more as you discover patterns:
```
add category Work with keywords project, meeting
[Later] add keywords deadline, report to category Work
[Later] add keywords presentation, conference to category Work
```

### 3. Combine with Organize Command
After adding categories, run:
```
organize my emails
```
The bot will use ALL your categories (default + custom) to organize emails.

### 4. Test with Specific Folder First
Before organizing everything, test with one folder:
```
organize to folder Test with keywords sample, test
```

---

## 📋 Complete Command Reference

| Command | What It Does | Example |
|---------|--------------|---------|
| `list folders` | Show all Outlook folders | `list folders` |
| `list categories` | Show configured categories | `list categories` |
| `add category NAME with keywords W1, W2` | Create new category | `add category Work with keywords project, meeting` |
| `add keywords W1, W2 to category NAME` | Add keywords to category | `add keywords urgent to category Important` |
| `organize to folder NAME with keywords W1, W2` | Move emails to specific folder | `organize to folder Work with keywords project` |
| `organize my emails` | Use all categories to organize | `organize my emails` |

---

## 🔧 Advanced Usage

### Scenario 1: Organize Work Emails
```
1. add category Work with keywords project, meeting, deadline, report
2. organize my emails
   → Bot creates "Work" folder and moves matching emails
```

### Scenario 2: Use Existing "Clients" Folder
```
1. organize to folder Clients with keywords invoice, proposal, contract
   → Bot uses your existing "Clients" folder
```

### Scenario 3: Build Complex Category
```
1. add category Important with keywords urgent, asap
2. add keywords critical, priority to category Important
3. add keywords action required to category Important
4. organize my emails
   → Bot uses all keywords to find important emails
```

### Scenario 4: Organize Old Emails
```
1. organize to folder Archive with keywords 2022, 2023, old
   → Moves old emails to Archive folder
```

---

## ⚠️ Important Notes

1. **Keywords are case-insensitive** - "Project" and "project" are the same
2. **Bot searches subject, sender, and email body** - Comprehensive matching
3. **Emails are moved, not copied** - Original location changes
4. **Folders are created automatically** - If they don't exist
5. **Can undo** - Just move emails back manually in Outlook

---

## 🎯 Real-World Examples

### For Work:
```
add category Work with keywords project, meeting, deadline, report, presentation
add category Clients with keywords invoice, proposal, contract, quote
add category Team with keywords standup, sprint, review, retrospective
```

### For Personal:
```
add category Family with keywords mom, dad, sister, brother, family
add category Finance with keywords bank, credit card, statement, payment
add category Travel with keywords flight, hotel, booking, reservation
```

### For School:
```
add category Classes with keywords assignment, homework, lecture, syllabus
add category Exams with keywords test, exam, quiz, midterm, final
add category Projects with keywords group project, presentation, research
```

---

**Now you have full control over your email organization! 🎉**