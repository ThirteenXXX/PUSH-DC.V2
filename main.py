import requests
import time
import os
import random
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

    # Ambil semua pesan dari channel
    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', 
                            headers={'Authorization': authorization})

    if response.status_code == 200:
        messages = response.json()
        if len(messages) > 0:
            # Ambil daftar pengguna yang mengirim pesan
            user_ids = list(set(message['author']['id'] for message in messages))

            # Pilih pengguna secara acak dari daftar pengguna
            if user_ids:
                random_user_id = random.choice(user_ids)  # Memilih pengguna secara acak

                # Ambil pesan balasan secara urut dari file
                current_message = words[current_message_index].strip()
                current_message_index = (current_message_index + 1) % len(words)  # Loop kembali ke awal jika sudah mencapai akhir

                # Siapkan payload untuk membalas pesan
                payload = {
                    'content': current_message,
                    'message_reference': {
                        'message_id': random.choice(messages)['id']  # Menggunakan ID pesan acak untuk referensi
                    }
                }

                headers = {
                    'Authorization': authorization
                }

                # Kirim pesan
                r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", 
                                 json=payload, 
                                 headers=headers)

                print(Fore.WHITE + f"Sent message to user ID {random_user_id}: ")
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
    
