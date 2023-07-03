from threading import Thread
from time import sleep
from json import dumps
from user import users


def __updater():
    def update():
        with open(__file__[:__file__.rfind('\\')] + '\\Users.json', 'w') as f:
            save = {}
            for k, v in users.items():
                save[str(k)] = v.__dict__
            f.write(dumps(save))

    while True:
        sleep(4000)
        update()


updater = Thread(target=__updater)
