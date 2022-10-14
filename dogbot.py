from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from gtts import gTTS

def bop(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="selam")

def main():
    TOKEN = "5645922373:AAFbabW_uATcSebJTXBhW0CrJih4icoMlGI"
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
