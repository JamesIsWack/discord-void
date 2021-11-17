import discord
from discord.ext import commands
import youtube_dl
import os

# clear nums:
x = 0

# task dictionary:
tasks = {}

# input test


# prefix
client = commands.Bot(command_prefix="V")


@client.event
async def on_ready():
    print("V Bot is working")
    
@client.command()
async def oid(ctx):
    await ctx.send('@Old Nail#7118')

# command list:
@client.command()
async def cmd(ctx):
    await ctx.send('Will be Updated soon')

# host server command:
@client.command()
async def h(ctx):
    await ctx.send('https://discord.gg/Y2MgAzCPuJ')

# poll command
@client.command()
async def poll(ctx, *, message):
    emb=discord.Embed(title="POLL", description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction(":grinning:")
    await msg.add_reaction(":neutral_face:")
    await msg.add_reaction(":frowning2:")



# invite bot command:
@client.command()
async def inv(ctx):
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=766757735639285851&permissions=8&scope=bot')

# status command:
@client.command()
async def stat(ctx):
    await ctx.send('Void is up and running!')


# clear command:
num = x
@client.command()
@commands.has_role('ACE')
# ace means admin command executive
async def c(ctx, ammount=2):
    x = ammount
    await ctx.channel.purge(limit=ammount + 1)
    if x < 2:
        if x > 300:
            await ctx.send('Number is to small, it has to be bigger than 2 !')
        else: ctx.send('Please choose a number smaller than 300 !')
    else:
        await ctx.send(str(x) + f' messages have been removed by @{ctx.author} !')
       
    
       # Music test
@client.command()
async def play(ctx, url : str,):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Vauidio')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
####


# task list command:
@client.command()
async def tskl(ctx):
    await ctx.send(tasks)

# input test
@client.command()
async def tes(ctx):
    await ctx.send("Test")
    await ctx.send(test)


client.run('XI')