"""
Configuration file for Outlook Email Bot
Customize these settings to match your preferences
"""

# Email categories and their keywords
# Add or remove keywords to improve categorization
EMAIL_CATEGORIES = {
    'Newsletters': [
        'newsletter', 'unsubscribe', 'subscription', 'digest',
        'weekly update', 'monthly update', 'mailing list'
    ],
    
    'Important': [
        'urgent', 'important', 'asap', 'priority', 'critical',
        'action required', 'immediate attention', 'time sensitive'
    ],
    
    'Social': [
        'facebook', 'twitter', 'linkedin', 'instagram', 'notification',
        'mentioned you', 'tagged you', 'friend request', 'connection request'
    ],
    
    'Promotions': [
        'sale', 'discount', 'offer', 'deal', 'promo', '% off',
        'limited time', 'special offer', 'save now', 'buy now'
    ],
    
    'Receipts': [
        'receipt', 'invoice', 'payment', 'order confirmation',
        'purchase', 'transaction', 'billing', 'statement'
    ]
}

# Number of days to look back when organizing emails
DAYS_TO_ORGANIZE = 30

# Number of days for statistics
DAYS_FOR_STATS = 7

# Voice settings
VOICE_RATE = 150  # Speed of speech (words per minute)
VOICE_VOLUME = 0.9  # Volume (0.0 to 1.0)

# Microphone settings
MICROPHONE_TIMEOUT = 5  # Seconds to wait for voice input
AMBIENT_NOISE_DURATION = 0.5  # Seconds to adjust for background noise

# Bot personality (customize responses)
BOT_GREETINGS = [
    "Hello! I'm your Outlook Email Assistant. How can I help you today?",
    "Hi there! Ready to organize your emails?",
    "Welcome back! What would you like me to do?"
]

BOT_GOODBYE = [
    "Goodbye! Have a great day!",
    "See you later! Your inbox is looking good!",
    "Bye! Keep that inbox organized!"
]

# Feature flags (enable/disable features)
ENABLE_VOICE = True  # Set to False to disable voice commands
ENABLE_AUTO_FOLDER_CREATION = True  # Automatically create folders
ENABLE_STATISTICS = True  # Show email statistics

# Advanced settings
MAX_EMAILS_TO_PROCESS = 1000  # Maximum emails to process in one run
VERBOSE_MODE = True  # Show detailed progress messages

# Made with Bob
