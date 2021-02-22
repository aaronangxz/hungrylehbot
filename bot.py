#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

import os
import logging
import random
import telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, ParseMode, Bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
PORT = int(os.environ.get('PORT', 5000))
TOKEN = os.environ["TOKEN"]
bot = telegram.Bot(token=TOKEN)

# Enable logging
logging.basicConfig(filename = 'bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

MYSTATE, ACTION, PHOTO, LOCATION, BIO = range(5)

def start(bot: Bot, update: Update, context: CallbackContext) -> int:
    giflink = 'https://media.giphy.com/media/12uXi1GXBibALC/giphy.gif'
    # update.message.reply_animation(
    #     animation=giflink, 
    #     caption= "HELLO",
    #     reply_markup=ReplyKeyboardRemove(),
    #     parse_mode=ParseMode.MARKDOWN
    # )

    reply_keyboard = [['I NEED IDEAS', 'Not hungry la', 'Anything']]
    bot.send_animation(
    chat_id=-1001613440161,
    animation= giflink,
    )

    # bot.sendDocument(chat_id = -1001613440161,Document=giflink),
    update.message.reply_text(
        'Helloo, this is Patrick.🤓\n',
        reply_markup=ReplyKeyboardRemove(),
    )
    update.message.reply_text(
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
        'Anything your head🙄🙄'
    )
    update.message.reply_text(
        'I anyhow give you suggestions ah, you sure?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    ) 
    return ACTION

def places_random(update: Update, context: CallbackContext) -> int:
    randomlist = ['https://goo.gl/maps/P5C5nDYrn8G19LPT6','https://g.page/pollensingapore?share','https://goo.gl/maps/HAeyHWqV3vmDQnNs9',
                    'https://g.page/OverEasySG?share','https://g.page/theassemblygroundcineleisure?share','https://goo.gl/maps/o8DuJkroyoSK1MqK9',
                    'https://goo.gl/maps/1iX2BCbDSKWUVepm7','https://goo.gl/maps/G4cv4uBhP3ve7soc8','https://goo.gl/maps/DGzoTrv45uD8HXKw5',
                    'https://goo.gl/maps/YKWo1ckMJ3qeEXVZA','https://g.page/wangdaebakbbq?share','https://goo.gl/maps/Fftfy929T1dS7V6t7',
                    'https://goo.gl/maps/3TANCBdHR9kfVm1w5','https://goo.gl/maps/LAhF4yuABZpGvHgr7','https://goo.gl/maps/rkNoBPjYK5LtK2Ax8',
                    'https://g.page/prego-sg?share','https://goo.gl/maps/74wZZ3vUwj3aFmGGA','https://g.page/jibiru?share',
                    'https://g.page/menbaka_sg?share','https://g.page/HaidilaoIMM?share','https://goo.gl/maps/x5e4Ro9NxgucRHjM8',
                    'https://g.page/BrotzeitWestgate?share','https://goo.gl/maps/UR37N1bBYAHfyPLN8','https://goo.gl/maps/QL6kJ1Hu9MxL3wVQ8',
                    'https://goo.gl/maps/JWNgN5uFBGo1FjTx8','https://goo.gl/maps/9hmwFiL9DC5ugpEN8','https://g.page/ENSakaba-JEM?share',
                    'https://goo.gl/maps/qDeTVYc9RxSbU9rv8','https://goo.gl/maps/Gz2XCxEdNP5oomxu7','https://goo.gl/maps/5VtjHapbwQ714RmF6',
                    'https://goo.gl/maps/MENsUrKojYjeVP649','https://goo.gl/maps/n3zcrLJZsXkZYiwT8','https://goo.gl/maps/v5MJhQGfwMrDy2d9A',
                    'https://g.page/OPPABBQ?share','https://g.page/burger-lobster-jewel-changi?share','https://goo.gl/maps/u7DJozX5Knsno5Gq6',
                    'https://g.page/elfuegosg?share','https://g.page/TanukiRawJewel?share','https://goo.gl/maps/Et4cABQ1rMkbe4u5A',
                    'https://goo.gl/maps/TLAJvBSW6bY9A4Kw5','https://goo.gl/maps/GYPWsS6sYiDVa7xQA','https://goo.gl/maps/fGzi5m6hUJcYBSBE9',
                    'https://goo.gl/maps/xDcAHz7fWh4aF8kL8','https://goo.gl/maps/ZCb5nQAVZRrii7Ab9','https://goo.gl/maps/3KhF4bfoRwtr9Tid8',
                    'https://goo.gl/maps/CrKBC3PQcaL5sU1M9','https://g.page/itacho-sushi-bedok-mall?share','https://goo.gl/maps/VoMsTWLwSMMMf1g88',
                    'https://goo.gl/maps/HKGCTcCXar1u9jN87','https://g.page/tonito-latin-american-kitchen?share','https://goo.gl/maps/B9MC5B9wYBdzFhG17',
                    'https://goo.gl/maps/nub6Auhu9TdnB14z7','https://goo.gl/maps/JU4gyNxV6qY1VXzbA'
                ]
    #bot.sendLocation(@hungrylehbot, latitude=lat, longitude=lon),
    update.message.reply_text(
        random.choice(randomlist),
        reply_markup=ReplyKeyboardRemove(),
    )    
    update.message.reply_text(
        'Nah, enjoy😛',
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
                    'https://g.page/jibiru?share','https://g.page/menbaka_sg?share','https://goo.gl/maps/B9MC5B9wYBdzFhG17'
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
                'https://g.page/tonito-latin-american-kitchen?share','https://goo.gl/maps/JU4gyNxV6qY1VXzbA']
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
                'https://goo.gl/maps/n3zcrLJZsXkZYiwT8','https://goo.gl/maps/v5MJhQGfwMrDy2d9A','https://g.page/OPPABBQ?share',
                'https://goo.gl/maps/nub6Auhu9TdnB14z7']
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

def exit(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! Chat me again next time ❤️', reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text('I''m a parrot🦜')
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    updater = Updater(token = TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                    CommandHandler('random', places_random),
                    CommandHandler('exit', exit)],
        states={
            MYSTATE: [MessageHandler(Filters.regex('^I NEED IDEAS$'), ideas),
                    MessageHandler(Filters.regex('^Not hungry la$'), Nah),
                    MessageHandler(Filters.regex('^Anything$'), randomplaces)],
            ACTION: [MessageHandler(Filters.regex('^Lmao lame$'), ideas),
                    MessageHandler(Filters.regex('^Nice!$'), ending),
                    MessageHandler(Filters.regex('^Central$'), places_central), 
                    MessageHandler(Filters.regex('^East$'), places_east),
                    MessageHandler(Filters.regex('^West$'), places_west),
                    MessageHandler(Filters.regex('^YES PLS$'), places_random)]
        },
        fallbacks=[CommandHandler('exit', exit)],
    )

    dp.add_handler(conv_handler)
    # on different commands - answer in Telegram
    #dp.add_handler(CommandHandler("start", start))
    #dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    #updater.bot.deleteWebhook()

    # Start the Bot
    #updater.start_polling()

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