from handler import message_handler, users
from main import bot

from handler.answers import texts, keyboards
from telebot.types import Message
from datetime import date
from re import fullmatch
from .answers.texts import emoji


@message_handler.state('start')
def default(message: Message):
    if message.text == '/start':
        users[message.from_user.id].state = 'default'
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.default_markup)


@message_handler.state('default')
def start_page(message: Message):
    id = message.from_user.id
    if message.text == 'About':
        bot.send_message(message.chat.id, texts.About_Button, reply_markup=keyboards.default_markup)
    if message.text == 'Help':
        bot.send_message(message.chat.id, texts.Help_Button, reply_markup=keyboards.default_markup)
        bot.send_message(message.chat.id, 'Merch from the InnoStore', reply_markup=keyboards.merch_markup)
    if message.text == 'Settings':
        users[id].state = 'notifications'
        bot.send_message(message.chat.id, texts.Notification_Button, reply_markup=keyboards.notifications_markup)
    if message.text == 'Sign up':
        if users[id].login == '':
            users[id].state = 'authorization_login'
            bot.send_message(message.chat.id, texts.login, reply_markup=keyboards.remove)
        else:
            bot.send_message(message.chat.id, texts.already_registered, reply_markup=keyboards.default_markup)
    if message.text == '/start':
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.default_markup)

@message_handler.state('notifications')
def notifications_page(message: Message):
    id = message.from_user.id
    if message.text == '/start':
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.default_markup)
    if message.text == f'{emoji["correct"]} ON':
        bot.send_message(message.chat.id, texts.Notifications_On, reply_markup=keyboards.notifications_markup)
    if message.text == f'{emoji["wrong"]} OFF':
        bot.send_message(message.chat.id, texts.Notifications_Off, reply_markup=keyboards.notifications_markup)
    if message.text == f'{emoji["back"]} Back':
        users[id].state = 'default'
        bot.send_message(message.chat.id, texts.Back, reply_markup=keyboards.default_markup)


@message_handler.state('authorization_login')
def authorization_page_login(message: Message):
    id = message.from_user.id
    txt = message.text.lower()
    if fullmatch('[a-z]+.[a-z]+@innopolis.university', txt):
        users[id].state = 'authorization_password'
        users[id].login = message.text
        bot.send_message(message.chat.id, texts.password, reply_markup=keyboards.remove)
    if message.text == '/start':
        users[id].state = 'default'
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.default_markup)

@message_handler.state('authorization_password')
def authorization_page_password(message: Message):
    id = message.from_user.id
    users[id].state = 'default'
    if message.text == '/start':
        bot.send_message(message.chat.id, texts.greetings, reply_markup=keyboards.default_markup)
    bot.send_message(message.chat.id, texts.registered, reply_markup=keyboards.default_markup)
