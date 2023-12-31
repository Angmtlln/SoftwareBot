from telebot.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    ReplyKeyboardRemove
from datetime import date, timedelta
from user import User
from .texts import emoji, merch

default_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
buttonAbout = KeyboardButton("About")
buttonHelp = KeyboardButton("Help")
buttonSettings = KeyboardButton("Settings")
buttonAuthorize = KeyboardButton("Sign up")
default_markup.add(buttonAbout, buttonHelp, buttonAuthorize, buttonSettings)



notifications_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
buttonOn = KeyboardButton(text=f'{emoji["correct"]} ON')
buttonOff = KeyboardButton(text=f'{emoji["wrong"]} OFF')
buttonBack = KeyboardButton(text=f'{emoji["back"]} Back')
notifications_markup.add(buttonOn, buttonOff, buttonBack)


merch_markup = InlineKeyboardMarkup(row_width=1)
for i in merch():
    buttonX = InlineKeyboardButton(text=i,callback_data='i')
    merch_markup.add(buttonX)


remove = ReplyKeyboardRemove()
