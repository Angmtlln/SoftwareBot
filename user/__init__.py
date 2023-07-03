from json import loads as __loads


class User:
    def __init__(self, state='start'):
        self.state = state
        self.login = ''
        self.password = ''
        self.notifications = {}

    #def init_notifications(self):
    #    for day in get_course(self.login, self.password).values():
    #        for num in day.values():
    #            self.notifications[f"{num['name']}({num['type']})"] = -1


users = {}

#with open(__file__[:__file__.rfind('\\')] + '\\Users.json') as f:
#    for id, data in __loads(f.read()).items():
#        id = int(id)
#        users[id] = User()
#        for k, v in data.items():
#            setattr(users[id], k, v)