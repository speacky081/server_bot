import discord as dc
from discord.ext import commands
import valheim_cog

intents = dc.Intents.default()
bot = commands.Bot("#", intents = intents)

with open("TOKEN.txt", "r", encoding="utf-8") as file:
    TOKEN = file.readlines()[0]

with open("ADMINID.txt", "r", encoding="utf-8") as file:
    ADMIN_ID = file.readlines()[0]

@bot.event
async def on_ready():
    '''load cog on ready'''
    await bot.add_cog(valheim_cog.Valheim(bot))

bot.run(TOKEN)
#test
