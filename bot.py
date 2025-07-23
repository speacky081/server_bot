import discord as dc
from discord.ext import commands
import valheim_cog

intents = dc.Intents.default()
bot = commands.Bot("§", intents = intents)

with open("/home/vhserver/server_bot.py/TOKEN.txt", "r", encoding="utf-8") as file:
    TOKEN = file.readlines()[0]

with open("/home/vhserver/server_bot.py/ADMINID.txt", "r", encoding="utf-8") as file:
    ADMIN_ID = file.readlines()[0]

@bot.event
async def on_ready():
    '''setup'''
    await bot.add_cog(valheim_cog.Valheim(bot))
    bot.tree.add_command(cmd_sync.app_command, override=True)
    # await bot.tree.sync()

@bot.hybrid_command(name='sync', description='Sync all commands.')
async def cmd_sync(ctx):
    '''syncs slash commands'''
    if ctx.user.id == ADMIN_ID:
        bot.tree.add_command(cmd_sync.app_command, override=True)
        await bot.tree.sync()
        await ctx.send('Synced successfully.', ephemeral=True)
    else:
        await ctx.send('You are not the owner.', ephemeral=True)

bot.run(TOKEN)
