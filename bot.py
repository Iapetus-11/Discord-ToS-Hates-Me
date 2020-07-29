from discord.ext import commands
import discord
import asyncio


user_token = "" # keep this safe
do_loops = False
global ctx_to_send


bot = commands.Bot(command_prefix="!", case_insensitive=True)

@bot.command(name='toggle', aliases=['toggleloops'])
async def toggle_loops(ctx):
    ctx_to_send = ctx
    do_loops = !do_loops
    if do_loops:
        await ctx.send(f"Loops are now running.")
    else:
        await ctx.send(f"Loops are not running.")

###############################################################################
# PUT YOUR LOOPS UNDER HERE
async def basic_loop():
    await asyncio.sleep(5)  # wait for bot to be ready

    while True:
        while do_loops:
            await ctx_to_send("HI FUCKER")
            print("basic loop")

            await asyncio.sleep(1)

        await asyncio.sleep(.01)

async def basic_loop_2():
    await asyncio.sleep(5)  # wait for bot to be ready

    while True:
        while do_loops:
            print("basic loop 2 thingy")
            await asyncio.sleep(3)

        await asyncio.sleep(.01)
# PUT YA LOOPS ABOVE HERE
###############################################################################

loops = [  # don't forget to add the loop here
    basic_loop(),
    basic_loop_2()
]
for loop in loops:
    bot.loop.create_task(loop)

bot.run(user_token, bot=False)
