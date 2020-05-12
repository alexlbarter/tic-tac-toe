import os
from discord.ext import commands
from dotenv import load_dotenv
from scripts import main, console_display

load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = commands.Bot(command_prefix="!")

bot.current_games = []


@bot.event
async def on_ready():
    print(f"Bot {bot.user} has connected")


@bot.command(name="play")
async def play_game(ctx, action, *move):
    if action == "new":
        for game in bot.current_games:
            if game.username == ctx.author:
                await ctx.send("You are already playing a game")
                break
        else:
            game = main.Game(1, mode="discord", username=ctx.author)
            bot.current_games.append(game)
            await ctx.send("New game created")
    elif action == "move":
        for game in bot.current_games:
            if game.username == ctx.author:
                break
        else:
            game = main.Game(1, mode="discord", username=ctx.author)
            bot.current_games.append(game)
            await ctx.send("New game created")




bot.run(BOT_TOKEN)
