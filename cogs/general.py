import discord
from discord.ext import commands
import asyncio
import youtube_dl
import os
import http.client
import datetime

class General(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def kolpala(self,msg):
        await msg.send(f"""Merhaba {msg.author.mention}, ben Geyik botu.
burak tarafından Geyik Server'ı için özenle tasarlandım:)""")

    @commands.command()
    async def bayrak(self,msg):
        with open('images\\flag.png', 'rb') as f:
            picture = discord.File(f)
            await msg.send(f'{msg.author.mention}, sana şanlı bayrağımızı gönderiyorum.')
            await msg.send(file=picture)
    @commands.command(aliases=['kurallar','constitution'])
    async def anayasa(self,msg):
        await msg.send("""1.MADDE: Geyik Sunucusu Bir Meşrutiyettir.
2.MADDE: Geyik Sunucusu, sunucunun huzuru, kolpacılar arası dayanışma ve adalet anlayışı içinde, kolpacı haklarına saygılı, Seko boşuna bağlı, başlangıçta belirtilen temel ilkelere dayanan, boş, gırgır ve gereksiz bir Geyik Sunucusu'dur.
3.MADDE: Geyik Sunucusu, üyeleri ile bölünmez bir bütündür. Dili Türkçedir.
4.MADDE: Kuralların 1'inci maddesindeki Sunucunun şeklinin Meşrutiyet olduğu hakkındaki hüküm ile, 2 nci maddesindeki Sunucunun nitelikleri ve 3'üncü maddesi hükümleri değiştirilemez ve değiştirilmesi teklif edilemez. Seko mutlak veto yetkisine sahiptir.
5.MADDE: Server'ın temel amaç ve görevleri, kolpacılar güruhunun bağımsızlığını ve bütünlüğünü, Server'ın bölünmezliğini, kolpayı ve boşu korumak, üyelerin ve Seko'nun refah, huzur ve mutluluğunu sağlamak; üyelerin temel hak ve hürriyetlerini, kolektif ve özgür boş ilkeleriyle bağdaşmayacak surette sınırlayan siyasal, ekonomik ve sosyal engelleri kaldırmaya, üyelerin maddî ve manevî varlığının gelişmesi için gerekli şartları hazırlamaya çalışmaktır
6.MADDE: Egemenlik, kayıtsız şartsız Seko'nundur.
7.MADDE: Yasama yetkisi Geyik Üyeleri adına Vekiller'e aittir. Bu yetki devredilemez. 
8.MADDE: Yürütme yetkisi ve görevi, Burak tarafından, Anayasaya ve kanunlara uygun olarak kullanılır ve yerine getirilir.
9.MADDE: Yargı yetkisi, Geyik Üyeleri adına Seko tarafından kullanılır.
10.MADDE: Herkes, dil, ırk, renk, cinsiyet, siyasî düşünce, felsefî inanç, din, mezhep ve benzeri sebeplerle ayırım gözetilmeksizin kanun önünde eşittir. 
11.MADDE: Anayasada yer alan hak ve hürriyetlerden hiçbiri, Geyik Server'ının ve üyeleriyle bölünmez bütünlüğünü  bozmayı ve insan haklarına dayanan boş ve kolpa, Meşrutiyet'i ortadan kaldırmayı amaçlayan faaliyetler biçiminde kullanılamaz.
12.MADDE: Hiç kimseye zorla boş yaptırılamaz. Ağır boş yasaktır. 
13.MADDE: Her kolpacı, düşünce , vicdan, dinî inanç ve kanaat hürriyetine sahiptir.""")
    
    @commands.command()
    async def ramazan(self,ctx):
        lower = str.maketrans("ABCÇçDEFGğĞHIıİJKLMNOÖPRŞşSTUüÜVYZ", "abcccdefggghiiijklmnoöprssstuuuvyz")
        conn = http.client.HTTPSConnection("api.collectapi.com")

        headers = {
            'content-type': "application/json",
            'authorization': "apikey 0xnsBwfgSQpagYl2Fx1DkO:4uGhcJqkOoC2tU1xnzSRcv"
            }
        print(ctx.message.content[10:].lower())
        conn.request("GET", f"/pray/all?data.city={ctx.message.content[10:].translate(lower)}", headers=headers)

        res = conn.getresponse()
        data = res.read()
        iftar_vakit  = data.decode('utf-8')[152:157]
        sahur_vakit  = data.decode('utf-8')[20:25]
        now = datetime.datetime.now()
        sahur_hour = int(sahur_vakit[:2])-(int(now.strftime("%H")))
        sahur_minute = int(sahur_vakit[3:])-(int(now.strftime("%M")))
        iftar_hour = int(iftar_vakit[:2])-(int(now.strftime("%H")))
        iftar_minute = int(iftar_vakit[3:])-(int(now.strftime("%M")))
        
        if iftar_minute<0:
            iftar_minute=60+iftar_minute
            iftar_hour-=1
        elif iftar_minute>=60:
            iftar_hour+=1
            iftar_minute-=60
        if iftar_hour<0:iftar_hour = 24+iftar_hour
          #--
        if sahur_minute<0:
            sahur_minute=60+sahur_minute
            sahur_hour-=1
        elif sahur_minute>=60:
            sahur_hour+=1
            sahur_minute-=60
        if sahur_hour<0:sahur_hour = 24+sahur_hour
        
        em = discord.Embed(title=f'{ctx.message.content[10:].capitalize()}'
                     )

        em.add_field(name='**İftar Vakti**',value = f"""```{iftar_vakit}```
                                              İftara {iftar_hour} saat {iftar_minute} dakika kaldı.""")
        em.add_field(name='**Sahur Vakti**',value = f"""```{sahur_vakit}```
                                              Sahura {sahur_hour} saat {sahur_minute} dakika kaldı.""")
        await ctx.message.channel.send(f"{ctx.message.author.mention}" )
        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(General(bot))
