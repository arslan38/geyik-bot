import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        em = discord.Embed(title='Yardım Komutu',
                           description = 'Daha fazla bilgi almak için g!help [komut] komutunu kullanabilirsin.')

        em.add_field(name='Bütün Komutlar',value = '```all```')
        em.add_field(name='Genel',value = '```anayasa,cena,kolpala```')
        #em.add_field(name='Müzik',value = 'play,skip,start,pause,loop,leave')
        em.add_field(name='Ramazan',value = '```ramazan,davul,ezan```')
        #em.add_field(name='YSK',value = 'oylama,anket')
        em.add_field(name='Yönetim',value = '```ban,kick,unban```')
        em.add_field(name='Sayaç',value = '```sayaç```')
        #em.add_field(name='Kayıt',value = 'kayıt-basla,kayıt-durdur')

        await ctx.send(embed = em)
    @help.command()
    async def all(self,ctx):
        await ctx.send("""```Genel:
   kolpala: g!kolpala
   anayasa: g!anayasa
   bayrak: g!bayrak
   cena: g!cena

Ramazan: 
   ramazan: g!ramazan <şehir adı>
   ezan: g!ezan
   davul: g!davul

Sayaç:
   sayaç: g!sayaç <süre> <mode>

Yönetim:
   kick: g!kick <kullanıcı>
   ban: g!ban <kullanıcı>
   unban: g!unban <kullanıcı>


Daha fazla bilgi almak için g!help [komut] komutunu kullanabilirsin.
  ```""")
    @help.command()
    async def kolpala(self,ctx):
        em = discord.Embed(title='Kolpala Komutu',
                           description = 'Bana kolpala de sana kim olduğumu söyleyeyim.')

        em.add_field(name='**Syntax**',value = '```g!kolpala```')
        await ctx.send(embed = em)
    @help.command()
    async def anayasa(self,ctx):
        em = discord.Embed(title='Anayasa Komutu',
                           description = 'Geyik Sunucu\'muzun anayasasını öğrenmek için kullanabilirsiniz')

        em.add_field(name='**Syntax**',value = '```g!anayasa```')
        await ctx.send(embed = em)        
    @help.command()
    async def bayrak(self,ctx):
        em = discord.Embed(title='Bayrak Komutu',
                           description = 'Geyik Sunucu\'muzun bayrağını öğrenmek için kullanabilirsiniz')

        em.add_field(name='**Syntax**',value = '```g!bayrak```')
        await ctx.send(embed = em)
    @help.command()
    async def cena(self,ctx):
        em = discord.Embed(title='Cena Komutu',
                           description = 'AND HIS NAME IS JOHN CENA!!!!!!')

        em.add_field(name='**Syntax**',value = '```g!cena```')
        await ctx.send(embed = em)
    #-------------------
    #-------------------
    @help.command()
    async def play(self,ctx):
        em = discord.Embed(title='Play Komutu',
                           description = '''Play komutunu kullanarak bir youtube videosu açabilirsiniz.
                           Hem sözlü olarak arama yaptırabilirsiniz hem de video linki girebilirsiniz.
                           Art arda yazılan şarkılar listeye eklenecektir.''')

        em.add_field(name='**Syntax**',value = '```g!play <şarkı adı>```')
        await ctx.send(embed = em)

    @help.command()
    async def skip(self,ctx):
        em = discord.Embed(title='Skip Komutu',
                           description = 'Skip komutunu sırada bulunan bir sonraki şarkıya geçebilirsiniz.')

        em.add_field(name='**Syntax**',value = '```g!skip```')
        await ctx.send(embed = em)
    #-------------------
    #-------------------
    @help.command()
    async def kick(self,ctx):
        em = discord.Embed(title='Kick Komutu',
                           description = 'Eğer bu kodu kullanacak kadar yetkili iseniz üyeleri geri gelebilecekleri şekilde serverdan atabilirsiniz.')

        em.add_field(name='**Syntax**',value = '```g!kick <kullanıcıadı>```')
        await ctx.send(embed = em)
    @help.command()
    async def ban(self,ctx):
        em = discord.Embed(title='Ban Komutu',
                           description = 'Eğer bu kodu kullanacak kadar yetkili iseniz üyeleri geri gelemeyecek şekilde serverdan atabilirsiniz.')

        em.add_field(name='**Syntax**',value = '```g!ban <kullanıcıadı>```')
        await ctx.send(embed = em)
    @help.command()
    async def unban(self,ctx):
        em = discord.Embed(title='Unban Komutu',
                           description = 'Eğer bu kodu kullanacak kadar yetkili iseniz üyelerin yasaklarını kaldırıp servera girmelerine izin verebilirsiniz.')

        em.add_field(name='**Syntax**',value = '```g!unban <kullanıcıadı>```')
        await ctx.send(embed = em)
    @help.command()
    #-------------------
    #-------------------
    async def ramazan(self,ctx):
        em = discord.Embed(title='Ramazan Komutu',
                           description = 'İftar ve sahura kaç dakika kaldığını görebilirsiniz.')

        em.add_field(name='**Syntax**',value = '```g!ramazan <şehir adı>```')
        await ctx.send(embed = em)
    @help.command()
    async def davul(self,ctx):
        em = discord.Embed(title='Davul Komutu',
                           description = 'Ramazan davulvusu geldi!!!')

        em.add_field(name='**Syntax**',value = '```g!davul```')
        await ctx.send(embed = em)
    @help.command()
    async def ezan(self,ctx):
        em = discord.Embed(title='Ezan Komutu',
                           description = 'Allah kabul etsin.')

        em.add_field(name='**Syntax**',value = '```g!ezan```')
        await ctx.send(embed = em)
    #-------------------
    #-------------------
    @help.command()
    async def sayaç(self,ctx):
        em = discord.Embed(title='Sayaç Komutu',
                           description = 'Canlı olarak geri sayım başlatabilirsiniz. Sayaç dolduğunda uyarılacaksınız.')

        em.add_field(name='**Syntax**',value = '```g!sayaç <süre(10m veya 1h gibi)> <mode(--s,--m)>```')
        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(Help(bot))
