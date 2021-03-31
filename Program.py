import discord
import random

# Your Discord Bot Token
TOKEN_FILE = open(r"token.txt", "r")
TOKEN = f"{TOKEN_FILE.readline()}"

client = discord.Client()

@client.event
async def on_ready():
    print(f"A Bot logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    content = message.content
    channel = message.channel

    if content.startswith("!hello"):
        await channel.send("Bot says Hello!")

    if content.startswith("!whoami"):
        user = channel.author.name
        await channel.send(user)
    
    if content.startswith("!coinflip"):
        choices = ["Heads", "Tails"]
        rancoin = random.choice(choices)
        await channel.send(rancoin)
    
    if content.startswith("!chooseside"):
        choices = ["Attack", "Defend"]
        ranside = random.choice(choices)
        await channel.send(ranside)

    if content.startswith("!givemeanemoji"):
        choices = ["😀", "😁", "😂", "🤣", "😎", "🤐", "😆"]
        emoji = random.choice(choices)
        await channel.send(emoji)

client.run(TOKEN)