#!/bin/python3

import discord
from os import getenv
from discord.ext import commands
from sys import stdout

TOKEN = getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

def log(st):
	if st:
		print(st)
		stdout.flush()

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="Henlo!"))
	log(f'{bot.user} has connected to Discord!')

@bot.listen('on_message')
async def on_message(message):

	if message.author.id==bot.application_id:
		return

	link, pre_fix=identify_link(message.content)
	log(link)
	if link:
		await message.channel.send(f'Enviado por: <@{message.author.id}> \n{str(message.content).lower().replace(link, pre_fix+link)}')
		await message.delete()


def identify_link(msg):
    if '/instagram.com/reels' in msg.lower() or 'www.instagram.com/reels' in msg.lower():
        return 'instagram', 'dd'
    elif '/twitter.com/' in msg.lower() or 'www.twitter.com/' in msg.lower():
        return 'twitter', 'vx'
    elif '/tiktok.com/' in msg.lower() or 'www.tiktok.com/' in msg.lower():
        return 'tiktok', 'vx'
    else:
        return False, False

bot.run(TOKEN)
