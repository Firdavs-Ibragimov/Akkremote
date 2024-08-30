from telethon.sync import TelegramClient
import csv
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import types, utils, errors
from telethon.tl.functions.account import UpdateStatusRequest

from telethon.tl.functions.channels import GetChannelsRequest, GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
print("Yaratuvchi @Firdavs_up")
phonecsv = "phone"

with open(f'{phonecsv}.csv', 'r') as f:
    phlist = [row[0] for row in csv.reader(f)]
print('NOMERLAR: ' + str(len(phlist)))

channels = []

# Kanallar linklarini so'rang
num_channels = int(input("Qancha kanalga a'zo bo'lishni xohlaysiz? "))
for i in range(num_channels):
    channel_link = input(f'Kanal linkini kiriting #{i + 1:}: ')
    channels.append(channel_link)

odamlarjm = 1
stop = int(str(len(phlist)))
stop = (odamlarjm + stop)
qowiwjm = 0
qowiwjm2 = int(str(len(phlist)))

indexx = 0

for deltaxd in phlist[qowiwjm:qowiwjm2]:
    try:
        indexx += 1
        phone = utils.parse_phone(deltaxd)
        print(f'[{indexx}]: {phone}')
        client = TelegramClient(f"sessions/{phone}", 22962676, '543e9a4d695fe8c6aa4075c9525f7c57')
        client.start(phone)
        client(UpdateStatusRequest(offline=False))

        async def main(channel_link):
            await client(JoinChannelRequest(channel_link))
            if odamlarjm >= stop:
                print(f'{odamlarjm + stop} TUGADI TAYYOR.')
                quit()

        for channel_link in channels:
            with client:
                client.loop.run_until_complete(main(channel_link))
    except Exception as e:
        print("ERROR: ", e)
        print("DAVOM ETAMIZ...")
        continue