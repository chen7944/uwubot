from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from config import *
import aiohttp

bot = commands.Bot(command_prefix="!", help_command=None)

@bot.event
async def on_ready():
    print("Ready")

def uwu(text):
    output = text
    output.replace("L", "W")
    output.replace("l", "w")
    output.replace("R", "W")
    output.replace("r", "W")
    output.replace("ove")

@bot.event
async def on_message(message):
    if not message.author.bot:
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
            await webhook.send(message.content, username=message.author.name, avatar_url=message.author.avatar_url)


bot.run(token)