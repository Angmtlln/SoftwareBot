import telebot
from telebot import types


bot = telebot.TeleBot('6155094584:AAE5isPBEmZ1quEGKICR2h5y7bZ9YGhN2sM')

emoji = {'correct': '\U00002705', 'wrong': '\U0000274C', 'back': '\U00002B05', }


@bot.message_handler(commands=['start'])
def bot_start(message: types.Message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("About")
    button2 = types.KeyboardButton("Help")
    button3 = types.KeyboardButton("Settings")
    markup1.add(button1, button2, button3)
    url_button = types.InlineKeyboardButton(text="Авторизоваться на сайте", url="https://sport.innopolis.university")
    bot.send_message(message.chat.id,
                     text='\tWelcome to InnoSportChallengesBot. To register you on Innopolis Sport website, please write your email',
                     reply_markup=markup1)


@bot.message_handler(content_types=['text'])
def Buttom(message):
    if message.text == "About":
        hi = '\U0001F44B'
        bot.send_message(message.chat.id,
                         f'{hi}Hello! \nIt is a bot with sport challenges for Innopolis University’s students. \nHere you can perform sports challenges, earn SportPoints for it and exchange them for merch.')
    elif message.text == "Help":
        bot.send_message(message.chat.id,
                         'If you have any questions or suggestions you can write it here: @sleeepy_zzzzz ')

    elif message.text == "Settings":
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button4 = types.KeyboardButton(text=f'{emoji["correct"]} ON')
        button5 = types.KeyboardButton(text=f'{emoji["wrong"]} OFF')
        markup2.add(button4, button5)
        bot.send_message(message.chat.id, "Turn the Notifications ON or OFF?", reply_markup=markup2)

    elif message.text == f'{emoji["correct"]} ON':
        bot.send_message(message.chat.id, "Notifications are ON")
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button4 = types.KeyboardButton(text=f'{emoji["correct"]} ON')
        button5 = types.KeyboardButton(text=f'{emoji["wrong"]} OFF')
        button6 = types.KeyboardButton(text=f'{emoji["back"]} Back')
        markup2.add(button4, button5, button6)
        bot.send_message(message.chat.id, "Turn the Notifications ON or OFF?", reply_markup=markup2)

    elif message.text == f'{emoji["wrong"]} OFF':
        markup1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton("About")
        button2 = types.KeyboardButton("Help")
        button3 = types.KeyboardButton("Settings")
        markup1.add(button1, button2, button3)
        url_button = types.InlineKeyboardButton(text="Авторизоваться на сайте",
                                                url="https://sport.innopolis.university")
        bot.send_message(message.chat.id,
                         text='\tWelcome to InnoSportChallengesBot. To register you on Innopolis Sport website, please write your email',
                         reply_markup=markup1)

    elif message.text == f'{emoji["back"]} Back':
        markup1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton("About")
        button2 = types.KeyboardButton("Help")
        button3 = types.KeyboardButton("Settings")
        markup1.add(button1, button2, button3)
        url_button = types.InlineKeyboardButton(text="Авторизоваться на сайте",
                                                url="https://sport.innopolis.university")
        bot.send_message(message.chat.id,
                         text='\tWelcome to InnoSportChallengesBot. To register you on Innopolis Sport website, please write your email',
                         reply_markup=markup1)
    elif "@innopolis.university" in message.text:
        markup1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton("About")
        button2 = types.KeyboardButton("Help")
        button3 = types.KeyboardButton("Settings")
        markup1.add(button1, button2, button3)
        url_button = types.InlineKeyboardButton(text="Авторизоваться на сайте",
                                                url="https://sport.innopolis.university")
        bot.send_message(message.chat.id,
                         text='\tPlease write your password',
                         reply_markup=markup1)
    else:
        markup1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button1 = types.KeyboardButton("About")
        button2 = types.KeyboardButton("Help")
        button3 = types.KeyboardButton("Settings")
        markup1.add(button1, button2, button3)
        url_button = types.InlineKeyboardButton(text="Авторизоваться на сайте",
                                                url="https://sport.innopolis.university")
        bot.send_message(message.chat.id,
                         text='\tYour account has been successfully registered',
                         reply_markup=markup1)
bot.polling(none_stop=True, interval=0)
