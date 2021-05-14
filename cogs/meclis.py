import discord
from discord.ext import commands
import asyncio
from datetime import datetime

class Meclis(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def oylama(self, ctx):
        Inputs = ctx.message.content[9:].split()
        timer = Inputs[0]
        convertTimeList = {'saniye':1,'s':1,'seconds':1, 'm':60,'dakika':60,'minutes':60, 'h':3600,'hours':3600,'saat':3600, 'day':86400,'gün':86400,'d':86400}
        time = int(timer[:-1]) * convertTimeList[timer[-1]]
        strx= ''
        for i in Inputs[1:]:strx += i+' '
        await ctx.message.delete()
        em = discord.Embed(title=f'Oylama Başlatılmıştır!',
                           timestamp = datetime.utcnow()
                           ,color = 0x21abcd)
        print(ctx.author.avatar)
        print(ctx.author.id)
        em.add_field(name=f'Konu: ',value=f'''`{strx}`

Takdirinize sunulur.''')
        if time//3600==0 and time%3600//60!=0 and time%60!=0:
            em.set_footer(text=f"""Süre: {time%3600//60} dakika {time%60} saniye""")
        elif time//3600==0 and time%3600//60==0 and time%60!=0:
            em.set_footer(text=f"""Süre: {time%60} saniye""")
        else:
            em.set_footer(text=f"""Süre: {time//3600} saat {time%3600//60} dakika {time%60} saniye""")
        
        em.set_thumbnail(url=ctx.author.avatar)
        em.set_author(name=f'{ctx.message.author}')
            
        msg = await ctx.send(embed = em)
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')
        await asyncio.sleep(time)
        
        message = await self.bot.get_channel(msg.channel.id).fetch_message(msg.id)
        most_voted = max(message.reactions , key = lambda r:r.count)
        min_voted = min(message.reactions , key = lambda r:r.count)
        
        await msg.delete()
        if min_voted.count==most_voted.count:
            em2 = discord.Embed(title=f'Oylama Bitmiştir!',color = 0x336dc4)
            em2.add_field(name=f'Konu:',value=f''' `{strx}`

    **Sonuç:**
    ✅ Evet : {most_voted.count}
    ❌ Hayır : {min_voted.count}

    Dosluk kazandı:)''')
            em2.set_thumbnail(url=ctx.author.avatar)
            em2.set_author(name=f'{ctx.message.author}')
        elif most_voted.emoji=='✅':
            em2 = discord.Embed(title=f'Oylama Bitmiştir!',color = 0x16db4b)
            em2.add_field(name=f'Konu:',value=f''' `{strx}`

    **Sonuç:**
    ✅ Evet : {most_voted.count}
    ❌ Hayır : {min_voted.count}

    Kabul edilmiştir. ✅ ''')
            em2.set_thumbnail(url=ctx.author.avatar)
            em2.set_author(name=f'{ctx.message.author}')
        elif most_voted.emoji=='❌':
            em2 = discord.Embed(title=f'Oylama Bitmiştir!',color = 0xc44233)
            em2.add_field(name=f'Konu:',value=f''' `{strx}`

    **Sonuç:**
    ✅ Evet : {min_voted.count}
    ❌ Hayır : {most_voted.count}

    Kabul edilmemiştir. ❌ ''')
            em2.set_thumbnail(url=ctx.author.avatar)
            em2.set_author(name=f'{ctx.message.author}')
        
        await ctx.send(f'{ctx.message.author.mention} oylama bitti!')
        await ctx.send(embed = em2)

        
def setup(bot):
    bot.add_cog(Meclis(bot))
