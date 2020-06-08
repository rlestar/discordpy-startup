from discord.ext import commands  
from random import randint,choice  

client = commands.Bot(command_prefix='$')  

def randBuki(buki_list, users):  
    len_u = len(users)  
    return {i:choice(buki_list) for i in users}  
with open('buki.csv', encoding='UTF-8') as f:  
    buki_list = f.readlines()  
    

    
@client.command()  
async def random(ctx):  
    # Botが既に他のVCに参加しているか  
    if ctx.voice_client:  
        # 参加している場合は出力  
        voice_channel = discord.utils.get(ctx.guild.channels, id=ctx.author.voice.channel.id)  
        p_list = voice_channel.members  
        voice_users= [ p_list[i].display_name for i in range(len(p_list))]  
        rand_buki = randBuki(buki_list1,voice_users)  
        mbuki = ''  
        stage = "Random Weapon"  
        for i in rand_buki.keys():  
            mbuki =  mbuki + '{}: {}'.format(i,rand_buki[i])  
        msg = discord.Embed(title=stage,description=mbuki, colour=0xffffff)  
        await ctx.send(embed=msg)  
    else:  
        # 参加していない場合  
        await ctx.send('`You need to join a voice channel to use this command`')  

client.run('NzE4MzQ2ODEyNDEwMjk4Mzk4.XtsHpw.5zn69sy--bfy_gh45ulonUELSbY')  