token = "5213269532:AAFrQiLuFeVgRfMmy1H6aXwLzdIsuE1x2Xs"
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import random

updater = Updater(token, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(f"your cocksize is {random.randint(0,50)}cm")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('cocksize', start))
  
updater.start_polling()