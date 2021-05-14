import discord
from discord.ext import commands
import asyncio 
import random

class Game(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def superloto(self, ctx):
        strx = ''
        true_values = []
        sayaç_values = []
        girdi_values = []
        sayaç = 0
        #kolon = int(input('Kaç kolon gireceksiniz: '))
        Inputs = list(map(int,ctx.message.content[12:].split()))
        print(Inputs)
        girdi_values = Inputs
        for i in range(6):
            RANDOM = random.randrange(60)
            strx += str(RANDOM).zfill(2)+' '
            true_values.append(RANDOM)

        resultStr = ''
        resultStr+= '-'*20+'\n'
        resultStr+= strx+ '   BÜYÜK İKRAMİYE\n'
        #resultStr+= '-'*20+'\n'
        print(f'{resultStr}')
        await ctx.send(f'```{resultStr}```')
        
        sayac=0
        print(true_values)
        for i in range(6):
            print(int(girdi_values[i]))
            if int(girdi_values[i]) in true_values:
                sayac+=1
        

        print(sayac)
        if sayac == 6 : await ctx.send(f'{ctx.message.author.mention} Tebrikler büyük ikramiyeyi kazandınız!!\n')
        if sayac == 5 : await ctx.send(f'{ctx.message.author.mention} Tebrikler amorti kazandın!!\n')
        if sayac == 0 : await ctx.send(f'{ctx.message.author.mention} ne cenabet adamsın bir tane bile tutmadı!\n')
        if sayac == 4 : await ctx.send(f'{ctx.message.author.mention} 4 değer tutturdun!!\n')
        if sayac == 3 : await ctx.send(f'{ctx.message.author.mention} 3 değer tutturdun!!\n')
        if sayac == 2 : await ctx.send(f'{ctx.message.author.mention} 2 değer tutturdun!!\n')
        if sayac == 1 : await ctx.send(f'{ctx.message.author.mention} 1 değer tutturdun!!\n')
        
def setup(bot):
    bot.add_cog(Game(bot))            
