import os
from discord.ext import commands
from dotenv import load_dotenv
from scripts import main

load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Bot {bot.user} has connected")


@bot.command(name="play")
async def play_game(ctx):
    pass
