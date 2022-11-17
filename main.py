
import random
import httpx
import os
import time
keys = [
                "LeU482c9-9I521pwS-4D1fuy09",
                "Cy798YL1-5I38Tuw1-sg927e1L",
                "2gC61hL3-3Sz89EL5-97xdfG65",
                "7wIq5l04-2ME4dg76-2vD98y7Z",
                "TM98h53f-82XAJ0N4-5HE6z9c3",
                "4zM8u57N-75V98JhO-6D5sZ03h",
                "4O21olg7-Fc5691Hp-6n9N5fT7",
                "63y0U4Ig-8Yl4HR27-94n5Jqc2",
                "uV1v95y2-GbV54Y98-l3O4n80J",
                "rS0R716n-684r9dBG-639N5qJG",
                "R7cF58O3-a8h460Xy-Rx15BX39",
                "5FtI7g13-b89iU10G-pkog9853",
                "u8T9O57e-L3w671vm-6h9mM05o",
                "S5NXl426-9Y62WRK0-0DS8Vx57",
                "Y9s608lS-I0C4Xw76-uQ72LY14",
                "1Afg08W9-goH6190J-0G3pE5f6",
                "9Cg84yY1-Hb7Tf304-83B6pmi1",
                "12Z0vc4x-906i7IPs-60v9wg1V",
                "17hs6oa9-46R98yqI-89Svy3W6",
                "76rT0D1K-pv46U0F1-2l9A8h5t",
                "n97rm1G0-714vbf3I-O05L16NJ",
                "iD8j457u-e314Fm8c-06x7RwN4",
            ]
gkeys = []
os.system('cls' if os.name == "nt" else 'clear')
# The most important line of code, nothing will work without it!
print("\n█░█░█ ▄▀█ █▀█ █▀█ ▄█▄\n▀▄▀▄▀ █▀█ █▀▄ █▀▀ ░▀░\n")
print('CREEPER (https://lolz.guru/creeper/) AND RIVZOR (https://lolz.guru/members/3043646/)')
# Window title
print()

# Getting a value for a loop
value_int = int(input("Welcome to the WARP+ Key Generator\nEnter the desired number of keys: "))
a = 0
# The most common while loop
while a < value_int:
    a += 1
    print("<======================================WARP+ Generate======================================>")
    print("Key is being created:", a)

    try:
        # Header with variables
        headers = {
            "CF-Client-Version": "a-6.11-2223",
            "Host": "api.cloudflareclient.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.12.1",
        }

        with httpx.Client(
                base_url="https://api.cloudflareclient.com/v0a2223", headers=headers, timeout=30.0
        ) as client:

            r = client.post("/reg")
            id = r.json()["id"]
            license = r.json()["account"]["license"]
            token = r.json()["token"]

            r = client.post("/reg")
            id2 = r.json()["id"]
            token2 = r.json()["token"]

            headers_get = {"Authorization": f"Bearer {token}"}
            headers_get2 = {"Authorization": f"Bearer {token2}"}
            headers_post = {
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Bearer {token}",
            }

            json = {"referrer": f"{id2}"}
            client.patch(f"/reg/{id}", headers=headers_post, json=json)

            client.delete(f"/reg/{id2}", headers=headers_get2)

            
            key = random.choice(keys)

            json = {"license": f"{key}"}
            client.put(f"/reg/{id}/account", headers=headers_post, json=json)

            json = {"license": f"{license}"}
            client.put(f"/reg/{id}/account", headers=headers_post, json=json)

            r = client.get(f"/reg/{id}/account", headers=headers_get)
            account_type = r.json()["account_type"]
            referral_count = r.json()["referral_count"]
            license = r.json()["license"]

            client.delete(f"/reg/{id}", headers=headers_get)

            print(f"Тип аккаунта: {account_type}")
            print(f"Data allocated: {referral_count} GB")
            # {license}
            print(f"License: {license}")

            # Writing a key to a file
            #with open('WARPKeys.txt', 'a') as f:
            #    f.write(license + '\n')
            #    f.close()
            #print("Key ready and saved в .txt file.")
            if a % 2 == 0:
                time.sleep(60)
            gkeys.append(license)
    # Error
    except Exception as er:
        print("Error.")
        print(er)
os.system('cls' if os.name == 'nt' else 'clear')
for x in gkeys:
    print(x)
input('\nPress Enter to exit\n')
