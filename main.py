import datetime
import random

import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

def get_welcome() -> str:
    current_time = datetime.datetime.now()
    if 0<= current_time.hour <6:
        return 'Доброй ночи!'
    if 6<= current_time.hour <12:
        return 'Доброе утро!'
    if 12<= current_time.hour <18:
        return 'Добрый день!'
    else:
        return 'Добрый вечер!'


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = f'{get_welcome()} Я бот, который поможет тебе выбрать, что посмотреть сегодня)\n\n'\
           f'Список команд:\n'\
           f'/get_film - получить фильм\n'\
           f'/get_series - получить сериал \n'\
           f'/get_cartoon - получить мультфильм '

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['get_film'])
def get_film(message: telebot.types.Message):
    with open('films.txt', 'r', encoding='Utf-8') as file:
        films = file.read().split('\n')
    film = random.choice(films)
    bot.send_message(message.chat.id, text=f'Сегодня вечером стоит посмотреть: "{film}"')


@bot.message_handler(commands=['get_series'])
def get_series(message: telebot.types.Message):
    with open('series.txt', 'r', encoding='Utf-8') as file:
        series = file.read().split('\n')
    serial = random.choice(series)
    bot.send_message(message.chat.id, text=f'Сегодня стоит начать смотреть: "{serial}"')


@bot.message_handler(commands=['get_cartoon'])
def get_cartoon(message: telebot.types.Message):
    with open('cartoons.txt', 'r', encoding='Utf-8') as file:
        cartoons = file.read().split('\n')
    cartoon = random.choice(cartoons)
    bot.send_message(message.chat.id, text=f'Сегодня стоит посмотреть: "{cartoon}"')

@bot.message_handler(func=lambda _: True)
def unknown_command(message: telebot.types.Message):
    bot.send_message(message.chat.id, text=f'Неизвестная команда')


if __name__=='__main__':
    print ('Бот запущен')
    bot.infinity_polling()
