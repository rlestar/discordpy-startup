###ここからプログラム###

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

@client.event
async def on_message(message): #メッセージを受け取る関数なので必ず必要
       if message.content == 'ブキ1':
            with open("buki.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       
       elif message.content == 'ブキ4':
             with open("buki.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
             textlist = data.split("\n")
             choice1 =random.choice(textlist)
             choice2 =random.choice(textlist)
             choice3 =random.choice(textlist)
             choice4 =random.choice(textlist)
             embed=discord.Embed(title="あなたたちのブキは",description=choice1+"\n"+"\n"+choice2+"\n"+"\n"+choice3+"\n"+"\n"+choice4+"\n"+"\n"+"です。")
             await message.channel.send(embed=embed)
       elif message.content == 'ヒーロー1':
            with open("hero.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'シューター1':
            with open("shooter.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'ブラスター1':
            with open("blaster.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'ローラー1':
            with open("roller.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'フデ1':
            with open("brush.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'チャージャー1':
            with open("charger.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)  
       elif message.content == 'スロッシャー1':
            with open("shosher.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'スピナー1':
            with open("splatling.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'マニューバー1':
            with open("dualies.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content == 'シェルター1':
            with open("brella.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
            textlist = data.split("\n")
            choice =random.choice(textlist) 
            embed=discord.Embed(title="あなたのブキは",description=choice + "です。")
            await message.channel.send(embed=embed)
       elif message.content =='擬似':
            await message.channel.send('https://cdn.discordapp.com/attachments/712589650694504508/719929619624624188/gijikaku.png')

# この＊＊＊に自分のトークンを書き替える
client.run(os.environ['DISCORD_BOT_TOKEN'])
