import discord
from discord.ext import commands
import os
import requests as r
from time import sleep
import asyncio

def start(printout: bool) -> str:
    falix = r.get("https://dev-panel.falixnodes.net/server/e397b58d")
    if printout:
        return falix.status_code
    else: pass

#intent = discord.Intents.default()
client = commands.Bot(intents=discord.Intents.all() ,command_prefix="!")



@client.event
async def on_ready():
    print(f"sesion initiation {client.user}")
    while True:
        channel = client.get_channel(1071107784680144906)
        await asyncio.sleep(600)
        await channel.send(f"falix: {start(True)}")
    
client.run("MTA3MTEwOTM2MzY4ODgxNjY5MA.G8Xsna.L-vYqlYXGobBVlWUzXsoEiyb2A5CRsQaJnqXbQ")