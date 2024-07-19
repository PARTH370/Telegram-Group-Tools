from telethon import TelegramClient, sync
from telethon.errors import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import time
from telethon.errors.rpcerrorlist import UserNotMutualContactError
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your API ID and Hash obtained from my.telegram.org
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
phone = os.getenv('TELEGRAM_PHONE')
group_username = os.getenv('TELEGRAM_GROUP_USERNAME')

# Create the client and connect
client = TelegramClient(phone, api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

## Get the group entity
group = client.get_entity(group_username)

# Read the list of users from a file
with open('users.txt', 'r') as file:
    users = file.readlines()

for user in users:
    user = user.strip()
    print(f"Adding {user} to the group")
    try:
        user_entity = client.get_entity(user)
        client(InviteToChannelRequest(group, [user_entity]))
        print(f"Added {user} to the group")
        time.sleep(15)  # Increased sleep to avoid hitting Telegram limits
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again later.")
        break
    except UserPrivacyRestrictedError:
        print(f"Privacy settings of {user} do not allow you to add them to the group")
    except UserNotMutualContactError:
        print(f"{user} is not a mutual contact")
    except Exception as e:
        print(f"Error: {e}")

client.disconnect()