from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import re
import json
from keys import bot_Token
from telegram.ext import updater


def get_quote():
    response = requests.get("https://zenquotes.io/api/random").json()
    json_data = json.loads(response.text)
    quote= json_data[0]['q'] + " -" + json_data[0]["a"]
    return(quote)

def send_quote(bot, update):
    url = get_quote()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, quote=url)

def main():
    updater = Updater('bot_Token')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('motivate',send_quote))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()


