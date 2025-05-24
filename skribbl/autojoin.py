import asyncio
import websockets
import json
import pyperclip
import os
import webbrowser
import argparse
import time
from colorama import Fore
from .windows_shortcut import create_shortcut

# for single player
async def connect():
    url = "wss://server3.skribbl.io/5004/?EIO=4&transport=websocket"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Origin": "https://skribbl.io",
        "Accept-Language": "en-US,en;q=0.5",
    }

    ws = None
    try:
        ws = await websockets.connect(url, extra_headers=headers)
        print("Initialized WebSocket connection...")

        await ws.send("40")
        print("Sent to server...")

        first_response = await ws.recv()
        print(f"Server Responded...")

        login_payload = '42["login",{"join":"","create":0,"name":"","lang":"0","avatar":[15,54,42,-1]}]'
        await ws.send(login_payload)
        print(f"Sent Login...")

        message = await ws.recv()
        message = await ws.recv()  # Here we get ID

        try:
            data = json.loads(message[2:])
            session_id = data[1]['data']['id']
            users = data[1]['data']['users']
            link = f"https://skribbl.io/?{session_id}"
            print(f"Copied to clipboard: {link}")
            pyperclip.copy(link)
            webbrowser.open(link)
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"Error parsing response: {e}")

    except websockets.exceptions.WebSocketException as e:
        print(f"WebSocket error: {e}")

    finally:
        if ws:
            await ws.close()
            print("WebSocket connection closed.")

#when you want to find space for friends too
async def connect_space():
    url = "wss://server3.skribbl.io/5004/?EIO=4&transport=websocket"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Origin": "https://skribbl.io",
        "Accept-Language": "en-US,en;q=0.5",
    }

    ws = None
    try:
        ws = await websockets.connect(url, extra_headers=headers)
        print("Initialized WebSocket connection...")

        await ws.send("40")
        print(Fore.WHITE+"Sent to server...")

        first_response = await ws.recv()
        print(Fore.WHITE+f"Server Responded...")

        login_payload = '42["login",{"join":"","create":0,"name":"","lang":"0","avatar":[15,54,42,-1]}]'
        await ws.send(login_payload)
        print(Fore.WHITE+f"Sent Login...")

        message = await ws.recv()
        message = await ws.recv()  # Here we get ID

        try:
            data = json.loads(message[2:])
            session_id = data[1]['data']['id']
            users = data[1]['data']['users']
            link = f"https://skribbl.io/?{session_id}"
             
    #         print(f"Copied to clipboard: {link}")
    #         pyperclip.copy(link)
    #         webbrowser.open(link)
    
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(Fore.RED+f"Error parsing response: {e}")

    except websockets.exceptions.WebSocketException as e:
        print(Fore.RED+f"WebSocket error: {e}")

    finally:
        if ws:
            await ws.close()
            print(Fore.WHITE+"WebSocket connection closed.")
    return users,link 

def run():
    parser = argparse.ArgumentParser(description="Shortcut Maker Argument Handler")
    parser.add_argument("--shortcut", action="store_true", help="Makes desktop shortcut for skribbl-public for windows")
    parser.add_argument("--space_required",'-r', help="if you are 3 friends set 3, enter 2 to 7")
    
    args = parser.parse_args()
    
    if args.shortcut:
        try:
            if os.name == 'nt':
                create_shortcut("Skribble - Public Room", "skribbl-public.exe")
                print("✅ Shortcut Created Successfully")
            else:
                print("⚠️  Not yet implemented for this operating system")
            
        except ModuleNotFoundError as e:
            print(f"❌ Failed to create shortcut: {e}")
            print("-- Reuires pywin32 module")
            print("-- Install by running `pip install pywin32` in your terminal")
            
        except Exception as e:
            print(f"❌ Failed to create shortcut: {e}")
    if int(args.space_required)>=2 and int(args.space_required)<=7:
        while True:
            users, link = asyncio.run(connect_space())
            print(Fore.GREEN+f"Link: {link}")
            print(Fore.WHITE+f"Users found: {len(users)}")
            for num,i in enumerate(users):
                print(i['name'],end=f'-({num+1}) ')
            print('\n')
            
            if 9-len(users) >= int(args.space_required):
                print(Fore.GREEN+f"✅ Users: {Fore.YELLOW}{len(users)} {Fore.WHITE}:--> copied to clipboard: {Fore.CYAN}{link}")
                pyperclip.copy(link)
                webbrowser.open(link)
                break
            time.sleep(1)
    else:
        asyncio.run(connect())

if __name__ == "__main__":
    run()
