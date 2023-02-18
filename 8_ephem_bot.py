import logging
import ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from random import randint

import settings

now_date = datetime.now()

logging.basicConfig(filename='bot.log', level=logging.INFO)

today = f'{now_date.year}/{now_date.month}/{now_date.day}'
planets = {'Mars' : ephem.Mars(today), 'Venus' : ephem.Venus(today), 'Mercury' : ephem.Mercury(today), 'Uranus' : ephem.Uranus(today), 'Jupiter' : ephem.Jupiter(today),
           'Neptune' : ephem.Neptune(today), 'Saturn' : ephem.Saturn(today)} 

def greet_user(update, context):
    print('Вызван /start')
    print(update)
    update.message.reply_text('Здравствуй!')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def ephem_f(update, context):
    comand, planet_name = map(str, update.message.text.split())
    print(planet_name)
    ephem_try = planets.get(planet_name, '1')
    if ephem_try != '1': 
        update.message.reply_text(ephem.constellation(planets[planet_name]))
    else:
        update.message.reply_text('Я не знаю такую планету(')
            

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', ephem_f))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()