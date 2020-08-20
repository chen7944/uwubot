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
    uwu_uri = "data:image/jpeg;base64,https://images.discordapp.net/avatars/520682706896683009/9750a6a354e927285a534d015e2a0044.png?size=512"
    if not message.author.bot:
        webhook_url = "https://discordapp.com/api/webhooks/745818180999577741/4Dhxv7n2YmXQnIhz_3oHZk1bs9Mavq9zTw5ZaAk70QeN57Tuuf3RMoyYmRn4Wh3ktK6o"
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
            await webhook.send(message.content, username=message.author.name, avatar_url=message.author.avatar_url)


bot.run(token)