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


def pick(list): return random.choices(list)[0]

def sanitize(word):
    return word.strip().lower().encode('ascii', 'ignore').decode('unicode_escape')

adjectives = [
    "blathering",
    "filthy",
    "massive",
    "unholy",
    "buttnaked",
    "cattywampus",
    "bloviating",
    "disgusting",
    "contemptable",
    "vile",
    "smelly",
    "buttlicking",
    "shitfilled",
    "satanic",
    "reptilian",
    "foul",
    "repugnant",
    "inarticulate",
    "vapid",
    "maimed",
    "vacuous",
    "grotesque",
    "gangling",
    "cloddish",
    "petty",
]

nouns = [
    "piece of shit",
    "slice of cheese",
    "walrus",
    "chicken fucker",
    "turkey leg of a person",
    "bumfuzzle",
    "lollygag",
    "diddle daddler",
    "santorum",
    "pelvic floor",
    "ignoramus",
    "invalid",
    "oaf",
    "earlobe",
    "buttfumbler",
]

shakespeare_adjectives_1 = [
    "artless",
    "bawdy",
    "beslubbering",
    "bootless",
    "churlish",
    "cockered",
    "clouted",
    "craven",
    "currish",
    "dankish",
    "dissembling",
    "droning",
    "errant",
    "fawning",
    "fobbing",
    "froward",
    "frothy",
    "gleeking",
    "goatish",
    "gorbellied",
    "impertinent",
    "infectious",
    "jarring",
    "loggerheaded",
    "lumpish",
    "mammering",
    "mangled",
    "mewling",
    "paunchy",
    "pribbling",
    "puking",
    "puny",
    "qualling",
    "rank",
    "reeky",
    "roguish",
    "ruttish",
    "saucy",
    "spleeny",
    "spongy",
    "surly",
    "tottering",
    "unmuzzled",
    "vain",
    "venomed",
    "villainous",
    "warped",
    "wayward",
    "weedy",
    "yeasty",
]

shakespeare_adjectives_2 = [
    "base-court",
    "bat-fowling",
    "beef-witted",
    "beetle-headed",
    "boil-brained",
    "clapper-clawed",
    "clay-brained",
    "common-kissing",
    "crook-pated",
    "dismal-dreaming",
    "dizzy-eyed",
    "doghearted",
    "dread-bolted",
    "earth-vexing",
    "elf-skinned",
    "fat-kidneyed",
    "fen-sucked",
    "flap-mouthed",
    "fly-bitten",
    "folly-fallen",
    "fool-born",
    "full-gorged",
    "guts-griping",
    "half-faced",
    "hasty-witted",
    "hedge-born",
    "hell-hated",
    "idle-headed",
    "ill-breeding",
    "ill-nurtured",
    "knotty-pated",
    "milk-livered",
    "motley-minded",
    "onion-eyed",
    "plume-plucked",
    "pottle-deep",
    "pox-marked",
    "reeling-ripe",
    "rough-hewn",
    "rude-growing",
    "rump-fed",
    "shard-borne",
    "sheep-biting",
    "spur-galled",
    "swag-bellied",
    "tardy-gaited",
    "tickle-brained",
    "toad-spotted",
    "unchin-snouted",
    "weather-bitten",
]

shakespeare_nouns = [
    "apple-john",
    "baggage",
    "barnacle",
    "bladder",
    "boar-pig",
    "bugbear",
    "bum-bailey",
    "canker-blossom",
    "clack-dish",
    "clotpole",
    "coxcomb",
    "codpiece",
    "death-token",
    "dewberry",
    "flap-dragon",
    "flax-wench",
    "flirt-gill",
    "foot-licker",
    "fustilarian",
    "giglet",
    "gudgeon",
    "haggard",
    "harpy",
    "hedge-pig",
    "horn-beast",
    "hugger-mugger",
    "joithead",
    "lewdster",
    "lout",
    "maggot-pie",
    "malt-worm",
    "mammet",
    "measle",
    "minnow",
    "miscreant",
    "moldwarp",
    "mumble-news",
    "nut-hook",
    "pigeon-egg",
    "pignut",
    "puttock",
    "pumpion",
    "ratsbane",
    "scut",
    "skainsmate",
    "strumpet",
    "varlot",
    "vassal",
    "whey-face",
    "wagtail",
]

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user.name} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@bot.command(name='insult', help='Creates an insult directed at a given target')
async def on_message(ctx, *args):
    if len(args) == 0:
        await ctx.send('Type the name of the person you would like me to insult after !insult')
    else:
        full_msg = ' '.join(args)
        split_msg = full_msg.split('.')
        target = split_msg[0]
        if 'bully' in sanitize(target) and 'bot' in sanitize(target) or 'buiiy' in sanitize(target):
            author=ctx.message.author.display_name
            await ctx.send(f'Fuck off {author}, I am not going to insult myself')
            target = author
        insults = [
            f"{target}'s mother was a hamster and their father smelled of elderberries",
            f"{target} is the kind of person that leaves their shopping cart loose in the parking lot",
            f"{target} is actually quite smart but they never apply themselves, so they will always be a shadow of who they could have been",
            f"{target} doesn't have the common decency to use turn signals",
            f"{target} is dumber than snake mittens",
            f"{target} is a sloppy drunk",
            f"{target} failed Psych 101 in college",
            f"{target} was not the favorite child in their household",
            f"If {target} was a spice, they'd be flour",
            f"{target} thought Atlas Shrugged was an interesting story",
            f"{target} fully believed the earth was flat well into their teens",
            f"{target} chews with their mouth open",
            f"{target} thinks they shit don't stank, but it do",
            f"{target} wipes their ass from back to front",
            f"{target}'s favorite comedian is Jeff Dunham",
            "Walruses can't feel love",
            f"{target} smells mildly of cheese",
            f"{target} never uses their goddamn turn signal",
            f"{target} is the Ringo Star of this friend group",
            f"{target}'s pee is dark yellow cuz they never drink water",
            f"{target} once tried to fart in someone's general direction as a prank, but they full on shat themselves and played it off like nothing happened.",
            f"{target}'s ringtone is Womanizer by Britney Spears",
            f"{target} prefers their french fries reheated",
            f"{target} wonders when Tupac is going to make his comeback",
            f"{target} rolls down their windows and blasts their music because they think they have cool taste and want validation from strangers",
            f"To be honest, I just fucking hate {target}",
            f"{target} thinks Aunt Jemima is better than Mrs Butterworth's",
            f"{target} is probably a baby rapist",
            f"{target} falls asleep to scat porn because it calms their nerves",
            f"{target} has never seen their butthole in person",
            f"{target} probably hasn't gone outside today",
            f"{target} is a lying dog-faced pony soldier",
            f"{target} types with just two fingers",
            f"{target} sucks ass",
            f"{target} pours their milk before their cereal",
            f"{target}'s favorite cereal is chex",
            f"{target} comes from the wrong nut",
            f"{target} asks fat women when they're due",
            f"{target} pretends to have forgotten their wallet, but really they just don't want to pay.",
            f"{target} talks loudly on the phone in the metro",
            f"{target} farts in elevators just before they leave",
            f"{target} likes to sing along with songs, but they are completely tone deaf",
            f"{target} talks about you behind your back",
            f"{target} lets the water run, but doesn't actually wash their hands",
            f"{target} spits when they talk",
            f"{target} is secretly attracted to the mom from Rolie Polie Olie",
            f"{target} sucks ass at foosball. Challenge me, pussy.  You don't stand a fucking chance.",
            f"{target} always showers right before they shit",
            f"{target} has small genitals. "*32,
            f"Fuck you. "*100,
            f"Fuck you {target}.",
            f"{target} is the most {pick(adjectives)} {pick(adjectives)} {pick(nouns)} I have ever known",
            f"{target} is a {pick(adjectives)} {pick(adjectives)} {pick(adjectives)} {pick(adjectives)} {pick(adjectives)} {pick(nouns)}",
            f"{target} is analogous to a {pick(nouns)}",
            f"The best way I can describe {target} is {pick(adjectives)}",
            f"{target} has a {pick(adjectives)} butthole",
            f"{target} can lick my {pick(adjectives)} ass",
            f"{target} looks like a {pick(adjectives)} {pick(nouns)} trying to pass as a {pick(adjectives)} {pick(nouns)}",
            f"If you think about it, {target} shares many character traits with Baron Harkonnen from Dune",
            f"{target} insists it is not weird for them to watch childrens TV shows because 'it's for all ages!'",
            f"{target} is never sure if is it okay for them to say gracias at a mexican restaurant",
            f"{target} over-pronounces foreign words",
            f"{target} likes doing jigsaw puzzles",
            f"{target} would go to a charity event just to make an appearance, grab a snack, and leave without actually doing anything",
            f"{target} asks people crying in public to keep it down",
            f"{target} texts in a movie theater during the movie",
            f"{target} will puke in the sink, even if a toilet or garbage can is available",
            f"{target}'s favorite beer is Miller High Life",
            f"{target} probably watches Sick Animations",
            f"{target} looks like the Globglogabgalab",
            f"{target} spends their weekends volunteering at a soup kitchen. Not because it's a good thing to do, but because they are unlikeable and no one cares about them enough to spend time with them",
            f"{target} is ashamed of their porn habits",
            f"{target} makes references no one understands",
            f"{target} needs to get their shit together. Get it all together. And put it in a backpack. All your shit. So it's together. And if you gotta take it somewhere, take it somewhere, you know, take it to the shit store and sell it... Or put it in a shit museum, I don't care what you do, you just gotta get it together. Get your shit together.",
            f"{target} is afraid of gnomes",
        ]
        response = pick(insults)
        await ctx.send(response)


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
            guild.categories, name='Bullying')

        if not existing_channel:
            # create a new channel
            positive_responses = [
                f"Oh yeah, it's time to bully {victim}",
                f"Good choice, {victim} is due for a bullying",
                f"You're right, {victim} was getting too uppity",
                f"{victim} needs to be taken down a notch",
                f"{victim}!, I hate that guy",
                f"Okay, I'm going to open a channel to bully {victim}. Don't be too harsh, {victim} is a delicate flower",
            ]
            response = pick(positive_responses)
            print(
                f'Creating a new channel for the purpose of bullying {victim}.')

            await guild.create_text_channel(channel_name, category=bullying_category)

        else:
            # make a sassy remark about how there is already a channel for this victim
            negative_responses = [
                f"If you want to bully {victim}, there is already a channel for that",
                f"Hey now, we already have a channel for bullying {victim}",
                f"I would appreciate it if you looked to see if there was a channel for bullying {victim} before you ask me to make one",
            ]
            response = pick(negative_responses)
        await ctx.send(response)

@bot.command(name='spurn', help='Creates a Shakespearean insult directed at a given target')
async def on_message(ctx, *args):
    if len(args) == 0:
        await ctx.send('Type the name of the person you would like me to insult with Shakespearean flair after !spurn')
    else:
        full_msg = ' '.join(args)
        split_msg = full_msg.split('.')
        target = split_msg[0]
        if 'bully' in sanitize(target) and 'bot' in sanitize(target) or 'buiiy' in sanitize(target):
            author=ctx.message.author.display_name
            await ctx.send(f'Fuck off {author}, I am not going to insult myself')
            target = author
        response = f"{target}, thou art a {pick(shakespeare_adjectives_1)}, {pick(shakespeare_adjectives_2)} {pick(shakespeare_nouns)}"
        await ctx.send(response)
bot.run(TOKEN)
