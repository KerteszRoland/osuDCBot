import discord, asyncio
from discord.ext import commands, tasks
import osu


def GetBearerToken():
    bearer_token = "NOT LOADED"
    with open("dc_api_key.txt", "r") as file:
        bearer_token = file.readline()
    return bearer_token


def GetOsuChannelID():
    channel_id = "NOT LOADED"
    with open("osu_text_channel_id.txt", "r") as file:
        channel_id = int(file.readline())
    return channel_id
    

client = commands.Bot(command_prefix = '!')
TOKEN = GetBearerToken()
osu_channel_id = GetOsuChannelID()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    refresh_token.start()
    osubot.start()

@tasks.loop(seconds=86000)
async def refresh_token():
    osu.TOKEN = osu.GetToken()
  

@tasks.loop(seconds=10)
async def osubot():
    users = osu.GetUsers()
    osu_channel = client.get_channel(osu_channel_id)
    for user in users:  
        status = osu.AddRecentBeatmapScore(user)
        if status == None:
            continue
        #await osu_channel.send(f"<@{users[user]}>") 
        await osu_channel.send(embed=status) 
       

@client.command()
async def osuadd(ctx, url):
    if ("https://osu.ppy.sh/users/" not in url):
        await ctx.channel.send("Wrong url!")
        return
        
    discord_id = str(ctx.author.id)
    osu_id = url.split('/')[-1]
    text = osu.AddUser(discord_id, osu_id)
    await ctx.channel.send(text)    
    
    
@client.command()
async def osuremove(ctx):
    discord_id = str(ctx.author.id)
    text = osu.RemoveUser(discord_id)
    await ctx.channel.send(text)    


client.run(TOKEN)