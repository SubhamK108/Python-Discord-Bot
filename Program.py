import discord

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

client.run(TOKEN)