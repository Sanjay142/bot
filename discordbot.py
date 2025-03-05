import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your bot token
TOKEN = 'YOUR_BOT_TOKEN'

# Set the command prefix (e.g., !hello)
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(f'The sum is {a + b}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Try !help for available commands.")
    else:
        await ctx.send("An error occurred.")

bot.run(TOKEN)
