# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='store', help='stores game info, example: ~storecode abcdef NA(capitalize the server)')
async def store(ctx, argc, args):
    print(f'{argc} {args}')
    
    if len(argc) != 6:
        await ctx.send('code isn\'t 6 characters!')
        return 0

    stored_code = argc.upper()
    f = open('newcode.txt',"w")
    f.write(stored_code)
    f.close()

    if len(args) != 2 or (args != 'NA' and args != 'EU' and args != 'AS'):
        await ctx.send("enter the capitalized, two letter abbrev. for the server region! i.e. NA, EU, AS")
        return 0
    stored_server = args.upper()
    f = open('newsrv.txt',"w")
    f.write(stored_server)
    f.close()

    await ctx.send(f'code and server stored! code: {stored_code}, server: {stored_server}')



@bot.command(name='get', help='returns the code and server')
async def getcode_server(ctx):
    f = open('newcode.txt',"r")
    stored_code = f.read()
    
    g = open('newsrv.txt',"r")
    stored_server = g.read()

    await ctx.send(f'code: {stored_code}, server: {stored_server}')


@bot.command(name='me', help='i need help too bro')
async def me(ctx):
    return 0

bot.run(TOKEN)