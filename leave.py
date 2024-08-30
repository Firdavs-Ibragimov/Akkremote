from telethon.sync import TelegramClient

import csv 

from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import types, utils, errors

from telethon.tl.functions.channels import LeaveChannelRequest
import time
#kutubhonani olish

phonecsv = "phone"

with open(f'{phonecsv}.csv', 'r') as f:
    global phlist
    phlist = [row[0] for row in csv.reader(f)]
print(' всего 📝: '+str(len(phlist)))

prchk = input(' если приватный 🔒(может не работать) вводи Y. если нет, тогда  🌏N  (Y/N)  вводи с большой буквы, не маленькой: ')
if prchk.lower() == 'y':
    prlink = input('вводи приватный линк ⛓: ')
elif prchk.lower() == 'n':
    prlink = input(' username через @ : ')
qowiwjm = 0
qowiwjm2 = int(str(len(phlist)))

indexx = 0
print(" создатель t.me/Facty_iq  ")
for deltaxd in phlist[qowiwjm:qowiwjm2]:
    indexx += 1
    phone = utils.parse_phone(deltaxd)
    print(f"Login {phone}")
    client = TelegramClient(f"sessions/{phone}", 2152072,'004e98412f47431215095770454c9da4')
    client.start(phone)
    print(f'Index : {indexx}')
    try:
        if prchk.lower() == 'y':
            time.sleep(2)
            client(ImportChatInviteRequest(prlink))
        elif prchk.lower() == 'n':
            time.sleep(2)
            client(LeaveChannelRequest(prlink))
    except Exception as e:
        print(e)
        continue