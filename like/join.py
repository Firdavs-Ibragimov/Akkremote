from telethon.sync import TelegramClient
import csv 
from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import types, utils, errors

from telethon.tl.functions.channels import GetChannelsRequest, GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
import time
#kutubhonani olish
phonecsv = "phone"

with open(f'{phonecsv}.csv', 'r') as f:
    global phlist
    phlist = [row[0] for row in csv.reader(f)]
print('Jami📝: '+str(len(phlist)))

prchk = input('agar yopiq🔒 bolsa y (ochiq) 🌏N yozin : ')
if prchk.lower() == 'y':
    prlink = input('Guruh private Link ⛓: ')
elif prchk.lower() == 'n':
    prlink = input('Guruh username : ')
odamlarjm = 1
stop = int(str(len(phlist)))
stop = (odamlarjm + stop)
qowiwjm = 0
qowiwjm2 = int(str(len(phlist)))

indexx = 0
print("yaratuvchi: t.me/al_haq_jaloliddin")
for deltaxd in phlist[qowiwjm:qowiwjm2]:
    indexx += 1
    phone = utils.parse_phone(deltaxd)
    print(f"Login {phone}")
    client = TelegramClient(f"sessions/{phone}", 2152072,'004e98412f47431215095770454c9da4')
    client.start(phone)
    print(f'Index : {indexx}')
    try:
        async def main():
            if prchk.lower() == 'y':
                await client(ImportChatInviteRequest(prlink))
            elif prchk.lower() == 'n':
                await client(JoinChannelRequest(prlink))
            if odamlarjm >= stop:
                print(f'{odamlarjm + stop} tayyor tugadi.')
                quit()
        with client:
            client.loop.run_until_complete(main())
    except errors.FloodWaitError as e:
        print('Uxlash vaqti', e.seconds, 'seconds')
        time.sleep(e.seconds)