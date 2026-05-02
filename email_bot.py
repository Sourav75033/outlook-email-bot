"""
Outlook Email Bot - Phase 1: Organize & Filter
A voice-enabled chat assistant to manage your Outlook emails
"""

import win32com.client
import speech_recognition as sr
import pyttsx3
import re
import json
import os
from collections import Counter
from datetime import datetime, timedelta
import time

class OutlookEmailBot:
    def __init__(self):
        """Initialize the Outlook Email Bot"""
        print("🤖 Initializing Outlook Email Bot...")
        
        # Connect to Outlook
        try:
            self.outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
            self.inbox = self.outlook.GetDefaultFolder(6)  # 6 = Inbox
            print("✅ Connected to Outlook successfully!")
        except Exception as e:
            print(f"❌ Error connecting to Outlook: {e}")
            print("Make sure Outlook is installed and running on your computer.")
            return
        
        # Initialize voice
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.recognizer = sr.Recognizer()
        
        # Email categories for filtering
        self.categories = {
            'newsletters': ['newsletter', 'unsubscribe', 'subscription', 'digest'],
            'important': ['urgent', 'important', 'asap', 'priority'],
            'social': ['facebook', 'twitter', 'linkedin', 'instagram', 'notification'],
            'promotions': ['sale', 'discount', 'offer', 'deal', 'promo', '% off'],
            'receipts': ['receipt', 'invoice', 'payment', 'order confirmation']
        }
        
        # Load existing folders
        self.existing_folders = self.get_existing_folders()
        
        # VIP management
        self.vip_file = 'vip_list.json'
        self.vip_list = self.load_vip_list()
        
        # Notification settings
        self.notification_enabled = True
        
        print("✅ Bot ready! You can type or speak commands.")
        print("\n💡 Try saying: 'analyze my inbox' or 'add VIP john@example.com'\n")
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"🤖 Bot: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen for voice commands"""
        with sr.Microphone() as source:
            print("🎤 Listening... (speak now)")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio)
                print(f"👤 You said: {command}")
                return command.lower()
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                print("❌ Sorry, I didn't understand that.")
                return ""
            except Exception as e:
                print(f"❌ Error: {e}")
                return ""
    
    def get_emails(self, folder=None, days=7):
        """Get emails from specified folder"""
        if folder is None:
            folder = self.inbox
        
        messages = folder.Items
        messages.Sort("[ReceivedTime]", True)  # Sort by newest first
        
        # Filter by date
        cutoff_date = datetime.now() - timedelta(days=days)
        filtered_messages = []
        
        for message in messages:
            try:
                if message.ReceivedTime.replace(tzinfo=None) >= cutoff_date:
                    filtered_messages.append(message)
            except:
                continue
        
        return filtered_messages
    
    def categorize_email(self, email):
        """Categorize email based on content"""
        subject = email.Subject.lower() if email.Subject else ""
        sender = email.SenderEmailAddress.lower() if email.SenderEmailAddress else ""
        body = email.Body.lower()[:500] if email.Body else ""  # First 500 chars
        
        content = f"{subject} {sender} {body}"
        
        for category, keywords in self.categories.items():
            for keyword in keywords:
                if keyword in content:
                    return category
        
        return 'general'
    
    def create_folder(self, folder_name):
        """Create a folder in Outlook if it doesn't exist"""
        try:
            # Check if folder exists
            for folder in self.inbox.Folders:
                if folder.Name == folder_name:
                    return folder
            
            # Create new folder
            new_folder = self.inbox.Folders.Add(folder_name)
            print(f"📁 Created folder: {folder_name}")
            return new_folder
        except Exception as e:
            print(f"❌ Error creating folder: {e}")
            return None
    
    def get_existing_folders(self):
        """Get list of existing folders in Outlook"""
        folders = []
        try:
            for folder in self.inbox.Folders:
                folders.append(folder.Name)
        except Exception as e:
            print(f"⚠️ Warning: Could not read existing folders: {e}")
        return folders
    
    def list_folders(self):
        """List all existing folders"""
        folders = self.get_existing_folders()
        if folders:
            self.speak(f"You have {len(folders)} folders")
            print("\n📁 Your Outlook folders:")
            for i, folder in enumerate(folders, 1):
                print(f"  {i}. {folder}")
        else:
            self.speak("No custom folders found in your inbox")
    
    def list_categories(self):
        """List all configured categories"""
        self.speak(f"You have {len(self.categories)} categories configured")
        print("\n📋 Current email categories:")
        for category, keywords in self.categories.items():
            print(f"\n  {category.capitalize()}:")
            print(f"    Keywords: {', '.join(keywords[:5])}")
            if len(keywords) > 5:
                print(f"    ... and {len(keywords) - 5} more")
    
    def add_category(self, category_name, keywords):
        """Add a new email category"""
        category_key = category_name.lower().replace(' ', '_')
        
        if category_key in self.categories:
            self.speak(f"Category {category_name} already exists. Adding keywords to it.")
            self.categories[category_key].extend(keywords)
        else:
            self.categories[category_key] = keywords
            self.speak(f"Created new category: {category_name}")
        
        print(f"✅ Category '{category_name}' configured with keywords: {', '.join(keywords)}")
        
        # Create folder for this category
        self.create_folder(category_name.capitalize())
    
    def add_keywords_to_category(self, category_name, keywords):
        """Add keywords to an existing category"""
        category_key = category_name.lower().replace(' ', '_')
        
        if category_key in self.categories:
            self.categories[category_key].extend(keywords)
            self.speak(f"Added {len(keywords)} keywords to {category_name}")
            print(f"✅ Keywords added: {', '.join(keywords)}")
        else:
            self.speak(f"Category {category_name} not found. Creating it now.")
            self.add_category(category_name, keywords)
    
    def organize_to_folder(self, folder_name, keywords):
        """Organize emails to a specific existing or new folder"""
        self.speak(f"Organizing emails to {folder_name} folder")
        
        # Get or create the folder
        target_folder = None
        for folder in self.inbox.Folders:
            if folder.Name.lower() == folder_name.lower():
                target_folder = folder
                break
        
        if not target_folder:
            target_folder = self.create_folder(folder_name)
        
        if not target_folder:
            self.speak(f"Could not create or find folder {folder_name}")
            return
        
        # Get emails and filter by keywords
        emails = self.get_emails(days=30)
        count = 0
        
        for email in emails:
            try:
                subject = email.Subject.lower() if email.Subject else ""
                sender = email.SenderEmailAddress.lower() if email.SenderEmailAddress else ""
                body = email.Body.lower()[:500] if email.Body else ""
                content = f"{subject} {sender} {body}"
                
                # Check if any keyword matches
                for keyword in keywords:
                    if keyword.lower() in content:
                        email.Move(target_folder)
                        count += 1
                        break
            except:
                continue
        
        self.speak(f"Moved {count} emails to {folder_name} folder")
    
    # ============ ADVANCED AI FEATURES ============
    
    def load_vip_list(self):
        """Load VIP list from file"""
        if os.path.exists(self.vip_file):
            try:
                with open(self.vip_file, 'r') as f:
                    return json.load(f)
            except:
                return {'emails': [], 'names': [], 'domains': []}
        return {'emails': [], 'names': [], 'domains': []}
    
    def save_vip_list(self):
        """Save VIP list to file"""
        try:
            with open(self.vip_file, 'w') as f:
                json.dump(self.vip_list, f, indent=2)
            print("✅ VIP list saved")
        except Exception as e:
            print(f"❌ Error saving VIP list: {e}")
    
    def add_vip(self, identifier, vip_type='email'):
        """Add VIP person/email/domain"""
        identifier = identifier.lower().strip()
        
        if vip_type == 'email':
            if identifier not in self.vip_list['emails']:
                self.vip_list['emails'].append(identifier)
                self.speak(f"Added {identifier} to VIP emails")
        elif vip_type == 'name':
            if identifier not in self.vip_list['names']:
                self.vip_list['names'].append(identifier)
                self.speak(f"Added {identifier} to VIP names")
        elif vip_type == 'domain':
            if identifier not in self.vip_list['domains']:
                self.vip_list['domains'].append(identifier)
                self.speak(f"Added {identifier} to VIP domains")
        
        self.save_vip_list()
    
    def remove_vip(self, identifier):
        """Remove VIP"""
        identifier = identifier.lower().strip()
        removed = False
        
        if identifier in self.vip_list['emails']:
            self.vip_list['emails'].remove(identifier)
            removed = True
        if identifier in self.vip_list['names']:
            self.vip_list['names'].remove(identifier)
            removed = True
        if identifier in self.vip_list['domains']:
            self.vip_list['domains'].remove(identifier)
            removed = True
        
        if removed:
            self.save_vip_list()
            self.speak(f"Removed {identifier} from VIP list")
        else:
            self.speak(f"{identifier} not found in VIP list")
    
    def list_vips(self):
        """List all VIPs"""
        total = len(self.vip_list['emails']) + len(self.vip_list['names']) + len(self.vip_list['domains'])
        
        if total == 0:
            self.speak("No VIPs configured yet")
            return
        
        self.speak(f"You have {total} VIPs")
        
        if self.vip_list['emails']:
            print("\n📧 VIP Emails:")
            for email in self.vip_list['emails']:
                print(f"  • {email}")
        
        if self.vip_list['names']:
            print("\n👤 VIP Names:")
            for name in self.vip_list['names']:
                print(f"  • {name}")
        
        if self.vip_list['domains']:
            print("\n🌐 VIP Domains:")
            for domain in self.vip_list['domains']:
                print(f"  • {domain}")
    
    def is_vip_email(self, email):
        """Check if email is from VIP"""
        try:
            sender = email.SenderEmailAddress.lower() if email.SenderEmailAddress else ""
            sender_name = email.SenderName.lower() if email.SenderName else ""
            
            # Check email
            if sender in self.vip_list['emails']:
                return True
            
            # Check name
            for vip_name in self.vip_list['names']:
                if vip_name in sender_name:
                    return True
            
            # Check domain
            for domain in self.vip_list['domains']:
                if domain in sender:
                    return True
            
            return False
        except:
            return False
    
    def show_notification(self, title, message):
        """Show desktop notification"""
        try:
            # For macOS
            os.system(f"""
                osascript -e 'display notification "{message}" with title "{title}" sound name "Glass"'
            """)
        except:
            # Fallback: just print
            print(f"\n🔔 NOTIFICATION: {title}")
            print(f"   {message}\n")
    
    def analyze_inbox(self):
        """Analyze inbox and suggest categories"""
        self.speak("Analyzing your inbox. This may take a moment.")
        
        emails = self.get_emails(days=90)  # Last 3 months
        print(f"\n📊 Analyzing {len(emails)} emails...")
        
        # Analyze senders
        senders = Counter()
        domains = Counter()
        subjects_words = Counter()
        
        for email in emails:
            try:
                sender = email.SenderEmailAddress.lower() if email.SenderEmailAddress else ""
                subject = email.Subject.lower() if email.Subject else ""
                
                if sender:
                    senders[sender] += 1
                    domain = sender.split('@')[-1] if '@' in sender else ""
                    if domain:
                        domains[domain] += 1
                
                # Extract keywords from subject
                words = [w for w in subject.split() if len(w) > 4]
                for word in words[:5]:  # Top 5 words per subject
                    subjects_words[word] += 1
            except:
                continue
        
        # Generate suggestions
        print("\n" + "="*60)
        print("📋 INBOX ANALYSIS & CATEGORY SUGGESTIONS")
        print("="*60)
        
        # Top senders
        print("\n👥 Top 10 Email Senders:")
        for sender, count in senders.most_common(10):
            print(f"  {count:3d} emails from {sender}")
        
        # Top domains
        print("\n🌐 Top 10 Domains:")
        for domain, count in domains.most_common(10):
            print(f"  {count:3d} emails from @{domain}")
        
        # Common keywords
        print("\n🔑 Top 20 Keywords in Subjects:")
        for word, count in subjects_words.most_common(20):
            print(f"  {count:3d} times: {word}")
        
        # Suggest categories
        print("\n💡 SUGGESTED CATEGORIES:")
        suggestions = []
        
        # Suggest based on top domains
        for domain, count in domains.most_common(5):
            if count > 10:  # At least 10 emails
                category_name = domain.split('.')[0].capitalize()
                suggestions.append(f"  • Category '{category_name}' with keywords: {domain}")
        
        # Suggest based on keywords
        keyword_groups = {
            'Work': ['project', 'meeting', 'deadline', 'report', 'presentation'],
            'Finance': ['invoice', 'payment', 'bill', 'statement', 'transaction'],
            'Shopping': ['order', 'shipping', 'delivery', 'purchase', 'tracking'],
            'Travel': ['flight', 'hotel', 'booking', 'reservation', 'itinerary']
        }
        
        for category, keywords in keyword_groups.items():
            matching_keywords = [w for w in keywords if w in subjects_words and subjects_words[w] > 5]
            if matching_keywords:
                suggestions.append(f"  • Category '{category}' with keywords: {', '.join(matching_keywords)}")
        
        if suggestions:
            for suggestion in suggestions:
                print(suggestion)
        else:
            print("  No specific suggestions. Your inbox seems well-organized!")
        
        # Suggest VIPs
        print("\n⭐ SUGGESTED VIPs (frequent senders):")
        for sender, count in senders.most_common(10):
            if count > 15:  # More than 15 emails
                print(f"  • {sender} ({count} emails)")
        
        print("\n" + "="*60)
        
        self.speak("Analysis complete. Check the suggestions above.")
    
    def monitor_inbox(self, duration_minutes=60):
        """Monitor inbox for new emails from VIPs"""
        self.speak(f"Starting inbox monitoring for {duration_minutes} minutes")
        print(f"\n🔍 Monitoring inbox for VIP emails...")
        print(f"⏰ Will monitor for {duration_minutes} minutes")
        print("💡 Press Ctrl+C to stop monitoring\n")
        
        # Get current email count
        current_emails = set()
        for email in self.inbox.Items:
            try:
                current_emails.add(email.EntryID)
            except:
                continue
        
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60)
        
        try:
            while time.time() < end_time:
                # Check for new emails
                new_emails = []
                for email in self.inbox.Items:
                    try:
                        if email.EntryID not in current_emails:
                            new_emails.append(email)
                            current_emails.add(email.EntryID)
                    except:
                        continue
                
                # Check if any new email is from VIP
                for email in new_emails:
                    if self.is_vip_email(email):
                        sender = email.SenderName if email.SenderName else email.SenderEmailAddress
                        subject = email.Subject if email.Subject else "(No Subject)"
                        
                        # Show notification
                        self.show_notification(
                            f"VIP Email from {sender}",
                            subject
                        )
                        
                        # Also speak it
                        self.speak(f"New VIP email from {sender}")
                        print(f"🔔 VIP Email: {sender} - {subject}")
                
                # Wait before checking again
                time.sleep(30)  # Check every 30 seconds
        
        except KeyboardInterrupt:
            print("\n⏹️  Monitoring stopped by user")
            self.speak("Monitoring stopped")
    
    def organize_emails(self):
        """Organize emails into folders by category"""
        self.speak("Organizing your emails. This may take a moment.")
        
        emails = self.get_emails(days=30)  # Last 30 days
        print(f"\n📧 Found {len(emails)} emails to organize...")
        
        organized_count = {
            'newsletters': 0,
            'important': 0,
            'social': 0,
            'promotions': 0,
            'receipts': 0
        }
        
        for email in emails:
            try:
                category = self.categorize_email(email)
                
                if category != 'general':
                    # Create folder if needed
                    folder = self.create_folder(category.capitalize())
                    
                    if folder:
                        # Move email to folder
                        email.Move(folder)
                        organized_count[category] += 1
                        
            except Exception as e:
                continue
        
        # Report results
        total = sum(organized_count.values())
        result = f"Done! Organized {total} emails: "
        details = [f"{count} {cat}" for cat, count in organized_count.items() if count > 0]
        result += ", ".join(details)
        
        self.speak(result)
    
    def filter_newsletters(self):
        """Filter and move newsletter emails"""
        self.speak("Filtering newsletters")
        
        emails = self.get_emails(days=30)
        newsletter_folder = self.create_folder("Newsletters")
        
        count = 0
        for email in emails:
            try:
                if self.categorize_email(email) == 'newsletters':
                    email.Move(newsletter_folder)
                    count += 1
            except:
                continue
        
        self.speak(f"Moved {count} newsletters to the Newsletters folder")
    
    def show_stats(self):
        """Show email statistics"""
        emails = self.get_emails(days=7)
        
        unread = sum(1 for e in emails if e.UnRead)
        total = len(emails)
        
        stats = f"You have {unread} unread emails out of {total} total emails from the last 7 days"
        self.speak(stats)
    
    def process_command(self, command):
        """Process user commands"""
        command = command.lower()
        
        if 'organize' in command or 'sort' in command:
            self.organize_emails()
        
        elif 'newsletter' in command or 'filter newsletter' in command:
            self.filter_newsletters()
        
        elif 'stats' in command or 'statistics' in command or 'how many' in command:
            self.show_stats()
        
        elif 'list folders' in command or 'show folders' in command:
            self.list_folders()
        
        elif 'list categories' in command or 'show categories' in command:
            self.list_categories()
        
        elif 'add category' in command:
            # Parse: "add category Work with keywords project, meeting, deadline"
            try:
                parts = command.split('with keywords')
                if len(parts) == 2:
                    category_part = parts[0].replace('add category', '').strip()
                    keywords_part = parts[1].strip()
                    keywords = [k.strip() for k in keywords_part.split(',')]
                    self.add_category(category_part, keywords)
                else:
                    self.speak("Please say: add category NAME with keywords WORD1, WORD2, WORD3")
            except Exception as e:
                self.speak("Sorry, I couldn't understand. Try: add category Work with keywords project, meeting")
        
        elif 'add keywords' in command:
            # Parse: "add keywords project, deadline to category Work"
            try:
                parts = command.split('to category')
                if len(parts) == 2:
                    keywords_part = parts[0].replace('add keywords', '').strip()
                    category_part = parts[1].strip()
                    keywords = [k.strip() for k in keywords_part.split(',')]
                    self.add_keywords_to_category(category_part, keywords)
                else:
                    self.speak("Please say: add keywords WORD1, WORD2 to category NAME")
            except Exception as e:
                self.speak("Sorry, I couldn't understand. Try: add keywords urgent, asap to category Important")
        
        elif 'organize to' in command or 'move to' in command:
            # Parse: "organize to folder Work with keywords project, meeting"
            try:
                parts = command.split('with keywords')
                if len(parts) == 2:
                    folder_part = parts[0].replace('organize to folder', '').replace('move to folder', '').replace('organize to', '').replace('move to', '').strip()
                    keywords_part = parts[1].strip()
                    keywords = [k.strip() for k in keywords_part.split(',')]
                    self.organize_to_folder(folder_part, keywords)
                else:
                    self.speak("Please say: organize to folder NAME with keywords WORD1, WORD2")
            except Exception as e:
                self.speak("Sorry, I couldn't understand. Try: organize to folder Work with keywords project, meeting")
        
        elif 'analyze' in command or 'suggest' in command:
            self.analyze_inbox()
        
        elif 'add vip' in command:
            # Parse: "add vip john@example.com" or "add vip John Smith"
            identifier = command.replace('add vip', '').strip()
            if '@' in identifier:
                self.add_vip(identifier, 'email')
            elif '.' in identifier and '@' not in identifier:
                self.add_vip(identifier, 'domain')
            else:
                self.add_vip(identifier, 'name')
        
        elif 'remove vip' in command:
            identifier = command.replace('remove vip', '').strip()
            self.remove_vip(identifier)
        
        elif 'list vip' in command or 'show vip' in command:
            self.list_vips()
        
        elif 'monitor' in command or 'watch' in command:
            # Parse: "monitor inbox for 60 minutes"
            try:
                import re
                match = re.search(r'(\d+)\s*minute', command)
                if match:
                    duration = int(match.group(1))
                else:
                    duration = 60  # Default 1 hour
                self.monitor_inbox(duration)
            except:
                self.monitor_inbox(60)
        
        elif 'help' in command:
            help_text = """
            📧 EMAIL ORGANIZATION:
            - 'organize my emails' - Sort emails into categories
            - 'filter newsletters' - Move newsletters to folder
            - 'organize to folder NAME with keywords WORD1, WORD2' - Move emails to specific folder
            
            📊 ANALYSIS & INSIGHTS:
            - 'analyze my inbox' - Get smart category suggestions based on your emails
            - 'show stats' - Display email statistics
            
            📁 FOLDER & CATEGORY MANAGEMENT:
            - 'list folders' - Show all your Outlook folders
            - 'list categories' - Show configured email categories
            - 'add category NAME with keywords WORD1, WORD2' - Create new category
            - 'add keywords WORD1, WORD2 to category NAME' - Add keywords to existing category
            
            ⭐ VIP MANAGEMENT:
            - 'add vip EMAIL or NAME' - Mark person/email as VIP
            - 'remove vip EMAIL or NAME' - Remove from VIP list
            - 'list vips' - Show all VIPs
            
            🔔 NOTIFICATIONS:
            - 'monitor inbox for 60 minutes' - Get alerts for VIP emails
            
            ❓ OTHER:
            - 'quit' or 'exit' - Close the bot
            """
            print(help_text)
            self.speak("I can organize emails, analyze your inbox, manage VIPs, and send notifications. What would you like me to do?")
        
        elif 'quit' in command or 'exit' in command or 'bye' in command:
            self.speak("Goodbye! Have a great day!")
            return False
        
        else:
            self.speak("I'm not sure what you want me to do. Try saying 'help' for available commands.")
        
        return True
    
    def run(self):
        """Main bot loop"""
        self.speak("Hello! I'm your Outlook Email Assistant. How can I help you today?")
        
        while True:
            print("\n" + "="*50)
            print("Type a command or say 'voice' to use voice input")
            print("="*50)
            
            user_input = input("👤 You: ").strip()
            
            if user_input.lower() == 'voice':
                command = self.listen()
                if command:
                    if not self.process_command(command):
                        break
            elif user_input:
                if not self.process_command(user_input):
                    break
            
            time.sleep(0.5)

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════╗
    ║   OUTLOOK EMAIL BOT - Phase 1           ║
    ║   Organize & Filter Your Emails         ║
    ╚══════════════════════════════════════════╝
    """)
    
    bot = OutlookEmailBot()
    bot.run()

# Made with Bob
