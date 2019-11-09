import telebot
import datetime
import pytz
import time
import emoji
import random
import os
token = os.environ.get('TOKEN')
sabina = int(os.environ.get('sabina'))
bot = telebot.TeleBot(token)
utcnow = datetime.datetime.now(tz=pytz.UTC)
russia = utcnow.astimezone(pytz.timezone('Europe/Moscow'))
now = utcnow.astimezone(pytz.timezone('Asia/Chongqing'))
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.reply_to(message, 'Ты опять время забыла да?' + emoji.emojize('\U0001F644'))
    bot.send_message(message.chat.id, str(now.strftime("%H:%M:%S, %A, %B %d, %Y")))
    if russia.day == 10 and russia.month == 11:
        bot.send_message(sabina, 'Happy birthday you still cutie little pie :3')
        x = random.randint(1, 8)
        photo = open(f'{x}.jpg', 'rb')
        bot.send_photo(sabina, photo)
        audio = open('Ирина_Аллегрова_С_днем_рождения!.mp3', 'rb')
        bot.send_audio(sabina, audio)


bot.polling(none_stop=True, timeout=60)
