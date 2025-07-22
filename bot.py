import discord as dc
from discord.ext import commands

intents = dc.Intents.default()
bot = commands.Bot("#", intents = intents)

with open("TOKEN.txt", "r", encoding="utf-8") as file:
    TOKEN = file.readlines()[0]

with open("ADMINID.txt", "r", encoding="utf-8") as file:
    ADMIN_ID = file.readlines()[0]

@bot.event
async def setup_hook():
    '''setup'''
    await bot.load_extension("valheim_cog")
    await bot.tree.sync()

bot.run(TOKEN)
