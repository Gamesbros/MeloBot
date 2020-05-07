import requests
import youtube_dl
import shutil
import os
#import dotenv
import discord
from discord.utils import get
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f"Discord Bot {client.user.name} is logged in")
    await client.change_presence(activity=discord.Game(name="I'm ready to play some music"))


# Get playlist from Melodice Website
def get_youtube_playlist(boardgame):

    page = requests.get("https://melodice.org/playlist/" + boardgame).text

    start = page.find("external_ids = [")
    end = page.find("]", start)

    page = page[start + 16: end]

    page = page.replace("'", "")
    page = page.replace("\n", "")
    page = page.replace(" ", "")

    videolist = page.split(',')

    return videolist

@client.command(pass_context=True)
async def join(ctx):
    """
    A Command to join the channel
    """
    
    return




client.run(TOKEN)