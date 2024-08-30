from telethon.sync import TelegramClient
import csv 
from telethon.tl.functions.messages import ImportChatInviteRequest, SendMessageRequest
from telethon import types, utils, errors
import random
from telethon.tl.functions.channels import LeaveChannelRequest
import time
#kutubhonani olish
phonecsv = "phone"

with open(f'{phonecsv}.csv', 'r') as f:
    global phlist
    phlist = [row[0] for row in csv.reader(f)]
print('Jami📝: '+str(len(phlist)))

prchk = 'Y'
bot = str(input("bot:"))
id = str(input("ref id yozing:"))
limit = int(input("time 2 akount bosish vaqti:"))
qowiwjm = 0
qowiwjm2 = int(str(len(phlist)))

indexx = 0
print("yaratuvchi: t.me/al_haq_jaloliddin")
for deltaxd in phlist[qowiwjm:qowiwjm2]:
    indexx += 1
    phone = utils.parse_phone(deltaxd)
    print(f"Login {phone}")
    api_id = 6810439
    api_hash = '66ac3b67cce1771ce129819a42efe02e'
    client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
    client.start(phone)
    print(f'Index : {indexx}')
    try:
        async def main():
            time.sleep(limit)
            username = await client.get_entity(bot)
            await client.send_message(username, f"/start {id}")

            m = await client.get_messages(username)
            print(m[0].message)


        with client:
            client.loop.run_until_complete(main())

    except Exception as e:
        print("error", e)
        print("Davom etamiz keyingi sessionda...")
        continue