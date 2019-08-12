import asyncio

from components.brain.goblinbrain import GoblinBrain
from components.warframe.equipment.parser import Parser
from discord.ext import commands
from discord import File
import random

brain = GoblinBrain()
parse = Parser()
bot = commands.Bot(command_prefix='!',
                   description='''You are dumb, you are sad, your bot run by GOBLIN! TAKE HIM OUT AND 
                   B̵̚͝E̴̚̕Ä̵̛T̵͛̕ ̴̽̚H̷̓̄I̶͆͠M̸̍͝''')


@bot.event
async def on_ready():
    print(f"You are dumb, you are sad, your bot run by {bot.user.name}!")
    print(bot.user.id)
    print('--------')


@bot.command()
async def change(ctx):
    """
    Change my profile picture.
    """
    rand_file = random.randint(1, 9)
    goblin_pics = './components/images/{}.png'.format(rand_file)
    with open(goblin_pics, 'rb') as f:
        await bot.user.edit(avatar=f.read())
    await ctx.send("This can be done every 30 minutes.")
    await asyncio.sleep(1)


@bot.command()
async def chance(ctx):
    """
    Use to get a random Frame and Weapon to use for the mission.
    """
    frame = await parse.oldFrame()
    weapon = await parse.oldWeapon()
    await ctx.send(frame)
    await asyncio.sleep(1)
    await ctx.send(weapon)
    await asyncio.sleep(1)


@bot.command()
async def build(ctx, rage: str):
    """
    Here's his damn Saryn build
    :param rage:
    :param ctx:
    """
    message = ctx.message
    area = message.channel
    if message.author.id == brain.andrew:
        if rage.lower() == "angry":
            await area.send("Here's the build", file=File('./components/images/build/build.png'))
        elif rage.lower() == "angrier":
            await area.send("We've been here before...", file=File('./components/images/build/build.png'))
        elif rage.lower() == "angriest":
            await area.send('You had your chance', file=File('./components/images/build/build2.png'))
        elif rage is None:
            await asyncio.sleep(1)
        else:
            await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)


bot.run(brain.secrets['token'])
