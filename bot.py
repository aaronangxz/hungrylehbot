#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import os
import logging
import random
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
# PORT = int(os.environ.get('PORT', 8443))
TOKEN = '1613440161:AAFlP57hml8a-bwMn1t3NDlNUuL9DbIVGjY'

# Enable logging
logging.basicConfig(filename = 'bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

MYSTATE, ACTION, PHOTO, LOCATION, BIO = range(5)

def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['I NEED IDEAS', 'Not hungry la', 'Random']]
    update.message.reply_text(
        'Helloo, this is Patrick.\n'
        'Not sure where to makan?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return MYSTATE

def ideas(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    reply_keyboard = [['Central', 'East','West']]
    logger.info("%s needs ideas", user.first_name)
    update.message.reply_text(
        'Where are you willing to travel to?📍',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION

def Nah(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s is not hungry.", user.first_name)
    update.message.reply_text(
        '??? You sure anot.🥺',
        reply_markup=ReplyKeyboardRemove(),
    )
    update.message.reply_text(
        'Nevermind come back later when you are.',
        reply_markup=ReplyKeyboardRemove(),
    )
    update.message.reply_text(
        'Bye!',
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END


def randomplaces(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    reply_keyboard = [['YES PLS']]
    logger.info("%s selected random.", user.first_name)
    update.message.reply_text(
        'Indecisive?🤔'
    )
    update.message.reply_text(
        'I give you random suggestions ah?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    ) 
    return ACTION

def places_random(update: Update, context: CallbackContext) -> int:
    randomlist = ['https://goo.gl/maps/P5C5nDYrn8G19LPT6','https://g.page/pollensingapore?share','https://goo.gl/maps/HAeyHWqV3vmDQnNs9',
                    'https://g.page/OverEasySG?share','https://g.page/theassemblygroundcineleisure?share','https://goo.gl/maps/o8DuJkroyoSK1MqK9',
                    'https://goo.gl/maps/1iX2BCbDSKWUVepm7','https://goo.gl/maps/G4cv4uBhP3ve7soc8','https://goo.gl/maps/DGzoTrv45uD8HXKw5',
                    'https://goo.gl/maps/YKWo1ckMJ3qeEXVZA','https://g.page/wangdaebakbbq?share','https://goo.gl/maps/Fftfy929T1dS7V6t7','https://goo.gl/maps/3TANCBdHR9kfVm1w5',
                    'https://goo.gl/maps/LAhF4yuABZpGvHgr7','https://goo.gl/maps/rkNoBPjYK5LtK2Ax8','https://g.page/prego-sg?share','https://goo.gl/maps/74wZZ3vUwj3aFmGGA',
                    'https://g.page/jibiru?share','https://g.page/menbaka_sg?share','https://g.page/HaidilaoIMM?share','https://goo.gl/maps/x5e4Ro9NxgucRHjM8','https://g.page/BrotzeitWestgate?share',
                'https://goo.gl/maps/UR37N1bBYAHfyPLN8','https://goo.gl/maps/QL6kJ1Hu9MxL3wVQ8','https://goo.gl/maps/JWNgN5uFBGo1FjTx8',
                'https://goo.gl/maps/9hmwFiL9DC5ugpEN8','https://g.page/ENSakaba-JEM?share','https://goo.gl/maps/qDeTVYc9RxSbU9rv8',
                'https://goo.gl/maps/Gz2XCxEdNP5oomxu7','https://goo.gl/maps/5VtjHapbwQ714RmF6','https://goo.gl/maps/MENsUrKojYjeVP649',
                'https://goo.gl/maps/n3zcrLJZsXkZYiwT8','https://goo.gl/maps/v5MJhQGfwMrDy2d9A','https://g.page/OPPABBQ?share',
                ]
    #bot.sendLocation(@hungrylehbot, latitude=lat, longitude=lon),
    update.message.reply_text(
        random.choice(randomlist),
        reply_markup=ReplyKeyboardRemove(),
    )    
    update.message.reply_text(
        'Here you go, enjoy😛',
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END

def places_central(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s selected Central.", user.first_name)
    reply_keyboard = [['Nice!', 'Lmao lame']]
    centrallist = ['https://goo.gl/maps/P5C5nDYrn8G19LPT6','https://g.page/pollensingapore?share','https://goo.gl/maps/HAeyHWqV3vmDQnNs9',
                    'https://g.page/OverEasySG?share','https://g.page/theassemblygroundcineleisure?share','https://goo.gl/maps/o8DuJkroyoSK1MqK9',
                    'https://goo.gl/maps/1iX2BCbDSKWUVepm7','https://goo.gl/maps/G4cv4uBhP3ve7soc8','https://goo.gl/maps/DGzoTrv45uD8HXKw5',
                    'https://goo.gl/maps/YKWo1ckMJ3qeEXVZA','https://g.page/wangdaebakbbq?share','https://goo.gl/maps/Fftfy929T1dS7V6t7','https://goo.gl/maps/3TANCBdHR9kfVm1w5',
                    'https://goo.gl/maps/LAhF4yuABZpGvHgr7','https://goo.gl/maps/rkNoBPjYK5LtK2Ax8','https://g.page/prego-sg?share','https://goo.gl/maps/74wZZ3vUwj3aFmGGA',
                    'https://g.page/jibiru?share','https://g.page/menbaka_sg?share',
                    'https://g.page/burger-lobster-jewel-changi?share','https://goo.gl/maps/u7DJozX5Knsno5Gq6','https://g.page/elfuegosg?share',
                'https://g.page/TanukiRawJewel?share','https://goo.gl/maps/Et4cABQ1rMkbe4u5A','https://goo.gl/maps/TLAJvBSW6bY9A4Kw5',
                'https://goo.gl/maps/GYPWsS6sYiDVa7xQA','https://goo.gl/maps/fGzi5m6hUJcYBSBE9','https://goo.gl/maps/xDcAHz7fWh4aF8kL8',
                'https://goo.gl/maps/ZCb5nQAVZRrii7Ab9','https://goo.gl/maps/3KhF4bfoRwtr9Tid8','https://goo.gl/maps/CrKBC3PQcaL5sU1M9',
                'https://g.page/itacho-sushi-bedok-mall?share','https://goo.gl/maps/VoMsTWLwSMMMf1g88','https://goo.gl/maps/HKGCTcCXar1u9jN87',
                'https://g.page/tonito-latin-american-kitchen?share'
                    ]
    #bot.sendLocation(@hungrylehbot, latitude=lat, longitude=lon),
    update.message.reply_text(
        random.choice(centrallist),
        reply_markup=ReplyKeyboardRemove(),
    )    
    update.message.reply_text(
        'Can ah?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION

def places_east(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s selected East", user.first_name)
    reply_keyboard = [['Nice!', 'Lmao lame']]
    eastlist = ['https://g.page/burger-lobster-jewel-changi?share','https://goo.gl/maps/u7DJozX5Knsno5Gq6','https://g.page/elfuegosg?share',
                'https://g.page/TanukiRawJewel?share','https://goo.gl/maps/Et4cABQ1rMkbe4u5A','https://goo.gl/maps/TLAJvBSW6bY9A4Kw5',
                'https://goo.gl/maps/GYPWsS6sYiDVa7xQA','https://goo.gl/maps/fGzi5m6hUJcYBSBE9','https://goo.gl/maps/xDcAHz7fWh4aF8kL8',
                'https://goo.gl/maps/ZCb5nQAVZRrii7Ab9','https://goo.gl/maps/3KhF4bfoRwtr9Tid8','https://goo.gl/maps/CrKBC3PQcaL5sU1M9',
                'https://g.page/itacho-sushi-bedok-mall?share','https://goo.gl/maps/VoMsTWLwSMMMf1g88','https://goo.gl/maps/HKGCTcCXar1u9jN87',
                'https://g.page/tonito-latin-american-kitchen?share']
    #bot.sendLocation(@hungrylehbot, latitude=lat, longitude=lon),
    update.message.reply_text(
        random.choice(eastlist),
        reply_markup=ReplyKeyboardRemove(),
    )    
    update.message.reply_text(
        'Can ah?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION

def places_west(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s selected West.", user.first_name)
    reply_keyboard = [['Nice!', 'Lmao lame']]
    westlist = ['https://g.page/HaidilaoIMM?share','https://goo.gl/maps/x5e4Ro9NxgucRHjM8','https://g.page/BrotzeitWestgate?share',
                'https://goo.gl/maps/UR37N1bBYAHfyPLN8','https://goo.gl/maps/QL6kJ1Hu9MxL3wVQ8','https://goo.gl/maps/JWNgN5uFBGo1FjTx8',
                'https://goo.gl/maps/9hmwFiL9DC5ugpEN8','https://g.page/ENSakaba-JEM?share','https://goo.gl/maps/qDeTVYc9RxSbU9rv8',
                'https://goo.gl/maps/Gz2XCxEdNP5oomxu7','https://goo.gl/maps/5VtjHapbwQ714RmF6','https://goo.gl/maps/MENsUrKojYjeVP649',
                'https://goo.gl/maps/n3zcrLJZsXkZYiwT8','https://goo.gl/maps/v5MJhQGfwMrDy2d9A','https://g.page/OPPABBQ?share']
    #bot.sendLocation(@hungrylehbot, latitude=lat, longitude=lon),
    update.message.reply_text(
        random.choice(westlist),
        reply_markup=ReplyKeyboardRemove()
    )    
    update.message.reply_text(
        'Can ah?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION

def ending(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s is exiting", user.first_name)
    update.message.reply_text(
        'Enjoy your meal!😋😋😋',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

'''
def photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text(
        'Gorgeous! Now, send me your location please, ' 'or send /skip if you don\'t want to.'
    )

    return LOCATION


def skip_photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text(
        'I bet you look great! Now, send me your location please, ' 'or send /skip.'
    )

    return LOCATION


def location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    update.message.reply_text(
        'Maybe I can visit you sometime! ' 'At last, tell me something about yourself.'
    )

    return BIO


def skip_location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text(
        'You seem a bit paranoid! ' 'At last, tell me something about yourself.'
    )

    return BIO


def bio(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Thank you! I hope we can talk again some day.')

    return ConversationHandler.END
'''


def exit(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! Chat me again next time ❤️', reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

# def start(update, context):
#     """Send a message when the command /start is issued."""
#     update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),CommandHandler('random', places_random)],
        states={
            MYSTATE: [MessageHandler(Filters.regex('^I NEED IDEAS$'), ideas),
                    MessageHandler(Filters.regex('^Not hungry la$'), Nah),
                    MessageHandler(Filters.regex('^Random$'), randomplaces)],
            ACTION: [MessageHandler(Filters.regex('^Lmao lame$'), ideas),
                    MessageHandler(Filters.regex('^Nice!$'), ending),
                    MessageHandler(Filters.regex('^Central$'), places_central), 
                    MessageHandler(Filters.regex('^East$'), places_east),
                    MessageHandler(Filters.regex('^West$'), places_west),
                    MessageHandler(Filters.regex('^YES PLS$'), places_random)]
                    #CommandHandler('skip', skip_photo)]
        },
        fallbacks=[CommandHandler('exit', exit)],
    )

    dp.add_handler(conv_handler)
    # on different commands - answer in Telegram
    #dp.add_handler(CommandHandler("start", start))
    #dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    updater.bot.deleteWebhook()

    # Start the Bot
    updater.start_polling()



    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port = PORT,
                          url_path= TOKEN)
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook('https://hungrylehbot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()