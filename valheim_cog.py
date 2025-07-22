import asyncio
import re
import subprocess
import discord as dc
from discord import app_commands

ANSI = re.compile(r'\x1b\[[0-9;]*[a-zA-Z]')

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
        await interaction.response.defer(thinking=True)
        server_name = subprocess.run(
            r"cd /home/vhserver/Servers/valheim_lgsm && ./vhserver details | grep Server\ name:",
            shell=True,
            capture_output=True,
            check=False,
            text=True
            ).stdout
        password = subprocess.run(
            r"cd /home/vhserver/Servers/valheim_lgsm && ./vhserver details | grep Server\ password:",
            shell=True,
            capture_output=True,
            check=False,
            text=True
            ).stdout
        status = subprocess.run(
            r"cd /home/vhserver/Servers/valheim_lgsm && ./vhserver details | grep Status:",
            shell=True,
            capture_output=True,
            check=False,
            text=True
            ).stdout
        await interaction.followup.send(ANSI.sub('', server_name).strip() + "\n" + ANSI.sub('', password).strip() + "\n" + ANSI.sub('', status).strip())

    @valheim.command(name="start", description="Startet den Server falls er noch nicht läuft")
    async def start(self, interaction: dc.Interaction):
        '''starts the server if not already up'''
        await interaction.response.defer(thinking=True)
        response = subprocess.run(
            "cd /home/vhserver/Servers/valheim_lgsm && ./vhserver start",
            shell=True,
            capture_output=True,
            check=False,
            text=True
        )
        await interaction.followup.send(ANSI.sub('', response.stdout).strip())

    @valheim.command(name="stop", description="Stoppt den Server")
    async def stop(self, interaction: dc.Interaction):
        '''stops the server if the user is a player'''
        await interaction.response.defer(thinking=True)
        players = [468142012466593792, 480411398703284266, 690908179407831070]
        if interaction.user.id in players:
            response = subprocess.run(
                "cd /home/vhserver/Servers/valheim_lgsm && ./vhserver stop",
                shell=True,
                capture_output=True,
                check=False,
                text=True
            )
            await interaction.followup.send(ANSI.sub('', response.stdout).strip())
        else:
            await interaction.followup.send("Du bist kein Spieler also darfst du das nicht")
