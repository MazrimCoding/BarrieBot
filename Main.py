
import os
import random

import discord
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    Barrie_quotes = [
        'Ah fuck I spilled water on the hob',
        '<:Barriebot:268101141621899264>',
        'Games in plat1/2 are actually good'
    ]

    memes = [
        'meme1.png',
        'meme2.png',
        'meme3.png',
        'meme4.png',
        'meme5.png',
        'meme6.png',
        'meme7.png',
        'meme8.png',
        'meme9.png',
        'meme10.png',
        'meme11.png',
        'meme12.png'
    ]

    if message.content == '!barriebot':
        response = random.choice(Barrie_quotes)
        await message.channel.send(response)

    if message.content == 'blanket':
        await message.channel.send(file=discord.File('barrie.png'))

    if message.content == '!apex':
        await message.channel.send(file=discord.File('Apex.png'))

    if message.content == '!notracist':
        await message.channel.send(file=discord.File('notracist.png'))

    if message.content == 'meme':
        response2 = random.choice(memes)
        await message.channel.send(file=discord.File(response2))




client.run(TOKEN)

