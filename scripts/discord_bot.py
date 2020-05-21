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
async def query(ctx, action=None):
    for role in ctx.author.roles:
        if role.id == 713077327445229569:
            permitted = True
            break
    else:
        permitted = False

    if permitted:
        if action == "games":
            singular = True if len(bot.current_games) == 1 else False
            await ctx.send(f"There {'is' if singular else 'are'} currently {len(bot.current_games)} "
                           f"{'person' if singular else 'people'} playing")

        elif action == "players":
            if len(bot.current_games) == 0:
                await ctx.send("There is currently nobody playing")
            else:
                await ctx.send("Currently playing:")
                player_list = []
                for game in bot.current_games:
                    player_list.append(str(game.username))
                players_str = "\n- ".join(player_list)
                await ctx.send(f"```{players_str}```")


bot.run(BOT_TOKEN)
