# import asyncio
# import discord
# from discord.ext import commands
#
# bot = commands.Bot("ss!", self_bot=True)
#
#
# @bot.event
# async def on_ready():
#     print(bot.user.name, "has been launched")
#
# @bot.event
# async def on_message(msg):
#     if isinstance(msg.channel, discord.channel.DMChannel):
#         print(f"{msg.author} sent {msg.content}")
#
#
# @bot.command()
# async def test(ctx):
#     await ctx.send("oof")
#
#
# bot.run("ODM1NTE5NzkzMTA4NzQ2MjQw.YIQqEg.Zt9khEWC5KXS3kUpVsVuIaHMxfQ")

import discum
from time import sleep

bot = discum.Client(token='ODM1NTE5NzkzMTA4NzQ2MjQw.YIQqEg.Zt9khEWC5KXS3kUpVsVuIaHMxfQ',
                    log={"console": False, "file": False})

bot.sendMessage("238323948859439", "Hello :)")


@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    if resp.event.message:
        m = resp.parsed.auto()
        guildID = m['guild_id'] if 'guild_id' in m else None  # because DMs are technically channels too
        channelID = m['channel_id']
        username = m['author']['username']
        discriminator = m['author']['discriminator']
        content = m['content']
        if guildID is None:
            print(f"{username} sent : {content}")
            sleep(10)
            bot.sendMessage(channelID="848904797138321419", message=f"{username}#{discriminator} has just sent me a DM.")


bot.gateway.run(auto_reconnect=True)
