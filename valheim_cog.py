import subprocess
import discord as dc
from discord import app_commands

class Valheim(dc.ext.commands.Cog):
    '''Cog that handles everything regarding the Valheim Server using Linuxgsm'''
    def __init__(self, bot):
        self.bot = bot

    valheim = app_commands.Group(
        name="valheim",
        description="Gruppe an Commands um den Valheim Server zu steuern"
    )

    @valheim.command(name="info", description="Gibt grundlegende Informationen über den Server")
    async def info(self, interaction: dc.Interaction):
        '''runs lsgm info command and returns basic info'''
        server_name = subprocess.run(
            r"cd /home/vhserver/Servers/valheim_lgsm && ./vhserver info | grep Server\ name:",
            shell=True,
            capture_output=True,
            check=False
            ).stdout
        password = subprocess.run(
            r"cd /home/vhserver/Servers/valheim_lgsm && ./vhserver info | grep Server\ password:",
            shell=True,
            capture_output=True,
            check=False
            ).stdout
        status = subprocess.run(
            r"cd /home/vhserver/Servers/valheim_lgsm && ./vhserver info | grep Status:",
            shell=True,
            capture_output=True,
            check=False
            ).stdout
        await interaction.response.send_message(server_name + "\n" + password + "\n" + status)

    @valheim.command(name="start", description="Startet den Server falls er noch nicht läuft")
    async def start(self, interaction: dc.Interaction):
        '''starts the server if not already up'''
        response = subprocess.run(
            "cd /home/vhserver/Servers/valheim_lgsm && ./vhserver start",
            shell=True,
            capture_output=True,
            check=False
        )
        await interaction.response.send_message(response.stdout)

    @valheim.command(name="stop", description="Stoppt den Server")
    async def stop(self, interaction: dc.Interaction):
        '''stops the server if the user is a player'''
        players = [468142012466593792, 480411398703284266, 690908179407831070]
        if interaction.user.id in players:
            response = subprocess.run(
                "cd /home/vhserver/Servers/valheim_lgsm && ./vhserver stop",
                shell=True,
                capture_output=True,
                check=False
            )
            await interaction.response.send_message(response.stdout)
        else:
            await interaction.response.send_message("Du bist kein Spieler also darfst du das nicht")


async def setup(bot):
    '''setup'''
    #cog = Valheim(bot)
    #await bot.add_cog(cog)
    #bot.tree.add_command(cog.valheim)
