import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        em = discord.Embed(title='Yardım Komutu',color =0x008000)
        em.add_field(name='Bütün Komutlar',value = """Genel:
   kolpala: `g!kolpala`
   anayasa: `g!anayasa`
   bayrak: `g!bayrak`
   cena: `g!cena`

Ramazan: 
   ramazan: `g!ramazan <şehir adı>`
   ezan: `g!ezan`
   davul: `g!davul`

Sayaç:
   sayaç: `g!sayaç <süre> <mode>`

Müzik:
    play: `g!play <şarkı linki ve ya adı>`
    skip: `g!skip`
    queue: `g!queue`
    repeat: `g!repeat <1 veya all>`
    pause: `g!pause`
    stop: `g!stop`
    shuffle: `g!shuffle`
    previous: `g!previous`
    connect: `g!connect <kanal adı(opsiyonel)>`
    disconnect: `g!disconnect`
    
Yönetim:
   kick: `g!kick <kullanıcı>`
   ban: `g!ban <kullanıcı>`
   unban: `g!unban <kullanıcı>`

Fonksiyonel:
   korona: `g!korona`
   sondakika: `g!sondakika` veya `g!sondakika korona`
   havadurumu: `g!havadurumu`
   imdb: `g!imdb <film veya dizi adı>`
   wikipedia: `g!wikipedia <word>`

Oyun:
    superloto: `g!superloto`

Meclis:
    oylama: `g!oylama <zaman(12m gibi)> <konu>`
    
Futbol:
   premierlig: `g!premierlig`
   superlig: `g!superlig`
   fikstur: `g!fikstur <superlig veya premierlig>`

""")
        em.set_footer(text='Daha fazla bilgi almak için g!help [komut] komutunu kullanabilirsin.')
        await ctx.send(embed = em)

    @help.command()
    async def kolpala(self,ctx):
        em = discord.Embed(title='Kolpala Komutu',
                           description = 'Bana kolpala de sana kim olduğumu söyleyeyim.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!kolpala```')
        await ctx.send(embed = em)
        
    @help.command()
    async def anayasa(self,ctx):
        em = discord.Embed(title='Anayasa Komutu',
                           description = 'Geyik Sunucu\'muzun anayasasını öğrenmek için kullanabilirsiniz',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!anayasa```')
        await ctx.send(embed = em)
        
    @help.command()
    async def bayrak(self,ctx):
        em = discord.Embed(title='Bayrak Komutu',
                           description = 'Geyik Sunucu\'muzun bayrağını öğrenmek için kullanabilirsiniz',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!bayrak```')
        await ctx.send(embed = em)
        
    @help.command()
    async def cena(self,ctx):
        em = discord.Embed(title='Cena Komutu',
                           description = 'AND HIS NAME IS JOHN CENA!!!!!!',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!cena```')
        await ctx.send(embed = em)
    #-------------------
    #-------------------
    @help.command()
    async def play(self,ctx):
        em = discord.Embed(title='Play Komutu',
                           description = '''Play komutunu kullanarak bir youtube videosu açabilirsiniz.
                           Hem sözlü olarak arama yaptırabilirsiniz hem de video linki girebilirsiniz.
                           Art arda yazılan şarkılar listeye eklenecektir.''',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!play <şarkı adı>```')
        await ctx.send(embed = em)

    @help.command()
    async def skip(self,ctx):
        em = discord.Embed(title='Skip Komutu',
                           description = 'Skip komutunu sırada bulunan bir sonraki şarkıya geçebilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!skip```')
        await ctx.send(embed = em)
    #-------------------
    #-------------------
    @help.command()
    async def kick(self,ctx):
        em = discord.Embed(title='Kick Komutu',
                           description = 'Eğer bu kodu kullanacak kadar yetkili iseniz üyeleri geri gelebilecekleri şekilde serverdan atabilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!kick <kullanıcıadı>```')
        await ctx.send(embed = em)
    @help.command()
    async def ban(self,ctx):
        em = discord.Embed(title='Ban Komutu',
                           description = 'Eğer bu kodu kullanacak kadar yetkili iseniz üyeleri geri gelemeyecek şekilde serverdan atabilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!ban <kullanıcıadı>```')
        await ctx.send(embed = em)
    @help.command()
    async def unban(self,ctx):
        em = discord.Embed(title='Unban Komutu',
                           description = 'Eğer bu kodu kullanacak kadar yetkili iseniz üyelerin yasaklarını kaldırıp servera girmelerine izin verebilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!unban <kullanıcıadı>```')
        await ctx.send(embed = em)
    @help.command()
    #-------------------
    #-------------------
    async def ramazan(self,ctx):
        em = discord.Embed(title='Ramazan Komutu',
                           description = 'İftar ve sahura kaç dakika kaldığını görebilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!ramazan <şehir adı>```')
        await ctx.send(embed = em)
    @help.command()
    async def davul(self,ctx):
        em = discord.Embed(title='Davul Komutu',
                           description = 'Ramazan davulvusu geldi!!!',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!davul```')
        await ctx.send(embed = em)
    @help.command()
    async def ezan(self,ctx):
        em = discord.Embed(title='Ezan Komutu',
                           description = 'Allah kabul etsin.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!ezan```')
        await ctx.send(embed = em)
    #-------------------
    #-------------------
    @help.command()
    async def sayaç(self,ctx):
        em = discord.Embed(title='Sayaç Komutu',
                           description = 'Canlı olarak geri sayım başlatabilirsiniz. Sayaç dolduğunda uyarılacaksınız.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!sayaç <süre(10h 10m gibi)>```')
        await ctx.send(embed = em)
    #-------------------
    #-------------------
    @help.command()
    async def sondakika(self,ctx):
        em = discord.Embed(title='Sondakika Komutu',
                           description = 'Çeşitli kaynaklardan 7 adet son dakika haberine ulaşabilirsiniz. Korona eki ile NTV Sağlıktan son dakika korona haberlerine ulaşabilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!sondakika or g!sondakika korona```')
        await ctx.send(embed = em)

    @help.command()
    async def korona(self,ctx):
        em = discord.Embed(title='Korona Komutu',
                           description = 'Türkiye için günlük korona verilerine ulaşabilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!korona```')
        await ctx.send(embed = em)

    @help.command()
    async def havadurumu(self,ctx):
        em = discord.Embed(title='Hava Durumu Komutu',
                description = 'İstenilen şehir için haftalık hava durumu verilerine ulaşabilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!havadurumu <şehir>```')
        await ctx.send(embed = em)
    @help.command()
    async def imdb(self,ctx):
        em = discord.Embed(title='IMDB Komutu',
                description = 'İstenilen film veya dizinin bütün verilerine ulaşabilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!imdb <film veya dizi adı>```')
        await ctx.send(embed = em)
    @help.command()
    async def wikipedia(self,ctx):
        em = discord.Embed(title='Wikipedia Komutu',
                description = 'Wikipedia\'dan istediğiniz aramayı İngilizce olarak yapabilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!wikipedia <aranacak ingilizce kelime>```')
        await ctx.send(embed = em)
    #-------------------
    #-------------------
    @help.command()
    async def premierlig(self,ctx):
        em = discord.Embed(title='Premier Lig Komutu',
                           description = 'Premier Ligdeki son durumu görebilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!premierlig```')
        await ctx.send(embed = em)
    @help.command()
    async def superlig(self,ctx):
        em = discord.Embed(title='Super Lig Komutu',
                           description = 'Super Ligdeki son durumu görebilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!superlig```')
        await ctx.send(embed = em)

    @help.command(aliases = ['fikstür'])
    async def fikstur(self,ctx):
        em = discord.Embed(title='Fikstür Komutu',
                           description = 'Super Ligdeki ve Premier Ligdeki güncel maçları görebilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!fikstur <superlig veya premierlig>` `')
        await ctx.send(embed = em)
    #-------------------
    #-------------------
    @help.command()
    async def superloto(self,ctx):
        em = discord.Embed(title='Super Loto Komutu',
                           description = 'Tek kolon girerek süper loto oynayabilirsiniz. Acaba ne kadar şanslısınız?',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!superloto <s1 s2 s3 s4 s5 s6>```')
        await ctx.send(embed = em)
    #-------------------
    #-------------------
    @help.command()
    async def oylama(self,ctx):
        em = discord.Embed(title='Oylama Komutu',
                           description = 'Herhangi bir konuyu dost meclisinizde oylamaya sunabilirsiniz.',color =0x008000)

        em.add_field(name='**Syntax**',value = '```g!oylama <zaman(örneğin 12h)> <konu>```')
        await ctx.send(embed = em)
        
def setup(bot):
    bot.add_cog(Help(bot))
