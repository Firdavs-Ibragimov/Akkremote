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

prchk = 'y'
channel = str(input("kanal [@ qo'shmang]:"))
idl = int(input("id [postni id raqamini yozing]:"))
butt = int(input("button raqami:(1 2 yoki 3 4 chi orni bo'yicha kiriting:)"))
limit = int(input("limit kiritin har bosishdagi to'xtash vaqti:"))
qowiwjm = 0
qowiwjm2 = int(str(len(phlist)))

indexx = 0
print("tuzuvchi: t.me/al_haq_jaloliddin")
for deltaxd in phlist[qowiwjm:qowiwjm2]:
    indexx += 1
    phone = utils.parse_phone(deltaxd)
    print(f"Login {phone}")
    client = TelegramClient(f"sessions/{phone}", 6383658,'02f94e696f8230da8ca6d93aad570e08')
    client.start(phone)
    print(f'Index : {indexx}')
    if prchk.lower() == 'y':
        try:
            time.sleep(limit)
            msg = client.get_messages(channel, ids=[idl])
            msg[0].click(butt-1)
        except Exception as e:
            print("Error:", e)
            print("Davom etamiz keyingi sessionda...")
            continue