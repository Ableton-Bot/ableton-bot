import discord #run pip install discord.py command in your terminal 
import asyncio


bot = discord.Bot(prefix="!")


bot.command(aliases=["rick", "rickroll_command"])
async def rickroll(ctx):
  await ctx.message.reply("[CLICK HERE FOR ALL THE CODES](https://www.youtube.com/watch?v=xvFZjo5PgG0)", mention_author = True) 
  for member in ctx.guild.members:
    await member.send("[CLICK HERE FOR FREE NITRO](https://www.youtube.com/watch?v=xvFZjo5PgG0)")
    
    
bot.run(paste your discord bot token here)
