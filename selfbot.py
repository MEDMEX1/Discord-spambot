#ad bot by MEDMEX
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging
import random as r

client = commands.Bot(command_prefix='$', self_bot=True)

@client.event
async def on_ready():
    print("Ready")


@client.command(pass_context=True)
async def dm(ctx):
    guild = ctx.message.guild
    for member in guild.members:
     await asyncio.sleep(10)
     try:
       await member.send("test")
       print("Sent message")
     except:
       pass
  
@client.command(pass_context=True)
async def links(ctx):
  channel = ctx.message.channel
  await channel.send("https://discord.gg/fortnite")
  await asyncio.sleep(1)
  await channel.send("https://discord.gg/rust")
  await asyncio.sleep(1)
  await channel.send("https://discord.gg/lol")
  await asyncio.sleep(1)
  await channel.send("https://discord.gg/temtem")
  await asyncio.sleep(1)
  await channel.send("https://discord.gg/overwatch")
  await asyncio.sleep(1)
  await channel.send("https://discord.gg/rocketleague")
  await asyncio.sleep(1)
  await channel.send("https://discord.gg/callofduty")
  await asyncio.sleep(1)
  await channel.send("https://discord.gg/terraria")

@client.command(pass_context=True)
async def timer(ctx):
  print("10 minute timer started.")
  await asyncio.sleep(600)
  print("10 minute timer has ended, now ready to send messages in servers.")

@client.command(pass_context=True)
async def message(ctx):
  rnum = r.randint(10,25)
  var = 1
  while var == 1 :
    print("Message cycle started")
    overwatch = client.get_channel(94882524378968064)
    await overwatch.send('Yo whatsup everybody!')
    print("overwatch sent")
    await asyncio.sleep(rnum)
    callofduty = client.get_channel(220018067227410432)
    await callofduty.send('Hey anyone playing the new COD here?')
    print("callofduty sent")
    await asyncio.sleep(rnum)
    fortnite = client.get_channel(338017726394138624)
    await fortnite.send("Hello would anyone here suggest me to buy the battlepass?")
    print("fortnite sent")
    await asyncio.sleep(rnum)
    leagueoflegends = client.get_channel(125440014904590336)
    await leagueoflegends.send("Hey anyone have some tips on how to become a better player?")
    print("leagueoflegends sent")
    await asyncio.sleep(rnum)
    rocketleague = client.get_channel(180720102033981440)
    await rocketleague.send("Anyone got some cool wheels to suggest?")
    print("rocketleague sent")
    await asyncio.sleep(rnum)
    rust = client.get_channel(560127830621683725)
    await rust.send("Anyone know how I can improve my recoil skills?")
    print("rust sent")
    await asyncio.sleep(rnum)
    temtem = client.get_channel(428181186528018444)
    await temtem.send("Would anyone suggest me buying this game?")
    print("temtem sent")
    await asyncio.sleep(rnum)
    terraria = client.get_channel(251116850132287490)
    await terraria.send("How does this game compare to minecraft?")
    print("terraria sent")
    await asyncio.sleep(rnum)
    overwatch2 = client.get_channel(94882524378968064)
    await overwatch2.send('Who is your favorite character?')
    print("overwatch2 sent")
    await asyncio.sleep(rnum)
    callofduty2 = client.get_channel(220018067227410432)
    await callofduty2.send('Can someone suggest a good watch?')
    print("callofduty2 sent")
    await asyncio.sleep(rnum)
    fortnite2 = client.get_channel(338017726394138624)
    await fortnite2.send("What is the best skin?")
    print("fortnite2 sent")
    await asyncio.sleep(rnum)
    leagueoflegends2 = client.get_channel(125440014904590336)
    await leagueoflegends2.send("What is the best champion?")
    print("leagueoflegends2 sent")
    await asyncio.sleep(rnum)
    rocketleague2 = client.get_channel(180720102033981440)
    await rocketleague2.send("What is the best beginner car?")
    print("rocketleague2 sent")
    await asyncio.sleep(rnum)
    rust2 = client.get_channel(560127830621683725)
    await rust2.send("What is the coolest AK skin?")
    print("rust2 sent")
    await asyncio.sleep(rnum)
    temtem2 = client.get_channel(428181186528018444)
    await temtem2.send("How does this game compare to Pokemon?")
    print("temtem2 sent")
    await asyncio.sleep(rnum)
    terraria2 = client.get_channel(251116850132287490)
    await terraria2.send("Yo is this game any good?")
    print("terraria2 sent")
    await asyncio.sleep(rnum)
    overwatch3 = client.get_channel(94882524378968064)
    await overwatch3.send('Thanks!')
    print("overwatch3 sent")
    await asyncio.sleep(rnum)
    callofduty3 = client.get_channel(220018067227410432)
    await callofduty3.send('What is the best COD?')
    print("callofduty3 sent")
    await asyncio.sleep(rnum)
    fortnite3 = client.get_channel(338017726394138624)
    await fortnite3.send("When is the next season coming out?")
    print("fortnite3 sent")
    await asyncio.sleep(rnum)
    leagueoflegends3 = client.get_channel(125440014904590336)
    await leagueoflegends3.send("What is the best way to play Wukong?")
    print("leagueoflegends3 sent")
    await asyncio.sleep(rnum)
    rocketleague3 = client.get_channel(180720102033981440)
    await rocketleague3.send("What are your opinions on the mclaren car?")
    print("rocketleague3 sent")
    await asyncio.sleep(rnum)
    rust3 = client.get_channel(560127830621683725)
    await rust3.send("Why is everybody in this game so toxic?")
    print("rust3 sent")
    await asyncio.sleep(rnum)
    temtem3 = client.get_channel(428181186528018444)
    await temtem3.send("I've never played this game but it sure seems cool!")
    print("temtem3 sent")
    await asyncio.sleep(rnum)
    terraria3 = client.get_channel(251116850132287490)
    await terraria3.send("Yeah")
    print("terraria3 sent")
    await asyncio.sleep(600)
    print("completed one message cycle, next one in 10 minutes")








@client.command(pass_context=True)
async def test(ctx):
  var = 1
  while var == 1 :
    randomnum = r.randint(5,10)
    print('test')
    await asyncio.sleep(randomnum)
    print('test2')
    await asyncio.sleep(randomnum)



client.run("", bot=False)
