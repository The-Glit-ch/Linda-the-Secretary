import discord
import asyncio
import os
import random
import youtube_dl
import shutil
from os import system
from discord.ext import commands
from discord.utils import get
from discord import Spotify

bot = commands.Bot(command_prefix='Linda ')


#VARS
global Lockdown
global voice
voice = None
Lockdown = False

Whitelist = [557339295325880320,762844152429412402]
Sus = [729169434278625330,773729542577717299,761762508268503081,763097081015042129]
NoNo = ["pls trap","pls porn","pls boobs","pls porn gif"]
MEMENames = ["1","2","3","4","5","6","7","8"]
Queues = []
#-----------ActList = ["competing","custom","listening","mro","playing","streaming","unknown","watching"]

#VARS

@bot.event
async def on_ready():
    print ("------------------------------------")
    print (f"Bot Name: {str(bot.user.name)}")
    print (f"Bot ID: {bot.user.id}")
    print ("------------------------------------")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening ,name="something"))
    
#
#Event Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#Event Spacer
#Event Spacer
#Event Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
@bot.command(aliases=['goodbye','cya_later'])
async def byebye(ctx):
    if ctx.author.id in Whitelist:
        print("Shutting Down")
        await ctx.send("Bye bye")
        await bot.logout()
    else:
        await ctx.send("Sorry your not my developer so i wont shut off")

#TODO: Fix spotify_link
@bot.command()
async def spotify_link(ctx):
    if ctx.author.id in Whitelist:
        await ctx.send("Now linking with your spotify...")
        UserAct = ctx.author.activities
        if isinstance(UserAct, Spotify):
            await ctx.send(f"{UserAct.title},{UserAct.artist}")
        else:
            print(UserAct)
            await ctx.send(f"It looks like spotify isint playing right now, Your current activity is {ctx.author.ActivityType}")
    else:
        await ctx.send("Sorry but you dont have access to use this command")

@bot.command()
async def update_status(ctx, Act, Text):
    await Tired(ctx=ctx)
    TLower = str(Act).lower()
    if ctx.author.id in Whitelist:
        if TLower == "competing":
            await Tired(ctx=ctx)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing ,name=Text))
            await ctx.send(f"Now changing Activity to: '**{Act}**' and Text to: '**{Text}**'")
            print(f"Now changing Activity to: '{Act}' and Text to: '{Text}'")
        elif TLower == "custom":
            await Tired(ctx=ctx)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom ,name=Text))
            await ctx.send(f"Now changing Activity to: '**{Act}**' and Text to: '**{Text}**'")
            print(f"Now changing Activity to: '{Act}' and Text to: '{Text}'")
        elif TLower == "listening":
            await Tired(ctx=ctx)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening ,name=Text))
            await ctx.send(f"Now changing Activity to: '**{Act}**' and Text to: '**{Text}**'")
            print(f"Now changing Activity to: '{Act}' and Text to: '{Text}'")
        elif TLower == "mro":
            await Tired(ctx=ctx)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.mro ,name=Text))
            await ctx.send(f"Now changing Activity to: '**{Act}**' and Text to: '**{Text}**'")
            print(f"Now changing Activity to: '{Act}' and Text to: '{Text}'")
        elif TLower == "playing":
            await Tired(ctx=ctx)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing ,name=Text))
            await ctx.send(f"Now changing Activity to: '**{Act}**' and Text to: '**{Text}**'")
            print(f"Now changing Activity to: '{Act}' and Text to: '{Text}'")
        elif TLower == "streaming":
            await Tired(ctx=ctx)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming ,name=Text))
            await ctx.send(f"Now changing Activity to: '**{Act}**' and Text to: '**{Text}**'")
            print(f"Now changing Activity to: '{Act}' and Text to: '{Text}'")
        elif TLower == "unknown":
            await Tired(ctx=ctx)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.unknown ,name=Text))
            await ctx.send(f"Now changing Activity to: '**{Act}**' and Text to: '**{Text}**'")
            print(f"Now changing Activity to: '{Act}' and Text to: '{Text}'")
        elif TLower == "watching":
            await Tired(ctx=ctx)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching ,name=Text))
            await ctx.send(f"Now changing Activity to: '**{Act}**' and Text to: '**{Text}**'")
            print(f"Now changing Activity to: '{Act}' and Text to: '{Text}'")
        else:
            await ctx.send(f"Sorry couldnt find any activity called '**{TLower}**'.")
#
#Dev only Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#Dev only Spacer
#Dev only Spacer
#Dev only Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
@bot.command()
async def dm(ctx, user:discord.User, *arg):
    await Tired(ctx=ctx)
    await ctx.send("Now dm-ing....")
    MSGembed = discord.Embed(title=f"Message from {ctx.author}",description=' '.join(arg),color=discord.Color.blue())
    await user.send(embed=MSGembed)
    print(f"Done dm-ing {user}")

@bot.command()
async def clear_history(ctx):
    await Tired(ctx=ctx)
    await ctx.send("Now purging")
    Delete=100

    async for message in bot.get_user(ctx.author.id).history(limit=Delete):
        if message.author.id == bot.user.id:
            await message.delete()
            print(f"Deleted msg:{message}")
            await asyncio.sleep(0.5)

@bot.command()
async def meme(ctx):
    await Tired(ctx=ctx)
    Temp = MEMENames[random.randint(0,len(MEMENames))]
    await ctx.send(file=discord.File(f"FILE_PATH"))

@bot.command()
async def die(ctx):
    Comebacks = ["Look at this waste of sperm talking","Imagine talking to a bot. Dont you have any friends, oh wait you dont"]
    await ctx.send(Comebacks[random.randint(0,len(Comebacks))])

#VC Cmds
@bot.command(aliases=['join'])
async def join_vc(ctx):
    await Tired(ctx=ctx)
    global voice
    
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        print(f"Moving to '{channel.name}'")
        await ctx.send(f"Moving to '**{channel.name}**'")
        await voice.move_to(channel)
    else:
        print(f"Joining '{channel.name}'")
        await ctx.send(f"Joining '**{channel.name}**'")
        voice = await channel.connect()

@bot.command(aliases=['disc','leave'])
async def disconnect(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        print(f"Disconnecting from '{channel.name}'")
        await ctx.send(f"Disconnecting from '**{channel.name}**'")
        await voice.disconnect()
    else:
        print("Not in a VC not leaving")
        await ctx.send("Im currently not in a VC")

#TODO FIX THE QUEUE
@bot.command(aliases=['p','vibe'])
async def play(ctx, url:str):
    await Tired(ctx=ctx)

    def Check_Q():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            Length = len(os.listdir(DIR))
            Still_Q = Length - 1
            try:
                First_File = os.listdir(DIR)[0]
            except:
                print("No more queued songs")
                Queues.clear()
                return
            
            Main_Location = os.path.dirname(os.path.realpath(__file__))
            Song_Path = os.path.abspath(os.path.realpath("Queue")+f"\\{First_File}")
            if Length !=0:
                print("Song done playing, now playing next in queue")
                print(f"Songs still left {Still_Q}")
                song_there = os.path.isfile("Song.mp3")
                if song_there:
                    os.remove("Song.mp3")
                shutil.move(Song_Path, Main_Location)
                for file in os.listdir("./Queue"):
                    if file.endswith(".mp3"):
                        os.rename(file, "Song.mp3")
                
                voice.play(discord.FFmpegPCMAudio("Song.mp3"), after=lambda e: Check_Q())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                Queues.clear()
                return
        else:
            Queues.clear()
            print("No songs were queued")
                
    song_there = os.path.isfile("Song.mp3")
    voice = get(bot.voice_clients, guild=ctx.guild)
    
    try:
        if song_there:
            print("Now removing song file")
            os.remove("Song.mp3")
            Queues.clear()
    except PermissionError:
        print("Song being used")
        await ctx.send("Music is currently playing. Please wait for it to finish")
        return
    

    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Removed old Queue folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No queue folder found")
    
    print("Getting ready to dowload the song")
    await ctx.send("Now downloading your selected song")

    ydl_opts = {
        "format":"bestaudio/best",
        "quite": True,
        "postprocessors":[{
            "key":"FFmpegExtractAudio",
            "preferredcodec":"mp3",
            "preferredquality":"192",}],
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Dowload object made, now dowloading song")
            ydl.download([url])
    except Exception:
        try:
            C_Path = os.path.dirname(os.path.realpath("Queue"))
            system(f"spotdl ${url}")
        except Exception:
            print("User didnt give an actual url")
            await ctx.send(f"Give me an actuall youtube or spotify url please and not '**{url}**' <@{ctx.author.id}>")
        
    

    for i in os.listdir("./"):
        if i.endswith(".mp3"):
            name = i
            print(f"File {name} found, now renaming")
            os.rename(name, "Song.mp3")
    
    voice.play(discord.FFmpegPCMAudio("Song.mp3"), after=lambda e: Check_Q())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-",2)
    await ctx.send(f"Now playing {nname}")

@bot.command()
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Pausing music")
        voice.pause()
        await ctx.send("Music paused")
    else:
        print("Cant pause")
        await ctx.send("Couldnt pause music. Im not in a VC or music isint playing")

@bot.command(aliases=['res'])
async def resume(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resuming music")
        voice.resume()
        await ctx.send("Music resumed")
    else:
        print("Music not paused")
        await ctx.send("Music is not paused")

@bot.command(aliases=['st'])
async def stop(ctx):
    
    voice = get(bot.voice_clients, guild=ctx.guild)
    Queues.clear()
    if voice and voice.is_playing():
        print("Stopping music")
        voice.stop()
        await ctx.send("Music stopped")
    else:
        print("Cant stop")
        await ctx.send("Couldnt stop the music. Im not in a VC or music isint playing")

#TODO FIX THE QUEUE
@bot.command()
async def BETA_Q_SYS(ctx, url:str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    Q_Int = len(os.listdir(DIR))
    Q_Int += 1
    Add_Queue = True
    while Add_Queue:
        if Q_Int in Queues:
            Q_Int += 1
        else:
            Add_Queue = False
            Queues.append(Q_Int)
    
    Queue_Path = os.path.abspath(os.path.realpath("Queue")+f"\song{Q_Int}.%(ext)s")

    ydl_opts = {
        "format":"bestaudio/best",
        "quite": True,
        "outtmpl": Queue_Path,
        "postprocessors":[{
            "key":"FFmpegExtractAudio",
            "preferredcodec":"mp3",
            "preferredquality":"192",}],
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Dowload object made, now dowloading song")
            ydl.download([url])
    except Exception:
        try:
            Q_Path = os.path.dirname(os.path.realpath(__file__))
            system(f"spotdl ${url}")
        except Exception:
            print("User didnt give an actual url")
            await ctx.send(f"Give me an actuall youtube or spotify url please and not '**{url}**' <@{ctx.author.id}>")
#VC Cmds   
    

#
#WORKING CODE Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#WORKING CODE Spacer
#WORKING CODE Spacer
#WORKING CODE Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#

@bot.command()
async def latency(ctx):
    await Tired(ctx=ctx)
    MSGembed = discord.Embed(title=f"Latency",description=f"{bot.latency}",color=discord.Color.green())
    await ctx.send(embed=MSGembed)

#
#DEBUG Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#DEBUG Spacer
#DEBUG Spacer
#DEBUG Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#

async def Tired(ctx):
    T = random.randint(0,100)
    print(f"Random number choosen {T}")
    if T <= 5:
        await ctx.send("Gosh im tired, I could use some coffee right now",file=discord.File("FILE_PATH"))

#
#FUNCTION Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#FUNCTION Spacer
#FUNCTION Spacer
#FUNCTION Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#


bot.run(TOKEN)