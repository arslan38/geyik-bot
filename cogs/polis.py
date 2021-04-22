
import discord
from discord.ext import commands 

class Polis(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Polis(bot))
