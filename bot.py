import discord as dc
from discord.ext import commands
import valheim_cog

intents = dc.Intents.default()
intents.message_content = True
bot = commands.Bot("§", intents = intents)

with open("/home/vhserver/server_bot/TOKEN.txt", "r", encoding="utf-8") as file:
    TOKEN = file.readlines()[0]

with open("/home/vhserver/server_bot/ADMINID.txt", "r", encoding="utf-8") as file:
    ADMIN_ID = int(file.readlines()[0])

@bot.event
async def setup_hook():
    '''Set up slash commands here. In on_ready the calls might be fired multiple times which can cause trouble'''
    cogv = valheim_cog.Valheim(bot)
    await bot.add_cog(cogv)
    if not bot.tree.get_command("valheim"):
        bot.tree.add_command(cogv.valheim)

@bot.hybrid_command(name='sync', description='Sync all commands.')
async def cmd_sync(ctx: commands.Context):
    '''syncs slash commands'''
    if ctx.author.id == ADMIN_ID:
        bot.tree.add_command(cmd_sync.app_command, override=True)
        await bot.tree.sync()
        await ctx.send('Synced successfully.', ephemeral=True)
    else:
        await ctx.send('You are not the owner.', ephemeral=True)

bot.run(TOKEN)
