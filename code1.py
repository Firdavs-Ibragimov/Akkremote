from telethon.sync import TelegramClient
from telethon import utils
import csv
from telethon import types, utils, errors
import time

api_id = 22962676
api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'

done = False

try:
    while True:
        raqam = input("NOMERNI KIRITING (exit yoki tugatish uchun 'exit' ni kiriting): ")
        
        if raqam == 'exit':
            break
        
        phone = utils.parse_phone(raqam)
        print(f"{phone}")
        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
        client.start(phone)

        async def raqam():
            a = input("JO'NATDINGIZMI: ")
            bot = 777000  # Bu qatorda yozib qo'ydim, siz o'zingizga kerakli botni tanlaysiz
            username = await client.get_entity(bot)
            history = await client.get_messages(username, limit=1)
            for m in history:
                print(m.message)

        with client:
            client.loop.run_until_complete(raqam())

except Exception as e:
    print("ERROR:  ", e)
    done = False

input("TAYYOR!" if done else "XATO!")