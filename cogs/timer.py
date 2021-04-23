import discord
from discord.ext import commands
import asyncio 

class Timer(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def sayaç(self, ctx, timeInput,timeInput2='0s',mode='--m',):
        time=0
        try:
            try:
                time = int(timeInput)
            except:
                convertTimeList = {'saniye':1,'s':1,'seconds':1, 'm':60,'dakika':60,'minutes':60, 'h':3600,'hours':3600,'saat':3600, 'day':86400,'gün':86400,'d':86400}
                for timer in [timeInput,timeInput2]:
                    time += int(timer[:-1]) * convertTimeList[timer[-1]]
                if convertTimeList[timeInput[-1]]==1:mode=='--s'
            await ctx.send(f"{ctx.author.mention} Sayaç başladı, tik tak...")
            await ctx.message.delete()
            if time > 86400:
                await ctx.send("Maalesef 1 günden fazlasını saymayı bilmiyorum.")
                return
            if time <= 0:
                await ctx.send("Negatif zaman mı olur pezevenk :/")
                return
            if time >= 3600:
                if mode=='--s':message = await ctx.send(f"```Sayaç: {time//3600} saat {time%3600//60} dakika {time%60} saniye```")
                elif mode=='--m':message = await ctx.send(f"```Sayaç: {time//3600} saat {time%3600//60} dakika```")
            elif time >= 60:
                if mode=='--s':message = await ctx.send(f"```Sayaç: {time//60} dakika {time%60} saniye```")
                elif mode=='--m':message = await ctx.send(f"```Sayaç: {time//60} dakika {time%60} saniye```")
            elif time < 60:
                message = await ctx.send(f"Sayaç: {time} saniye")
            while True:
                if mode=='--s':
                    try:
                        await asyncio.sleep(1)
                    except:
                        print('wtf')
                    time -= 1
                elif mode=='--m':
                    try:
                        await asyncio.sleep(60)
                    except:
                        print('wtf')
                    time -= 60
                    
                if time >= 3600:
                    if mode=='--s':await message.edit(content=f"```Sayaç: {time//3600} saat {time %3600//60} dakika {time%60} saniye```")
                    elif mode=='--m':await message.edit(content=f"```Sayaç: {time//3600} saat {time %3600//60} dakika```")
                elif time >= 60:
                    if mode=='--s':await message.edit(content=f"```Sayaç: {time//60} dakika {time%60} saniye```")
                    elif mode=='--m':await message.edit(content=f"```Sayaç: {time//60} dakika```")
                elif time < 60:
                    await message.edit(content=f"```Sayaç: {time} saniye```")
                if time <= 0:
                    await message.edit(content="Finito!")
                    await ctx.send(f"{ctx.author.mention} Ders kolpası bitti! Mola vakti.")
                    break

        except:
            await ctx.send(f"""Önce düzgün gir üstad. Misal, **g!sayaç 10m 15s**
Aynı anda 3 parametre girmeyin(1h 15m 15s **çalışmaz**)
Eğer **--s** modunu kullanmak istiyorsanız 10m 0s gibi ikili girdi verin.""")



def setup(bot):
    bot.add_cog(Timer(bot))
