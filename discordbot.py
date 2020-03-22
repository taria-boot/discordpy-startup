from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def tasu(ctx, a: int, b: int):
    await ctx.send(a+b)
    
@bot.command()
async def kakeru(ctx, a: int, b: int):
    await ctx.send(a*b)  
    
@bot.command()
async def hiku(ctx, a: int, b: int):
    await ctx.send(a-b)  
    
@bot.command()
async def waru(ctx, a: int, b: int):
    await ctx.send(a/b)      
    
@bot.command()
async def beki(ctx, a: int, b: int):
    await ctx.send(a**b)      
        
@bot.command()
async def kai(ctx, a: int):
    await ctx.send(factorial.(a)) 
        
bot.run(token)

