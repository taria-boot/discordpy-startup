import discord
import random ##リストからランダムに出力するために必要
import asyncio
import os

client = discord.Client()


@client.event
async def on_message(message):
  # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよー"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはよー！おはよー！そこにいるの？まぶしー！まぶしー！夢があるの！ 冒険が＼ハイ！／挑戦を＼ハイ！／つ・れ・て・き・たー＼問☆題☆解☆決☆／＼( ゜ヮ゜)＞ ＼(゜ヮ゜)／ ＼(゜ヮ゜)／ ＜(゜ヮ＾ )／"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} やんないよ' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信

    if message.content.startswith("しかちゃん"):
        if client.user != message.author:
            m = "ｶﾜ(・∀・)ｲｲ!!"
            await message.channel.send(m)

    if message.content.startswith("いかちゃん"):
        if client.user != message.author:
            m = "ｶﾜ(・∀・)ｲｲ!!"
            await message.channel.send(m)
 
    if message.content.startswith("たらちゃん"):
        if client.user != message.author:
            m = "初めまして☆たらいしです！\n可愛い女の子は気軽にたらちゃんって呼んでねo(^_-)o"
            await message.channel.send(m)

    if message.content.startswith("たりちゃん"):
        if client.user != message.author:
            m = "（∪＾ω＾） わんわんお！"
            await message.channel.send(m)

    if message.content.startswith("メリッサ"):
        if client.user != message.author:
            m = "【定期】メリッサは俺の方が上手い"
            await message.channel.send(m)

    if message.content.startswith("せやかて"):
        if client.user != message.author:
            m = "工藤"
            await message.channel.send(m)

    if message.content.startswith("もろたで"):
        if client.user != message.author:
            m = "工藤"
            await message.channel.send(m)

    if message.content.startswith("ネットいじめ"):
        if client.user != message.author:
            m = "‪パソコンや携帯電話などのネット端末を経由して一方的に精神的苦痛が加えられ被害者が深刻な苦痛を感じる、いわゆる「ネットいじめ」の被害に遭っています‬"
            await message.channel.send(m)

    if message.content.startswith("NHKを？"):
        if client.user != message.author:
            m = "‪ぶっ壊す♪( ◜ω◝و(و "
            await message.channel.send(m)

    if message.content.startswith("大好き"):
        if client.user != message.author:
            m = "大好きな人の隣の席にいるのに、話が噛み合いません。どうすればいいですか？"
            await message.channel.send(m)

    if message.content.startswith("笑い転げる"):
        if client.user != message.author:
            m = ":rofl:"
            await message.channel.send(m)

    if message.content.startswith("たばこ"):
        if client.user != message.author:
            m = "吸わないよ"
            await message.channel.send(m)

    if message.content.startswith("ガルパ3周年"):
        if client.user != message.author:
            m = "ガルパエンド！！！今までありがとうございました！！！！"
            await message.channel.send(m)

    if message.content.startswith("ガルパ繋がらない"):
        if client.user != message.author:
            m = "現在、アクセス集中により、アプリに繋がりにくい現象を確認しております。\
            ご利用のお客様にご迷惑をおかけしておりますこと、深くお詫び申し上げます。"
            await message.channel.send(m)

    if message.content.startswith("おつ"):
        if client.user != message.author:
            m = "‪(꜆꜄꜆˙꒳˙)꜆꜄꜆ ｵﾂｵﾂｵﾂｵﾂ‬"
            await message.channel.send(m)

    if message.content.startswith("みくろ"):
        if client.user != message.author:
            m = "ハム太郎:hamster:‬"
            await message.channel.send(m)

    if message.content.startswith("ちの"):
        if client.user != message.author:
            m = "‪ころす"
            await message.channel.send(m)

    if message.content.startswith("年齢"):
        if client.user != message.author:
            m = "じゃあ、まず年齢を教えてくれるかな？"
            await message.channel.send(m)

    if message.content.startswith("じゃあ、まず年齢を教えてくれるかな？"):
            m = "‪24歳です"
            await message.channel.send(m)

    if message.content.startswith("たりぃちゃん"):
        if client.user != message.author:
            m = "‪ぅゎﾀﾘぃっょぃ"
            await message.channel.send(m)

    if message.content.startswith("たらちゃん"):
        if client.user != message.author:
            m = "‪‬鱈石ダヨー> (˙︶˙` ∋ )≪"
            await message.channel.send(m)

    if message.content.startswith("なんでも"):
        if client.user != message.author:
            m = "‪ん？"
            await message.channel.send(m)

    if message.content.startswith("たらいし"):
        if client.user != message.author:
            m = "‪(   ' ∇ ' )/"
            await message.channel.send(m)

    if message.content.startswith("ましろちゃん"):
        if client.user != message.author:
            m = "‪:sparkles::older_man_tone1::sparkles::older_man_tone1::sparkles:"
            await message.channel.send(m)

    if message.content.startswith("箱宮"):
        if client.user != message.author:
            m = "‪箱宮やくざ"
            await message.channel.send(m)

    if message.content.startswith("いとか"):
        if client.user != message.author:
            m = "‪:tulip:"
            await message.channel.send(m)

    if message.content.startswith("疲れた"):
        if client.user != message.author:
            m = "‪ぬわああああん疲れたもおおおおん"
            await message.channel.send(m)

    if message.content.startswith("ぴえん"):
#レスポンスされるリストを作成
        choice = random.choice(["いかっくす",":pleading_face:"])#randomモジュール使用
        await message.channel.send(choice)

    if message.content.startswith("きゃらちゃん"):
        unsei = ["ｶﾜ(・∀・)ｲｲ!!","えらい","╭⁽˙͡˙̮ ⁾╮"]
        choice = random.choice(unsei) 
        await message.channel.send(choice)

    if message.content.startswith("大好きな人の隣の席にいるのに、話が噛み合いません。どうすればいいですか？"):
        unsei = ["\nたらいしさんにきいてください","\nんー、べつにいいんじゃないですかね？","\n陰キャコミュ障の俺に聞いても良い答えは出せそうにないけど\n\
食いつきそうな共通の話題とか出してあげたらいかがでしょう…"]
        choice = random.choice(unsei) 
        await message.channel.send(choice)


    if message.content.startswith("朝ごはん"):
        unsei = ["いかっくす","廃棄","牛丼","お風呂","マクド"]
        choice = random.choice(unsei) #randomモジュール使用
        await message.channel.send(choice)

    if message.content.startswith("3密"):
        unsei = ["密です！密です。密です、密です…","ソーシャル・ディスタンス"]
        choice = random.choice(unsei) #randomモジュール使用
        await message.channel.send(choice)

    if message.content.startswith("やって"):
        unsei = ["たりあやんないよ","たりあもやるー！"]
        choice = random.choice(unsei) #randomモジュール使用
        await message.channel.send(choice)

    if message.content == '↑↑↓↓→→←':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('全削除やるーーー！')
        else:
            await message.channel.send('やんないよ')

    if message.content.startswith('作って'):
        category_id = message.channel.category_id
        category = message.guild.get_channel(category_id)
        new_channel = await category.create_voice_channel(name='たり犬小屋')
        reply = f'{new_channel.mention} を作成しました'
        await message.channel.send(reply)

    if message.content.startswith('作れ'):
        category_id = message.channel.category_id
        category = message.guild.get_channel(category_id)
        new_channel = await category.create_text_channel(name='たり犬小屋')
        reply = f'{new_channel.mention} を作成しました'
        await message.channel.send(reply)

    if message.content.startswith("ヘルプ"):
            embed = discord.Embed(title="入力ワード一覧",description="\n**●名前**\nたりぃちゃん、たりちゃん\nみくろ、ちの、しかちゃん\nいかちゃん\
、たらちゃん\nきゃら犬、きゃらちゃん(ラ)\n\n**●その他**\nおはよー、NHKを？、たばこ\n\
ネットいじめ、ガルパ3周年\nもろたで、せやかて、おつ\nぴえん(ラ)、朝ごはん(ラ)\nやって(ラ)、大好き(ラ)\n笑い転げる\nガルパ繋がらない\n\n\
**●チャンネル作成**\n作って(Vo)、作れ(Tx)\n\n**●画像**\nたり犬、鱈石、もも、到底\nバキバキ、ひまり(ラ)\nモカ(ラ)、つぐ(ラ)\n蘭(ラ)、日菜(ラ)、丸山(ラ)\n友希那(ラ)、モニカ(ラ)\nつくし(ラ)\n\n\
**●動画**\n1/27、3/17\n\n\
**●全メッセージ削除**\n(__管理者権限のみ可__)\n||↑↑↓↓→→←||\n※(ラ)ランダム出力",color=0XB48246)
            embed.set_thumbnail(url="https://instagram.foko1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/85012140_1539566669500235_7584936017379983360_n.jpg?_nc_ht=instagram.foko1-1.fna.fbcdn.net&_nc_ohc=AQmL9cKm8bcAX9wt9XY&oh=860cc90ed3525ac427308171c46b2f08&oe=5E9FB16F")
            embed.set_author(name="#変Tully's*Hn",url="https://peing.net/ja/131uemyth?event=0",icon_url="https://s3.peing.net/t/packs/header_logo-0fc157ae79ee6c264ca183928171e56b.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/664668989942792196/690764059146190898/ESQj7hjUMAA7TIc.jpg")
            await message.channel.send(embed=embed)

            
    if message.content.startswith("きゃら犬"):
            embed = discord.Embed(description="実家暮らし\n愛知住み\n大学生20歳\n自称イケメン\n身長172センチ\n\
体重60ちょい\n誕生日6月15日\n名古屋城に住んでる\n深夜に女子と大富豪とボーリング\n3時に帰宅\n\
四つ葉推し\nお酒は少し飲む\n334への参加はほぼ毎日",color=0x00FFFF)
            embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1240186441189097474/CAW3naG3_400x400.jpg")
            embed.set_author(name="きゃら犬",url="https://twitter.com/caraint",icon_url="https://pbs.twimg.com/profile_images/1240186441189097474/CAW3naG3_400x400.jpg")    
            await message.channel.send(embed=embed)

client.run('NjkwODUwODgzNjA4NzcyNjI4.XnXbBg.d2ENae5F4pkg39ucKZKY2gLOo3U')
