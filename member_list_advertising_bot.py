import discord
from discord.ext import commands
import asyncio
from random import randint


key = "haha you thought"

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

async def loop():
  await asyncio.sleep(1)

  while True:
    print('iteration')
    
    for user in bot.users:
      try:
        await user.send(advert_msg)
        print(f"Dmed {user} ({user.id})")
      except Exception:
        print(f"Error while dming {user}")

bot.loop.create_task(loop())

bot.run(key, bot=False)
