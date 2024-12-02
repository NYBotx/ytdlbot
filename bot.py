import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from ui import start_message, help_message, quality_keyboard, downloading_message, completed_message
from download import process_download
from send import send_file

# Ensure a downloads directory exists
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Replace with your bot token

async def start(update: Update, context):
    """Welcome message with options."""
    await update.message.reply_text(**start_message())

async def help_command(update: Update, context):
    """Help message."""
    await update.message.reply_text(**help_message())

async def handle_video_link(update: Update, context):
    """Display quality options for a given video link."""
    url = update.message.text
    if "youtube.com" in url or "youtu.be" in url:
        await update.message.reply_text("Choose the quality to download:", reply_markup=quality_keyboard(url))
    else:
        await update.message.reply_text("❌ Invalid URL. Please provide a valid YouTube link.")

async def download_handler(update: Update, context):
    """Download and process video based on the selected quality."""
    query = update.callback_query
    await query.answer()

    resolution, url = query.data.split("|")
    await query.edit_message_text(**downloading_message(resolution))

    # Download and process video
    file_path, title = process_download(url, resolution, DOWNLOAD_DIR)

    # Send the file
    await send_file(query, context.bot, file_path, title)

def main():
    """Run the bot."""
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_video_link))
    app.add_handler(CallbackQueryHandler(download_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
