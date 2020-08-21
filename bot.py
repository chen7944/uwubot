import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from config import *
import aiohttp

bot = commands.Bot(command_prefix="?", help_command=None)
read_channel = ""

@bot.event
async def on_ready():
    print("Ready")

def uwuify(text):
    length = len(text)
    output_text = ''
    for i in range(length):
        current_char = text[i]
        previous_char = 'q!1u&7u&7p)0q!1e#3'
        upper_vowels = ['A', 'E', 'I', 'O', 'U']
        lower_vowels = ['a', 'e', 'i', 'o', 'u']
        if i > 0:
            previous_char = text[i - 1]

        if current_char == 'L' or current_char == 'R':
            output_text += 'W'

        elif current_char == 'l' or current_char == 'r':
            output_text += 'w'

        elif current_char in upper_vowels:
            if previous_char == 'N' or previous_char == 'M':
                output_text += "Y"
                output_text += current_char
            else:
                output_text += current_char

        elif current_char in lower_vowels:
            if previous_char == 'n' or previous_char == 'm':
                output_text += "y"
                output_text += current_char
            else:
                output_text += current_char

        elif current_char == 'S':
            if previous_char == 'I':
                output_text += "W"
            else:
                output_text += current_char

        elif current_char == 's':
            if previous_char == 'i':
                output_text += "w"
            else:
                output_text += current_char

        elif current_char == 'OVE':
            output_text += 'UV'

        elif current_char == 'ove':
            output_text += 'uv'

        else:
            output_text += current_char

    return output_text

@bot.command(name="info")
async def info(ctx):
    emb = discord.Embed(
        title="Info",
        color=0xf47fff,
        description="UwU-fies message from one channel and sends them in another"
    )
    await ctx.channel.send(embed=emb)

@bot.command(name="set")
async def set_channel(ctx, channel):
    global read_channel
    read_channel = channel[2:len(channel)-1]


@bot.event
async def on_message(message):
    if not message.author.bot and str(message.channel.id) == read_channel:
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
            await webhook.send(uwuify(message.content), username=message.author.name, avatar_url=message.author.avatar_url)
    await bot.process_commands(message)


bot.run(token)