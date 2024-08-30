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
channel = str(input("rostan ham hamma kanallarda chqb ketaszmi? = Y"))
qowiwjm = 0
qowiwjm2 = int(str(len(phlist)))

indexx = 0
print("yaratuvchi: t.me/al_haq_jaloliddin")
for deltaxd in phlist[qowiwjm:qowiwjm2]:
    indexx += 1
    phone = utils.parse_phone(deltaxd)
    print(f"Login {phone}")
    client = TelegramClient(f"sessions/{phone}", 6383658,'02f94e696f8230da8ca6d93aad570e08')
    client.start(phone)
    print(f'Index : {indexx}')
    if prchk.lower() == 'y':
        try:
            for dialog in client.iter_dialogs():
                if dialog.is_channel:
                    dialog.delete()
        except Exception as e:
            print("Error:", e)
            print("Davom etamiz keyingi sessionda...")
            continue