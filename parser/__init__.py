import requests
import lxml.html
from vk_api import VkApi
from environ import Env

env = Env()
Env.read_env('../.env')


if __name__ == '__main__':
    vk = VkApi(login=env('VK_LOGIN'), password=env('VK_PASSWORD'), token=env('VK_TOKEN'))
    vk.auth()

    response = vk.http.get('https://vk.com/studio/artist/1659885348465312512', stream=True)

    response.raw.decode_content = True

    tree = lxml.html.parse(response.raw)

    res = tree.xpath('//*[@id="box_layer_bg"]')
    # res = tree.xpath('//*[@id="react_root"]/div/div/div[2]/div[2]/div/div/section/div/div[3]')

    print(1)
