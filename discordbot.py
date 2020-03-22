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
        
@bot.event
async def on_message(message):
    global current_ans
    if message.author.bot: # メッセージの送信者がBotなら何もしない
        pass 
    elif current_ans == '':
        await bot.change_presence(activity=discord.Game("（∪＾ω＾） わんわんお！"))
    else:
        await bot.change_presence(activity=discord.Game("ぅゎﾀﾘぃっょぃ"))
    await bot.process_commands(message) # 忘れないように        
        
bot.run(token)

