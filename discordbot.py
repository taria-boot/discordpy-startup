from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

class Greet(commands.Cog, name='あいさつ'):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="こんにちは")
    async def hello(self, ctx):
        """出会いのあいさつをする"""
        await ctx.send(f"どうも、{ctx.author.name}さん!")

    @commands.command(name="さようなら")
    async def goodbye(self, ctx):
        """別れの挨拶をする"""
        await ctx.send(f"じゃあね、{ctx.author.name}さん!")

class GameRPS:
    __rps_done_member_list = []
    __msg_daily_limit_exceeded = textwrap.dedent("""\
        じゃんけんは1日1回まで！
        ほな、また明日！
    """)
    __msg_too_many_hands = textwrap.dedent("""\
        手を複数同時に出すのは反則やで！
    """)
    __msg_win = textwrap.dedent("""\
        やるやん。
        明日は俺にリベンジさせて。
        では、どうぞ。
    """)
    __msg_lose_r = textwrap.dedent("""\
        俺の勝ち！
        負けは次につながるチャンスです！
        ネバーギブアップ！
        ほな、いただきます！
    """)
    __msg_lose_s = textwrap.dedent("""\
        俺の勝ち！
        たかがじゃんけん、そう思ってないですか？
        それやったら明日も、俺が勝ちますよ
        ほな、いただきます！
    """)
    __msg_lose_p = textwrap.dedent("""\
        俺の勝ち！
        なんで負けたか、明日まで考えといてください。
        そしたら何かが見えてくるはずです
        ほな、いただきます！
    """)
    __filenames_win = [
        "honda_win.png"
    ]
    __filenames_lose_r = [
        # "honda_p.png",
        "honda_p.gif"
    ]
    __filenames_lose_s = [
        # "honda_r.png",
        "honda_r.gif"
    ]
    __filenames_lose_p = [
        # "honda_s.png",
        "honda_s.gif"
    ]

    __youtube_lose_r = "https://youtu.be/LhPJcvJLNEA"
    __youtube_lose_s = "https://youtu.be/SWNCYpeDTfo"
    __youtube_lose_p = "https://youtu.be/28d78XP1TJs"

    def __init__(self):
        pass
        
        
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
       
bot.run(token)

