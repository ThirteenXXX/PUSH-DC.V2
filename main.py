import requests
import time
import os
import random
from colorama import Fore

ascii_art = r'''
  ________    _      __                 _  __
 /_  __/ /_  (_)____/ /____  ___  ____ | |/ /
  / / / __ \/ / ___/ __/ _ \/ _ \/ __ \|   / 
 / / / / / / / /  / /_/  __/  __/ / / /   |  
/_/ /_/ /_/_/_/   \__/\___/\___/_/ /_/_/|_|  

  >>> BOT AUTO CHAT-AUTO REPLY DISCORD V.2
============================================
'''

def gradient_text(text, colors):
    colored_text = ""
    color_index = 0
    for char in text:
        if char == ' ':
            colored_text += " "
        else:
            colored_text += f"\033[{colors[color_index]}m{char}\033[0m"
        color_index = (color_index + 1) % len(colors)
    return colored_text

colors = [
    '32',
]

colored_ascii = gradient_text(ascii_art, colors)
print(colored_ascii)

time.sleep(1)

channel_id = input("Masukkan ID channel: ")
waktu1 = int(input("Set Waktu Kirim Pesan: "))

time.sleep(1)
print("Loading...")
time.sleep(1)
print("Loading...")
time.sleep(1)
print("Loading...")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

# Read messages from file
with open("pesan.txt", "r") as f:
    words = f.readlines()

# Read token from file
with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
    channel_id = channel_id.strip()

    # Retrieve all messages from the channel
    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', 
                            headers={'Authorization': authorization})

    if response.status_code == 200:
        messages = response.json()
        if len(messages) > 0:
            # Get list of user IDs from the messages
            user_ids = list(set(message['author']['id'] for message in messages))

            # Choose a random user from the list
            if user_ids:
                random_user_id = random.choice(user_ids)  # Select random user

                # Choose a random message from the list
                current_message = random.choice(words).strip()

                # Prepare the payload to reply to the message
                payload = {
                    'content': current_message,
                    'message_reference': {
                        'message_id': random.choice(messages)['id']  # Use a random message ID for reference
                    }
                }

                headers = {
                    'Authorization': authorization
                }

                # Send the message
                r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", 
                                 json=payload, 
                                 headers=headers)

                print(Fore.WHITE + f"Sent message reply to user ID {random_user_id}: ")
                print(Fore.YELLOW + payload['content'])

                time.sleep(waktu1)
            else:
                print("Tidak ada pengguna untuk dibalas.")
                break
        else:
            print("Tidak ada pesan untuk dibalas.")
            break
    else:
        print(f'Gagal mendapatkan pesan di channel: {response.status_code}')
        break

    time.sleep(waktu1)
