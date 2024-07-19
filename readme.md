# Telegram Member Adder Script & Get All Group List Script

## Telegram Member Adder Script

### How to use

#### Step 1 : Get the API ID and API HASH from [Telegram](https://my.telegram.org/auth)
Note: You need to login to your Telegram account to access this page and get the API ID and API HASH.
[MORE INFO](https://www.esegece.com/help/sgcWebSockets_NET/Components/APIs/Other/Telegram/API_Telegram.htm)

#### Step 2 : Install the required packages
```bash
pip install -r requirements.txt
```

#### Step 3 : Create a file named `users.txt` and add the usernames of the users you want to add to the group
```bash
username1
username2
username3
```


#### Step 4 : Create a file named `.env` and add the following code
```bash
API_ID=your_api_id
API_HASH=your_api_hash
PHONE=your_phone_number
TELEGRAM_GROUP_USERNAME=your_telegram_group_username
```
Note: if you don't have a Telegram group, you can create one and get the username. or you can run the script group_list.py to get all the groups you are in.

#### Step 5 : Run the script
```bash
python main.py
```


