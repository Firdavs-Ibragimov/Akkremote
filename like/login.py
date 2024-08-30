from telethon.sync import TelegramClient
from telethon import utils
import csv
from csv import reader
from data import er, err

done = False
#kutubhonani olish
print("\nDasturchi jm7uz\n")
with open('phone.csv', 'r') as f:
    str_list = [row[0] for row in csv.reader(f)]

    
    po = 0
    for pphone in str_list:
        api_id = er
        api_hash = err
        phone = utils.parse_phone(pphone)
        po += 1

        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
        client.start(phone)

        client.disconnect()
        print()
    done = True