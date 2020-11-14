#!/usr/bin/env python3
# bullyBot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user.name} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@bot.command(name='bully', help='Creates a new channel for bullying a new member')
async def on_message(ctx, *args):

    # if args is len is 0 you want to deliever help dialog, otherwise you want to grab the first arg as victim
    print(args)
    if len(args) == 0:
        await ctx.send('Type the name of the person you want to bully after !bully')
    else:
        victim = args[0]

        victim = victim.lower().strip()
        channel_name = f'making-fun-of-{victim}'
        guild = ctx.guild
        # look to see if there is already a channel for this victim
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        bullying_category = discord.utils.get(
            guild.categories, name='bullying')

        if not existing_channel:
            # create a new channel
            positive_responses = [
                f"Oh yeah, it's time to bully {victim}",
                f"Good choice, {victim} is due for a bullying",
                f"You're right, {victim} was getting too uppity",
                f"{victim} needs to be taken down a notch",
                f"{victim}!, I hate that guy"
                f"Okay, I'm going to open a channel to bully {victim}. Don't be too harsh, {victim} is a delicate flower"
            ]
            response = random.choices(positive_responses)[0]
            print(
                f'Creating a new channel for the purpose of bullying {victim}.')

            await guild.create_text_channel(channel_name, category=bullying_category)

        else:
            # make a sassy remark about how there is already a channel for this victim
            negative_responses = [
                f"If you want to bully {victim}, there is already a channel for that",
                f"Hey now, we already have a channel for bullying {victim}",
                f"I would appreciate it if you looked to see if there was a channel for bullying {victim} before you ask me to make one"
            ]
            response = random.choices(negative_responses)[0]

        await ctx.send(response)

bot.run(TOKEN)
