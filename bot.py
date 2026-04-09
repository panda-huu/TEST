import os  # <--- Ye add karo
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# ... (baaki handlers same rahenge) ...
# 1. Setup logging to see what's happening
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
BOT_TOKEN = "8344312549:AAGKxZix5YjEaOyMhxPBaZ3zlyU1zQ1TMPo"
# 2. Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Hello {update.effective_user.first_name}! I'm your Python bot. How can I help?"
    )

# 3. Command: /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Try sending me a message, and I'll echo it back!")

# 4. Message Handler: Echoes the user's text
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

if __name__ == '__main__':
    # ⚠️ UPDATE: Panel se bhej gaya token read karo
    token = os.environ.get('BOT_TOKEN')
    
    if not token or token == 'YOUR_TOKEN_HERE':
        print("❌ Error: BOT_TOKEN nahi mila!")
    else:
        application = ApplicationBuilder().token(token).build()
        
        application.add_handler(CommandHandler('start', start))
        application.add_handler(CommandHandler('help', help_command))
        application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
        
        print("✅ Bot is polling...")
        application.run_polling()
