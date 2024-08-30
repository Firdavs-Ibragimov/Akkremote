from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

api_id = '22962676'
api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'
phone_number = '+998940460706'

print("Yaratuvchi: @Firdavsbek")
phonecsv = "phone"

async def main():
    global phlist
    with open(f'{phonecsv}.csv', 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]

client = TelegramClient('session_name', api_id, api_hash)

async def change_bio(new_bio):
    await client.start(phone_number)
    await client(UpdateProfileRequest(about=new_bio))

new_bio = 'salom bu bio'
client.loop.run_until_complete(change_bio(new_bio))
