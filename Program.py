import discord
from discord import Message, User
from discord.channel import TextChannel
from discord.ext.commands import Bot, Context
import random
import os
import requests

# Set The Random Seed
random.seed(os.urandom(1024))

""" 
Your Discord Bot token should be stored in a file named "token.txt" in 
the root directory. "token.txt" is already added in the .gitignore 
file, so it won't be tracked by Git. 
"""
TOKEN_FILE = open(r"token.txt", "r")
TOKEN = TOKEN_FILE.readline()

prefix = "!"
description = "A Bot made by Rohan and Subham"
bot = Bot(command_prefix = prefix, description = description)

@bot.event
async def on_ready() -> None:
    print(f"A Bot logged in as {bot.user}")

@bot.event
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

@bot.command(aliases = ["flipcoin", "tosscoin", "cointoss", "toss"])
async def coinflip(context: Context) -> None:
    choices = ["Heads", "Tails"]
    ranchoice = random.choice(choices)
    await context.send(ranchoice)

@bot.command(aliases = ["diceroll"])
async def rolldice(context: Context) -> None:
    choices = [1, 2, 3, 4, 5, 6]
    rannum = random.choice(choices)
    await context.send(rannum)

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

@bot.command(aliases = ["emoji"])
async def givemeanemoji(context: Context) -> None:
    choices = ["😀", "😁", "😂", "🤣", "😎", "🤐", "😆", "😥", "😑", "🤩", "😴"]
    ranemoji = random.choice(choices)
    await context.send(ranemoji)

@bot.command(aliases = ["quote"])
async def inspire(context: Context) -> None:
    response = requests.get("https://api.quotable.io/random")
    json = response.json()
    quote = f"{json['content']} \n - {json['author']}"
    await context.send(quote)

@bot.command(aliases = ["tips"])
async def advice(context: Context) -> None:
    response = requests.get("https://api.adviceslip.com/advice")
    json = response.json()
    advice = json["slip"]["advice"]
    await context.send(advice)

""" 
Following commands are temporarily made to greet Happy Birthday to one of 
our friends. These will be removed after some time.
"""

@bot.command()
async def deb(context: Context) -> None:
    file = open(r"./messages/deb.txt", "r")
<<<<<<< HEAD
    text1 = "🎉🎉🎉 Deb Daipayan is wishing Monosij Happy Birthday 🎉🎉🎉"
=======
    text1 = "Deb Daipayan is wishing Monosij Happy Birthday..."
>>>>>>> 6cfa0ce6082462e6fd5858ff7e3e61fe4b87f34a
    text2 = file.read()
    await context.send(text1)
    await context.send(text2)
    file.close()

@bot.command()
async def debayan(context: Context) -> None:
    file = open(r"./messages/debayan.txt", "r")
<<<<<<< HEAD
    text1 = "🎉🎉🎉 Debayan is wishing Monosij Happy Birthday 🎉🎉🎉"
=======
    text1 = "Debayan is wishing Monosij Happy Birthday..."
>>>>>>> 6cfa0ce6082462e6fd5858ff7e3e61fe4b87f34a
    text2 = file.read()
    await context.send(text1)
    await context.send(text2)
    file.close()

@bot.command()
async def rishi(context: Context) -> None:
    file = open(r"./messages/rishi.txt", "r")
<<<<<<< HEAD
    text1 = "🎉🎉🎉 Rishi is wishing Monosij Happy Birthday 🎉🎉🎉"
=======
    text1 = "Rishi is wishing Monosij Happy Birthday..."
>>>>>>> 6cfa0ce6082462e6fd5858ff7e3e61fe4b87f34a
    text2 = file.read()
    await context.send(text1)
    await context.send(text2)
    file.close()

@bot.command()
async def rohan(context: Context) -> None:
    file = open(r"./messages/rohan.txt", "r")
<<<<<<< HEAD
    text1 = "🎉🎉🎉 Rohan is wishing Monosij Happy Birthday 🎉🎉🎉"
=======
    text1 = "Rohan is wishing Monosij Happy Birthday..."
>>>>>>> 6cfa0ce6082462e6fd5858ff7e3e61fe4b87f34a
    text2 = file.read()
    await context.send(text1)
    await context.send(text2)
    file.close()

@bot.command()
async def srijita(context: Context) -> None:
    file = open(r"./messages/srijita.txt", "r")
<<<<<<< HEAD
    text1 = "🎉🎉🎉 Srijita is wishing Monosij Happy Birthday 🎉🎉🎉"
=======
    text1 = "Srijita is wishing Monosij Happy Birthday..."
>>>>>>> 6cfa0ce6082462e6fd5858ff7e3e61fe4b87f34a
    text2 = file.read()
    await context.send(text1)
    await context.send(text2)
    file.close()

@bot.command()
async def subhamk(context: Context) -> None:
    file = open(r"./messages/subhamk.txt", "r")
<<<<<<< HEAD
    text1 = "🎉🎉🎉 Subham is wishing Monosij Happy Birthday 🎉🎉🎉"
=======
    text1 = "Subham is wishing Monosij Happy Birthday..."
>>>>>>> 6cfa0ce6082462e6fd5858ff7e3e61fe4b87f34a
    text2 = file.read()
    await context.send(text1)
    await context.send(text2)
    file.close()

bot.run(TOKEN)