#bullyBot.py
import os
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
    
    #if args is len is 0 you want to deliever help dialog, otherwise you want to grab the first arg as victim
    print(args)
    if len(args) == 0:
        await ctx.send('Type the name of the person you want to bully after !bully')
    else:
        victim = args[0]

        victim=victim.lower().strip()
        channel_name=f'making-fun-of-{victim}'
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        bullying_category = discord.utils.get(guild.categories, name='bullying')

        if not existing_channel:
            response = f'Good choice, {victim} is due for a bullying'
            #print(f'Creating a new channel for the purpose of bullying {victim}.')
            await guild.create_text_channel(channel_name, category=bullying_category)

        else:
            response = f'Hey now, we already have a channel for bullying {victim}'

        await ctx.send(response)

bot.run(TOKEN)