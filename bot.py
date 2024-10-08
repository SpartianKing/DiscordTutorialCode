import discord
from discord.ext import commands

# Enable intents to allow the bot to read message content
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

# Create the bot instance with intents
bot = commands.Bot(command_prefix="!", intents=intents) # Can change prefix

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Respond to the !hi command
@bot.command()
async def hi(ctx):
    await ctx.send('Hi!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot with your token
bot.run('PASTE DISCORD TOKEN HERE')
