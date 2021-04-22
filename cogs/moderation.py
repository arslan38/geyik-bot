import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('burak,Artvin')
    async def kick(self,ctx,member:discord.Member,*args,reason = 'boş'):
        await member.kick(reason=reason)
        print(f'{member} kicked')
        em = discord.Embed(title='Kicked',
                           description = f'{member}, {reason} nedeniyle kicklenmiştir.')
        await ctx.send(embed = em)

    @commands.command()
    @commands.has_role('burak,Artvin')
    async def ban(self,ctx,member:discord.Member,*args,reason = 'boş'):
        await member.ban(reason=reason)
        print(f'{member} banned')
        em = discord.Embed(title='Banned',
                           description = f'{member}, {reason} nedeniyle banlanmıştır.')
        await ctx.send(embed = em)

    @commands.command()
    @commands.has_role('burak,Artvin')
    async def unban(self,ctx,*,member):
        banned_users = await ctx.guild.bans()
        member_name,member_id = member.split('#')
        for i in banned_users:
            user = i.user
            if (user.name,user.discriminator)==(member_name,member_id):
                await ctx.guild.unban(user)
                em = discord.Embed(title='Unbanned',
                           description = f'{member}\'ın, {reason} nedeniyle banı kalkmıştır.')
                await ctx.send(embed = em)
                print(f'{member} unbanned')


def setup(bot):
    bot.add_cog(Moderation(bot))
