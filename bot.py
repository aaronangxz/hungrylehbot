#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

import os
import logging
import random
import telegram
import json
from time import sleep 
#from random import random 
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, ParseMode, Bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from googleplaces import GooglePlaces, types, lang

prevlocation = None
prevrequest = None
repeat = False
chose_central = False
chose_east = False
chose_west = False

GOOGLEAPI = os.environ["GOOGLEAPI"]
google_places = GooglePlaces(GOOGLEAPI)
PORT = int(os.environ.get('PORT', 5000))
TOKEN = os.environ["TOKEN"]
bot = telegram.Bot(token=TOKEN)
TYPESPEED = [0.25,0.5,0.75,1]
QUERYDELAY = [0,1,2,3,4,5,6,7,8,9]

# Enable logging
logging.basicConfig(filename='bot.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

MYSTATE, ACTION, USERLOCATION= range(3)

def start(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    giflink = 'https://media.giphy.com/media/12uXi1GXBibALC/giphy.gif'
    # update.message.reply_animation(
    #     animation=giflink, 
    #     caption= "HELLO",
    #     reply_markup=ReplyKeyboardRemove(),
    #     parse_mode=ParseMode.MARKDOWN
    # )


    reply_keyboard = [['I NEED IDEAS', 'Not hungry la', 'Anything']]

    context.bot.send_animation(
    chat_id=update.message.chat_id,
    animation= giflink,
    )

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))
    # bot.sendDocument(chat_id = -1001613440161,Document=giflink),
    
    update.message.reply_text(
        'Helloo ' + user.first_name + ', this is Patrick 🤓\n',
        reply_markup=ReplyKeyboardRemove(),
    )

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'Not sure where to makan?\n'
        'See /help for a list of commands!',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return MYSTATE

def ideas(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    reply_keyboard = [['Central', 'East','West','Near me','Send Location']]
    logger.info("%s needs ideas", user.first_name)

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'Where are you willing to travel to?📍',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION

def location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    update.message.reply_text(
        'Send me you location!\n'
        'Attach > Location > Send My Location'
    )
    return USERLOCATION

def getLocation(update: Update, context: CallbackContext) -> int:
    # msg = update.message
    # user_data['msg'] = msg
    # user_data['id'] = update.update_id
    # update.message.reply_text('lat: {}, lng: {}'.format(
    #     msg.location.latitude, msg.location.longitude))
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    # update.message.reply_text(
    #     'Your location is ' + str(user_location.latitude) + ', ' + str(user_location.longitude)
    # )
    
    query_result = google_places.nearby_search(
        lat_lng={'lat': user_location.latitude, 'lng': user_location.longitude},
        radius= 500, types=[types.TYPE_AIRPORT,
                            types.TYPE_AMUSEMENT_PARK,
                            types.TYPE_AQUARIUM,
                            types.TYPE_ART_GALLERY,
                            types.TYPE_ATM,
                            types.TYPE_BAKERY,
                            types.TYPE_BANK,
                            types.TYPE_BAR,
                            types.TYPE_BOOK_STORE,
                            types.TYPE_BOWLING_ALLEY,
                            types.TYPE_BUS_STATION,
                            types.TYPE_CAFE,
                            types.TYPE_CAMPGROUND,
                            types.TYPE_CASINO,
                            types.TYPE_CHURCH,
                            types.TYPE_CITY_HALL,
                            types.TYPE_CLOTHING_STORE,
                            types.TYPE_CONVENIENCE_STORE ,
                            types.TYPE_COURTHOUSE ,
                            types.TYPE_DENTIST,
                            types.TYPE_DEPARTMENT_STORE ,
                            types.TYPE_DOCTOR,
                            types.TYPE_ELECTRONICS_STORE ,
                            types.TYPE_EMBASSY ,
                            types.TYPE_ESTABLISHMENT ,
                            types.TYPE_FINANCE ,
                            types.TYPE_FIRE_STATION ,
                            types.TYPE_FLORIST ,
                            types.TYPE_FOOD ,
                            types.TYPE_FURNITURE_STORE ,
                            types.TYPE_GAS_STATION ,
                            types.TYPE_GROCERY_OR_SUPERMARKET ,
                            types.TYPE_GYM,
                            types.TYPE_HAIR_CARE ,
                            types.TYPE_HEALTH,
                            types.TYPE_HOME_GOODS_STORE ,
                            types.TYPE_HOSPITAL,
                            types.TYPE_INSURANCE_AGENCY ,
                            types.TYPE_JEWELRY_STORE ,
                            types.TYPE_LIBRARY,
                            types.TYPE_LIQUOR_STORE ,
                            types.TYPE_LOCAL_GOVERNMENT_OFFICE,
                            types.TYPE_LODGING ,
                            types.TYPE_MEAL_DELIVERY ,
                            types.TYPE_MEAL_TAKEAWAY ,
                            types.TYPE_MOSQUE ,
                            types.TYPE_MOVIE_RENTAL ,
                            types.TYPE_MOVIE_THEATER ,
                            types.TYPE_MOVING_COMPANY ,
                            types.TYPE_MUSEUM,
                            types.TYPE_NIGHT_CLUB ,
                            types.TYPE_PAINTER,
                            types.TYPE_PARK,
                            types.TYPE_PARKING,
                            types.TYPE_PET_STORE ,
                            types.TYPE_PHARMACY ,
                            types.TYPE_PHYSIOTHERAPIST ,
                            types.TYPE_PLACE_OF_WORSHIP,
                            types.TYPE_PLUMBER ,
                            types.TYPE_POLICE ,
                            types.TYPE_POST_OFFICE ,
                            types.TYPE_REAL_ESTATE_AGENCY ,
                            types.TYPE_RESTAURANT ,
                            types.TYPE_ROOFING_CONTRACTOR,
                            types.TYPE_RV_PARK,
                            types.TYPE_SCHOOL ,
                            types.TYPE_SHOE_STORE ,
                            types.TYPE_SHOPPING_MALL ,
                            types.TYPE_SPA,
                            types.TYPE_STADIUM ,
                            types.TYPE_STORAGE ,
                            types.TYPE_STORE ,
                            types.TYPE_SUBWAY_STATION ,
                            types.TYPE_SYNAGOGUE,
                            types.TYPE_TAXI_STAND ,
                            types.TYPE_TRAIN_STATION ,
                            types.TYPE_TRAVEL_AGENCY ,
                            types.TYPE_UNIVERSITY,
                            types.TYPE_VETERINARY_CARE ,
                            types.TYPE_ZOO])
    # delaytime = random.randint(0,len(query_result.places)-1)

    logger.info("query results: %s",query_result)
    logger.info("query results are: %s",query_result.places)


    if query_result.places == []:
                update.message.reply_text('Hmmm, I can\'t find any landmarks near you..')
    else: 
        for place in query_result.places:        
            # query_result.places.get_details()
            update.message.reply_text('Let me guess..you are at ' + query_result.places[0].name + ' now? 🤔\n')
            break

    
    update.message.reply_text('Oops this is all I can do now, check back later!\n'
                                'See /help for a list of other commands!')
    # logger.info("query results: %s",query_result[0].name)
    # global prevlocation
    # global prevrequest
    # prevlocation = query_result.places[0].name 
    # prevrequest = prevlocation
    return ConversationHandler.END 

def maprequest(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Where are you?\n'
                                 '(Type the name of the nearest mall / mrt / area)\n\n'
                                 'I am slowly learning and slightly smarter now!\n'
                                 'Try short names e.g. JEM, NEX, 313 etc. 😛\n\n'
                                 'I will search through places up to a 1km radius so sometimes it will be a little bit far away from you 🥺\n'
                                 'And also I have a tiny brain, forgive me if I repeat the same place multiple times 🙈' )
    # global prevrequest 
    
    return USERLOCATION

def maprequest_again(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Where are you?\n'
                                 '(Type the name of the nearest mall / mrt)\n\n'
                                 'I am still dumb so try to give me more details!\n\n'
                                 'For example: "313 Somerset" will yield better results than "313"')
    return USERLOCATION

def mapquery(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s queries map", user.first_name)
    reply_keyboard = [['Nice!', 'Nahh']]
    global chose_central, chose_east, chose_west
    global repeat
    global prevrequest 
    global prevlocation 

    if repeat == False:
        update.message.reply_text(
            'Okay here you go 😬',
            reply_markup=ReplyKeyboardRemove(),
        )
    else: 
        update.message.reply_text(
            'Okay I try again 🥺',
            reply_markup=ReplyKeyboardRemove(),
        )
    

    # prevrequest = update.message.text
    # logger.info("prevrequest is %s",prevrequest)
    
    # prevlocation =  update.message.text

    # logger.info("prevlocation is %s",prevlocation)
    # context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    # sleep(random.choice(TYPESPEED))

    # userquery = MessageHandler(Filters.text)
    #sleep(random.choice(TYPESPEED))
    # query_result = ''
    # global prevlocation
    # if prevlocation is None:
    #     prevlocation = update.message.text

    if prevlocation == None:
        prevlocation = update.message.text
        prevrequest = prevlocation
        logger.info("prevlocation is %s",prevlocation)
    elif prevlocation == 'Nahh' or prevlocation == 'Near Me' or prevlocation == "Lmao lame": 
        prevlocation = prevrequest
        logger.info("prevlocation is %s",prevlocation)
    elif prevlocation == '/exit':
        return ConversationHandler.END

    logger.info("prevlocation is %s",prevlocation)
    repeat = True

    if chose_central == True or chose_east == True or chose_west == True:
        randomradius = random.randint(100,5000)
    else: randomradius = random.randint(100,1000)

    query_result = google_places.nearby_search(
        location= (prevlocation + ' Singapore'),
        radius= randomradius, types=[types.TYPE_FOOD,types.TYPE_RESTAURANT,types.TYPE_CAFE])
    logger.info("%s searched %s with radius of %d", user.first_name,prevlocation,randomradius)
    logger.info("query results are: %s",query_result.places)

    delaytime = random.randint(0,len(query_result.places)-1)
    logger.info("delaytime is %f",delaytime)
    logger.info("query result: %s",query_result.places[delaytime].name)

    for place in query_result.places:        
        query_result.places[delaytime].get_details()
        update.message.reply_text('Want to try ' + query_result.places[delaytime].name + ' ? 🤔\n'
                                    + query_result.places[delaytime].url)
        # jsondata = json.loads( query_result.places[delaytime].get_details())
        context.bot.sendLocation(update.message.chat_id, latitude= float(place.geo_location['lat']),longitude=float(place.geo_location['lng']))
        # context.bot.sendLocation(update.message.chat_id, latitude= query_result.places[delaytime].geo_location['lat'], longitude=query_result.places[delaytime].geo_location['lng'])
        
        for photo in query_result.places[delaytime].photos:
            photo.get(maxheight=500, maxwidth=500)
            context.bot.sendPhoto(chat_id=update.message.chat_id,photo = photo.url)
            # logger.info("details: %s",query_result.places[delaytime].details)
            # logger.info("Price level is %s",query_result.places[delaytime].details['price_level'])
            # logger.info("Ratings: %s",query_result.places[delaytime].details['rating'])
            # update.message.reply_text('Ratings: %s',query_result.places[delaytime].details['result']['rating'])
            break

        context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
        sleep(random.choice(TYPESPEED))
        update.message.reply_text(
                'Can ah?',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
            )
        return ACTION

def Nah(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s is not hungry.", user.first_name)

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        '??? You sure anot.🥺',
        reply_markup=ReplyKeyboardRemove(),
    )

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))
    
    update.message.reply_text(
        'Nevermind come back later when you are.',
        reply_markup=ReplyKeyboardRemove(),
    )
    update.message.reply_text(
        'Bye😗',
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

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'I anyhow give you suggestions ah, you sure?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    ) 
    return ACTION

def places_random(update: Update, context: CallbackContext) -> int:
    query_result = None
    user = update.message.from_user
    logger.info("%s selected random.", user.first_name)

    randomradius = random.randint(250,15000)

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    query_result = google_places.nearby_search(
        location= 'Singapore', keyword= 'food',
        radius= randomradius, types=[types.TYPE_FOOD,types.TYPE_RESTAURANT,types.TYPE_CAFE])
    logger.info("%s chose random with a radius of %d", user.first_name,randomradius)
    logger.info("query results are: %s",query_result.places)

    delaytime = random.randint(0,len(query_result.places)-1)
    logger.info("delaytime is %f",delaytime)
    logger.info("random result: %s",query_result.places[delaytime].name)

    for place in query_result.places:        
        query_result.places[delaytime].get_details()
        update.message.reply_text('Okay, go to ' + query_result.places[delaytime].name + '😛\n'
                                    + query_result.places[delaytime].url)
        # context.bot.sendLocation(update.message.chat_id, latitude= place.geo_location['lat'], longitude=place.geo_location['lng'])
        context.bot.sendLocation(update.message.chat_id, latitude= float(query_result.places[delaytime].geo_location['lat']), longitude=float(query_result.places[delaytime].geo_location['lng']))
        break
    for photo in query_result.places[delaytime].photos:
        photo.get(maxheight=500, maxwidth=500)
        context.bot.sendPhoto(chat_id=update.message.chat_id,photo = photo.url)
        return ConversationHandler.END        

'''
def places_random(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s selected random.", user.first_name)
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
    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))
    
    update.message.reply_text(
        'Nah, enjoy😛',
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END
'''
def places_central(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s selected Central.", user.first_name)
    reply_keyboard = [['Nice!', 'Lmao lame']]

    global repeat
    global chose_central
    global prevlocation
    global prevrequest

    repeat = True
    chose_central = True
    prevlocation = "Central"
    prevrequest = prevlocation

    randomradius = random.randint(0,5000)

    query_result = google_places.nearby_search(
        location= 'Central, Singapore', keyword= 'food',
        radius= randomradius, types=[types.TYPE_FOOD,types.TYPE_RESTAURANT,types.TYPE_CAFE])
    logger.info("%s chose Central with a radius of %d", user.first_name,randomradius)
    logger.info("query results are: %s",query_result.places)

    delaytime = random.randint(0,len(query_result.places)-1)
    logger.info("delaytime is %f",delaytime)
    logger.info("Central result: %s",query_result.places[delaytime].name)

    for place in query_result.places:        
        query_result.places[delaytime].get_details()
        update.message.reply_text('Okay, want to try ' + query_result.places[delaytime].name + '?😛\n'
                                    + query_result.places[delaytime].url)
        # context.bot.sendLocation(update.message.chat_id, latitude= place.geo_location['lat'], longitude=place.geo_location['lng'])
        context.bot.sendLocation(update.message.chat_id, latitude= float(query_result.places[delaytime].geo_location['lat']), longitude=float(query_result.places[delaytime].geo_location['lng']))
        for photo in query_result.places[delaytime].photos:
            photo.get(maxheight=500, maxwidth=500)
            context.bot.sendPhoto(chat_id=update.message.chat_id,photo = photo.url)
            break
        break

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'Can ah?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION

'''
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
    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'Can ah?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION
'''

def places_east(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s selected East", user.first_name)
    reply_keyboard = [['Nice!', 'Lmao lame']]

    global prevlocation
    global prevrequest
    global repeat
    global chose_east
    prevlocation = "Tampines"
    prevrequest = prevlocation
    chose_east = True
    repeat = True

    randomradius = random.randint(1000,5000)

    query_result = google_places.nearby_search(
        location= 'Tampines, Singapore', keyword= 'food',
        radius= randomradius, types=[types.TYPE_FOOD,types.TYPE_RESTAURANT,types.TYPE_CAFE])
    logger.info("%s chose East with a radius of %d", user.first_name,randomradius)
    logger.info("query results are: %s",query_result.places)

    delaytime = random.randint(0,len(query_result.places)-1)
    logger.info("delaytime is %f",delaytime)
    logger.info("East result: %s",query_result.places[delaytime].name)

    for place in query_result.places:        
        query_result.places[delaytime].get_details()
        update.message.reply_text('Okay, want to try ' + query_result.places[delaytime].name + '?😛\n'
                                    + query_result.places[delaytime].url)
        # context.bot.sendLocation(update.message.chat_id, latitude= place.geo_location['lat'], longitude=place.geo_location['lng'])
        context.bot.sendLocation(update.message.chat_id, latitude= float(query_result.places[delaytime].geo_location['lat']), longitude=float(query_result.places[delaytime].geo_location['lng']))
        for photo in query_result.places[delaytime].photos:
            photo.get(maxheight=500, maxwidth=500)
            context.bot.sendPhoto(chat_id=update.message.chat_id,photo = photo.url)
            break
        break

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'Can ah?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION

'''
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
    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'Can ah?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION
'''
def places_west(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s selected West.", user.first_name)
    reply_keyboard = [['Nice!', 'Lmao lame']]

    global prevlocation
    global prevrequest
    global repeat
    global chose_west

    prevlocation = "Jurong East"
    prevrequest = prevlocation
    repeat = True
    chose_west = True

    randomradius = random.randint(0,5000)

    query_result = google_places.nearby_search(
        location= 'Jurong East, Singapore', keyword= 'food',
        radius= randomradius, types=[types.TYPE_FOOD,types.TYPE_RESTAURANT,types.TYPE_CAFE])
    logger.info("%s chose West with a radius of %d", user.first_name,randomradius)
    logger.info("query results are: %s",query_result.places)

    delaytime = random.randint(0,len(query_result.places)-1)
    logger.info("delaytime is %f",delaytime)
    logger.info("West result: %s",query_result.places[delaytime].name)

    for place in query_result.places:        
        query_result.places[delaytime].get_details()
        update.message.reply_text('Okay, want to try ' + query_result.places[delaytime].name + '?😛\n'
                                    + query_result.places[delaytime].url)
        # context.bot.sendLocation(update.message.chat_id, latitude= place.geo_location['lat'], longitude=place.geo_location['lng'])
        context.bot.sendLocation(update.message.chat_id, latitude= float(query_result.places[delaytime].geo_location['lat']), longitude=float(query_result.places[delaytime].geo_location['lng']))
        for photo in query_result.places[delaytime].photos:
            photo.get(maxheight=500, maxwidth=500)
            context.bot.sendPhoto(chat_id=update.message.chat_id,photo = photo.url)
            break
        break

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'Can ah?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION

'''
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
    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'Can ah?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return ACTION
'''
def ending(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s is exiting", user.first_name)

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'Enjoy your meal!😋😋😋',
        reply_markup=ReplyKeyboardRemove()
    )
    global chose_central, chose_east, chose_west
    global prevrequest
    global prevlocation
    global repeat
    repeat = False
    prevrequest = None
    prevlocation = None
    chose_central = chose_east = chose_west = False
    return ConversationHandler.END

def exit(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)

    # context.bot.sendLocation(update.message.chat_id, latitude=1.290188, longitude=103.851563),

    context.bot.sendChatAction(chat_id=update.message.chat_id, action = telegram.ChatAction.TYPING)
    sleep(random.choice(TYPESPEED))

    update.message.reply_text(
        'Bye! Chat with me again next time ❤️', reply_markup=ReplyKeyboardRemove()
    )
    global chose_central, chose_east, chose_west
    global prevrequest
    global prevlocation
    global repeat
    repeat = False
    prevrequest = None
    prevlocation = None
    chose_central = chose_east = chose_west = False
    return ConversationHandler.END

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Hello! Welcome to Hungry Leh. Patrick will try his best to help you decide what to eat.\n\n'
                                '🍔Commands\n'
                                '/start to start asking\n'
                                '/random to generate random places\n'
                                '/help to access help menu\n'
                                '/exit to quit\n\n'
                                '🍣Features\n'
                                'Patrick will look for random restaurants within a few km radius.\n'
                                'He will then send you the restaurant name, google maps link and pictures!\n'
                                'Feel free to hurt his feelings by rejecting his suggestions and ask for a new one.\n\n'
                                '🍺Future Developments\n'
                                '- To choose cuisine / price range\n'
                                '- Suggest places based on overall ratings\n\n'
                                'By @zzeexxuuaann')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text('Something is wrong.. try /start')
    #update.message.reply_text(update.message.text)

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
                    CommandHandler('exit', exit),
                    CommandHandler("help", help)],
        states={
            MYSTATE: [MessageHandler(Filters.regex('^I NEED IDEAS$'), ideas),
                    MessageHandler(Filters.regex('^Not hungry la$'), Nah),
                    MessageHandler(Filters.regex('^Anything$'), randomplaces),
                    CommandHandler('random', places_random),
                    CommandHandler("exit", exit),
                    CommandHandler("help", help)],
            ACTION: [MessageHandler(Filters.regex('^Central$'), places_central), 
                    MessageHandler(Filters.regex('^East$'), places_east),
                    MessageHandler(Filters.regex('^West$'), places_west),
                    MessageHandler(Filters.regex('^Near me$'), maprequest),
                    MessageHandler(Filters.regex('^YES PLS$'), places_random),
                    MessageHandler(Filters.regex('^Lmao lame$'), mapquery),
                    MessageHandler(Filters.regex('^Nahh$'), mapquery),
                    MessageHandler(Filters.regex('^Nice!$'), ending),
                    MessageHandler(Filters.regex('^Send Location$'), location),
                    CommandHandler('random', places_random),
                    CommandHandler("exit", exit),
                    CommandHandler("help", help)],
            USERLOCATION: [MessageHandler(Filters.text,mapquery),
                        MessageHandler(Filters.location, getLocation),
                        CommandHandler('random', places_random),
                        CommandHandler("exit", exit),
                        CommandHandler("help", help)],
        },
        fallbacks=[CommandHandler('exit', exit)],
    )

    dp.add_handler(conv_handler)
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler('random', places_random))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))
    #dp.add_handler(MessageHandler(Filters.text, mapquery))

    # log all errors
    dp.add_error_handler(error)

    #updater.bot.deleteWebhook()

    # Start the Bot
    # updater.start_polling()

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