import requests
from pprint import pprint


APP_ID = 7332332
ACCESS_TOKEN = '972b62ebb4ffa7ffbc8c342930cb5526361204c02408a3076877c618d57fd5b8f4eb795182bc88a7a5958'
vk = 'https://vk.com/id'


class User:
    users = input('Введите идентификатор пользователей: ')
    split_users = users.split()

    def __init__(self, vk):
        self.vk = vk

    def get_user1(self):
        return self.split_users[0]

    def get_user2(self):
        return self.split_users[2]

    def get_params(self):
        return {
            'access_token': ACCESS_TOKEN,
            'source_uid': self.get_user1(),
            'target_uid': self.get_user2(),
            'v': 5.52
        }

    def get_friends(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return response.json()


user = User(vk)
friends = user.get_friends()

for friend in friends['response']:
    friends_adress = (vk + str(friend))
    print(friends_adress)
    friend = 'id' + str(friend)


# 2402235 & 81133852
