import discord
from discord.ext import commands
import asyncio
import os
import http.client
import datetime
from omdbapi.movie_search import GetMovie
import wikipedia

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
        
        em = discord.Embed(title=f'{ctx.message.content[10:].capitalize()}',color = 0x21abcd
                     )

        em.add_field(name='**İftar Vakti**',value = f"""```{iftar_vakit}```
                                              İftara {iftar_hour} saat {iftar_minute} dakika kaldı.""")
        em.add_field(name='**Sahur Vakti**',value = f"""```{sahur_vakit}```
                                              Sahura {sahur_hour} saat {sahur_minute} dakika kaldı.""")
        await ctx.message.channel.send(f"{ctx.message.author.mention}" )
        await ctx.send(embed = em)
     

    @commands.command()
    async def sondakika(self,ctx):
        conn = http.client.HTTPSConnection("api.collectapi.com")

        headers = {
            'content-type': "application/json",
            'authorization': "apikey 0xnsBwfgSQpagYl2Fx1DkO:4uGhcJqkOoC2tU1xnzSRcv"
            }
        if ctx.message.content[12:]=='korona':
            conn.request("GET", "/corona/coronaNews", headers=headers)
        else:
            conn.request("GET", "/news/getNews?country=tr&tag=general", headers=headers)

        res = conn.getresponse()
        data = res.read()

        tumhaberler = []
        for idi,i in enumerate(data.decode("utf-8").split('}')):
            try:
                if 8>idi>0:
                    splitt = i.split('"')
                    if ctx.message.content[12:]=='korona':
                        haber = [splitt[19],splitt[7],splitt[3],splitt[15],splitt[23]]
                    else:
                        haber = [splitt[7],splitt[19],splitt[15],splitt[23],splitt[11]]
                    
                    tumhaberler.append(haber)

            except:
                break
        if ctx.message.content[12:]=='korona':
            em = discord.Embed(title=f'Son Dakika Korona Haberleri',color = 0xff033e)
        else:
            em = discord.Embed(title=f'Son Dakika Haberler',color = 0xff033e)
        for idh,haber in enumerate(tumhaberler):
            em.set_image(url='https://im.haberturk.com/2021/04/16/ver1618590442/3042228_620x410.jpg')
        
            em.add_field(name=f'**Haber {idh+1}**',value = f"""`{haber[1]}`
{haber[4][:150]}...
**Kaynak**: {haber[3]}
**Link**: {haber[0]}""")
            #em.set_author(name='***Geyik Botundan son dakika haberler...***')
            #em.set_footer(text="""-------------------------------------------------------------------------------------------------Detaylı bilgi için g!sondakika <haber numarası>""")
            
        await ctx.send(embed = em)


    @commands.command()
    async def korona(self,ctx):
        conn = http.client.HTTPSConnection("api.collectapi.com")

        headers = {
            'content-type': "application/json",
            'authorization': "apikey 0xnsBwfgSQpagYl2Fx1DkO:4uGhcJqkOoC2tU1xnzSRcv"
            }

        conn.request("GET", "/corona/countriesData", headers=headers)

        res = conn.getresponse()
        data = res.read()

        turkey = data.decode("utf-8").split("}")[4]
        tr = turkey.split("\"")
        totalcase = tr[7]
        dailycase = tr[11]
        totaldeath = tr[15]
        dailydeath = tr[19]
        totalrecovered= tr[23]
        activeCases= tr[27]
        em = discord.Embed(title=f'Günlük Korona Tablosu',color =0x21abcd)
        if len(dailycase)<3:
            dailycase = '*güncellenmedi*'
        if len(dailydeath)<3:
            dailydeath = '*güncellenmedi*'
        em.add_field(name=f'**Türkiye**',value = f"""**Toplam Vaka: ** {totalcase}
**Toplam Ölüm: ** {totaldeath}
**Toplam İyileşen: ** {totalrecovered}
**Günlük Vaka: ** {dailycase}
**Günlük Ölüm: ** {dailydeath}
""")
        em.set_image(url='https://i2.milimaj.com/i/milliyet/75/750x0/6082e0c45542851a500d84b5')
        em.set_footer(text='En doğru bilgi için: https://covid19.saglik.gov.tr/')
        await ctx.send(embed = em)

    @commands.command()
    async def superlig(self,ctx):
        
        conn = http.client.HTTPSConnection("api.collectapi.com")

        headers = {
            'content-type': "application/json",
            'authorization': "apikey 0xnsBwfgSQpagYl2Fx1DkO:4uGhcJqkOoC2tU1xnzSRcv"
            }

        conn.request("GET", "/sport/league?data.league=spor-toto-super-lig", headers=headers)

        res = conn.getresponse()
        data = res.read()
        takimlar = []
        data = data.decode("utf-8").split('}')
        for element in data[0:1]:
            splitt = element.split('"')[2:]
            takimlar.append([splitt[3],splitt[39],splitt[19],splitt[23],splitt[15],splitt[11],splitt[7],splitt[27],splitt[31]])

        for element in data[1:]:
            try:
                splitt = element.split('"')
                takimlar.append([splitt[3],splitt[39],splitt[19],splitt[23],splitt[15],splitt[11],splitt[7],splitt[27],splitt[31]])
            except:
                pass

        strX = ''
        strX += f'Sıra|Takım                             O| S| G| Y| B| A|\n'
        for takim in takimlar:
            a=35-len(takim[1])
            strX += f'{takim[0].zfill(2)}  |{takim[1]}{takim[2]:>{a}}|{takim[3].zfill(2)}|{takim[4].zfill(2)}|{takim[5].zfill(2)}|{takim[6].zfill(2)}|{str(int(takim[7].zfill(2))-int(takim[8])).zfill(2)}|\n'
        await ctx.send(f'{ctx.author.mention} için Super Lig\'den güncel sonuçları getirdim.')
        await ctx.send(f'```{strX}```')


    @commands.command()
    async def premierlig(self,ctx):
        
        conn = http.client.HTTPSConnection("api.collectapi.com")

        headers = {
            'content-type': "application/json",
            'authorization': "apikey 0xnsBwfgSQpagYl2Fx1DkO:4uGhcJqkOoC2tU1xnzSRcv"
            }

        conn.request("GET", "/sport/league?data.league=ingiltere-premier-ligi", headers=headers)

        res = conn.getresponse()
        data = res.read()
        takimlar = []
        data = data.decode("utf-8").split('}')
        for element in data[0:1]:
            splitt = element.split('"')[2:]
            takimlar.append([splitt[3],splitt[39],splitt[19],splitt[23],splitt[15],splitt[11],splitt[7],splitt[27],splitt[31]])

        for element in data[1:]:
            try:
                splitt = element.split('"')
                takimlar.append([splitt[3],splitt[39],splitt[19],splitt[23],splitt[15],splitt[11],splitt[7],splitt[27],splitt[31]])
            except:
                pass

        strX = ''
        strX += f'Sıra|Takım                             O| S| G| Y| B| A|\n'
        for takim in takimlar:
            a=35-len(takim[1])
            strX += f'{takim[0].zfill(2)}  |{takim[1]}{takim[2]:>{a}}|{takim[3].zfill(2)}|{takim[4].zfill(2)}|{takim[5].zfill(2)}|{takim[6].zfill(2)}|{str(int(takim[7].zfill(2))-int(takim[8])).zfill(2)}|\n'
        await ctx.send(f'{ctx.author.mention} için Premier Lig\'den güncel sonuçları getirdim.')
        await ctx.send(f'```{strX}```')


    @commands.command()
    async def havadurumu(self,ctx):
        conn = http.client.HTTPSConnection("api.collectapi.com")

        headers = {
            'content-type': "application/json",
            'authorization': "apikey 0xnsBwfgSQpagYl2Fx1DkO:4uGhcJqkOoC2tU1xnzSRcv"
            }
        try:
            lower = str.maketrans("ABCÇçDEFGğĞHIıİJKLMNOÖPRŞşSTUüÜVYZ", "abcccdefggghiiijklmnoöprssstuuuvyz")
            conn.request("GET", f"/weather/getWeather?data.lang=tr&data.city={ctx.message.content[13:].translate(lower)}", headers=headers)
            res = conn.getresponse()
            data = res.read()
            havadurumu = []
            for element in data.decode("utf-8").split('}')[0:1]:
                splitt = element.split('"')[4:]
                havadurumu.append([splitt[7],splitt[11],splitt[15],splitt[19],splitt[23],splitt[27],splitt[39],splitt[31],splitt[35],splitt[43]])
     
            for element in data.decode("utf-8").split('}')[1:]:
                splitt = element.split('"')
                try:
                    havadurumu.append([splitt[3],splitt[7],splitt[11],splitt[15],splitt[19],splitt[23],splitt[35],splitt[27],splitt[31],splitt[39]])
                except:
                    pass
        
            em = discord.Embed(title=f'{ctx.message.content[13:].capitalize()} için Hava Durumu',color =0x21abcd)
            for day in havadurumu:
                em.add_field(name=f'**{day[0]} {day[1]} Günü**',value =f"""Hava Durumu: `{day[3]}`
    Ort. Sıcaklık: `{day[5]}`
    Min. Sıcaklık: `{day[7]}`
    Max. Sıcaklık: `{day[8]}`
    Gece Sıcalığı: `{day[6]}`
    Nem Oranı: `{day[9]}`""")
            em.set_image(url='https://www.mardinlife.com/uploads/2021/01/batman-hava-durumu-23-ocak-2021-52458.jpg?234234.234234')
       
            await ctx.send(f'{ctx.author.mention} için {ctx.message.content[13:].capitalize()} şehrinin 1 haftalık hava durumu sonuçları:')
            await ctx.send(embed = em)
        except:
            await ctx.send(f'{ctx.author.mention} maalesef aradığın şehri bulamadım.')


    @commands.command()
    async def imdb(self,ctx):
        
        lower = str.maketrans("ABCÇçDEFGğĞHIıİJKLMNOÖPRŞşSTUüÜVYZ", "abcccdefggghiiijklmnoöprssstuuuvyz")
        alldata = GetMovie(title=f'{ctx.message.content[7:].translate(lower)}', api_key='613ccdd1')
        movie = alldata.get_all_data()
        try:
            em = discord.Embed(title=f'IMDB',color =0x21abcd)
            em.add_field(name=f'__**{movie["Title"].upper()}**__',value =f"""**Vizyon Tarihi:** `{movie["Released"]}`
    **Derecelendirme**: `{movie["Rated"]}`
    **Uzunluğu**: `{movie["Runtime"]}`
    **Yönetmen:** `{movie["Director"]}`
    **Senarist:** `{movie["Writer"]}`
    **Aktörler:** `{movie["Actors"]}`
    **Hakkında:** `{movie["Plot"]}`
    **Ödüller:** `{movie["Awards"]}`
    **Metascore:** `{movie["Metascore"]}`
    **IMDB Puanı:** `{movie["imdbRating"]}`

    """)
            em.set_image(url=movie["Poster"])
            await ctx.send(embed = em)
        except:
            await ctx.send(f'{ctx.author.mention} maalesef aradığın filmi bulamadım.')


    @commands.command(aliases=['fikstür'])
    async def fikstur(self,ctx):

        conn = http.client.HTTPSConnection("api.collectapi.com")

        headers = {
            'content-type': "application/json",
            'authorization': "apikey 0xnsBwfgSQpagYl2Fx1DkO:4uGhcJqkOoC2tU1xnzSRcv"
            }
        if ctx.message.content[10:]=='premierlig' or ctx.message.content[10:]=='premier lig':
            lig = 'ingiltere-premier-ligi'
            baslik = 'Premier Lig'
        else:
            lig = 'spor-toto-super-lig'
            baslik = 'Süper Lig'
        conn.request("GET", f"/sport/results?data.league={lig}", headers=headers)

        res = conn.getresponse()
        data = res.read()

        alldata = data.decode("utf-8").split('}')
        fikstur = []
        for element in alldata[0:1]:
            try:
                splitt = element.split('"')[2:]
                fikstur.append([splitt[3],splitt[7],splitt[11],splitt[15]])
            except:
                pass
        for element in alldata[1:]:
            try:
                splitt = element.split('"')
                fikstur.append([splitt[3],splitt[7],splitt[11],splitt[15]])
            except:
                pass

        
        em = discord.Embed(title=f'{baslik} Fikstür',color =0x21abcd)
        for idm,mac in enumerate(fikstur):
            em.add_field(name=f'__**Maç {idm+1}**__',value =f"""*Tarih:* `{mac[1]}`
*Taraflar:* `{mac[3]} - {mac[2]}`
*Skor:* `{mac[0]}`
""")
        await ctx.send(f'{ctx.author.mention} için fikstürü getirdim.')
        await ctx.send(embed = em)


    @commands.command()
    async def wikipedia(self, ctx, word):
        try:
            def viki_sum(arg):
                definition = wikipedia.summary(arg, sentences=3, chars=1000)
                return definition
            msg = await ctx.send(f'{ctx.author.mention} için aranıyor...')
            em = discord.Embed(title=f'Wikipedia',color =0x21abcd)
            em.add_field(name=f'__**{ctx.message.content[12:].capitalize()}**__',value =f"{viki_sum(ctx.message.content[12:])}")
            await msg.edit(content = f'{ctx.author.mention} için bulundu:)')
            await ctx.send(embed = em)
        except:
            await msg.edit(content = f'{ctx.author.mention} maalesef bulamadım:(')
        
def setup(bot):
    bot.add_cog(General(bot))
