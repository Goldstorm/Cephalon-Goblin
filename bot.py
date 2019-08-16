import asyncio
import os

from components.brain.goblinbrain import GoblinDataClass, GoblinBrain
from discord.ext import commands
from discord import File, errors
import random

brain = GoblinBrain()
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
    rand_file = random.randint(1, len(os.listdir(f"{brain.path}images/"))-1)
    rand_saying = random.randint(0, len(brain.goblin_says)-1)
    goblin_pics = f"{brain.path}images/{rand_file}.png"
    with open(goblin_pics, 'rb') as f:
        try:
            await bot.user.edit(avatar=f.read())
        except errors.HTTPException:
            await ctx.send("Discord hate it when my SHINY pic is changed twice every 15 minutes.")
        await ctx.send(brain.goblin_says[rand_saying])
    await asyncio.sleep(1)


@bot.command()
async def chance(ctx, category: str):
    """
    Use to get a random Frame and Weapon to use for the mission.
    """
    frame = await brain.oldFrame()
    weapon = await brain.oldWeapon()
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
            await area.send("Here's the build", file=File(f'{brain.path}images/build/build.png'))
        elif rage.lower() == "angrier":
            await area.send("I know we've been here before, did your brain stop working?",
                            file=File(f'{brain.path}images/build/build.png'))
        elif rage.lower() == "angriest":
            await area.send("You had your chance to actually use your eyes last time, here's a build just for you.",
                            file=File(f'{brain.path}images/build/build2.png'))
        elif rage is None:
            await asyncio.sleep(1)
        else:
            await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)


bot.run(brain.secrets['token'])
