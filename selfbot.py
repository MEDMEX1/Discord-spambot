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
  var = 1
  while var == 1 :
    rnum = r.randint(10,25)
    messages = ['Hey', 'What is your fav game?', 'anyone got some movie suggestions?', 'Who is the best streamer to watch?', 'Anyone else outta school now?', 'You guys like Drake?','Whats good','Up up upitty', 'Suggest me some shows','Im going to the store, anyone need anything?','Im a fortnite prodigy','Im cool','Nice weather out huh?','where you guys from?', 'Tell me something interesting', 'Tell a joke', 'Anyone need some advice?', 'Favorite actor?','Whats the best game out rn?','whats ur favorite soccer club?',"how is coronacation for y'all", 'You guys play CSGO?','Howmany hours you guys got in the game?','Is mark zuckerberg a lizard?','What GPU u guys got?','You guys fw 21 savage?', 'Who is your idol?','you guys blaze?','Rip x', 'Yo','Hello','Who is the best pranker?','What is Obamas last name?']
    print("Message cycle started")
    overwatch = client.get_channel(94882524378968064)
    await overwatch.send(r.choice(messages))
    print("overwatch sent")
    await asyncio.sleep(rnum)
    callofduty = client.get_channel(220018067227410432)
    await callofduty.send(r.choice(messages))
    print("callofduty sent")
    await asyncio.sleep(rnum)
    fortnite = client.get_channel(338017726394138624)
    await fortnite.send(r.choice(messages))
    print("fortnite sent")
    await asyncio.sleep(rnum)
    leagueoflegends = client.get_channel(125440014904590336)
    await leagueoflegends.send(r.choice(messages))
    print("leagueoflegends sent")
    await asyncio.sleep(rnum)
    rocketleague = client.get_channel(180720102033981440)
    await rocketleague.send(r.choice(messages))
    print("rocketleague sent")
    await asyncio.sleep(rnum)
    rust = client.get_channel(560127830621683725)
    await rust.send(r.choice(messages))
    print("rust sent")
    await asyncio.sleep(rnum)
    temtem = client.get_channel(428181186528018444)
    await temtem.send(r.choice(messages))
    print("temtem sent")
    await asyncio.sleep(rnum)
    terraria = client.get_channel(251116850132287490)
    await terraria.send(r.choice(messages))
    print("terraria sent")
    print("completed one message cycle, next one in 0.5-2m")
    cyclecooldown = r.randint(30,120)
    await asyncio.sleep(cyclecooldown)

@client.command(pass_context=True)
async def yo(ctx):
    guild = ctx.message.guild
    dmdelay = r.randint(2,10)
    for member in guild.members:
     await asyncio.sleep(dmdelay)
     try:
        messages = messages = ["Yo", "Whatsup", 'Sup', 'You good buddy?', 'Hey man', 'How you doing bro', 'All good?', 'Everything fine?', 'You got a min?', 'u alright there?']
        await member.send(r.choice(messages))
        print("DM sent")
     except:
       pass








client.run("", bot=False)
