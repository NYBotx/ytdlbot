from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_message():
    """Return the start message."""
    return {
        "text": "👋 Welcome to YouTube Downloader Bot!\n\nSend me a YouTube link to get started 🎥",
        "parse_mode": "Markdown"
    }

def help_message():
    """Return the help message."""
    return {
        "text": "📖 *How to Use*\n\n1. Send me a YouTube link.\n2. Choose your desired quality.\n3. Wait while I process your video.\n4. Download and enjoy! 😄",
        "parse_mode": "Markdown"
    }

def quality_keyboard(url):
    """Generate the quality selection keyboard."""
    keyboard = [
        [InlineKeyboardButton("360p", callback_data=f"360p|{url}"), InlineKeyboardButton("480p", callback_data=f"480p|{url}")],
        [InlineKeyboardButton("720p", callback_data=f"720p|{url}"), InlineKeyboardButton("1080p", callback_data=f"1080p|{url}")]
    ]
    return InlineKeyboardMarkup(keyboard)

def downloading_message(resolution):
    """Return the downloading message."""
    return {
        "text": f"⏳ Downloading video in *{resolution}*... Please wait.",
        "parse_mode": "Markdown"
    }

def completed_message(title):
    """Return the completed message."""
    return {
        "text": f"✅ *{title}* is ready! Sending it to you now...",
        "parse_mode": "Markdown"
  }
  
