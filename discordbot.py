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
    
@bot.event   
activity = discord.Game(name="Just")
    await client.change_presence(status=discord.Status.idle, activity=activity)

@bot.command()
async def dog(ctx):
    await ctx.send(f'{ctx.author.mention} （∪＾ω＾） わんわんお！')
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def tasu(ctx, a: float, b: float):
    await ctx.send(a+b)
    
@bot.command()
async def kakeru(ctx, a: float, b: float):
    await ctx.send(a*b)  
    
@bot.command()
async def hiku(ctx, a: float, b: float):
    await ctx.send(a-b)  
    
@bot.command()
async def waru(ctx, a: float, b: float):
    await ctx.send(a/b)      
    
@bot.command()
async def beki(ctx, a: float, b: int):
    await ctx.send(a**b)      
       
bot.run(token)

