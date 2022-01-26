import Bots.nkwasiasem.key as keys
from telegram.ext import *
import Bots.nkwasiasem.responses as Response


print('Bot has started')

def start(update, context):
    update.message.reply_text('type bibia')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = Response.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print("Update " + {update}  + "caused error" + {context.error})

def main():
    updater = Updater(keys.NKWASIASEM_key, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))


    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

    main()