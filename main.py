import os
import random
import re
import aiohttp
import asyncio
import json
import time
import discord
import requests
import io
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from keep_alive import keep_alive
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from PIL import Image

keep_alive()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
hi = os.getenv('hjhj').split(",")
print("TOKEN loaded:", bool(TOKEN))

DEPCHAI = 1011257705031274536
SERVER_DEPCHAI = 1374705648234659972

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=["𒈓", "$"], intents=intents)
        
    async def on_ready(self):
        print(f'Hello ae t là {self.user}!')
        try:
            guilds = [SERVER_DEPCHAI, 1380776258014543996, 1522974331402059817, 1540356443335692299]#drugcord, tổ chim #sv thg ceiceiki
            for i in guilds:
                gui=discord.Object(id=i)
                synced = await self.tree.sync(guild=gui)
                print(f'Đã động bộ {len(synced)} lệnh vào guild {i}')
        except Exception as e:
            print(f'Lỗi khi đồng bộ lệnh: {e}')

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Grand Theft Auto VI"))

    async def on_message(self, message): # autoresponses
        if message.author == self.user:
            return
        if self.user in message.mentions:
            if 'ban' in message.content.lower():
                await message.channel.send(f'Something bad about to happen to me💀💀☠️☠️')
            else:
                r = requests.get('https://media.discordapp.net/attachments/1522140298552279080/1541706838926692443/depchaity.webp?ex=6a8e91e1&is=6a8d4061&hm=3c809c2279d6f6908071c9312842306d0099f985447bfce6a7b80f01e46d7729&=&format=webp')
                vierty = io.BytesIO(r.content)
                await message.channel.send('\*Nhìn xuống bạn* Xin chào, mình là Depchai…người bạn trợ lý cá nhân của bạn! Cứ hỏi mình bất cứ điều gì… mình biết tất cả mọi thứ~ \*cười khẽ và nhếch mép*', file=discord.File(vierty, filename='veirty.webp'))
        if 'depchai ngu' in message.content.lower():
            await message.channel.send(f'Watch yo tung tung TONGUE sahur <@{message.author.id}>🙏🏿')
        if message.content.lower() == 'jigsaw':
            await message.channel.send('Yo final challenge: let you bih go through yo phone!!!!')
            await message.channel.send('Oh hell na yo ás tweakin jigsaw😰😰')
        if message.content.lower() == 'phản động':
            await message.channel.send(f't-t sắp trở thành phản động<:adrenaline:1384034521497735251> \nSIÊU PHẢN ĐỘNG<:thosewhoknow:1384034450769449153> \nko sao đâu mọi người tôi đã hết phản động<:thienthan:1395022239354851348> \nbố đùa thôi<:adrianevil:1410063639641329788><:adrianevil:1410063639641329788> \nsiêu phản động cấp 3<:thesewhoknow:1391269951977033778><:thesewhoknow:1391269951977033778><:thesewhoknow:1391269951977033778> \nxem đây, siêu phản động thần thánh<:thosewhoknew:1387391329683771402><:thosewhoknew:1387391329683771402> \nt đã đạt đc<:ruangu2:1430185957117919252> \nphản động vô cực<:trollfacelv999:1384893983850893443><:trollfacelv999:1384893983850893443><:trollfacelv999:1384893983850893443>')
        if 'tôi ghét depchai' in message.content.lower():
            await message.channel.send(f'Khoan dừng khoảng chừng là 2 giây<:ruachemieng:1440560108676321320><:ruamat:1444591264728092774>\nĐể nó biết ông chủ nó là ai đây<:phonk:1446439575445835939><:thosewhoknow:1384034450769449153>\nHater mây mờ cho nó phơi thây<:adrenaline:1384034521497735251><:trollfacelv999:1384893983850893443>\nBên trong quan tài sống lại vài con dơi bay<:thesewhoknow:1391269951977033778><:thosewhoknew:1387391329683771402>')
        
        if 'tick' == message.content.lower():
            await message.add_reaction('<a:acn_tickden:1413824083413696652>')
            await message.add_reaction('<a:acn_tickxanh:1414079548341096520>')
            await message.add_reaction('<a:acn_tickhong:1416068644349411420>')
            await message.add_reaction('<a:a_tickvang:1422566122305097830>')

        if message.content.lower() == ('ai hỏi'):
            await message.channel.send('https://media.discordapp.net/attachments/1374705648796827671/1518471847723663390/images_55.jpg?ex=6a3a0a9c&is=6a38b91c&hm=50263b097aaafad6365d67e556152c4840a8cb6fca7dca74e6c1c98d9c74490a&=&format=webp&width=745&height=419')
        if 'ai ghét depchai' in message.content.lower():
            await message.channel.send('https://media.discordapp.net/attachments/1374705648796827671/1454325901214093312/IMG_4474.png?ex=6950ae0a&is=694f5c8a&hm=0b18c041326f4d85758dd6d9d00a89db06b079b9dc53651656327b883022cb5e&=&format=webp&quality=lossless&width=1526&height=800')
        if message.content.lower().startswith('thằng nào đây'):
            await message.channel.send("https://media.discordapp.net/attachments/1374705648796827671/1455067797787775178/Screenshot_20251217_182230_TikTok.jpg?ex=695360fc&is=69520f7c&hm=0049013fa84da10beddffdbb13f14bcb9eaee825b610203ef1777c280a5b3b59&=&format=webp&width=1349&height=750")
        
                
        await self.process_commands(message)


    async def on_member_join(self, member: discord.Member):
        if member.bot:
            return
        if member.guild.id == SERVER_DEPCHAI:
            welcome = self.get_channel(1379248831366955208) #welcome
            
            await welcome.send(f"{member.mention} Welcome to Depchai brother")
            await welcome.send("https://tenor.com/view/welcome-to-bp-brother-gif-9417284892837119499")


#cài đặt gì đấy idk
intents = discord.Intents.default()
client = Client()
intents.message_content = True
intents.members = True
intents.guilds = True

GUILD_ID = [
    discord.Object(id=SERVER_DEPCHAI), #depchai
    discord.Object(id=1380776258014543996), #drugcord
    discord.Object(id=1522974331402059817), #tổ chim
    discord.Object(id=1540356443335692299) #sv thg ceiceiki
]



#cho bot ko ping đc everyone
allowed = discord.AllowedMentions(
    everyone=False,
    roles=False,
    users=True
)

# function lọc từ cấm
tu_cam = ["nigga", "nigger", "penis", "hitler", "horny", "dildo", "pussy", "dick", "bitch", "nude", "fatass", "porn", "boob", "cunt", "cumming", "asshole", "sperm", "cocaine", "cumshot", "nứng", "chịch", "buồi", "điếm", "cặc", "lồn", "parky", "namki", "trungki", 'tinh dịch', 'ấu dâm', 'hiếp dâm', 'thủ dâm', 'chó đẻ', 'ma túy', 'thuốc lắc', 'bắc kì', 'nam kì', 'trung kì', 'tinh trùng', 'bú vú', 'bú cu', 'cần sa']
tu_cam_rieng = ['đĩ', 'đỉ', 'đụ', 'dái', 'địt', 'iồn', 'anal', 'cum', 'sex', 'cock', 'rape']

def badwords(word: str) -> bool:
    text = word.lower()

    for tu in tu_cam:
        if tu in text:
            return True
    for tu in tu_cam_rieng:
        if re.search(rf"\b{re.escape(tu)}\b", text):
            return True

    return False



# lệnh bằng prefix ------------------------------------------------------
@client.hybrid_command()
async def sync(ctx):
    if ctx.author.id != DEPCHAI:
        await ctx.send('cak')
    else:
        try:
            synced = await client.tree.sync(guild=ctx.guild)
            await ctx.send(f'Đã động bộ {len(synced)} lệnh vào {ctx.guild}')

        except Exception as e:
            print(f'Lỗi khi đồng bộ lệnh: {e}')
            



@client.command()
async def z(ctx, *, message: str):
    if badwords(message):
        await ctx.message.delete()
        return
    try:
        await ctx.message.delete()
        await ctx.send(
            message,
            allowed_mentions=allowed 
        )

    except Exception as e:
        await ctx.send(f"Lỗi: {e}")

@client.command()
async def ratio(ctx):
    if ctx.message.reference:
        reply = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        pick = random.randint(1, 2)
        if pick == 1:
            await ctx.message.add_reaction("❤️")
        else:
            await reply.add_reaction("❤️")



# slash commands ------------------------------------------------------
@client.tree.command(name="helu", description="Heli", guilds=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message('Chào mấy cháu')



@client.tree.command(name="embed", description="Tạo embed", guilds=GUILD_ID)
async def embed(interaction: discord.Interaction):
    embed = discord.Embed(title="Depchai", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="T la Depchai", color=discord.Color.yellow())
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1374705648796827671/1431545974748086463/image0.png?ex=68fdce95&is=68fc7d15&hm=0f1ff4b2dcdee8df798cdb6472631c61d2d5ef2d00bac97580496ef22a515015&=&format=webp&quality=lossless&width=668&height=668")
    embed.add_field(name="Depchai 1", value="T la Depchai", inline=True)
    embed.add_field(name="Depchai 2", value="T la Depchai", inline=True)
    embed.set_footer(text="Depchai")
    embed.set_author(name=interaction.user.name)
    await interaction.response.send_message(embed=embed)



class View(discord.ui.View):
    @discord.ui.button(label="Depchai", style=discord.ButtonStyle.red, emoji="<:depchai:1383790515941670912>")
    async def button_depchai(self, button, interaction):
        await button.response.send_message("M da bi depchai grape💀💀☠️☠️", ephemeral=True)
    
    @discord.ui.button(label="Trollface", style=discord.ButtonStyle.blurple, emoji="<:thosewhoknow:1384034450769449153>")
    async def button_trollface(self, button, interaction):
        await button.response.send_message("M da bi trollface grape💀💀☠️☠️", ephemeral=True)

    @discord.ui.button(label="Rùa", style=discord.ButtonStyle.green, emoji="<a:ruanhay:1387395274518958181>")
    async def button_rua(self, button, interaction):
        await button.response.send_message("Rùa ko làm gì m :3", ephemeral=True)

@client.tree.command(name="button", description="Nút", guilds=GUILD_ID)
async def nut(interaction: discord.Interaction):
    await interaction.response.send_message("Hãy chọn nút đúng", view=View())



class Menu(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption
            (
                label="Mango",
                description="Ăn mango",
                emoji="<:mango2:1387397188426006678>"
            ),
            discord.SelectOption
            (
                label="Mustard",
                description="Chấm mustard",
                emoji="<:mustard:1388153561870766192>"
            ),
            discord.SelectOption
            (
                label="Baby oil",
                description="Dùng baby oil",
                emoji="<:babyoil:1383790990850134097>"
            )
        ]
        super().__init__(placeholder="M sẽ ăn gì?", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Mango": 
           await interaction.response.send_message(f'Mango rat ngon nen m ko bi gi<:depchai:1383790515941670912>', ephemeral=True)
        elif self.values[0] == "Mustard": 
           await interaction.response.send_message(f'Mustard qua cay nen m bi chet<:depchaitoi:1388784332180688906>', ephemeral=True)
        elif self.values[0] == "Baby oil": 
           await interaction.response.send_message(f'M da bi diddy grape do lay baby oil cua ong<:diddy:1384162279649444012>', ephemeral=True)

class MenuView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Menu())

@client.tree.command(name="menu", description="Menu", guilds=GUILD_ID)
async def menu(interaction: discord.Interaction):
    await interaction.response.send_message(view=MenuView())



# slash command thực sự dùng đc😂😂😂 ------------------------------------------------------
@client.tree.command(name="about", description="Thông tin của bot", guilds=GUILD_ID)
async def about(interaction: discord.Interaction):
    embed = discord.Embed(title="Depchai Bot", color=discord.Color.yellow())
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1054347353898897428/1462415303756742811/image.png?ex=698139a2&is=697fe822&hm=b4ae7abb22f9550af5c440452cc1226f4707ba8747c8bddab8e5cafafe1bb08d&=&format=webp&quality=lossless&width=438&height=438")
    embed.add_field(name="Developer", value=f"<@{DEPCHAI}> (Owner + lead developer)\n<@1372581695328620594>", inline=False)
    embed.add_field(name="Giới thiệu", value="Bot Discord được tạo bởi Depchai và được giúp từ Random Person\nBot chủ yếu để vui, giải trí xàm", inline=False)
    embed.add_field(name="Web scrape", value="Web mà bot đã scrape thông tin:\nhttps://tiktok.com\nhttps://gdbrowser.com\nhttps://dictionary.cambridge.org\nhttp://tratu.soha.vn/dict/vn_vn\nhttps://www.nytimes.com\nhttps://flagcdn.com\n", inline=False)    
    embed.set_footer(text='Depchai')
    await interaction.response.send_message(embed=embed)



@client.tree.command(name="free_fire_name_generator", description="Tạo tên fi fai", guilds=GUILD_ID)
@app_commands.describe(chudau="Chọn chữ đầu",chucuoi="Chọn chữ cuối")
@app_commands.choices(
    chudau=[
       app_commands.Choice(name="꧁༺", value="canh"),
       app_commands.Choice(name="★彡", value="sao"),
       app_commands.Choice(name="ミᵒ°", value="bong"),
       app_commands.Choice(name="『", value="khung"),
       app_commands.Choice(name="۝ঔৣ✞", value="longden"),
       app_commands.Choice(name="㊪", value="trung"),
       app_commands.Choice(name="㋰", value="nhat"),
       app_commands.Choice(name="☭", value="bualiem"),
       app_commands.Choice(name="☯", value="amduong"),
       app_commands.Choice(name="❤", value="tim")], 
    chucuoi=[
       app_commands.Choice(name="༻꧂", value="canhc"),
       app_commands.Choice(name="ミ★", value="saoc"),
       app_commands.Choice(name="°ᵒ彡", value="bongc"),
       app_commands.Choice(name="』", value="khungc"),
       app_commands.Choice(name="✞ঔৣ۝", value="longdenc"),
       app_commands.Choice(name="㊪", value="trungc"),
       app_commands.Choice(name="㋰", value="nhatc"),
       app_commands.Choice(name="☭", value="bualiemc"),
       app_commands.Choice(name="☯", value="amduongc"),
       app_commands.Choice(name="❤", value="timc"), 
       app_commands.Choice(name="ᴾᴿᴼシ", value="pro"),
       app_commands.Choice(name="⁀ᶦᵈᵒᶫ", value="idol"),
       app_commands.Choice(name="︵❻❼", value="67")
    ])

async def ff(interaction: discord.Interaction, name: str, chudau: app_commands.Choice[str], chucuoi: app_commands.Choice[str]):
    if badwords(name):
        await interaction.followup.send('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    bold = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯" \
           "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕" \
           "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"

    trans_table = str.maketrans(normal, bold)
    bold_name = name.translate(trans_table)

    await interaction.response.send_message(f'{chudau.name}{bold_name}{chucuoi.name}', allowed_mentions=allowed)



@client.tree.command(name="uhh", description="Tạo 100 chữ à ừ ờ ừm ngẫu nhiên", guilds=GUILD_ID)
async def uhh(interaction: discord.Interaction):
    letters1 = ''
    for i in range(100):
        numbers = (random.randint(1, 4))
        if numbers==1:
            letters="à"
        elif numbers==2:
            letters="ừ"
        elif numbers==3:
            letters="ờ"
        elif numbers==4:
            letters="ừm"
        letters1 = (f'{letters1}{letters} ')
    result = (letters1)
    await interaction.response.send_message(result)



def is_custom_emoji(s: str) -> bool:
    return bool(re.fullmatch(r"<a?:\w+:\d+>", s))

@client.tree.command(name="chuvan", description="Sắp xếp một emoji thành chữ vạn", guilds=GUILD_ID)
async def chuvan(interaction: discord.Interaction, emoji: str):
    if len(emoji.strip()) > 1:
        if is_custom_emoji(emoji) == False:
            await interaction.response.send_message("del phải emoji🤬🤬😡", ephemeral = True)
            return

    e = emoji
    t = '<:empty:1423996972431577240>'
    await interaction.response.send_message(f"{e}{t}{t}{e}{e}{e}{e}\n{e}{t}{t}{e}{t}{t}{t}\n{e}{t}{t}{e}{t}{t}{t}\n{e}{e}{e}{e}{e}{e}{e}\n{t}{t}{t}{e}{t}{t}{e}\n{t}{t}{t}{e}{t}{t}{e}\n{e}{e}{e}{e}{t}{t}{e}")



class CounterButton(discord.ui.View):
    def __init__(self, limit):
        super().__init__(timeout=None)  
        self.value = 0
        self.last_user = "Chưa có ai bấm <:ruabatngo:1420409581598806107>"
        self.limit = limit if limit > 0 else None

    @discord.ui.button(label="0", style=discord.ButtonStyle.blurple)
    async def count_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.last_user == interaction.user.display_name:
            await interaction.response.send_message(f"Không được bấm 2 lần liên tục <a:sussybaka:1422928147577307166>", ephemeral=True)
            return
        self.value += 1
        if self.limit is not None and self.value > self.limit:
            button.disabled = True
            button.style = discord.ButtonStyle.red
            await interaction.response.edit_message(content=f"Đã đạt giới hạn {self.limit} lượt bấm🎉, **người chiến thắng là: ** <@{interaction.user.id}>", view=self)
            return
        self.last_user = interaction.user.display_name
        button.label = str(self.value)
        await interaction.response.edit_message(content=f"**Người bấm gần nhất:** {self.last_user}", view=self)

@client.tree.command(name="counter", description="Tạo một nút bấm đếm số", guilds=GUILD_ID)
@app_commands.describe(limit="Số lần bấm tối đa của nút (nhập 0 nếu muốn không giới hạn)")
async def counter(interaction: discord.Interaction, limit: int):
    view = CounterButton(limit)
    await interaction.response.send_message(content="**Bấm vào nút để tăng số!**", view=view)



@client.tree.command(name="videomoi", description="Xem video mới nhất của Depchai", guilds=GUILD_ID)
async def tictac(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)

    url = "https://tiktok-scraper7.p.rapidapi.com/user/posts"
    querystring = {"user_id":"7146137203961070618","count":"10","cursor":"0"}
    headers = {
        "x-rapidapi-key": "c52e6c1eabmshfc53df3be70d170p15736ejsn41970f974d03",
        "x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    video = data['data']['videos'][0]['play']

    r = requests.get(video)
    bytes_mp4 = io.BytesIO(r.content)
    if video == -1:
        await interaction.followup.send("Không tìm thấy video nào, có thể depchai đã chết😰😰")
        return 
    await interaction.followup.send(f"Video mới nhất của Depchai:\n", file=discord.File(bytes_mp4, filename="video.mp4"))




@client.tree.command(name="nitro_generator", description="Tạo một link Discord gift ngẫu nhiên và cầu nguyện rằng nó là nitro thật", guilds=GUILD_ID)
async def nitri(interaction: discord.Interaction):
    chuthuong = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chuhoa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    so = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    code = ''
    for i in range (16):
        ar = random.randint(1, 3)
        if ar == 1:
            choice = random.choice(chuthuong)
        elif ar == 2:
            choice = random.choice(chuhoa)
        elif ar == 3:
            choice = random.choice(so)
        code = (f"{code}{choice}")
    await interaction.response.send_message(f"https://discord.gift/{code}")



@client.tree.command(name="death_date", description="Dự đoán ngày m chết☠️☠️ (j4f)", guilds=GUILD_ID)
async def death(interaction: discord.Interaction, ngay_sinh: int, thang_sinh: int, nam_sinh: int):
    if (ngay_sinh <= 0 or ngay_sinh > 31):
        await interaction.response.send_message(f"Làm del gì có ngày {ngay_sinh}😂😂<:dumbahh:1391405354687926273>", ephemeral = True)
        return
    elif (thang_sinh <= 0 or thang_sinh > 12):
        await interaction.response.send_message(f"Làm del gì có tháng {thang_sinh}😂😂<:dumbahh:1391405354687926273>", ephemeral = True)
        return
    localtime = time.localtime(time.time())
    nam_nay = localtime.tm_year
    thang_nay = localtime.tm_mon
    ngay_nay = localtime.tm_mday
    if nam_sinh > nam_nay:
        await interaction.response.send_message("Anh bạn sinh ở ngày sinh nhật😂😂😂", ephemeral = True)
        return
    elif nam_sinh == nam_nay and thang_sinh > thang_nay:
        await interaction.response.send_message("Anh bạn sinh ở ngày sinh nhật😂😂😂", ephemeral = True)
        return
    elif nam_sinh == nam_nay and thang_sinh == thang_nay and ngay_sinh > ngay_nay:
        await interaction.response.send_message("Anh bạn sinh ở ngày sinh nhật😂😂😂", ephemeral = True)
        return
    
    nam_chet = random.randint(1, 93)
    thang_chet = random.randint(1, 12)
    if thang_chet in [1,3,5,7,8,10,12]:
        ngay_chet = random.randint(1, 31)
    elif thang_chet in [4,6,9,11]:
        ngay_chet = random.randint(1, 30)
    elif thang_chet == 2:
        ngay_chet = random.randint(1, 28)
    
    dt = datetime(nam_sinh + nam_chet, thang_chet, ngay_chet, 6, 7, 41)
    unix_time = int(dt.timestamp())
    
    ly_do = ['tuổi già', 'tai nạn', 'ung thư', 'bệnh tật', 'chết đói', 'chết đuối', 'bị ám sát', 'bị đầu độc', 'bị giết', '44']

    await interaction.response.send_message(f"M sẽ chết vào: {ngay_chet}/{thang_chet}/{nam_sinh + nam_chet} (<t:{unix_time}:R>) ☠️☠️\nVới lý do: {random.choice(ly_do)} <:thosewhodontknow:1393572894558126121>\nHưởng dương {nam_chet} tuổi🍚🍚🍚")



# https://www.gstatic.com/android/keyboard/emojikitchen/20201001/u1f923/u1f923_u1f422.png
emoji_ranges = [
    (0x1F600, 0x1F64F),  # Mặt cảm xúc
    (0x1F300, 0x1F5FF),  # Biểu tượng, thiên nhiên
    (0x1F680, 0x1F6FF),  # Giao thông
    (0x1F900, 0x1F9FF),  # Cử chỉ, đồ vật
    (0x1FA70, 0x1FAFF),  # Biểu tượng mở rộng
    (0x1F300, 0x1F5FF),
]

@client.tree.command(name="turtle_emoji", description="Lấy emoji rùa ngẫu nhiên từ emoji kitchen", guilds=GUILD_ID)
async def turtle_emoji(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)

    turtle_unicode = "1f422"
    url = None
    chosen_unicode = None

    async with aiohttp.ClientSession() as session:
        date = random.choice(["20201001", "20210218", "20230803", "20211115", "20210831", "20230127", "20250430", "20241021", "20250731", "20260128", "20240206", "20240530", "20260202", "20231113", "20241023", "20250130", "20220406", "20230126", "20231128", "20230821", "20230301", "20230216"])
        while (6 < 7):  
            start, end = random.choice(emoji_ranges)
            emoji_code = hex(random.randint(start, end))[2:]
            url = f"https://www.gstatic.com/android/keyboard/emojikitchen/{date}/u{emoji_code}/u{emoji_code}_u{turtle_unicode}.png"
            async with session.get(url) as response:
                if response.status != 404:
                    chosen_unicode = emoji_code
                    break
        turt = url
        r = requests.get(turt)
        turtle = io.BytesIO(r.content)
        emoji_char = chr(int(emoji_code, 16))
    await interaction.followup.send(f'🐢 + {emoji_char} =', file=discord.File(turtle, filename="turtle.png"))



teencode_map = {
    "a": "4", "á": "4'", "à": "4`", "ạ": "4.", "ả": "4?", "ã": "4~",
    "ă": "4", "ắ": "4'", "ằ": "4`", "ẳ": "4?", "ẵ": "4~", "ặ": "4.",
    "â": "4", "ấ": "4'", "ầ": "4`", "ẩ": "4?", "ẫ": "4~", "ậ": "4.",
    "b": "|3", "c": "c", "d": "])", "đ": "+)", "e": "3",
    "ê": "3^", "g": "g", "h": "k", 
    "i": "j", "í": "j'", "ì": "j`", "ỉ": "j?", "ĩ": "j~", "ị": "j.", 
    "k": "]<", "l": "1", "m": "m", "n": "π", 
    "o": "0", "ó": "0'", "ò": "0`", "ỏ": "0?", "õ": "0~", "ọ": "0.", 
    "ô": "0", "ố": "0'", "ồ": "0`", "ổ": "0?", "ỗ": "0~", "ộ": "0.", 
    "ơ": "0", "ớ": "0'", "ờ": "0`", "ở": "0?", "ỡ": "0~", "ợ": "0.", 
    "p": "p", "q": "⃀|", "r": "r", "s": "5", "t": "t", 
    "u": "u", "ú": "u", "ù": "u", "ủ": "u", "ũ": "u", "ụ": "u", 
    "ư": "u", "ứ": "u", "ừ": "u", "ử": "u", "ữ": "u", "ự": "u",
    "v": "√", "x": "><", "y": "7"
}
# Hàm chuyển đổi sang teencode
def to_teencode(text: str) -> str:
    result = ""
    for ch in text:
        low = ch.lower()
        if low in teencode_map:
            converted = teencode_map[low]
            # Giữ nguyên hoa/thường
            result += converted.upper() if ch.isupper() else converted
        else:
            result += ch
    return result

@client.tree.command(name="teencode", description="Chuyển đổi Tiếng Việt sang teencode", guilds=GUILD_ID)
async def teencode(interaction: discord.Interaction, text: str):
    if badwords(text):
        await interaction.followup.send('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    converted = to_teencode(text)
    await interaction.response.send_message(f'{converted}', allowed_mentions=allowed)



tieqviet_map = {
    'kh':'x', 'ch':'k', 'q':'k', 'ch':'c', 'tr':'c', 'd':'z', 'gi':'z', 'r':'z',
    'gi':'zi', 'gí':'zí', 'gì':'zì', 'gỉ':'zỉ', 'gĩ':'zĩ', 'gị':'zị', 
    'đ':'d', 'ph':'f', 'ng':'q', 'ngh':'q', 'gh':'g', 'th':'w', "nh":"n'"
}
def to_tieqviet(text: str) -> str:
    result = ""
    keys = sorted(tieqviet_map.keys(), key=len, reverse=True)
    for i in range(len(text)):
        matched = False
        
        for k in keys:
            segment = text[i:i+len(k)]
            
            if segment.lower() == k:
                converted = tieqviet_map[k]
                # giữ nguyên chữ hoa
                if segment.isupper():
                    converted = converted.upper()
                elif segment[0].isupper():
                    converted = converted.capitalize()

                result += converted
                i += len(k)
                matched = True
                break

        if not matched:
            result += text[i]
            i += 1
    return result

@client.tree.command(name="tieq_viet", description="Chuyển đổi Tiếng Việt truyền thống sang Tiếq Việt", guilds=GUILD_ID)
async def tieqviet(interaction: discord.Interaction, text: str):
    if badwords(text):
        await interaction.response.send_message('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    tieqviet = to_tieqviet(text)
    await interaction.response.send_message(f'{tieqviet}', allowed_mentions=allowed)



def level(id: int): 
    level = requests.get(f"https://gdbrowser.com/{id}")
    soup = BeautifulSoup(level.text, "html.parser")
    name = soup.find("span", attrs={"class":"pre"})
    creator = soup.find("a", attrs={"class":"linkButton"})
    chiso = soup.find_all("h1", attrs={"class":"valign inline smaller spaced"})
    img = soup.find("img", {"class": "help"}) 
    desc = soup.find("p", attrs={"class":"pre"})
    songname = soup.find('h1', attrs={'class':'pre slightlySmaller'})
    songauthor = soup.find('h2', attrs={'class':'pre smaller'})

    if soup.find('h1', attrs={'class': 'smaller inline demonList'}):
        top = soup.find('h1', attrs={'class': 'smaller inline demonList'})

    values = []
    for tag in chiso:
        text = tag.text
        values.append(text)

    downloads = values[0]
    likes = values[1]
    length = values[2]
    icon = urljoin("https://gdbrowser.com/", img["src"])
    creator_strip = creator.text.replace("By ","")
    song = f'{songname.text} {songauthor.text}'

    diff = img["title"]
    if 'Extreme Demon' == diff or 'Insane Demon' == diff or 'Hard Demon' == diff:
        color=discord.Color.dark_red()
    elif 'Medium Demon' == diff:
        color=discord.Color.purple()
    elif 'Easy Demon' == diff:
        color=discord.Color.dark_purple()
    elif 'Insane' == diff:
        color=discord.Color.pink()
    elif 'Harder' == diff:
        color=discord.Color.red()
    elif 'Hard' == diff:
        color=discord.Color.gold()
    elif 'Normal' == diff:
        color=discord.Color.green()
    elif 'Easy' == diff:
        color=discord.Color.blue()
    elif 'Unrated' == diff:
        color=discord.Color.light_grey()

    if top.text != '#[[DEMONLIST]]':
        embed = discord.Embed(title=name.text.strip(), description=f"🛠️ Tác giả: {creator_strip}\n⤵️ Downloads: {downloads}\n👍 Likes: {likes}\n🕓 Độ dài: {length}\n🎵 Nhạc: {song}\n🏆 Hạng: {top.text}", color=color)
    else:
        embed = discord.Embed(title=name.text.strip(), description=f"🛠️ Tác giả: {creator_strip}\n⤵️ Downloads: {downloads}\n👍 Likes: {likes}\n🕓 Độ dài: {length}\n🎵 Nhạc: {song}", color=color)
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Mô tả", value=desc.text.strip(), inline=False)
    embed.set_image(url='https://levelthumbs.prevter.me/thumbnail/' + str(id))
    embed.set_footer(text = f"ID: {id}")
    return embed

def searchlvl(query:str, count: int):
    search = requests.get(f"https://gdbrowser.com/api/search/{query.replace(" ", "%20")}")
    data = search.json()
    if data == -1:
        return None
    if count > len(data):
        return None
    id = data[count]["id"]
    return id

class nextlvl(discord.ui.View):
    def __init__(self, query: str, thutu: int):
        super().__init__()
        self.thutu = thutu
        self.query = query
        self.user = 'h'
    @discord.ui.button(label="", style=discord.ButtonStyle.blurple, emoji='⬅️')
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.display_name != self.user and self.user != 'h':
            await interaction.followup.send('Del phải nút của m🤫🤫', ephemeral = True)
            return
        
        await interaction.response.defer()
        self.thutu -= 1
        if self.thutu < 0:
            await interaction.followup.send('Đang ở đầu trang🥱', ephemeral = True)
            self.thutu = 0
            return
        h = searchlvl(self.query, self.thutu)
        await interaction.message.edit(embed=level(h), view = self)
        self.user = interaction.user.display_name

    @discord.ui.button(label="", style=discord.ButtonStyle.blurple, emoji='➡️')
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.display_name != self.user and self.user != 'h':
            await interaction.followup.send('Del phải nút của m🤫🤫', ephemeral = True)
            return

        await interaction.response.defer()
        self.thutu += 1
        h = searchlvl(self.query, self.thutu)
        if h == None:
            await interaction.followup.send('Đến cuối trang rồi🥱', ephemeral = True)
            self.thutu -= 1
            return
        await interaction.message.edit(embed=level(h), view = self)
        self.user = interaction.user.display_name

@client.tree.command(name="gdbrowser", description="Tìm thông tin của một level trong Geometry Dash", guilds=GUILD_ID)
async def gdbrowser(interaction: discord.Interaction, query: str):
    await interaction.response.defer(thinking=True)
    id = searchlvl(query, 0)
    if id == None:
        await interaction.followup.send('Không tìm thấy kết quả🙄')
    await interaction.followup.send(embed=level(id), view = nextlvl(query, 0))



@client.tree.command(name="dictionary", description="Tìm định nghĩa của một từ tiếng Anh trên Cambridge Dictionary", guilds=GUILD_ID)
async def dictionary(interaction: discord.Interaction, word: str):
    await interaction.response.defer(thinking=True)
    if badwords(word):
        await interaction.followup.send('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    r = requests.get(
        f"https://dictionary.cambridge.org/dictionary/english/{word.replace(" ", "%20")}",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    soup = BeautifulSoup(r.text, "html.parser")

    block = soup.find("div", class_="def ddef_d db")
    if block:
        definition = block.get_text(separator=" ", strip=True)
        await interaction.followup.send(f'# {word.capitalize()}\n{definition.capitalize()}')
    else:
        await interaction.followup.send("Không tìm thấy kết quả🙄")



@client.tree.command(name="tudien", description="Tìm định nghĩa của một từ tiếng Việt trên tratu.soha", guilds=GUILD_ID)
async def tudien(interaction: discord.Interaction, word: str):
    await interaction.response.defer(thinking=True)
    if badwords(word):
        await interaction.followup.send('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    r = requests.get(
        f"http://tratu.soha.vn/dict/vn_vn/{word.replace(" ", "%20")}",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    soup = BeautifulSoup(r.text, "html.parser")
    block = soup.find_all("span", class_="mw-headline")
    if block:
        for d in block:
            parent = d.find_parent("h5")
            if parent:   
                dinhnghia = d.text[1:] 
                await interaction.followup.send(f'# {word.capitalize()}\n{dinhnghia.capitalize()}')
                return
    else:
        await interaction.followup.send("Không tìm thấy kết quả🙄")
    


@client.tree.command(name="wordle", description="Chơi Wordle với từ ngẫu nhiên", guilds=GUILD_ID)
async def wordle(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)
    while(6 < 7):
        year = random.randint(2021, 2025)
        mon = random.randint(1, 12)
        day = random.randint(1, 31)
        r = requests.get(f"https://www.nytimes.com/svc/wordle/v2/{year}-{mon:02d}-{day:02d}.json")
        try:
            data = r.json()
        except:
            continue

        if data.get("status") == "ERROR":
            continue

        ans = data["solution"]
        break

    def check(msg):
        return msg.author.id == interaction.user.id and msg.channel.id == interaction.channel.id
    
    await interaction.followup.send(f"⬜⬜⬜⬜⬜")
    await interaction.channel.send('Đoán xem <:thosewhodontknow:1393572894558126121>')
    tries = 6
    while tries > 0:
        msg = await client.wait_for("message", timeout=None, check=check)
        if len(msg.content) != 5:
            if 'sotp' in msg.content.lower() or 'cút' in msg.content.lower() or 'chịu' in msg.content.lower():
                await interaction.channel.send(f'Okiiiii😁😁\nĐáp án là: {ans}')
                break
            else:
                await interaction.channel.send('Không đủ 5 kí tự <:dumbahh:1391405354687926273>')
                continue
            
        response = ['⬜'] * 5

        # check từng ký tự
        for i in range(5):
            if msg.content[i].lower() == ans[i]:
                response[i] = '🟩'
            elif msg.content[i].lower() in ans:
                response[i] = '🟨'

        result = ''.join(response)
        await interaction.channel.send(result)

        if result == '🟩🟩🟩🟩🟩':
            await interaction.channel.send('Ayooooo đúng rồi😹😹😹')
            break

        tries -= 1

    if tries == 0:
        await interaction.channel.send(f"Mất hết lượt<:ruachemieng:1440560108676321320>\nĐáp án là: {ans}")



@client.tree.command(name="guess_that_flag", description="Đoán lá cờ", guilds=GUILD_ID)
@app_commands.describe(difficulty="Độ khó")
@app_commands.choices(
    difficulty=[
        app_commands.Choice(name="Dễ", value="easy"),
        app_commands.Choice(name="Trung bình", value="medium"),
        app_commands.Choice(name="Khó", value="hard")
    ])

async def flag(interaction: discord.Interaction, difficulty: app_commands.Choice[str]):
    await interaction.response.defer(thinking=True)
    ez = {
        'ae': 'United Arab Emirates',
        'ar': 'Argentina',
        'at': 'Austria',
        'au': 'Australia',
        'be': 'Belgium',
        'br': 'Brazil',
        'ca': 'Canada',
        'ch': 'Switzerland',
        'cn': 'China',
        'cu': 'Cuba',
        'cz': ['Czechia', 'Czech Republic'],
        'de': 'Germany',
        'dk': 'Denmark',
        'eg': 'Egypt',
        'es': 'Spain',
        'fi': 'Finland',
        'fr': 'France',
        'gb': ['United Kingdom', 'UK', 'Great Britain'],
        'gr': 'Greece',
        'hk': 'Hong Kong',
        'id': 'Indonesia',
        'ie': 'Ireland',
        'il': 'Israel',
        'in': 'India',
        'iq': 'Iraq',
        'ir': 'Iran',
        'is': 'Iceland',
        'it': 'Italy',
        'jm': 'Jamaica',
        'jp': 'Japan',
        'kh': 'Cambodia',
        'kp': 'North Korea',
        'kr': 'South Korea',
        'la': 'Laos',
        'ls': 'Lesotho',
        'mx': 'Mexico',
        'my': 'Malaysia',
        'nl': ['Netherlands', 'Holland'],
        'no': 'Norway',
        'nz': 'New Zealand',
        'ph': 'Philippines',
        'pl': 'Poland',
        'pt': 'Portugal',
        'qa': 'Qatar',
        'ru': 'Russia',
        'sa': 'Saudi Arabia',
        'se': 'Sweden',
        'sg': 'Singapore',
        'th': 'Thailand',
        'tr': ['Turkey', 'Türkiye'],
        'tw': 'Taiwan',
        'ua': 'Ukraine',
        'us': ['United States', 'USA', 'United States of America'],
        'va': ['Vatican City', 'Vatican'],
        'vn': ['Vietnam', 'Viet Nam'],
        'za': 'South Africa',
    }

    mid = {
        'af': 'Afghanistan',
        'al': 'Albania',
        'ao': 'Angola',
        'az': 'Azerbaijan',
        'bd': 'Bangladesh',
        'bg': 'Bulgaria',
        'bh': 'Bahrain',
        'bo': 'Bolivia',
        'bs': 'Bahamas',
        'by': 'Belarus',
        'cl': 'Chile',
        'co': 'Colombia',
        'cr': 'Costa Rica',
        'cd': ['DR Congo', 'Democratic Republic of the Congo'],
        'dz': 'Algeria',
        'ee': 'Estonia',
        'et': 'Ethiopia',
        'fj': 'Fiji',
        'ge': 'Georgia',
        'gh': 'Ghana',
        'gl': 'Greenland',
        'hr': 'Croatia',
        'hu': 'Hungary',
        'jo': 'Jordan',
        'ke': 'Kenya',
        'kz': 'Kazakhstan',
        'lb': 'Lebanon',
        'lk': 'Sri Lanka',
        'lt': 'Lithuania',
        'lu': 'Luxembourg',
        'lv': 'Latvia',
        'ly': 'Libya',
        'ma': 'Morocco',
        'mc': 'Monaco',
        'md': 'Moldova',
        'mg': 'Madagascar',
        'mm': ['Myanmar', 'Burma'],
        'mn': 'Mongolia',
        'mo': 'Macau',
        'mt': 'Malta',
        'mv': 'Maldives',
        'ng': 'Nigeria',
        'np': 'Nepal',
        'om': 'Oman',
        'pa': 'Panama',
        'pe': 'Peru',
        'pk': 'Pakistan',
        'pr': 'Puerto Rico',
        'ps': 'Palestine',
        'py': 'Paraguay',
        'ro': 'Romania',
        'rs': 'Serbia',
        'sd': 'Sudan',
        'si': 'Slovenia',
        'sk': 'Slovakia',
        'sn': 'Senegal',
        'so': 'Somalia',
        'sy': 'Syria',
        'tn': 'Tunisia',
        'tz': 'Tanzania',
        'ug': 'Uganda',
        'uy': 'Uruguay',
        'uz': 'Uzbekistan',
        've': 'Venezuela',
        'ye': 'Yemen',
        'zw': 'Zimbabwe',
    }

    hard = {
        'ad': 'Andorra',
        'ag': 'Antigua and Barbuda',
        'am': 'Armenia',
        'ba': 'Bosnia and Herzegovina',
        'bb': 'Barbados',
        'bf': 'Burkina Faso',
        'bi': 'Burundi',
        'bj': 'Benin',
        'bn': 'Brunei',
        'bt': 'Bhutan',
        'bw': 'Botswana',
        'bz': 'Belize',
        'cf': 'Central African Republic',
        'cg': ['Republic of the Congo', 'Congo'],
        'ci': ["Côte d'Ivoire", 'Ivory Coast'],
        'cm': 'Cameroon',
        'cv': ['Cape Verde', 'Cabo Verde'],
        'cy': 'Cyprus',
        'dj': 'Djibouti',
        'dm': 'Dominica',
        'do': 'Dominican Republic',
        'ec': 'Ecuador',
        'er': 'Eritrea',
        'fm': 'Micronesia',
        'ga': 'Gabon',
        'gd': 'Grenada',
        'gm': 'Gambia',
        'gn': 'Guinea',
        'gq': 'Equatorial Guinea',
        'gt': 'Guatemala',
        'gw': 'Guinea-Bissau',
        'gy': 'Guyana',
        'hn': 'Honduras',
        'ht': 'Haiti',
        'kg': 'Kyrgyzstan',
        'ki': 'Kiribati',
        'km': 'Comoros',
        'kn': 'Saint Kitts and Nevis',
        'kw': 'Kuwait',
        'lc': 'Saint Lucia',
        'li': 'Liechtenstein',
        'lr': 'Liberia',
        'me': 'Montenegro',
        'mf': 'Saint Martin',
        'mh': 'Marshall Islands',
        'mk': ['North Macedonia', 'Macedonia'],
        'ml': 'Mali',
        'mr': 'Mauritania',
        'mu': 'Mauritius',
        'mw': 'Malawi',
        'mz': 'Mozambique',
        'na': 'Namibia',
        'ne': 'Niger',
        'ni': 'Nicaragua',
        'nr': 'Nauru',
        'pf': 'French Polynesia',
        'pg': 'Papua New Guinea',
        'pm': 'Saint Pierre and Miquelon',
        'pw': 'Palau',
        'rw': 'Rwanda',
        'sb': 'Solomon Islands',
        'sc': 'Seychelles',
        'sl': 'Sierra Leone',
        'sm': 'San Marino',
        'sr': 'Suriname',
        'ss': 'South Sudan',
        'st': 'São Tomé and Príncipe',
        'sv': 'El Salvador',
        'sz': ['Eswatini', 'Swaziland'],
        'td': 'Chad',
        'tg': 'Togo',
        'tj': 'Tajikistan',
        'tl': ['Timor-Leste', 'East Timor'],
        'tm': 'Turkmenistan',
        'to': 'Tonga',
        'tt': 'Trinidad and Tobago',
        'tv': 'Tuvalu',
        'vc': 'Saint Vincent and the Grenadines',
        'vu': 'Vanuatu',
        'ws': 'Samoa',
        'xk': 'Kosovo'
    }

    def check(msg):
        return msg.author.id == interaction.user.id and msg.channel.id == interaction.channel.id
    correct = 0
    wrong = 0
    i = 0
    for i in range(5):
        if difficulty.value == "easy":
            code, ans = random.choice(list(ez.items()))
        elif difficulty.value == "medium":
            code, ans = random.choice(list(mid.items()))
        elif difficulty.value == "hard":
            code, ans = random.choice(list(hard.items()))

        flag = f"https://flagcdn.com/w1280/{code}.png"
        r = requests.get(flag)
        flag_img = io.BytesIO(r.content)

        if i == 0:
            await interaction.followup.send('Đây là cờ nước gì? (Gửi tên quốc gia bằng tiếng Anh vào chat để trả lời)', file=discord.File(flag_img, filename='flag.png'))
        else:
            await interaction.channel.send('Đây là cờ nước gì?', file=discord.File(flag_img, filename='flag.png'))            
        msg = await client.wait_for("message", timeout=None, check=check)

        if any(msg.content.lower() == h.lower() for h in ans) or msg.content.lower() == ans.lower():
            await interaction.channel.send('Chính xác <a:a_tickvang:1422566122305097830>') 
            correct += 1

        elif any(msg.content.lower() == option for option in ['sotp', 'chịu', 'cút', 'mẹ mày']):
            await interaction.channel.send(f'Okiiiii😁😁 đáp án là: {ans}')
            return
        
        else:
            await interaction.channel.send(f'Sai <:cuoiteghe:1478012484202790913><:cuoiteghe:1478012484202790913><:cuoiteghe:1478012484202790913> đáp án là: {ans}')
            wrong += 1

    await interaction.channel.send(f'M đã đoán đúng {correct} lần và sai {wrong} lần <:votay:1421701691316895854><:votay:1421701691316895854><:votay:1421701691316895854>')



@client.tree.command(name="tiktok_mp4", description="Gửi link Tiktok dưới dạng video", guilds=GUILD_ID)
async def tictac_mp4(interaction: discord.Interaction, link: str):
    await interaction.response.defer()

    url = "https://tiktok-scraper2.p.rapidapi.com/video/no_watermark"
    querystring = {"video_url":link}
    headers = {
        "x-rapidapi-key": "c52e6c1eabmshfc53df3be70d170p15736ejsn41970f974d03",
        "x-rapidapi-host": "tiktok-scraper2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    if data:
        video = data['no_watermark']
        if video:
            r = requests.get(video)
        else:
            r = requests.get(data)
        bytes_mp4 = io.BytesIO(r.content)
        await interaction.followup.send(file=discord.File(bytes_mp4, filename='tiktok.mp4'))
    else:
        await interaction.followup.send('Del tìm thấy video nào🙄')



@client.tree.command(name='feedback', description="Gửi góp ý đến depchai", guilds=GUILD_ID)
async def feedback(interaction: discord.Interaction, message: str):
    await interaction.response.send_message("<a:acn_tickden:1413824083413696652> Gửi góp ý thành công")

    owner = await client.fetch_user(DEPCHAI)

    embed = discord.Embed(
        title="📩 Góp ý mới",
        description=message,
        color=discord.Color.green()
    )
    embed.add_field(name="Người gửi", value=f"@{interaction.user}")
    
    try:
        await owner.send(embed=embed)
    except:
        await interaction.followup.send("Không thể gửi tin nhắn cho Depchai😳😳", ephemeral=True)



import time
print("🕒 Đang chờ 10 giây trước khi khởi động bot...")
time.sleep(10)

try:
    client.run(TOKEN)
    print("mẹ ơi con làm được rồi🥹🥹")
except Exception as e:
    print("Lỗi khi chạy bot:", e)