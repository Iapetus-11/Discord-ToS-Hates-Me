import discord
from discord.ext import commands
import asyncio
from random import randint


key = ""

bot = commands.Bot(command_prefix="!\uFEFF!\uFEFF!ABC--132%%{", help_command=None)

advert_msg = """▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
__**Xenon**__

**-** 2 Minecraft servers (one for Bedrock Edition, one Java Edition network)
**-** Contests (Like art, mc builds, photography, etc...)
**-** Memes
**-** Fun bots
**-** Active community with over 400 members
**-** Earnable status/permission roles
**-** Server partnerships
**-** Handpicked mods

Check us out! https://discord.gg/ESZnFkD
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""

try:
  with open('dmed_already', 'r') as dmed:
    dmed_users_ids = dmed.readlines()
except Exception:
  dmed_users_ids = []

async def loop():
  await asyncio.sleep(5)

  while True:
    print('iteration')
    
    for user in bot.users:
      if str(user.id) not in dmed_users_ids:
        try:
          await asyncio.sleep(3)
          await user.send(advert_msg)
          print(f"Dmed {user} ({user.id})")
          dmed_users_ids.append(user.id)
        except Exception:
          await asyncio.sleep(1.5)
          print(f"Error while dming {user}")
          dmed_users_ids.append(str(user.id))

bot.loop.create_task(loop())

try:
  bot.run(key, bot=False)
except KeyboardInterrupt:
  with open('dmed_already', 'w+') as dmed:
    dmed.write('\n'.join(dmed_users_ids))
