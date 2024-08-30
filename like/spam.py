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
bot = "@spambot"
limit = int(input("time 2 akount bosish vaqti:"))
qowiwjm = 0
qowiwjm2 = int(str(len(phlist)))
spam = []
spam_emas = []
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
            await client.send_message(username, f"/start")
            m = await client.get_messages(username)
            print(m[0].text)
            if ("Dear" in m[0].text or "Hurmatli" in m[0].text or "Здравствуйте" in m[0].text):
                spam.append(phone)
                print("s+")
            else:
                spam_emas.append(phone)
                print("-se")
        with client:
            client.loop.run_until_complete(main())

    except Exception as e:
        print("error", e)
        print("Davom etamiz keyingi sessionda...")
        continue

s1 = int(str(len(spam)))
s2 = int(str(len(spam_emas)))

print(f"\n\n\n{s1} - spam \n{s2} - spam emas")