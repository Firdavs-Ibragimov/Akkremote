import csv
import getpass
from telethon.sync import TelegramClient
from telethon.errors import PasswordHashInvalidError
from telethon.tl.functions.account import GetPasswordRequest, UpdatePasswordSettingsRequest
from telethon.tl.types import InputCheckPasswordSRP

# Replace these with your values
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
hint = 'New hint'


async def main():
    global phlist
    with open(f'{phonecsv}.csv', 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
    print('NOMERLAR: ' + str(len(phlist)))

async def change_password(client, phone_number, current_password, new_password):
    try:
        await client.start(phone_number)
        me = await client.get_me()
        print(f'Logged in as {me.username}')

        # Get the current password settings
        password = await client(GetPasswordRequest())

        # Check the current password
        password_hash = password.current_password_hash
        password_input = InputCheckPasswordSRP(
            id=password.srp_id,
            srp_id=password.srp_id,
            srp_B=password.srp_B,
            srp_M1=password.srp_M1
        )

        # Update the password settings
        await client(UpdatePasswordSettingsRequest(
            password=password_input,
            new_password_hash=password_hash,
            hint=hint,
            email_unset=False
        ))
        print('Password changed successfully')
    except PasswordHashInvalidError:
        print('Invalid current password')
    except Exception as e:
        print(f'Failed to change password for {phone_number}: {e}')

async def main():
    current_password = getpass.getpass('Enter current password: ')
    new_password = getpass.getpass('Enter new password: ')

    with open('phone.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            phone_number = row['phone_number']
            client = TelegramClient(f'session_{phone_number}', api_id, api_hash)
            await change_password(client, phone_number, current_password, new_password)

import asyncio
asyncio.run(main())