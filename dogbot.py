from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from gtts import gTTS

# import loggins

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
#
# logger = logging.getLogger(__name__)

# Introduce the application
def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Beep boop! \n/bop for dog pics \n/mew for cats \n/meow for cat facts")


def bop(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="selam")


# mew for cat
def cat_get_url():
    contents = requests.get('https://cataas.com/cat?json=true').json()
    extension = contents['url']
    url = "https://cataas.com" + extension
    return url

def mew(update, context):
    url = cat_get_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

# meow for cat fact
def meow(update, context):
    contents = requests.get('https://catfact.ninja/fact').json()
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=contents['fact'])

# secret function
def phew(update, context):
    text = "We will be okay, my love"
    output = gTTS(text=text, lang='en', slow=False)
    output.save('ouraudio.mp3')
    chat_id = update.message.chat_id
    context.bot.send_audio(chat_id=chat_id, audio=open('ouraudio.mp3', 'rb'))

# main function
def main():
    TOKEN = "5645922373:AAFbabW_uATcSebJTXBhW0CrJih4icoMlGI"
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('mew', mew))
    dp.add_handler(CommandHandler('meow', meow))
    dp.add_handler(CommandHandler('phew', phew))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
