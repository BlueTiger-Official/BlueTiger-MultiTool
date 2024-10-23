import os
import discord
from discord.ext import commands
from colorama import Fore
import time

def Slow(texte):
    for line in texte.splitlines():
        print(line)
        time.sleep(0.05)

ascii_banner = f"""{Fore.RED}

 ▄████▄   ██▓    ▓█████ ▄▄▄       ██▀███     ▓█████▄  ███▄ ▄███▓
▒██▀ ▀█  ▓██▒    ▓█   ▀▒████▄    ▓██ ▒ ██▒   ▒██▀ ██▌▓██▒▀█▀ ██▒
▒▓█    ▄ ▒██░    ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒   ░██   █▌▓██    ▓██░
▒▓▓▄ ▄██▒▒██░    ▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄     ░▓█▄   ▌▒██    ▒██ 
▒ ▓███▀ ░░██████▒░▒████▒▓█   ▓██▒░██▓ ▒██▒   ░▒████▓ ▒██▒   ░██▒
░ ░▒ ▒  ░░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░    ▒▒▓  ▒ ░ ▒░   ░  ░
  ░  ▒   ░ ░ ▒  ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░    ░ ▒  ▒ ░  ░      ░
░          ░ ░      ░    ░   ▒     ░░   ░     ░ ░  ░ ░      ░   
░ ░          ░  ░   ░  ░     ░  ░   ░           ░           ░   
░                                             ░                     
                                                              

"""

Slow(ascii_banner)

Slow(f"{Fore.YELLOW}Enter your token")
token = input(f"{Fore.YELLOW}Token: ")
Slow(f"{Fore.YELLOW}Write \"!clear\" in one of your DMs to delete your messages")

global bot
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")

@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    Slow(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Removed {passed} messages with {failed} fails")
    input(f"""\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to exit""")

input(Fore.BLUE + "[x] Appuyer sur entrée pour retourner au menu principal.")
os.system('python ../../main.py')

bot.run(token, bot=False)
