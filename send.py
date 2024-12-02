import os
from telegram.constants import ChatAction

async def send_file(query, bot, file_path, title):
    """Send the processed video to the user."""
    try:
        await bot.send_chat_action(chat_id=query.message.chat_id, action=ChatAction.UPLOAD_DOCUMENT)
        await bot.send_document(chat_id=query.message.chat_id, document=open(file_path, "rb"), caption=f"🎉 Here is your video: *{title}*", parse_mode="Markdown")
        query.edit_message_text("✅ Download complete! Enjoy your video.")
    finally:
        os.remove(file_path)  # Cleanup after sending
