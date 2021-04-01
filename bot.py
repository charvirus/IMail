import asyncio
import discord
from discord.ext import commands
import os


app = discord.Client()

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    await app.change_presence(status=discord.Status.online)



@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!안녕":
        await message.channel.send("안녕하세요.")

app.run(os.environ['token'])