from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateUsernameRequest


api_id = '22962676'
api_hash = '543e9a4d695fe8c6aa4075c9525f7c57'
phone_number = '+998940460706'

client = TelegramClient('session_name', api_id, api_hash)

async def change_username(new_username):
    await client.start(phone_number)
    await client(UpdateUsernameRequest(username=new_username))

new_username = 'your_new_username'
client.loop.run_until_complete(change_username(new_username))
