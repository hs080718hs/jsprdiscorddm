# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
import os

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(bot.user.name)

def is_victoria(ctx):
    if ctx.author.id == 765372606601494558: return True
    return False

@bot.command()
@commands.check(is_victoria)
@commands.guild_only()
async def 디엠(self, ctx, *, text):
    if "&&" not in text:
        return await ctx.send("`!디엠 제목&&내용`")
    fail = []
    title = text.split("&&")[0]
    desc = text.split("&&")[1]
    for member in ctx.guild.members:
        try:
            await member.send(embed=discord.Embed(title=title, description=desc))
        except:
            fail.append(member.name)
    try:
        await ctx.send(f"""완료!
DM 전송 실패한 사람들 (디엠을 막았을수도 있습니다) : 
{', '.join(fail)}
다음은 실패한 사람들의 수 입니다.
{len(fail)}
""")
    except:
        await ctx.send(f"""완료!
DM 전송 실패한 사람들이 너무 많아 보낼 수 없습니다. 다음은 실패한 사람들의 수 입니다.
{len(fail)}""")

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
