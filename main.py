import discord
from discord.ext import commands,tasks
from discord.errors import Forbidden
import os
import http.client
import datetime
import re

intents = discord.Intents.all()
Bot = commands.Bot(command_prefix='g!',intents=intents)
Bot.remove_command('help')

#Token = open('token.txt','r').read()

@Bot.event
async def on_ready():
    #oto_mesaj.start() #oto mesaj
    await Bot.change_presence(activity=discord.Game(name='g!help'))
    print('Kolpaya Hazırım!')
"""
bannedWords = ['kes','1000dolars','1000 dolars','fuck','siktir','yarrak','sik','am','amcık','sikerim','amına']

def msg_contains_word(msg,word):
    return re.search(fr'\b({word})\b',msg) is not None

@Bot.event
async def on_message(message):
    messageAuthor = message.author

    if bannedWords != None and (isinstance(message.channel,discord.channel.DMChannel)==False):
        for bannedWord in bannedWords:
            if msg_contains_word(message.content.lower(),bannedWord):
                await message.delete()
                await message.channel.send(f'{messageAuthor.mention} yasaklı kelime kullandınız!')
"""

@Bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            em = discord.Embed(title='GEYİK BOTU',
                            description= 'Geyik Server\'ı için özel olarak tasarlandım.')
            em.set_image(url="attachment://images//geyik.png")
            em.add_field(name='Geyik Botu kimdir?',value = 'burak tarafından yaratıldım.')
            em.add_field(name='Help',value = 'g!help komutunu kullanarak benim hakkımda her şeyi öğrenebilirsin.')
            em.add_field(name='Aktiflik',value = 'Şu anda **3** sunucuda aktifim.')
            em.add_field(name='Prefix',value = 'g!')
            await channel.send(embed = em)

@tasks.loop(hours=24)
async def oto_mesaj():
    for channel in Bot.get_all_channels():
        if channel.id == 813080714747969549:
            await channel.send('Kolpaya Gelin!')
#------------------------------------------------------------------

#------------------------------------------------------------------
@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels,name = '👋hoşgeldin')
    await channel.send(f"Sa {member.mention}, :deer:GEYİK:deer: Server'ına Hoşgeldin. Kolpalamaya hazır ol.")

@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels,name = '👋hoşgeldin')
    await channel.send(f"{member} ayrıldı:( Umarım geri gelirsin kardeş.")
#------------------------------------------------------------------

#------------------------------------------------------------------
'''
@Bot.event
async def on_message(message):
    bad_words=['nigger','kes']
    for badword in bad_words:
        if badword in message.content.lower():
            await message.delete()
            await message.channel.send(f'{message.author.mention} yasaklı kelime yazdığı için 10 dakika ban yemiştir.')
'''

@Bot.command()
async def cena(ctx, url='https://www.youtube.com/watch?v=2D-ZO2rGcSA&ab_channel=GamingSoundFX'):
    try:

        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            
        await channel.connect()
        voice = discord.utils.get(Bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("sounds\\cena.mp3"))
    except:
        await ctx.send(f'{ctx.author.mention} bütün Server\'a anons yapmamı mı istiyorsun? Önce bir sesli sohbet kanalına gir!')


@Bot.command()
async def davul(ctx, url='https://www.youtube.com/watch?v=2D-ZO2rGcSA&ab_channel=GamingSoundFX'):
    try:
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
        await channel.connect()
        voice = discord.utils.get(Bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("sounds\\davul.mp3"))
    except:
        await ctx.send(f'{ctx.author.mention} bütün Server\'a anons yapmamı mı istiyorsun? Önce bir sesli sohbet kanalına gir!')


@Bot.command()
async def ezan(ctx, url='https://www.youtube.com/watch?v=2D-ZO2rGcSA&ab_channel=GamingSoundFX'):
    try:
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
        await channel.connect()
        voice = discord.utils.get(Bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio("sounds\\ezan.mp3"))
    except:
        await ctx.send(f'{ctx.author.mention} bütün Server\'a anons yapmamı mı istiyorsun? Önce bir sesli sohbet kanalına gir!')

#------------------------------------------------------------------

#------------------------------------------------------------------
@Bot.command()
@commands.has_role('burak')
async def load(ctx,extension):
    Bot.load_extension(f'cogs.{extension}')

@Bot.command()
@commands.has_role('burak')
async def unload(ctx,extension):
    Bot.unload_extension(f'cogs.{extension}')

@Bot.command()
@commands.has_role('burak')
async def reload(ctx,extension):
    Bot.unload_extension(f'cogs.{extension}')
    Bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        Bot.load_extension(f'cogs.{filename[:-3]}')
#------------------------------------------------------------------

#------------------------------------------------------------------
TOKEN = open('TOKEN.txt','r').read()
Bot.run(TOKEN)
