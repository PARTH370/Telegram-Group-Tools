import os
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, Channel, Chat

# Load environment variables from .env file
load_dotenv()

# Your API ID and Hash obtained from my.telegram.org
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
phone = os.getenv('TELEGRAM_PHONE')

async def main():
    # Create the client and connect
    client = TelegramClient(phone, api_id, api_hash)
    await client.connect()

    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        await client.sign_in(phone, input('Enter the code: '))

    # Fetch the list of dialogs
    result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=200,
        hash=0
    ))

    # List all group chats
    for chat in result.chats:
        if isinstance(chat, Channel) and chat.megagroup:
            print(f'chat.creator: {chat.creator}')
            print(f"Group name: {chat.title}, Group ID: {chat.id}")
            print(f"Group username: {chat.username}")

    await client.disconnect()

# Run the main function in an event loop
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
