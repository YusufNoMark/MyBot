import random
import os
import discord
from discord.ext import commands
import colorama
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

from colorama import Fore, Back, Style



colorama.init()

def botp(bot, message):
    
    # gayet basit bir şekilde prefix eklenebiliyor
    prefixler = ['!', '.', 'b!']

    # mesaj dm den mi yoksa sunucudan mı gelmiş ona bakar
    if not message.guild:
        # sadece dm için ? kullanmaya açık
        return '?'

  
    return commands.when_mentioned_or(*prefixler)(bot, message)

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix=botp, intents=intents)


player = {}


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Bilgisayar Günlükleri"))
    print("OK")

    #🔒┇kayıt
    #🚪┇gelen-giden




@client.event
async def on_member_join(member):
    guild = member.guild
    gelen = discord.utils.get(member.guild.text_channels, name="🚪┇gelen-giden")
    channel = discord.utils.get(member.guild.text_channels, name="🔒┇kayıt")
    geldi = discord.utils.get(member.guild.text_channels, name="🚪┇gelen-giden")
    kayıtsızRol = discord.utils.get(guild.roles, name="KAYITSIZ")

    await member.add_roles(kayıtsızRol)
    sorumlu = "947173857964486676"
    await channel.send(f":alarm_clock: <@&{sorumlu}> Yeni Bir Üye Geldi!")
    embed = discord.Embed(title=":crossed_swords: Bg Kayıt Sistemi.", description=":bellhop: Yeni Bir Kullanıcı Var!", color=0x000000)
    embed.add_field(name="Sunucumuza Hoş Geldin Yoldaş!", value=f"👋 {member.mention}")
    embed.add_field(name="Lütfen Yetkilileri Bekleyiniz.", value=f"{member.mention}", inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
    sayımız = guild.member_count
    hg = discord.Embed(title="Yeni Bir YOLDAŞ! :partying_face:", description=f"*Hoş Geldin.* {member.mention}", color=discord.Colour.green())
    hg.add_field(name="Seni Görmek Güzel", value=f"*Senin İle Beraber ``{sayımız}`` Kişi Olduk!*", inline=False)
    hg.set_image(url=member.avatar_url)
    
    await gelen.send(embed=hg)
                 
                 
                 
@client.event
async def on_member_remove(member):
    sayımız = member.guild.member_count
    giden = discord.utils.get(member.guild.text_channels, name="🚪┇gelen-giden")
    bb = discord.Embed(title="Bir Yoldaş Kaybettik! :cry:", description=f"*Aramızdan Ayrıldı* {member.mention}", color=discord.Colour.purple())
    bb.add_field(name="Görüşmek Üzere :(", value=f"*Sensiz ``{sayımız}`` Kişi kaldık*", inline=False)
    bb.set_image(url=member.avatar_url)
    
    await giden.send(embed=bb)            
                
                 
                 
    



@client.command()
@commands.has_role("Kayıt Sorumlusu")
async def kayıt(ctx, member: discord.Member, nick):
    guild = ctx.guild
    yaratıcım = 935455852607987742
    bildirme = discord.utils.get(guild.text_channels, name="💬┇genel-sohbet")
    kayıtlırol = discord.utils.get(guild.roles, name="❤ ۰ Üye")
    kayıtsızRol = discord.utils.get(guild.roles, name="KAYITSIZ")
    

      
        
        
    await member.edit(nick=f"⧖ {nick}")

    await member.remove_roles(kayıtsızRol)
    await member.add_roles(kayıtlırol)

    yetkili_id = ctx.author.id

    embed = discord.Embed(title="Bg Kayıt Sistemi", description="Kayıt Başarılı!", color=discord.Colour.green())
    embed.add_field(name=f"Kullanıcı Başarılı Bir Şekilde Kayıt Edildi!", value=f"Kayıt Edilen Kullanıcı: {member.mention} , Kayıt Eden Yetkili: <@{yetkili_id}>", inline=False)
    embed.set_thumbnail(url="https://c.tenor.com/Mw__8SvDbi8AAAAC/checkmark-black.gif")
    await ctx.channel.send(embed=embed)
    await bildirme.send(embed=embed)
    
    kurallarımız = """
    **
    Kurallar Lütfen Okuyunuz. Aksi Taktirde Ben Bilmiyordum Gibi Bahaneler Kabul Etmiyoruz

    1:  Üyelere Karşı Saygılı Olunmalıdır.

    2: Düzgün Bir Şekilde Saygılı Ve Küfürsüz Konuşulmalıdır.

    3: bane,31,napim Gibi Bebekçe Kelimelere Kullanmak Yasaktır

    4: Spam Veya Flood Atmak Yasaktır

    5: Yetkililere Saygılı Olunmalıdır

    6: Sunucumuzun Tagı Adda Bulundurulması Zorunludur Nitro İle Değiştirilemez.

    7: Özelden Üyeleri Rahatsız Etmek Yasaktır.(Yetkililer Dahil)

    8: Bot Komutlarını Gelip 💻┇bot-komut Adlı Kanalda Yazılmalıdır.

    9: Dil,Din,Irk Ayrımı Yasaktır

    10: Siyasi Konuların Konuşulması Yasaktır (isteyen dm)

    11: Dini konuların Konuşulması Yasaktır


    Sunucuya Girdiğiniz Andan İtibaren Kuralları Okumuş Sayılırsınız.

    **
    
    ```
    İyi Eğlenceler Değerli üyemiz.
    ```
"""
    
    
    
    usersend = discord.Embed(title="Sunucumuza Hoş Geldin Yoldaş!", description="Lütfen Kuralları Okuyunuz.", color=discord.Colour.green())
    usersend.add_field(name="Bilgilendirme!", value="*Abone Rolü İçin Abone Kanıt Adlı Kısma 2 Kanalada Abone Olup Bildirimleri Açtığına Dair SS Atman Gerekir. Yetkililerimiz İlgilenecektir Değerli Üyemiz.*", inline=False)
    usersend.add_field(name="Kurallar.", value=f"{kurallarımız}", inline=True)
    
    await member.send(embed=usersend)
        
        
        
        
        
@client.command()
async def deneme(ctx, member: discord.Member):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content in ["1", "2"]
    msg = await client.wait_for("message", check=check)

    if msg.content == "1":
        await msg.send("Ok")
    else:
        pass
     


@client.command()
async def bildir(ctx, arg1):
    id = ctx.author.id
    ad = ctx.author
    embed = discord.Embed(title="Bildirme Sistemi.", description="Hatanız Başarılı Bir Şekilde Bildirildi.", color=discord.Colour.green())
    embed.add_field(name="Dikkat!", value="``Eğerki Boş Veya Yalan Bir Şeyi Bildirirseniz Sunucuda Uyarı Değil Ceza Alırsınız.``", inline=False)
    await ctx.channel.send(embed=embed)

    print(Fore.LIGHTCYAN_EX + f"---- Ad: {ad} ---- İd: {id} ---- Bildirme: {arg1}")
    os.system(f"\necho ---- Ad: {ad} ---- Id: {id} ---- Bildirme: {arg1}>> bildirme.txt")


@client.command()
async def stat(ctx, member: discord.Member):
    id = ctx.author.id
    yaratıcım = 935455852607987742

    if member.id == yaratıcım:
        #time.sleep(1)
        await ctx.channel.send("``Yusuf Abime Laf Ettirmem!``")
        return


    love = random.choice(["+", "++", "+++", "++++", "A+", "A++", "A+++", "S+"])
    healt = random.choice(["+", "++", "+++", "++++", "A+", "A++", "A+++", "S+"])
    money = random.choice(["+", "++", "+++", "++++", "A+", "A++", "A+++", "S+"])
    students = random.choice(["+", "++", "+++", "++++", "A+", "A++", "A+++", "S+"])
    level = random.choice(["+", "++", "+++", "++++", "A+", "A++", "A+++", "S+"])

    embed = discord.Embed(title="Stat Sistemi", description=f"**{member.mention}** ``Adlı Kullanıcının Statlarına`` **<@{id}>** ``Tarafından Bakıldı``")
    embed.add_field(name="Sevgi Durumu", value=f"{love}", inline=False)
    embed.add_field(name="Sağlık Durumu", value=f"{healt}", inline=False)
    embed.add_field(name="Para Durumu", value=f"{money}", inline=False)
    embed.add_field(name="Oğretim Durumu", value=f"{students}", inline=False)
    embed.add_field(name="Karakter Seviyesi Durumu", value=f"{level}", inline=False)
    await ctx.channel.send(embed=embed)

#⧖ Mrs.Major ⧖#0310


@client.command()
async def yardım(ctx):
    embed = discord.Embed(title="Yardım Menusu",url="https://emojigraph.org/static/img/logo.fa9e46678e09.png", description="Burda Komutları Görebilirsin.", colour=0x9f715)
    embed.add_field(name=":man_police_officer: !yetkili", value="Yetkili Menüsünü Açar", inline=True)
    embed.add_field(name=":joy: !eğlence ", value="Eğlence Menüsünü Açar", inline=False)
    embed.add_field(name=":gear: !bot ", value="Bot Komutlarını Gösterir.", inline=False)
    embed.set_thumbnail(url="https://xn--engitrentacar-htc.com/wp-content/uploads/2017/11/Support_Services-512.png")
    await ctx.channel.send(embed=embed)





@client.command()
async def yetkili(ctx):
    embed = discord.Embed(title="Yetkili Menüsü", description="Burda Yetkili Komutlarını Görebilirsiniz.", colour=0x9f715)
    embed.add_field(name=":broom: !sil <Adet>", value="Verilen Değer kadar Mesaj Siler.", inline=True)
    embed.add_field(name=":hammer: !ban <Kullanıcı> <Sebep> ", value="Verilen Etiketteki Kullanıcıyı Banlar.", inline=False)
    embed.add_field(name=":leg: !kick <Kullanıcı> <Sebep> ", value="Verilen Etiketteki Kullanıcıyı Kickler.", inline=False) 
    embed.add_field(name=":mute: !mute <Kullanıcı> <Sebep> ", value="Verilen Etiketteki Kullanıcıyı Susturur.", inline=False)
    embed.add_field(name=":sound: !unmute <Kullanıcı>", value="Verilen Etiketteki Kullanıcının Mutesini Kaldırır", inline=False)        
    embed.set_thumbnail(url="https://cdn2.iconfinder.com/data/icons/web-application-icons-part-2/100/Artboard_76-512.png")
    await ctx.channel.send(embed=embed) 


@client.command()
async def eğlence(ctx):
    embed = discord.Embed(title="Eğlence Menüsü", description="Burda Eğlence Komutlarını Görebilirsiniz.", colour=0x9f715)
    embed.add_field(name=":joy: !hayat <Argüman Gerekmez>", value="Rastgele Hayat Hikayesi Söyler.", inline=True)
    embed.add_field(name=":joy: !kaçcm <Argüman Gerekmez>", value="Daşşağının Boyunu Söyler.", inline=False)
    embed.add_field(name=":joy: !smash <Kullanıcı Argüman> ", value="Etiketlenen Kişileri SMASHLER", inline=False)
    embed.add_field(name=":joy: !slap <Kullanıcı Argüman> ", value="Etiketlenen Kişileri Slapler", inline=False)
    embed.add_field(name=":joy: !nitrover <Kullanıcı Argüman> ", value="Bot Etiketlenen Kişiye Beleş Nitro Verir.", inline=False) 
    embed.add_field(name=":joy: !meme <Argüman Gerekmez>", value="Komik Bir Fotoğraf Gösterir.", inline=False)
    embed.add_field(name=":joy: !aşkölçer <Kullanıcı Argüman> ", value="Etiketlenen Kişi İle Aşk Durumunuz Hesaplanır.", inline=False)
    embed.add_field(name=":joy: !öp <Kullanıcı>", value="Etiketlenen Kişiyi EMCÜKLEYEREK ÖPER.", inline=False)
    embed.add_field(name=":joy: !token <Argüman Gerekmez> ", value="Botun Tokenini Verir.", inline=False) 
    embed.set_thumbnail(url="https://w7.pngwing.com/pngs/378/300/png-transparent-nightclub-disco-dance-others-vector-icons-disco-ball-party.png")
    await ctx.channel.send(embed=embed)

        #📗⎪kayıt


@client.command()
async def bot(ctx):
    embed = discord.Embed(title="Özel", description="Burda özel Komutları Görebilirsiniz.", colour=0x9f715)
    embed.add_field(name=":joy: !token <Argüman Gerekmez>", value="Botun Tokenini Söyler.", inline=True)
    embed.add_field(name=":joy: !linkbot <Argüman Gerekmez>", value="Botun Davet Linkini Verir.", inline=False)     
    embed.add_field(name=":joy: !news <Argüman Gerekmez>", value="Botun Yeniliklerini Söyler.", inline=False)
    embed.add_field(name=":mute: !bildir <Tek Argüman>", value="Lütfen Kelimeden Kelimeye Geçerken Alt Çizgi Kullanınız. Aksi Taktirde İşlem Gerçekleşmez ``Örn Kullanım: botun_şu_açığı_vardır``")
    embed.add_field(name=":joy: !sik <Kullanıcı Argüman>", value="Bot Etiketlenen Kişiyi SİKER.", inline=False)
    embed.set_thumbnail(url="https://cdn.dribbble.com/users/2118561/screenshots/14203460/media/d12200f55f84178be88626f03668dc0a.png")
    await ctx.channel.send(embed=embed)



@client.command()
async def öp(ctx, member: discord.Member):
    id = ctx.author.id
    yaratıcım = 935455852607987742

    if member.id == yaratıcım:
        #time.sleep(1)
        await ctx.channel.send("``Abimi Öptürtmem!!``")
        return
    embed = discord.Embed(title="Öp!!", description=f"{member.mention} Adlı Kullanıcı <@{id}> Tarafından EMCÜKLENEREK ÖPÜLDÜ")
    embed.add_field(name=":white_check_mark: Görev Başarılı!", value="Bol YALAMALI", inline=False)
    embed.set_image(url="https://c.tenor.com/rRILSsVKsUwAAAAC/passionate-kiss.gif")
    await ctx.channel.send(f"``Hepsi Bir Rüya {member.mention}``")

    await ctx.channel.send(embed=embed)




@client.command()
async def meme(ctx):
    meme25 = "https://i.pinimg.com/564x/b5/e8/1e/b5e81e35a13103f3ce6ba032d2279e44.jpg"
    meme25 = "https://i.pinimg.com/564x/56/bf/57/56bf57e4b0ffdb144342005712cec7cd.jpg"
    meme24 = "https://i.pinimg.com/736x/be/c0/37/bec03723987d469895729aeb2c87258a.jpg"
    meme23 = "https://i.pinimg.com/564x/9b/58/a7/9b58a78ea43a00d1f05be881bfd1d5fd.jpg"
    meme22 = "https://i.pinimg.com/564x/3f/bb/03/3fbb034894b4c18444c1538163a1a287.jpg"
    meme21 = "https://i.pinimg.com/564x/20/de/89/20de8962417fd40714fde2308bbe3f26.jpg"
    meme20 = "https://img.wattpad.com/b61bd20b1452a74fcc671518dd3840ff775d3252/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f3749546c533471647961494767773d3d2d3438352e313632326538353435303366323432623831343333383535313831382e6a7067?s=fit&w=720&h=720"
    meme19 = "https://i.redd.it/aiwv8l7ikk051.jpg"
    meme18 = "https://pbs.twimg.com/media/EW8hq5gXYAczpbT?format=jpg&name=small"
    meme17 = "https://i.redd.it/vbmc9s2p2go41.jpg"
    meme16 = "https://forum.shiftdelete.net/media/666666666.692/full?d=1491836297"
    meme15 = "https://pbs.twimg.com/media/Ek3Pi91WkAEHwXO?format=jpg&name=medium"
    meme14 = "https://64.media.tumblr.com/e00dec1ffdb27cbb3f66d3d193da93b5/tumblr_pmgc5dhJro1w3ixpn_400.jpg"
    meme13 = "https://64.media.tumblr.com/23e6b3586ad437be37465d5d866a905c/tumblr_pmgc5daYnE1w3ixpn_250sq.jpg"
    meme12 = "https://64.media.tumblr.com/7ad8986ecc43db42b980c39c4528cd13/tumblr_ppl4amvVye1w3ixpn_540.jpg"
    meme11 = "https://64.media.tumblr.com/e33a4e96192e6ed536fc9de52b951dcf/19834515b22bc92f-a8/s540x810/14b0b833ed1a576135a9e1cf7106012d26d425fd.jpg"
    meme10 = "https://64.media.tumblr.com/c5a589dae57a6c72a07f982bf588bb37/65e93f585b175356-84/s540x810/7e2fa47462502591166eaa1b7ae04632598507be.jpg"
    meme9 = "https://64.media.tumblr.com/c8c52cae17f068d73bfa8e335055bff0/762d24e841d995d2-8d/s540x810/d5109569a86cfc9400b886ada3e54974c7106f24.png"
    meme8 = "https://i.pinimg.com/originals/65/67/02/6567029c784d6d0f3a314156b6ff11d7.jpg"
    meme7 = "https://img-s1.onedio.com/id-6023b6da0c7fbeb7268cf3fb/rev-0/w-635/f-jpg/s-94744a59c6201ba31fa5b981aae7b95eacd287e4.jpg"
    meme6 = "https://img-s1.onedio.com/id-6023b6d59d46d7dd25c1c01e/rev-0/w-635/f-jpg/s-ae396f36935ccaa8258b176b692416a4571d6e74.jpg"
    meme5 = "https://img-s1.onedio.com/id-6023b6e43d30345e247a294e/rev-0/w-635/f-jpg/s-cc0bf12d2992a36b2a6fc267c26b98483a1c5cd9.jpg"
    meme4 = "https://img-s1.onedio.com/id-6023b6d9c8c26eed27c2d93b/rev-0/w-635/f-jpg/s-bac76c8e214aef72d39951bf110ffd158df2f3a2.jpg"
    meme3 = "https://img-s3.onedio.com/id-6023b6e712a8386726294285/rev-0/w-635/f-jpg/s-b81bceea0badf5e224c395411ba63d0c1b4f5238.jpg"
    meme2 = "https://pbs.twimg.com/media/EOocRB3XUAAHVP6?format=jpg&name=900x900"
    meme1 = "https://scontent.fadb3-1.fna.fbcdn.net/v/t1.6435-9/170678733_2794071487477051_3216418934535094575_n.jpg?_nc_cat=107&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=r_lOOpA6p3oAX-ON29_&_nc_ht=scontent.fadb3-1.fna&oh=00_AT_lmC_tJlOFSth7jif-HdmoZcsJyyXSS0kWR20VW5veDg&oe=621944FD"
    randommemes = random.choice([meme1, meme2, meme3, meme4, meme5, meme6, meme7, meme8, meme9, meme10, meme11, meme12, meme13, meme14, meme15, meme16, meme17, meme18, meme19, meme20, meme21, meme22, meme23, meme24, meme25])
    embed = discord.Embed(title="Meme", description="Meme Foto :joy: ")
    embed.set_image(url=randommemes)
    await ctx.channel.send(embed=embed)



@client.command()
async def pp(ctx, member:discord.Member):
    yaratıcım = 935455852607987742

    if member.id == yaratıcım:
        #time.sleep(1)
        await ctx.channel.send("``Bakma Lan Abimin ppye``")
        return
    embed = discord.Embed(title=member.name , description=member.mention ,color = discord.Colour.green())
    embed.add_field(name="İd", value=member.id, inline=True)
    embed.add_field(name="Takma Ad", value=member.nick, inline=True)
    embed.add_field(name="Rol", value=member.top_role.name, inline=True)
    embed.set_image(url=member.avatar_url)
    await ctx.channel.send(embed=embed)




@client.command()
@commands.has_role("Ovh")
async def sil(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
        
    embed = discord.Embed(title="Sil", description="Sil İnfo", color=discord.Colour.blue())
    embed.add_field(name="Silinen Mesaj Sayısı", value=f"{amount}", inline=True)
    embed.add_field(name=f"Silen Yetkili", value=f"{ctx.author}", inline=False)
    embed.set_thumbnail(url="https://c.tenor.com/Mw__8SvDbi8AAAAC/checkmark-black.gif")
    await ctx.channel.send(embed=embed)



@client.command()
@commands.has_role("Ovh")
async def kick(ctx, member:discord.Member, *args, reason=None):
    id = ctx.author.id
    yaratıcım = 935455852607987742

    if member.id == yaratıcım:
        #time.sleep(1)
        await ctx.channel.send("``Abimi Kicklemem!``")
        return
    await member.kick(reason=reason)
    #await ctx.channel.send("``Kullanıcı başarılı bir Şekilde Kicklendi``")
    embed = discord.Embed(title="Kick", description="Kick İnfo", color=discord.Colour.red())
    embed.add_field(name="Kicklenen Kullanıcı", value=f"{member.mention}")
    embed.add_field(name="Kickleyen Yetkili", value=f"{ctx.author}")
    embed.add_field(name="Açıklama", value=f"{reason}")
    embed.set_image(url="https://c.tenor.com/hKetc97Uc_EAAAAC/flying-kick-kick.gif")
    await ctx.channel.send(embed=embed)





@client.command()
async def token(ctx):
    embed= discord.Embed(title="Tokenim", description="Tokenimi Burada Görebilirsin")
    embed.set_image(url="https://c.tenor.com/tQM-V9L3g9YAAAAM/el-hareketi.gif")
    await ctx.channel.send(embed=embed)



@client.command()
@commands.has_role("Ovh")
async def ban(ctx, member:discord.Member, *args, reason=None):
    id = ctx.author.id
    yaratıcım = 935455852607987742

    if member.id == yaratıcım:
        #time.sleep(1)
        await ctx.channel.send("``Abimi Banlatmam!``")
        return
    await member.ban(reason=reason)
    #await ctx.channel.send("``Kullanıcı Başarılı Bir Şekilde Banlandı!``")

    embed = discord.Embed(title="Ban", description="Ban İnfo", color=discord.Colour.red())
    embed.add_field(name="Banlanan Kullanıcı", value=f"{member.mention}")
    embed.add_field(name="Banlayan Yetkili", value=f"{ctx.author}")
    embed.add_field(name="Açıklama", value=f"{reason}")
    embed.set_image(url="https://c.tenor.com/m5Uwk-w7B18AAAAC/banned-thor.gif")
    await ctx.channel.send(embed=embed)


@client.command()
async def hayat(ctx):
    hikaye = random.choice(["televizyon izlerken telatabinin antenleri götüne girdi ve öldü", "Yolda Yürürken Kafana Everest Dağı Düşüp Öldü", "Uçaktayken Benzin Borusu Girdi Ve Felç Kaldı", "Jony Sinsle Vs Attı Ve Kısır Kalarak İntihar Etti", "Eyfel Kulesi Girerek Öldü", "Yemek İçerken Boğuldu", "Yolda Yürürken Uçak Çaprtı Ve Öldü", "Üst Geçitte Yürürken Araba Çarptı Ve Öldü", "Uçaktayken Sel Bastı Ve Öldü", "Arabadayken Kaza Oldu Ve Emniyet kemeri Götüne Girerek Öldü"])
    embed = discord.Embed(title="Rastgele Hikayeler", description="", color=discord.Colour.blue())
    embed.add_field(name="Hayatının Tahmini Sonu", value=f"{hikaye}")
    embed.set_image(url="https://i.pinimg.com/originals/4e/f2/72/4ef27259821ca68ead9551c9affad02e.gif")

    await ctx.channel.send(embed=embed)


@client.command()
@commands.has_role("Ovh")
async def sik(ctx, member: discord.Member):
    id = ctx.author.id
    yaratıcım = 935455852607987742

    if member.id == yaratıcım:
        #time.sleep(1)
        await ctx.channel.send("``Sie kendini sik``")
        return
    embed = discord.Embed(title="Bol Döllü", description=f"{member.mention} Adlı Kullanıcı Vahşice Sikildi", color=discord.Colour.red())
    embed.set_image(url="https://c.tenor.com/qC7OMlSm00EAAAAC/sex-love.gif")

    await ctx.channel.send(embed=embed)




@client.command()
async def news(ctx):
    embed = discord.Embed(title="Yeniliklerim Burada!", description="Version: 1.2", color=discord.Colour.green())
    embed.add_field(name="1. Yenilik", value="Kayıt Sistemi Eklendi.", inline=False)
    embed.add_field(name="2. Yenilik", value="Komutlara Embed Eklendi.", inline=False)
    embed.add_field(name="3. Yenilik", value="Yeni Memesler Eklendi.", inline=False)
    embed.set_thumbnail(url="https://www.iconsdb.com/icons/preview/red/new-xxl.png")
    await ctx.channel.send(embed=embed)



@client.command()
async def linkbot(ctx):
    embed = discord.Embed(title="Davet Linkim Burada!", description="Bota Admin Yetkisi Verilmelidir Aksi Taktirde Botun Bazı Özellikleri Çalışmayabilir.", color=discord.Colour.purple())
    embed.add_field(name="Link", value="https://discord.com/api/oauth2/authorize?client_id=935794875620798514&permissions=8&scope=bot", inline=False)
    embed.set_image(url="https://media.istockphoto.com/vectors/invitation-icon-on-transparent-background-vector-id1283403251")
    await ctx.channel.send(embed=embed)






@client.command()
async def kaçcm(ctx):
    cm = random.choice(["-25cm", "-10cm", "-3cm", "-1cm", "0", "1cm", "2cm", "3cm", "4cm", "5cm", "6cm", "7cm", "8cm", "9cm", "10cm", "13cm", "14cm", "20cm", "24cm", "31cm", "32cm", "33cm", "34cm", "35cm", "40cm", "45cm", "46cm", "47cm", "48cm", "49cm", "50cm", "51cm", "52cm", "53cm", "54cm", "55cm", "56cm", "57cm", "58cm", "59cm", "1m", "2m", "3m", "4m", "10m", "1km", "50km"])
    embed = discord.Embed(title="Daşşak Ölçer", description="Daşşak Ölçer Şuan Şimdi Burada!!!", color=discord.Colour.blue())
    embed.add_field(name="Daşşak Ölçerin Ölçtüğü Boyut Tam Olarak", value=f"{cm}")
    embed.set_image(url="https://i.pinimg.com/originals/4e/f2/72/4ef27259821ca68ead9551c9affad02e.gif")

    await ctx.channel.send(embed=embed)

    if cm == "1m":
        await ctx.channel.send("ha??")

    elif cm == "4m":
        await ctx.channel.send("ha??")
        

    elif cm == "10m":
        await ctx.channel.end("oa??")



    elif cm == "1km":
        await ctx.channel.send("LAN BUNE")


    elif cm == "50km":
        await ctx.channel.send("LAN MANİSA-İZMİR ARASI ZTN 50KM BUNE LOO")



    elif cm == "0":
        await ctx.channel.send("BUNE LAN QWUOEQUWEOIWUQEOWI 0 CM NE QWĞEOQĞWO")

        
    elif cm == "-1cm":
        await ctx.channel.send("-1 Mİ YENİ DOĞAN BEBENİN BİLE 1CM LAN")


    elif cm == "-3cm":
        await ctx.channel.send("-3 Mü YENİ DOĞAN BEBENİN BİLE 1CM LAN")



    elif cm == "-10cm":
        await ctx.channel.send("HACI KIZLARIN BİLE BU KADAR YOK QWEQWEQWEQWEQQEQ")


    elif cm == "-20cm":
        await ctx.channel.send("OHA ŞUAN Jules Aarons MEZARINDA YAN GELDİ QWOIUEWQEUQOUWI")


    elif cm == "-25cm":
        await ctx.channel.send("Jony Sins:BUNE OĞLUM AMINA")









@client.command()
@commands.has_role("Ovh")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    id = ctx.author.id
    yaratıcım = 935455852607987742

    if member.id == yaratıcım:
        #time.sleep(1)
        await ctx.channel.send("``Abimi Muteleyemen!``")
        return
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)


    await member.add_roles(mutedRole, reason=reason)
        #await ctx.send(f"**Susturuldu: {member.mention} Açıklama: {reason}**")
    await member.send(f"**{guild.name}** Adlı Sunucudan Susturuldun  Sebebi: **{reason}**")

    embed = discord.Embed(title="Mute", description=":mute: Mute İnfo", color=discord.Colour.red())
    embed.add_field(name="Susturulan", value=f"{member.mention}")
    embed.add_field(name="Susturan", value=f"{ctx.author}")
    embed.add_field(name="Açıklama", value=f"{reason}")
    embed.set_image(url="http://iconsetc.com/icons-watermarks/flat-circle-white-on-red/raphael/raphael_microphone-mute/raphael_microphone-mute_flat-circle-white-on-red_512x512.png")

    await ctx.channel.send(embed=embed)




@client.command()
@commands.has_role("Ovh")
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
        #await ctx.send(f"**{member.mention} Susturulması Kalktı.**")
    await member.send(f"**{guild.name}** Adlı Sunucudaki Susturulmanız Kalktı")
        
    embed = discord.Embed(title="Un Mute", description=":sound: Un Mute İnfo", color=discord.Colour.green())
    embed.add_field(name="Susturulması Kalkan", value=f"{member.mention}")
    embed.add_field(name="Susturulmasını Kaldıran", value=f"{ctx.author}")
    embed.set_image(url="https://cdn4.iconfinder.com/data/icons/interface-glyph-34/32/unmute-512.png")

    await ctx.channel.send(embed=embed)




@client.command()
async def smash(ctx, member: discord.Member):
    id = ctx.author.id
    yaratıcım = 935455852607987742

    if member.id == yaratıcım:
        #time.sleep(1)
        await ctx.channel.send("``Kendine Vur Lan!``")
        return
    embed = discord.Embed(title="Smash!", description=f"UNİTED STATES OF SMASH!! :boom:", color=discord.Colour.red())
    embed.set_image(url="https://c.tenor.com/qOk3nVxPmjcAAAAd/one-for-all-united-states-of-smash.gif")
    embed.add_field(name="Smashed!!!", value=f"{member.mention}", inline=False)

    await ctx.channel.send(embed=embed)

    embed.set_image(url="https://c.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif")




@client.command()
async def aşkölçer(ctx, member: discord.Member):
    id = ctx.author.id
    user = f"<@{id}>"
    askdurum = random.choice(["1", "5", "13", "15", "20", "24", "25", "29", "31", "35", "39", "46", "50",  "54", "55", "60", "64", "69", "74", "82", "88", "89", "90"])
    embed = discord.Embed(title=":revolving_hearts: Aşk Ölçer İnfo!", description="Ölçüm Sonucu Burda!", color=discord.Colour.red())
    embed.add_field(name="Toplam yüzde", value=f"<@{id}> ile {member.mention} aşk durumu = % {askdurum}", inline=False)
    embed.set_thumbnail(url="https://www.starpng.com/public/uploads/preview/red-heart-shaped-red-love-heart-shaped-png-image-and-clipart-101576169307f1r09kqckx.png")
    await ctx.channel.send(embed=embed)
 







@client.command()
async def slap(ctx, member: discord.Member):
    id = ctx.author.id
    yaratıcım = 935455852607987742

    if member.id == yaratıcım:
        #time.sleep(1)
        await ctx.channel.send("``Kendine Vur Lan!``")
        return
    embed = discord.Embed(title="Slap!", description=f"UNİTED STATES OF SLAPP", color=discord.Colour.red())
    embed.set_image(url="https://c.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif")
    embed.add_field(name="Slaped!!!", value=f"{member.mention}", inline=False)

    await ctx.channel.send(embed=embed)



@client.command()
async def nitrover(ctx, member: discord.Member):
    id = ctx.author.id
    yaratıcım = 935455852607987742

    if member.id == yaratıcım:
        #time.sleep(1)
        await ctx.channel.send("``Abimde Nitro Var Zaten!``")
        return
    embed = discord.Embed(title="Alsana Beleş Nitro", description=f"Kaçırma Bu Fırsatı!", color=discord.Colour.blue())
    embed.add_field(name="Nitron H.O", value=f"{member.mention} ADLI KULLANICIMIZA FREE NİTRO VERİLMİŞTİR VE BAŞINI ALDI")
    embed.set_image(url="https://c.tenor.com/tQM-V9L3g9YAAAAM/el-hareketi.gif")

    await ctx.channel.send(embed=embed)




    #@Bot.command()
    #async def link(ctx, member: discord.Member):
        #embed = discord.Embed(title="Botun Davet Linki!", description="", color=di)




#=========================================================================================
#=========================================================================================
#=========================================================================================




    

#client.run(os.getenv("TOKEN"))
client.run("OTM1Nzk0ODc1NjIwNzk4NTE0.YfD05A.ThRq8vW_vskY6uq1BFmck-Fn8s8")
