from telethon.sync import TelegramClient
import csv 
from telethon.tl.functions.messages import GetMessagesViewsRequest, ImportChatInviteRequest, SendMessageRequest
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
kanal = str(input("kanal [faqat ochiq kanal!]: "))
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
            time.sleep(1)
            username = await client.get_entity(kanal)
            result = await client.get_messages(username, limit=25)
            a = []
            for m in result:  # show the 10 messages
                a.append(m.id)
            time.sleep(2)
            await client(GetMessagesViewsRequest(peer=username, id=a, increment=True))
            print(f"prosmotr boldi {kanal}")

        with client:
            client.loop.run_until_complete(main())

    except Exception as e:
        print("error", e)
        print("Davom etamiz keyingi sessionda...")
        continue
#s = [44, 46, 46, 45, 44, 40, 38, 38, 118, 105, 98, 94, 224, 216, 207, 204, 265, 671, 626, 739, 664, 939, 760, 707, 634, 606, 644, 598, 589, 600, 608, 684, 606, 563, 543, 519, 535, 526, 510, None, 481, 465, None, 452, 419, 425, 436, None, 418, 388]