import discord
from discord.ext import commands
import os
import requests as r
import asyncio

def start(printout: bool) -> str:
    falix = r.get("https://www.saashub.com/falixnodes-status")
    content = falix.content
    if printout and falix.status_code >= 199 and falix.status_code <= 300:
        #parse
        content = '<div class="down-status down-status--up">👌 Up</div>'
        class_start = content.find('<div class="down-status down-status--up">')
        class_end = content.find('</div>', class_start) + 6
        target_class = content[class_start:class_end]
        if target_class == "<div class=\"down-status down-status--up\">👌 Up</div>": return "up"
        else: return "down"
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
