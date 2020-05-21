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


@bot.command(name="create")
async def create_game(ctx):
    for game in bot.current_games:
        if game.username == ctx.author:
            await ctx.send("You are already playing a game")
            break
    else:
        game = main.Game(1, mode="discord", username=ctx.author)
        bot.current_games.append(game)
        await ctx.send("New game created")


@bot.command(name="move")
async def make_move(ctx, *move):
    for game in bot.current_games:
        if game.username == ctx.author:
            break
    else:
        game = main.Game(1, mode="discord", username=ctx.author)
        bot.current_games.append(game)
        await ctx.send("New game created")

    await ctx.send(f"Interpreted move:\n```{' '.join(move)}```")


@bot.command(name="query")
async def query(ctx, action):
    if action == "games":
        await ctx.send(f"There are currently {len(bot.current_games)} people playing")
        for game in bot.current_games:
            await ctx.send(game.username)

bot.run(BOT_TOKEN)
