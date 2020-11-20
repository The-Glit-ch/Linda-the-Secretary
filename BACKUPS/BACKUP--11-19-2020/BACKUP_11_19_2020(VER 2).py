import discord
import asyncio
import os
import random
import youtube_dl
import shutil
import praw
from os import system
from discord.ext import commands
from discord.utils import get
from discord import Spotify
from discord.ext.commands.errors import MissingPermissions, MissingRequiredArgument
from discord.ext.commands import has_permissions

bot = commands.Bot(command_prefix='Linda ')
bot.remove_command('help')

#VARS
global Lockdown
global voice
TOKEN = ""
voice = None
Lockdown = False

Whitelist = [557339295325880320,762844152429412402]
Sus = [729169434278625330]
Queues = []
ActList = ["competing","custom","listening","mro","playing","streaming","unknown","watching"]

#VARS

@bot.event
async def on_ready():
    print ("------------------------------------")
    print (f"Bot Name: {str(bot.user.name)}")
    print (f"Bot ID: {bot.user.id}")
    print ("------------------------------------")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening ,name="something"))


@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name="Unverified member")
    await member.add_roles(role)
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

#
#Dev only Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#Dev only Spacer
#Dev only Spacer
#Dev only Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#

@bot.command(aliases=['Ban'])
@has_permissions(ban_members=True)
async def ban(ctx, user:discord.Member, *reason:str):
    await ctx.send(f"Now banning {user}, bye bye love ;3")
    await user.ban(reason=' '.join(reason))

@bot.command(aliases=['Kick'])
@has_permissions(kick_members=True)  
async def kick(ctx, user:discord.Member, *reason:str):
    await ctx.send(f"{user} is now being kicked, bye bye love ;3")
    await user.kick(reason=' '.join(reason))

#@kick.error
#async def kick_error(error,ctx):
    #if isinstance(error, MissingPermissions):
        #await ctx.send("Sorry, but you dont have permission to use that command")

#@ban.error
#async def ban_error(error,ctx):
    #if isinstance(error, MissingPermissions):
        #await ctx.send("Sorry, but you dont have permission to use that command")

#
#Admin only Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#Admin only Spacer
#Admin only Spacer
#Admin only Spacer^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
    await ctx.send("Now purging dms")
    Delete=100

    async for message in bot.get_user(ctx.author.id).history(limit=Delete):
        if message.author.id == bot.user.id:
            await message.delete()
            print(f"Deleted msg:{message}")
            await asyncio.sleep(0.5)

@bot.command(aliases=['reddit','br'])
async def browse_reddit(ctx, sub):
    try:
        await Tired(ctx=ctx)
        reddit = praw.Reddit(client_id="client_id", client_secret="client_secret",
                            password="password", user_agent="user_agent",
                            username="username")
            
        Sub = reddit.subreddit(sub)
        submission = Sub.random()
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
    Death = [f"{user} died to fall damage",f"{user} dies from seeing {Author}'s face",f"{user} had enough of this world and just dies",f"{user} fucked a monkey and died of aids",f"{user} had a stroke from reading {Author}'s dm",f"{user} died from jacking off too {Author} 50 times in a row",f"{user}'s mom caught them watching gay no-no video",f"{Author} kamakazied {user}",f"{user} got killed by {Author}'s thicc thighs",f""]
    try:
        await ctx.send(Death[random.randint(0,len(Death))])
    except:
        await ctx.send(Death[random.randint(0,len(Death))])

@bot.command(aliases=['h','Help'])
async def help(ctx):
    Embed = discord.Embed(title="List of commands", description="""
    **Dev Commands:**

        ``Linda byebye`` Shuts down the bot **(Aliases=``goodbye``,``cya``,``cya_later``,``<a:peaceout:491498410604625921>``)**\n
        ``Linda spotify_link`` Under development **(Aliases=None)**\n
        ``Linda update_status <activity> <message>`` Updates Linda's activity **(Aliases=None)**\n
        
    **Admin/Mod Commands:**

        ``Linda kick <user> <reason>`` Kicks user **(Aliases=``Kick``)**\n
        ``Linda ban <user> <reason>`` Bans user **(Aliases=``Ban``)**\n

    **Commands:**

        ``Linda dm <user> <msg>`` Dms the specified user with the specified message **(Aliases=None)**\n
        ``Linda clear_history`` Clears your dm history with linda **(Aliases=None)**\n
        ``Linda browse_reddit <subreddit>`` Browse reddit(NSFW Posts will be messaged to you) **(Aliases=``reddit``,``br``)**\n
        ``Linda kill <user>`` Either the specified user dies, you die, or you both die ¯\_(ツ)_/¯ **(Aliases=None)**\n
        ``Linda help`` Do I really have to explain this **(Aliases=``h``,``Help``)**\n
        ``Linda profile <user>`` Get info on a user's profile **(Aliases=None)**

    **VC Commands:**

    *(VC Code is a mess curently, dont expect it to be perfect --The_Glit-ch)*
        ``Linda join_vc`` Linda joins the VC channel your in **(Aliases=``join``)**\n
        ``Linda disconnect`` Linda leaves the current channel she is in **(Aliases=``disc``,``leave``)**\n
        ``Linda play <url/song name>`` Linda plays any song/audio you want **(Aliases=``p``,``vibe``)**\n
        ``Linda pause`` Linda pauses the current playing song/audio **(Aliases=``None``)**\n
        ``Linda resume`` Linda resumes the song/audio **(Aliases=``res``)**\n
        ``Linda stop`` Linda stop the song/audio **(Aliases=``st``)**\n
    
    **Other/Debug**
    
        ``Linda latency`` Get the current latency **(Aliases=``lat``)**\n""",color=discord.Color.red())
    await ctx.send("Now sending you a dm")
    await ctx.author.send(embed=Embed)

@bot.command()
async def profile(ctx,user:discord.Member):
    Embed = discord.Embed(title=f"{user} user info",description=f"Profile Info:\nUser Nick: **{user.nick}**\nUser Join Date: **{user.joined_at}**\nUser Nitro Since: **{user.premium_since}**\nUser Status: {user.activity}\nUser profile picture {user.avatar_url}\n",color=discord.Color.gold()).set_image(url=user.avatar_url)
    await ctx.send(embed=Embed)

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
@bot.command(aliases=['p','vibe'])
async def play(ctx, *url:str):
    await Tired(ctx=ctx)
    JoinedURL = ' '.join(url)
    voice = get(bot.voice_clients, guild=ctx.guild)

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
        
    

    for i in os.listdir("./"):
        if i.endswith(".mp3"):
            SongName = i
            print(f"File {SongName} found, now renaming")
            os.rename(SongName, "Song.mp3")
    
    voice.play(discord.FFmpegPCMAudio("Song.mp3"), after=lambda e: Check_Q())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    Emoji = discord.utils.get(bot.emojis,name="xar")
    Embed = discord.Embed(title="Now Playing", description=f"{str(Emoji)} **{JoinedURL}** {str(Emoji)}",color=discord.Color.green())
    await ctx.send(embed=Embed)

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
    Queues.clear()
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