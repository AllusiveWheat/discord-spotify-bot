import os
from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
import lavapy

from dotenv import load_dotenv
load_dotenv()
bot = Client(intents=Intents.default())
slash = SlashCommand(bot)
async def initialiseNodes():
    """
    Wait until the bot is ready then create a Lavapy node
    """
    await bot.wait_until_ready()

    await lavapy.NodePool.createNode(client=bot,
                                     host="0.0.0.0",
                                     port=2333,
                                     password="password")
token = os.getenv("token")
@slash.slash(name="test")
async def test(ctx: SlashContext):
    embed = Embed(title="Embed Test")
    await ctx.send(embed=embed)

bot.run(token)