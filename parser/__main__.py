import logging

import vk_api
import requests
from environ import Env

env = Env()
Env.read_env('../.env')


if __name__ == '__main__':
    session = vk_api.VkApi(login=env('VK_LOGIN'), password=env('VK_PASSWORD'), token=env('VK_TOKEN'))
    session.auth(token_only=True)

    vk = session.get_api()

    print(1)
