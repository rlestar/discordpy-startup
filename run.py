import discord #discordでBOTを使うのにこれが必ず
import random
import os

client = discord.Client()
@client.event #BOT起動時にCMDに表示される部分で無くてもよい
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
def callnick(message):
       nick = message.author.nick
       if nick is None:
        return message.author.name
       else:
        return nick    



server = 632216411514601506
lot_channel_id = 761856789888499712
@client.event
async def on_message(message): #メッセージを受け取る関数なので必ず必要
       global choice
       choice = False
       with open("giji.txt", "r",encoding="utf-8_sig") as g:
         gij = g.read()
       giji=gij.split('\n')
       if message.content == 'ブキ1':
            with open("buki.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'ブキ4':
             with open("buki.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
             textlist = data.split("\n")
             choice1 =random.choice(textlist)
             choice2 =random.choice(textlist)
             choice3 =random.choice(textlist)
             choice4 =random.choice(textlist)
             embed=discord.Embed(title=f"{callnick(message)}さんたちのブキは",description=choice1+"\n"+choice2+"\n"+choice3+"\n"+choice4+"\n"+"です。")
             await message.channel.send(embed=embed)
       elif message.content == 'ヒーロー1':
            with open("hero.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'シューター1':
            with open("shooter.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'ブラスター1':
            with open("blaster.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'ローラー1':
            with open("roller.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'フデ1':
            with open("brush.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'チャージャー1':
            with open("charger.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)  
       elif message.content == 'スロッシャー1':
            with open("shosher.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'スピナー1':
            with open("splatling.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'マニューバー1':
            with open("dualies.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'シェルター1':
            with open("brella.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content =='擬似':
            embed=discord.Embed(title="",description="")
            embed.set_image(url='https://cdn.discordapp.com/attachments/712589650694504508/719929619624624188/gijikaku.png')
            await message.channel.send(embed=embed)
       elif message.content == "ブキ1d":
            with open("buki.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
            if choice in giji:
                ki = choice
                choice =""
                embed=discord.Embed(title= "",description=ki+"はメイン性能アップギアによって疑似確が可能です。\n必要なギアの数については下の表をご覧ください。",color=0x52ffae)
                embed.set_image(url='https://cdn.discordapp.com/attachments/712589650694504508/719929619624624188/gijikaku.png')
                dm = await message.author.create_dm()
                await dm.send(embed=embed)
       elif message.content == 'ヒーロー1d':
            with open("hero.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'シューター1d':
            with open("shooter.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'ブラスター1d':
            with open("blaster.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'ローラー1d':
            with open("roller.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'フデ1d':
            with open("brush.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'チャージャー1d':
            with open("charger.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'スロッシャー1d':
            with open("shosher.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'スピナー1d':
            with open("splatling.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'マニューバー1d':
            with open("dualies.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif message.content == 'シェルター1d':
            with open("brella.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title=f"{callnick(message)}さんのブキは",description=choice + "です。")
            dm = await message.author.create_dm()
            await dm.send(embed=embed)
       elif choice in giji:
                ki = choice
                choice =""
                embed=discord.Embed(title= "",description=ki+"はメイン性能アップギアによって疑似確が可能です。\n必要なギアの数については下の表をご覧ください。",color=0x52ffae)
                embed.set_image(url='https://cdn.discordapp.com/attachments/712589650694504508/719929619624624188/gijikaku.png')
                await message.channel.send(embed=embed)
       elif message.content == '///c':
            if message.author.guild_permissions.administrator:
                global sw
                sw =False
                await message.channel.send('このチャンネルの思い出を一括削除します。\nこうかいしませんね？\n消す場合はyesと打ってください。消さない場合はnoと打ってください。')
                sw =True
            else:
                await message.channel.send('鯖主に頼んでください')
       elif message.content == 'yes' and sw:
            if message.author.guild_permissions.administrator:
                await message.channel.purge()
                await message.channel.send('削除しました。')
                sw = False
       elif message.content == 'no'and sw:
            if message.author.guild_permissions.administrator:
                await message.channel.send('削除しませんでした。')
                sw = False
       elif message.content == '/mw':
            with open("atama.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choicea =random.choice(textlist) 
            with open("huku.txt", "r",encoding="utf-8_sig") as g: 
              data = g.read() 
            textlist = data.split("\n")
            choiceb =random.choice(textlist) 
            with open("kutu.txt", "r",encoding="utf-8_sig") as h: 
              data = h.read() 
            textlist = data.split("\n")
            choicec =random.choice(textlist) 
            embed=discord.Embed(title="このメインギアパワーがついたギアを使いましょう",color=0xf038db)
            embed.add_field(name="アタマ", value=choicea, inline=False)
            embed.add_field(name="フク", value=choiceb, inline=False)
            embed.add_field(name="クツ", value=choicec, inline=False)
            await message.channel.send(embed=embed)
                
                     
# この＊＊＊に自分のトークンを書き替える
client.run(os.environ['DISCORD_BOT_TOKEN'])
