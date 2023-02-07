from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import Unauthorized, BadRequest

TOKEN = ""

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

def start(update, context):
  update.message.reply_text("Hello brooo, me alive")


def main():
    """Start the bot."""
    dp.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    main()
