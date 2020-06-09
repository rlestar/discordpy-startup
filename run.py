###ここからプログラム###

import discord #discordでBOTを使うのにこれが必ず
import random


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
            await message.channel.send("あなたのブキは{}です。".format(choice)) #結果を出力
       
       elif message.content == 'ブキ4':
             with open("buki.txt", "r",encoding="utf-8_sig") as f: 
              data = f.read() 
             textlist = data.split("\n")
             choice1 =random.choice(textlist)
             choice2 =random.choice(textlist)
             choice3 =random.choice(textlist)
             choice4 =random.choice(textlist)
             await message.channel.send("あなたたちのブキは\n{0}\n{1}\n{2}\n{3}\nです。".format(choice1,choice2,choice3,choice4)) #結果を出力

  

# この＊＊＊に自分のトークンを書き替える
client.run(os.environ['DISCORD_BOT_TOKEN'])
