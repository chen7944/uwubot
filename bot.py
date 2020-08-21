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
    await bot.change_presence(activity=discord.Game(name='?help'))

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

def error_response(error_text):
    emb = discord.Embed(
            description=error_text,
            title='Error :x:',
            color=0xff4444
        )
    emb.set_footer(text='For more help with commands, use ?help.')
    return emb

@bot.command()
async def help(ctx):
    emb = discord.Embed(
        title="Help",
        color=0xf47fff,
        description="The curly braces {} should not be included in the actual command"
    )
    emb.add_field(name="?info", value="Info about the bot", inline=False)
    emb.add_field(name="?set {channel}", value="Sets the channel the bot will read from", inline=False)
    emb.add_field(name="?config", value="See which channel the bot is reading from", inline=False)
    emb.set_footer(text="For more information, visit my github https://github.com/chen7944/uwubot")
    await ctx.channel.send(embed=emb)

@bot.command()
async def info(ctx):
    emb = discord.Embed(
        title="Info",
        color=0xf47fff,
        description="UwU-fies message from one channel and sends them in another"
    )
    await ctx.channel.send(embed=emb)

@bot.command(name="set")
async def set_channel(ctx, channel=None):
    global read_channel
    if channel is None:
        await ctx.channel.send(embed=error_response("Invalid parameters, use ?help for more information"))
        return
    read_channel = channel[2:len(channel)-1]
    emb = discord.Embed(
        title="Channel set :white_check_mark:",
        color=0xf47fff,
        description=f"Messages will now be read from {channel}"
    )
    await ctx.channel.send(embed=emb)

@bot.command()
async def config(ctx):
    emb = discord.Embed(
        title="Config",
        color=0xf47fff,
        description=f"I am currently reading messages from <#{read_channel}>"
    )
    await ctx.channel.send(embed=emb)

@bot.event
async def on_message(message):
    if not message.author.bot and str(message.channel.id) == read_channel:
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
            await webhook.send(uwuify(message.content), username=message.author.name, avatar_url=message.author.avatar_url)
    await bot.process_commands(message)


bot.run(token)