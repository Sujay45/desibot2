import discord 
import youtube_dl
from discord.ext import commands
import asyncio

token = 'NTEwOTEyMTE0NzczMzI3OTA5.DsjP7w.8uoYn20dQGRh4X-XufV_Ax3OopA'
client = discord.Client()
client = commands.Bot(command_prefix='?')
players = {}

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='im coming sooon!'))
	print('This Bot Is Ready.')
	
@client.command()
async def GG():
	await client.say('Good Game')
	
@client.command(pass_context=True)
async def join(ctx):
	
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)
	
	
@client.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	await voice_client.disconnect()
	
@client.command(pass_context=True)
async def play(ctx, url):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = await voice_client.create_ytdl_player(url)
	players[server.id] = player
	player.start()

client.run(token)