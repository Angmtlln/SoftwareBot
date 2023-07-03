from telebot import types
from user import User, users


class Handler:
    def __init__(self):
        self.__handlers = {}

    def handle(self, mess: types.Message):
        user_id = mess.from_user.id
        if user_id not in users:
            users[user_id] = User()
        state = users[user_id].state
        args = []
        if state in self.__handlers:
            self.__handlers[state](mess, *args)

    def state(self, name: str):
        def decorator(func):
            self.__handlers[name] = func

        return decorator


message_handler = Handler()
callback_query_handler = Handler()

from . import message_handles
from . import callback_query_handles
