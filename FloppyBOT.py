#Import Stuff
import discord
import asyncio 

from discord.ext import commands

bot = commands.Bot(command_prefix="fp!")

#Remove default help command
bot.remove_command("help")

#Show that the bot is online
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="fp!help"))

@bot.command()
async def help(ctx):
    await ctx.send("The bot curently has no commands since floppy can't decide what he wants the bot to do")

bot.run('token')
