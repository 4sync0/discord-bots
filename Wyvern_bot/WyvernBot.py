#bot messages are in spanish as this bot is ment to be for a private server, posted into github so that if anyone wants to, they can modify it to their likings
#as long as credit is given

import discord
from discord.ext import commands

import os
import time
import asyncio
import pika

#intent = discord.Intents.default()
client = commands.Bot(intents=discord.Intents.all() ,command_prefix="!")



@client.event
async def on_ready():
    print(f"sesion initiation {client.user}")


#commands

@client.command()
async def falixhq(ctx): #ping falixnodes server
    pinghq = os.system("ping game6.falixserver.net")
    channel = client.get_channel("1071107784680144906")
    await channel.send(f"respuesta ping a falixnodes: {pinghq}")

@client.command()
async def contador(message, time, channelID):  #timer, when ended, sends x message to channel
    channel = client.get_channel(channelID)
    user = message.author
    await asyncio.sleep(time)
    await channel.send(f"{user.mention} wants to say: {message}")

@client.command()
async def peticion(message): #petition to open the server
    user = client.get_user("805411326801084446")
    await user.send(f"@Victor, {message.author} quiere que abras el server")

@client.command()
async def msganonim(ctx): #sends an anonimous message & deletes the user's message
    dm = await ctx.send(f"tienes un mensaje de un miembro de Wyvern, quiere permanecer anonimo:\n {ctx}")
    messages = await ctx.channel.history(limit=2).flatten()
    await messages[0].delete()

@client.command()
async def estado(ctx): #chequea el estado del servidor de falixnodes
    channel = client.get_channel("1071107784680144906")
    callback_checkpoint = False
    try:
        import consumer
    except pika.exceptions.IDK: await channel.send("servidor apagado")

    if callback_checkpoint: await channel.send("servidor encendido")
    else: await channel.send("servidor apagado")
client.run("token")