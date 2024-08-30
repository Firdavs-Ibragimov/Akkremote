from telethon.sync import TelegramClient
import csv
from telethon import types, utils, errors
import time

api_id = 6810439
api_hash = '66ac3b67cce1771ce129819a42efe02e'

jm7uz = int(input("sessionda mavjud raqam kiriting: "))
bot = 777000



phone = utils.parse_phone(jm7uz)
print(f"Login {phone}")
client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
client.start(phone)

try:
    async def jm7uz():
        a = input("kode jonatizmi:")
        username = await client.get_entity(bot) 
        history = await client.get_messages(username, limit=1)
        for m in history: 
            print(m.message)
        
    with client:
        client.loop.run_until_complete(jm7uz())


except Exception as e:
    print("error:  " , e)