from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "7029542469:AAHLcGlDBRo_qwI4QCWApiNJ78w989J_MI0"
BOT_USERNAME: Final =  "@App_demo_123_bot"
GAME_URL: Final = "t.me/App_demo_123_bot/AppDemo123App"

# Command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text(f"Hello!!! \nPlease start the game by clicking the URL: {GAME_URL}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("This is demo app for rabitap!")


# Responses
def handle_response(text: str) -> str:
  processed: str = text.lower()

  if "hello" in processed:
    return "hey there!"
  elif "how are you?" in processed:
    return "I am good"
  else:
    return "I do not understand your message! Please try again!"
  
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  messag_type: str = update.message.chat.type
  text: str = update.message.text

  print(f"User ({update.message.chat.id}) in {messag_type}: '{text}'")

  if messag_type == "group":
    if BOT_USERNAME in text:
      new_text: str = text.replace(BOT_USERNAME, "").strip()
      response: str = handle_response(new_text)
    else:
      return
  else:
    response: str = handle_response(text)

  print("BOT: ", response)
  await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
  print(f"Update {update} caused error {context.error}")

if __name__ == "__main__":
  print("Starting bot...")
  app = Application.builder().token(TOKEN).build()

  # Commands
  app.add_handler(CommandHandler("start", start_command))
  app.add_handler(CommandHandler("help", help_command))

  # Messages
  app.add_handler(MessageHandler(filters.TEXT, handle_message))

  # Errors
  app.add_error_handler(error)

  # Polls the bot
  print("Polling...")
  app.run_polling(poll_interval=1)