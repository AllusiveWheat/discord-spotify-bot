import os
from aiohttp import client
from discord.ext import commands
import lavapy
bot = commands.Bot(command_prefix="!")
from dotenv import load_dotenv
from lavapy.ext import spotify

load_dotenv()

async def initialiseNodes():
    """
    Wait until the bot is ready then create a Lavapy node
    """
    await bot.wait_until_ready()
    await lavapy.NodePool.createNode(client=bot,
                                     host="localhost",
                                     port=2333,
                                     password="youshallnotpass",
                                     spotifyClient=spotify.SpotifyClient(os.getenv("clientId"), os.getenv("clientSecret")))


@bot.command()
async def play(ctx: commands.Context, *query) -> None:
    """
    Play a Youtube song from a given search query.

    If the bot is not connected, connect it to the user's voice channel. For this
    to work, the user must be connected to a voice channel
    """
    if not ctx.voice_client:
        # Bot is not connected to a voice channel
        try:
            player: lavapy.Player = await ctx.author.voice.channel.connect(cls=lavapy.Player)
        except AttributeError:
            # User is not connected to a voice channel
            await ctx.channel.send("You must be connected to a voice channel")
            return
    else:
        # Bot is connected to a voice channel
        player: lavapy.Player = ctx.voice_client
    # Parse URL to see what to play
    if query[0].startswith("https://www.youtube.com/watch?v="):
        # Play a Youtube video
        track = await lavapy.YoutubeTrack.search(query[0], player.node)
    elif query[0].startswith("https://open.spotify.com/track/"):
        # Play a Spotify track
        track = await spotify.SpotifyTrack.search(query[0], player.node)
    else:
        # Search for a Youtube video
        track = await lavapy.SoundcloudTrack.search(query[0], player.node)
     
    await player.play(track)


bot.loop.create_task(initialiseNodes())
bot.run(os.getenv("token"))
