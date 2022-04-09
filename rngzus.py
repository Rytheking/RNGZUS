import os
import random
import discord
import time
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')
channel_id=945685026207584279

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


@bot.command(name='rngzus', help='takes a comma sepearted list of users and will choose 1 to win a give away')
async def give_away(ctx, timedelay: int):
    response="react to this message"
    message = await ctx.send(response)
    message_id=message.id
    users = []
    time.sleep(timedelay)
    message = await ctx.fetch_message(message_id)
    for reaction in message.reactions:
        async for user in reaction.users():
            users.append(user)
    response = random.choice(users).name
    await ctx.send('@'+str(response))

bot.run(TOKEN)