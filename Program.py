import discord
from discord import Message, User
from discord.channel import TextChannel
from discord.ext.commands import Bot, Context
import random
import os

# Set The Random Seed
random.seed(os.urandom(1024))
<<<<<<< HEAD

# Your Discord Bot token should be stored in a file named token.txt
TOKEN_FILE = open(r"token.txt", "r")
TOKEN = f"{TOKEN_FILE.readline()}"

prefix = "!"
description = "A Bot made by Rohan and Subham"
bot = Bot(command_prefix = prefix, description = description)

@bot.event
async def on_ready() -> None:
    print(f"A Bot logged in as {bot.user}")

@bot.event
=======

# Your Discord Bot token should be stored in a file named token.txt
# TOKEN_FILE = open(r"token.txt", "r")
# TOKEN = f"{TOKEN_FILE.readline()}"
TOKEN = "ODI1OTYzODcxODUxNTExODE4.YGFkzA.yRt1oZbSqQralSzCHx8MtDXhwCM"

prefix = "!"
description = "A Bot made by Rohan and Subham"
bot = Bot(command_prefix = prefix, description = description)

@bot.event
async def on_ready() -> None:
    print(f"A Bot logged in as {bot.user}")

@bot.event
>>>>>>> fe3b2d5afeeec2747de067955b2306b0a9a1958a
async def on_message(message: Message) -> None:
    user: User = message.author
    # Don't reply to own messages or any message coming from another bot
    if user == bot.user or user.bot:
        return
    await bot.process_commands(message)

@bot.command(aliases = ["hi", "sup"])
async def hello(context: Context) -> None:
    user: User = context.author
    await context.send(f"Bot says hello to {user.name}")

@bot.command()
async def whoami(context: Context) -> None:
    user: User = context.author
    await context.send(f"You are {user.name}")

<<<<<<< HEAD
@bot.command(aliases = ["flipcoin", "tosscoin", "cointoss", "toss"])
=======
@bot.command(aliases = ["flipcoin", "tosscoin", "cointoss"])
>>>>>>> fe3b2d5afeeec2747de067955b2306b0a9a1958a
async def coinflip(context: Context) -> None:
    choices = ["Heads", "Tails"]
    ranchoice = random.choice(choices)
    await context.send(ranchoice)

<<<<<<< HEAD
@bot.command(aliases = ["diceroll"])
async def rolldice(context: Context) -> None:
    choices = [1, 2, 3, 4, 5, 6]
    rannum = random.choice(choices)
    await context.send(rannum)

=======
>>>>>>> fe3b2d5afeeec2747de067955b2306b0a9a1958a
@bot.command()
async def chooseside(context: Context) -> None:
    choices = ["Attack", "Defend"]
    ranside = random.choice(choices)
    await context.send(ranside)

@bot.command()
async def choosemap(context: Context) -> None:
    choices = ["Ascent", "Split", "Bind", "Haven", "Icebox"]
    ranmap = random.choice(choices)
    await context.send(ranmap)

<<<<<<< HEAD
@bot.command(aliases = ["emoji"])
async def givemeanemoji(context: Context) -> None:
    choices = ["😀", "😁", "😂", "🤣", "😎", "🤐", "😆", "😥", "😑", "🤩", "😴"]
=======
@bot.command()
async def givemeanemoji(context: Context) -> None:
    choices = ["😀", "😁", "😂", "🤣", "😎", "🤐", "😆"]
>>>>>>> fe3b2d5afeeec2747de067955b2306b0a9a1958a
    ranemoji = random.choice(choices)
    await context.send(ranemoji)

bot.run(TOKEN)