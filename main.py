import time
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord_slash import SlashCommand
import requests
load_dotenv()

token = os.environ.get('BOT_TOKEN')

bot = commands.Bot(command_prefix='/')
slash = SlashCommand(bot, sync_commands=True)

def post_meme():
    try:
        response = requests.get('https://backend-omega-seven.vercel.app/api/getjoke')
        print(response)
        joke = response.json()[0]
        question=joke['question']
        punchline = joke['punchline']
        # print(joke)
        embed = discord.Embed(title="#Joke", description=f"{question} \n\n **{punchline}**")
    except:
        print("Error occured while fetching joke")
        return ""
            
    return embed


@bot.event
async def on_ready():
    print(f"{bot.user} has logged in")

@slash.slash(name="ping", description="to ping the bot")
async def ping(ctx):
    await ctx.reply("Pong")


@slash.slash(name="jokes", description="to activate/deactivate stewie to post jokes")
async def jokes(ctx):
    i = 0
    await ctx.reply(embed=discord.Embed(description="**Here is your jokes pack**"))
    while i <= 10:
        embed = post_meme()
        if embed == "":
            print("Error")
            continue
        await ctx.send(embed=embed)
        i+=1
        time.sleep(5)
try:
    bot.run(token)
except:
    print("Some error occured")