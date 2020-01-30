from bot import openfromfile, getmuudatused, parsepage, makemuudatused, write_msg
import vk_api as vkapi
import schedule
import time
import os

mysql_l = os.environ['MYSQL_LOGIN']
mysql_p = os.environ["MYSQL_PASS"]
access_token = os.environ["ACCESS_TOKEN"]
vk = vkapi.VkApi(token=access_token)

def sendeveryday():
    usergroup = openfromfile(usergroup)
    print("Запускаю рассылку:")
    print(time.strftime("%H:%M:%S"))
    for i in usergroup.keys():
        getmuudatused(usergroup[i], i)

while True:
    if time.strftime("%H:%M:%S") == "22:50:00":
        sendeveryday()
    time.sleep(1.1)
    continue
