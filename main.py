import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = "!"
token = os.getenv("TOKEN")

#use the .env feature to hide your token

keep_alive()


#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

#the game thing

@bot.event
async def on_ready():
    activity = discord.Game(name="ChainLink", type=4)
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print(f'''{Fore.BLUE}
░█████╗░██╗░░██╗░█████╗░██╗███╗░░██╗
██╔══██╗██║░░██║██╔══██╗██║████╗░██║
██║░░╚═╝███████║███████║██║██╔██╗██║
██║░░██╗██╔══██║██╔══██║██║██║╚████║
╚█████╔╝██║░░██║██║░░██║██║██║░╚███║
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝
{Fore.MAGENTA}         
██╗░░░░░██╗███╗░░██╗██╗░░██╗
██║░░░░░██║████╗░██║██║░██╔╝
██║░░░░░██║██╔██╗██║█████═╝░
██║░░░░░██║██║╚████║██╔═██╗░
███████╗██║██║░╚███║██║░╚██╗
╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝

{Fore.GREEN}

Chain Link Is Alive!
''')







@bot.command(pass_context=True)
async def minedmc(ctx):
    await ctx.message.delete()
    await ctx.send('DMC mining is now **enabled**!')
    await ctx.send('Auto miners v2')
    await ctx.send('updated!')
    await ctx.send('Without banning you or getting suspecious')
    await ctx.send('@here make sure miner have 500 dmc')
    await ctx.send('in the wallet')
    await ctx.send('pls daily')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(5)
            await ctx.send('pls bal')
            print(f"{Fore.GREEN}cash tested !")
            await asyncio.sleep(15)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully beg")
            await asyncio.sleep(15)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await asyncio.sleep(15)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully dig")
            await asyncio.sleep(15)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await asyncio.sleep(15)
            await ctx.send('pls bal')
            print(f"{Fore.GREEN}cash tested !")
            await asyncio.sleep(15)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully beg")
            await asyncio.sleep(15)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await asyncio.sleep(15)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully dig")
            await asyncio.sleep(15)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await asyncio.sleep(15)
            await ctx.send('pls bal')
            print(f"{Fore.GREEN}cash tested !")
            await asyncio.sleep(15)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully beg")
            await asyncio.sleep(15)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await asyncio.sleep(15)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully dig")
            await asyncio.sleep(15)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await asyncio.sleep(15)
            await ctx.send('pls bal')
            print(f"{Fore.GREEN}cash tested !")
            await asyncio.sleep(15)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully beg")
            await asyncio.sleep(15)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await asyncio.sleep(15)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully dig")
            await asyncio.sleep(15)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await asyncio.sleep(15)
            await ctx.send('pls bal')
            print(f"{Fore.GREEN}cash tested !")
            await asyncio.sleep(15)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully beg")
            await asyncio.sleep(15)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await asyncio.sleep(15)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully dig")
            await asyncio.sleep(15)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await asyncio.sleep(15)
            await ctx.send('pls bal')
            print(f"{Fore.GREEN}cash tested !")
            await asyncio.sleep(15)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully beg")
            await asyncio.sleep(15)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await asyncio.sleep(15)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully dig")
            await asyncio.sleep(15)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await asyncio.sleep(15)
            await ctx.send('pls bal')
            print(f"{Fore.GREEN}cash tested !")
            await asyncio.sleep(15)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully beg")
            await asyncio.sleep(15)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await asyncio.sleep(15)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully dig")
            await asyncio.sleep(15)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await asyncio.sleep(15)
            await ctx.send('pls bal')
            print(f"{Fore.GREEN}cash tested !")
            await asyncio.sleep(15)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully beg")
            await asyncio.sleep(15)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await asyncio.sleep(15)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully dig")
            await asyncio.sleep(15)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await asyncio.sleep(15)
            await ctx.send('pls bal')
            print(f"{Fore.GREEN}cash tested !")
            await asyncio.sleep(15)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully beg")
            await asyncio.sleep(15)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await asyncio.sleep(15)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully dig")
            await asyncio.sleep(15)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await asyncio.sleep(15)
            await ctx.send('pls bal')
            print(f"{Fore.GREEN}cash tested !")
            await asyncio.sleep(15)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully beg")
            await asyncio.sleep(15)
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await asyncio.sleep(15)
            await ctx.send('pls dig')
            print(f"{Fore.GREEN}succefully dig")
            await asyncio.sleep(15)
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await asyncio.sleep(15)
            await ctx.send('pls sell garbage all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell junk all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell bread all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell lifesaver')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls post meme')
            print(f"{Fore.GREEN}succefully memepost")
            await asyncio.sleep(15)
            await ctx.send('pls sell ant all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell fish all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell duck all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell jellyfish all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell skunk all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell worm all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell stickbug all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell boar all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell sand all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell alchol all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell rabbit all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell seaweed all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell worm all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell cheese all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell banhammer all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell cookie all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)
            await ctx.send('pls sell candy all')
            print(f"{Fore.GREEN}succefully sell")
            await asyncio.sleep(15)

@bot.command(pass_context=True)
async def gifspam(ctx):
    await ctx.message.delete()
    await ctx.send('*Spam*')
    await ctx.send('@here This is bad i know')
    await ctx.send('im sorry')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/toilet-fly-away-toilet-bowl-funny-gif-16664668')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/manners-manners-makes-a-man-kingsman-gif-11678867')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/middle-finger-chris-pratt-peter-quill-star-lord-gif-5722402')
            await asyncio.sleep(1)
            await ctx.send('https://c.tenor.com/He2W0AQvZfsAAAAM/hacked-hack.gif')
            await asyncio.sleep(1)
            await ctx.send('https://cdn.discordapp.com/emojis/586228314541260802.gif?size=64')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/2va-kuthu-tamil-vijay-soori-gif-17779181')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/diplein-karate-martial-kungfu-fall-down-gif-17786041')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/trampoline-fail-pool-party-dive-gif-18076918')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/iron-golem-dream-dies-puny-speedrunner-gif-21959265')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/doge-dog-smiling-dog-smiling-smiling-doge-gif-20418511')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/minecraft-lava-dead-gif-18488732')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/weird-meow-cat-funny-gif-15167727')


keep_alive()
bot.run(token, bot=False)
