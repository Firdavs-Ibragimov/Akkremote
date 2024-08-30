import asyncio
from telethon import TelegramClient, utils
from telethon.tl.types import Message
from telethon.tl.functions.account import UpdateStatusRequest
import csv
import aiosqlite

print("Yaratuvchi: @Firdavsbek")
phonecsv = "phone"

async def main():
    global phlist
    with open(f'{phonecsv}.csv', 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
    print('NOMERLAR: ' + str(len(phlist)))

    api_id = 22962676
    api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'

    yutmagan_raqamlar = []  # Raqamlar uchun ro'yhat
    yutgan = []  # Yutgan raqamlar uchun bo'sh ro'yhat

    for index, deltaxd in enumerate(phlist, start=1):
        try:
            phone = utils.parse_phone(deltaxd)
            print(f'{index}-akkaunt: {phone}')
            async with aiosqlite.connect(f"sessions/{phone}.db", timeout=10) as db:
                client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
                await client.start(phone)
                await client(UpdateStatusRequest(offline=False))

                async def raqam():
                    bot = 777000
                    username = await client.get_entity(bot)
                    history = await client.get_messages(username, limit=5)
                    is_message = all(isinstance(m, Message) and m.message for m in history)
                    if is_message:
                        yutmagan_raqamlar.append(phone)
                    else:
                        yutgan.append(phone)
                    s1 = len(yutmagan_raqamlar)
                    s2 = len(yutgan)          
                    print(f"{s1} - yutmadi \n{s2} - yutdi \n")

                await raqam()
        except Exception as e:
            print(f"ERROR: {e}")
            continue
        finally:
            await client.disconnect()

    s1 = len(yutmagan_raqamlar)
    s2 = len(yutgan)         
    print(f"{s1} - yutmadi \n{s2} - yutdi \n")     

    print("Yutgan raqamlar: ")
    for index, phone in enumerate(yutgan, start=1):
        try:
            async with aiosqlite.connect(f"sessions/{phone}.db", timeout=10) as db:
                client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
                await client.start(phone)
                user = await client.get_me()
                print(f"   Raqami: {user.phone}, Ismi: {user.first_name}, Useri: {user.username}")
        except Exception as e:
            print(f"   ERROR: {e}")
        finally:
            await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())