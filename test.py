import requests
import time
import os
from colorama import Fore

print("===========================================")
print('BOT AUTO CHAT DISCORD BY Thirteen𝕏')
print("===========================================\n")

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

# Initialize message index
current_message_index = 0

while True:
    channel_id = channel_id.strip()

    # Get current message and increment index
    current_message = words[current_message_index].strip()
    current_message_index = (current_message_index + 1) % len(words)  # Loop back to start when reaching end

    payload = {
        'content': current_message
    }

    headers = {
        'Authorization': authorization
    }

    # Send message
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", 
                     data=payload, 
                     headers=headers)
    
    print(Fore.WHITE + "Sent message: ")
    print(Fore.YELLOW + payload['content'])

    # Check channel status
    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', 
                          headers=headers)

    if response.status_code == 200:
        messages = response.json()
        if len(messages) == 0:
            is_running = False
            break
        else:
            time.sleep(waktu1)
    else:
        print(f'Gagal mendapatkan pesan di channel: {response.status_code}')
    
    time.sleep(waktu1)
    
