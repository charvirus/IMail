import asyncio
import discord

app = discord.Client()

token = "ODI0MzA4NTY1Mzg0MjMzMDAw.YFtfLA.b9mIkRX1pSrXxY8PhD8lr9ZWsOI"

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("안녕하세요 :)")
    await app.change_presence(status=discord.Status.online, activity=game)



@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!안녕":
        await message.channel.send("안녕하세요.")

app.run(token)