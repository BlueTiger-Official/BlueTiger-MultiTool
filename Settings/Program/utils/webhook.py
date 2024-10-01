import asyncio
import aiohttp
from pystyle import Colors, Colorate

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

async def main():
    clear()
    print(Colorate.Horizontal(Colors.blue_to_purple, "============================================="))
    print(Colorate.Horizontal(Colors.blue_to_purple, "           Discord Webhook Sender            "))
    print(Colorate.Horizontal(Colors.blue_to_purple, "============================================="))

    webhook_url = input(Colorate.Horizontal(Colors.blue_to_cyan, "\nEnter webhook URL: "))
    message = "@here @everyone discord.gg/toolsfr"
    
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.post(webhook_url, data={"content": message}) as response:
                if response.status == 204:
                    print(Colorate.Horizontal(Colors.green_to_yellow, "\nMessage sent successfully."))
                else:
                    print(Colorate.Horizontal(Colors.red_to_yellow, f"\nFailed to send message. Status code: {response.status}"))

if __name__ == "__main__":
    asyncio.run(main())
