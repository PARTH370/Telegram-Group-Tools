import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_message_to_group( message):
    # Replace 'YOUR_BOT_TOKEN' with your bot's token and 'YOUR_CHANNEL_ID' with your channel ID
    bot_token = os.getenv('BOT_TOKEN')
    channel_id = os.getenv('CHANNEL_ID')
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': channel_id,
        'text': message
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f'Failed to send message. Status code: {response.status_code}, Response: {response.text}')

 # Use '@' for channel usernames or use a numerical ID
message = 'Hello, this is a test message!'

send_message_to_group( message)
