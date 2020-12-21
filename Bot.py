#import asyncio
#import os
#import random
#import youtube_dl
#import shutil
#import praw
from typing import ContextManager
import discord, asyncio, os, random, youtube_dl, shutil, praw, time
from discord.colour import Color
from mee6_py_api import API
from os import pathsep, system
from mutagen.mp3 import MP3
from discord import Spotify, Member, Intents
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands.errors import MissingPermissions, MissingRequiredArgument

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='Linda ',intents=intents)
Pre = "Linda"
bot.remove_command('help')

#Tokens
TOKEN = "Ha no"
RedditAPI = {
    "Ha no",
}

#VARS
global voice
voice = None

Whitelist = [557339295325880320,762844152429412402]
Blacklist = [729169434278625330,764133892923588628]
ActList = ["competing","custom","listening","mro","playing","streaming","unknown","watching"]
#VARS


@bot.event
async def on_ready():
    print ("------------------------------------")
    print (f"Bot Name: {str(bot.user.name)}")
    print (f"Bot ID: {bot.user.id}")
    print ("------------------------------------")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening ,name="something, idk"))

@bot.event
async def on_member_join(member):
    TS = bot.get_channel(762761198277230592)
    role = get(member.guild.roles, name="Unverified member")
    await member.add_roles(role)
    await TS.send(f"Welcome {member} to the server")

@bot.event
async def on_member_remove(member):
    TS = bot.get_channel(762761198277230592)
    await TS.send(f"Well that fucker {member} left")


@bot.event
async def on_message(ctx):
    if ctx.author.id in Blacklist:
        pass
    else:
        await bot.process_commands(ctx)

#
#Event Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#Event Spacer
#Event Spacer
#Event Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
@bot.command(aliases=['goodbye','cya','cya_later','<a:peaceout:491498410604625921>'])
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
        await ctx.send(str(ctx.author.activities[0].name))

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
            await ctx.send(f"Sorry couldnt find any activity called '**{TLower}**'. Here are the available activities ``{str(ActList)}``")

@bot.command()
async def blacklist(ctx):
    List = []
    if ctx.author.id in Whitelist:
        await ctx.send("Current blacklist")
        for i in Blacklist:
            List.append(f"<@{i}>")
            print(List)

        FList = str(List).replace("[","").replace("]","").replace("'","").replace(",","\n")
        Embed = discord.Embed(title="All Blacklisted users",description=FList,color=discord.Color.red())
        await ctx.send(embed=Embed)
    else:
        await ctx.send("Generic no allowed access message here")
#
#Dev only Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#Dev only Spacer
#Dev only Spacer
#Dev only Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#

@bot.command(aliases=['Ban'])
@has_permissions(ban_members=True)
async def ban(ctx, user:discord.Member):
    await ctx.send(f"Now banning {user}, bye bye love ;3")
    await user.ban(reason="Banned by Linda")

@bot.command(aliases=['Kick'])
@has_permissions(kick_members=True)  
async def kick(ctx, user:discord.Member):
    await ctx.send(f"{user} is now being kicked, bye bye love ;3")
    await user.kick(reason="Kicked by Linda")

#
#Admin only Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#Admin only Spacer
#Admin only Spacer
#Admin only Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    await ctx.send("Now purging dms")
    Delete=100

    async for message in bot.get_user(ctx.author.id).history(limit=Delete):
        if message.author.id == bot.user.id:
            await message.delete()
            print(f"Deleted msg:{message}")
            await asyncio.sleep(0.5)

@bot.command(aliases=['reddit','br'])
async def browse_reddit(ctx, sub):
    #try:
    await Tired(ctx=ctx)
    reddit = praw.Reddit(client_id=RedditAPI.get("client_id"), client_secret=RedditAPI.get("client_secret"),
                            password=RedditAPI.get("password"), user_agent=RedditAPI.get("user_agent"),
                            username=RedditAPI.get("username"))
    
    print(reddit.user.me())        
    Sub = reddit.subreddit(sub)
    submission = Sub.random()
    try:
        if submission.over_18 is True:
            print("Post marked NSFW, now dm-ing")
            print(f"Reddit Post Data:\nTitle:{submission.title}\nAuthor:{submission.author}\nSub:{sub}\nNSFW:{submission.over_18}\nScore:{submission.score}\nURL:{submission.url}\nUser:{ctx.author}\n")
            Embed = discord.Embed(title=f"**{submission.title}**\nFrom: **{submission.author}** in: **{sub}**",description=f"Current score of {submission.score}. Look at the post here {submission.url}", color= discord.Color.red()).set_image(url=submission.url)
            await ctx.author.send(embed=Embed)
        else:
            print(f"Reddit Post Data:\nTitle:{submission.title}\nAuthor:{submission.author}\nSub:{sub}\nNSFW:{submission.over_18}\nScore:{submission.score}\nURL:{submission.url}\nUser:{ctx.author}\n")
            Embed = discord.Embed(title=f"**{submission.title}**\nFrom: **{submission.author}** in: **{sub}**",description=f"Current score of {submission.score}. Look at the post here {submission.url}", color= discord.Color.red()).set_image(url=submission.url)
            await ctx.send(embed=Embed)
    except:
      await ctx.send("You must specify a **REAL** subreddit and make sure its written **CORRECTLY**(Ex: ``Linda browse_reddit ProgrammerHumor`` **OR** ``Linda reddit ProgrammerHumor``)")
    
@bot.command()
async def kill(ctx,user:discord.Member):
    Author = ctx.author
    Death = [f"Ex Death: {user} was killed by {Author}"]
    try:
        await ctx.send(Death[random.randint(0,len(Death))])
    except:
        await ctx.send(Death[random.randint(0,len(Death))])

@bot.command(aliases=['h','Help'])
async def help(ctx):
    DevCMDS = discord.Embed(title="``Dev`` Commands List", description="""
    **Dev Commands:**

        ``Linda byebye``Shuts down the bot**(Aliases=``goodbye``,``cya``,``cya_later``,``<a:peaceout:491498410604625921>``)**\n
        ``Linda spotify_link``Under development**(Aliases=``None``)**\n
        ``Linda update_status <activity> <message>``Updates Linda's activity**(Aliases=``None``)**\n
        ``Linda blacklist`` Shows all users blacklisted **(Aliases=``None``)**\n""",color=discord.Color.red())
    
    AdminCMDS = discord.Embed(title="``Admin`` Commands List",description="""
    **Admin Commands:**
    
        ``Linda ban`` Bans the specified user **(Aliases=``Ban``)**\n
        ``Linda kick`` Kicks the specified user **(Aliases=``Kick``)**\n""",color=discord.Color.red())
    
    CommandCMDS = discord.Embed(title="``Commands`` List",description="""
    **Commands:**
    
        ``Linda dm <user> <message>`` Direct Messages the specified person with your message **(Aliases=``None``)**\n
        ``Linda clear_history`` Clears your direct message history with Linda **(Aliases=``None``)**\n
        ``Linda browse_reddit <subreddit>`` Browse Reddit **(Aliases=``reddit``,``br``)**\n
        ``Linda kill <user>`` Kills the specified user...or you ;) **(Aliases=``None``)**\n
        ``Linda help`` Shows this :O **(Aliases=``h``,``Help``)**\n
        ``Linda profile <user>`` Get user info on the specified user **(Aliases=``info``)**\n
        ``Linda repeat <message>`` Repeats what you say **(Aliases=``say``)**\n
        ``Linda minecraft "<top_text>" "<bottom_text>"`` Get a minecraft achivement type thing **(Aliases==``mc``)**\n""",color=discord.Color.red())
    
    VCCMDS = discord.Embed(title="``Voice Channel`` Commands List",description="""
    **Voice Channel Commands:**
    --Note VC commands are currently a mess, dont expect them to be perfect
    
        ``Linda join_vc`` Joins the current VC your in **(Aliases=``join``)**\n
        ``Linda disconnect`` Disconnects from the VC **(Aliases=``disc``,``leave``)**\n
        ``Linda play <audio_url/audio_name>`` Plays the Audio in VC **(Aliases=``p``,``vibe``,``pl``)**\n
        ``Linda pause`` Pauses the current playing audio **(Aliases=``None``)**\n
        ``Linda resume`` Resumes playing the current audio **(Aliases=``res``)**\n
        ``Linda stop`` Stops playing the current audio **(Aliases=``st``)**\n""",color=discord.Color.red())
    

    await ctx.send("Now sending you some dms")
    await ctx.author.send(embed=DevCMDS)
    await ctx.author.send(embed=AdminCMDS)
    await ctx.author.send(embed=CommandCMDS)
    await ctx.author.send(embed=VCCMDS)

@bot.command(aliases=['info'])
async def profile(ctx,user:discord.Member):
    try:
        print(f"Getting user info from {user}, requested by {ctx.author}")
        mee6API = API(ctx.message.guild.id)
        Details = await mee6API.levels.get_user_details(user.mention.replace("<@","").replace(">","").replace("!","").replace("<@","").replace(">",""))
        LVL = dict(Details).get("level")
        XP = dict(Details).get("xp")
        MSG = dict(Details).get("message_count")
        Embed = discord.Embed(title=f"{user} user info",description=f"Profile Info:\nUser Nick: **{user.nick}**\nUser Join Date: **{user.joined_at}**\nUser Nitro Since: **{user.premium_since}**\nUser MEE6 Stats:\n Level: **{LVL}**\n Message Count: **{MSG}**\nXP: **{XP}**\nUser profile picture: {user.avatar_url}\n",color=discord.Color.gold()).set_image(url=user.avatar_url)
        await ctx.send(embed=Embed)
    except:
        Embed = discord.Embed(title=f"{user} user info",description=f"Profile Info:\nUser Nick: **{user.nick}**\nUser Join Date: **{user.joined_at}**\nUser Nitro Since: **{user.premium_since}**\nUser profile picture: {user.avatar_url}\n",color=discord.Color.gold()).set_image(url=user.avatar_url)
        await ctx.send(embed=Embed)

@bot.command(aliases=['say'])
async def repeat(ctx, msg:str):
    Fmsg = str(ctx.message.content).replace(f"{Pre} repeat","").replace(f"{Pre} say","").lower()
    print(f"Now saying {Fmsg} by {ctx.author}")
    if "stupid" in Fmsg:
        await ctx.send("We know")
    else:
        await ctx.send(Fmsg)
        await ctx.message.delete()

@bot.command(aliases=['mc'])
async def minecraft(ctx, ytext:str, wtext:str):
    YTemp = ytext.replace(" ","+")
    WTemp = wtext.replace(" ","+")
    print(f"New request from {ctx.author}, https://mcgen.herokuapp.com/a.php?i=1&h={YTemp}&t={WTemp}")
    await ctx.send(f"https://mcgen.herokuapp.com/a.php?i=1&h={YTemp}&t={WTemp}")

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
    if ctx.message.author.voice.channel != None:
        if voice and voice.is_connected():
            print(f"Disconnecting from '{channel.name}'")
            await ctx.send(f"Disconnecting from '**{channel.name}**'")
            await voice.disconnect()
        else:
            print("Not in a VC not leaving")
            await ctx.send("Im currently not in a VC")
    else:
        await ctx.send("You must be in a VC to use the 'disconnect' command")

#TODO FIX THE QUEUE
@bot.command(aliases=['p','vibe','pl'])
async def play(ctx, *url:str):
    Timer = time.time()
    await Tired(ctx=ctx)
    SongListData = []
    JoinedURL = ' '.join(url)
    voice = get(bot.voice_clients, guild=ctx.guild)
                
    song_there = os.path.isfile("Song.mp3")
    SongList = []
    Int = 0
    
    try:
        for i in os.listdir("./"):
            if i.endswith(".mp3"):
                os.remove(i)
                SongList.clear()
                Int=0
    except PermissionError:
        print("Song being used")
        await ctx.send("Music is currently playing. Please wait for it to finish")
        return
    
    print("Getting ready to dowload the song")
    await ctx.send("Now downloading your selected song. Please be patient it might take a while(Especially with spotify songs)")

    ydl_opts = {
        "format":"bestaudio/best",
        "quite":True,
        "postprocessors":[{
            "key":"FFmpegExtractAudio",
            "preferredcodec":"mp3",
            "preferredquality":"192",}],
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Dowload object made, now dowloading song")
            ydl.download([JoinedURL])
    except Exception:
        try:
            Temp = JoinedURL.replace(" ","_")
            C_Path = os.path.dirname(os.path.realpath("Queue"))
            system(f"spotdl ${Temp}")
        except Exception:
            print("User didnt give an actual url")
            await ctx.send(f"Give me an actuall Youtube or Spotify url please and not '**{JoinedURL}**'. You can also specify a song name(EX: ``Linda p BFG Division``) <@{ctx.author.id}>")
        
    
    print(f"Song download took {time.time() - Timer}")
    
    

    for i in os.listdir("./"):
        if i.endswith(".mp3"):
            SongListData.append(i)
            SongList.append(f"Song{Int}.mp3")
            print(f"File {i} found, now renaming")
            os.rename(i, f"Song{Int}.mp3")
            Int = Int+1
    
    async def p_song(itter):
        voice.play(discord.FFmpegPCMAudio(itter), after=lambda e: print("Now playing next song"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.10
        #T = str(SongListData).replace(".mp3","").replace("-"," ").replace(",","\n").replace("[","").replace("]","")
        Emoji = discord.utils.get(bot.emojis,name="xar")
        Embed = discord.Embed(title="Now Playing", description=f"{str(Emoji)} **{JoinedURL}** {str(Emoji)}",color=discord.Color.green())
        await ctx.send(embed=Embed)

    for i in SongList:
        await p_song(i)
        print(f"Song length is {MP3(i).info.length}")
        await asyncio.sleep(MP3(i).info.length)      

    SongListData.clear()

@bot.command()
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.message.author.voice.channel != None:
        if voice and voice.is_playing():
            print("Pausing music")
            voice.pause()
            await ctx.send("Music paused")
        else:
            print("Cant pause")
            await ctx.send("Couldnt pause music. Im not in a VC or music isint playing")
    else:
        await ctx.send("You must be in a VC to use the 'pause' command")

@bot.command(aliases=['res'])
async def resume(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.message.author.voice.channel != None:
        if voice and voice.is_paused():
            print("Resuming music")
            voice.resume()
            await ctx.send("Music resumed")
        else:
            print("Music not paused")
            await ctx.send("Music is not paused")
    else:
        await ctx.send("You must be in a VC to use the 'resume' command")

@bot.command(aliases=['st'])
async def stop(ctx):
    
    voice = get(bot.voice_clients, guild=ctx.guild)
    if ctx.message.author.voice.channel != None:
        if voice and voice.is_playing():
            print("Stopping music")
            voice.stop()
            await ctx.send("Music stopped")
        else:
            print("Cant stop")
            await ctx.send("Couldnt stop the music. Im not in a VC or music isint playing")
    else:
        await ctx.send("You must be in a VC to use the 'stop' command")

#TODO FIX THE QUEUE
def collapse():
    # @bot.command()
    # async def BETA_Q_SYS(ctx, url:str):
    #     Queue_infile = os.path.isdir("./Queue")
    #     if Queue_infile is False:
    #         os.mkdir("Queue")
    #     DIR = os.path.abspath(os.path.realpath("Queue"))
    #     Q_Int = len(os.listdir(DIR))
    #     Q_Int += 1
    #     Add_Queue = True
    #     while Add_Queue:
    #         if Q_Int in Queues:
    #             Q_Int += 1
    #         else:
    #             Add_Queue = False
    #             Queues.append(Q_Int)
        
    #     Queue_Path = os.path.abspath(os.path.realpath("Queue")+f"\song{Q_Int}.%(ext)s")

    #     ydl_opts = {
    #         "format":"bestaudio/best",
    #         "quite": True,
    #         "outtmpl": Queue_Path,
    #         "postprocessors":[{
    #             "key":"FFmpegExtractAudio",
    #             "preferredcodec":"mp3",
    #             "preferredquality":"192",}],
    #     }

    #     try:
    #         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #             print("Dowload object made, now dowloading song")
    #             ydl.download([url])
    #     except Exception:
    #         try:
    #             Q_Path = os.path.dirname(os.path.realpath(__file__))
    #             system(f"spotdl ${url}")
    #         except Exception:
    #             print("User didnt give an actual url")
    #             await ctx.send(f"Give me an actuall youtube or spotify url please and not '**{url}**' <@{ctx.author.id}>")
    pass
#VC Cmds   

#
#WORKING CODE Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#WORKING CODE Spacer
#WORKING CODE Spacer
#WORKING CODE Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#

@bot.command(aliases=['lat'])
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
        await ctx.send("Gosh im tired, I could use some coffee right now",file=discord.File(os.path.abspath(__file__).replace("\Bot.py","\Tired.png")))

#
#FUNCTION Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#FUNCTION Spacer
#FUNCTION Spacer
#FUNCTION Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#


bot.run(TOKEN)