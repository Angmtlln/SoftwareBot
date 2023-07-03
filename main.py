from telebot import TeleBot, types
from handler import message_handler, callback_query_handler
import config
from user.update import updater

bot = TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def message(mess: types.Message):
    message_handler.handle(mess)


@bot.callback_query_handler(lambda _: True)
def callback_query(callback: types.CallbackQuery):
    callback_query_handler.handle(callback)


if __name__ == '__main__':
    print('Bot started working')
    updater.start()
    bot.polling(none_stop=True)
    updater.join()
