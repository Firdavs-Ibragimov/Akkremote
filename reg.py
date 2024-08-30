from telethon.sync import TelegramClient
from telethon import utils
import csv
from csv import reader
import getopt

import time
er = 6539950
err = '111b6f6f44ba09b5858f9fee99a97322'
done = False
#kutubhonani olish
api_id = er
api_hash = err

while(True):
    number = input("Number(+ qo'ymang): ")
    print(f"Login {number}")
    client = TelegramClient(f"sessions/{number}", api_id, api_hash)

    client.start(number)
    with open('phone.csv', 'a') as f:
        f.write(f"\n+{number}")
    
    client.disconnect()

    done = True

    input("✅✅Tayyor!" if done else "😡Xato!")
