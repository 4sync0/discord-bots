import discord
from discord.ext import commands
import os
import requests as r
import asyncio

def start(printout: bool) -> str:
    falix = r.get("https://www.saashub.com/falixnodes-status")
    if printout and falix.status_code >= 199 and falix.status_code <= 300:
        host = "SERVER"
        response = os.system(f"ping -c 1 {host}")
        host_cut = host.split(":")
        
        if response == 0:
            return (f"Host {host_cut[0]}:xxxxx is reachable")
        else:
            return (f"Host {host_cut[0]}:xxxxx is not reachable")

    else: pass

#intent = discord.Intents.default()
client = commands.Bot(intents=discord.Intents.all() ,command_prefix="!")



@client.event
async def on_ready():
    print(f"sesion initiation {client.user}")
    while True:
        channel = client.get_channel(1071107784680144906)
        await asyncio.sleep(1800)
        await channel.send(f"falix: {start(True)}")

client.run("TOKEN")
