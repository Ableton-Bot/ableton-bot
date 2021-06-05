import discord #run pip install discord.py command in your terminal 
import asyncio

bot = discord.Bot(prefix="!")


bot.command(aliases=["kek", "kek_command"])
async def kekw(ctx):
  
  await ctx.message.reply("<:KEKW:850745103215231036> Are you sure you want to KEK the server?", mention_author = True) 
  def check(m):
    if m.author.id == user.id and m.content.lower() == 'yes':
        return True
      return False
    
  try:
    await client.wait_for('message', timeout=25.00, check=check)
  except asyncio.TimeoutError:
            await ctx.send('<:KEKW:850745103215231036> YOU DIN\'T ANSWER IN TIME! PLEASE BE QUICKER NIXT TIME!')
            return
  
  for member in ctx.guild.members:
    await member.send(f"<:KEKW:850745103215231036> yOu hAvE bEeN kEkeD by {ctx.author.mention}!")
  await asyncio.sleep(2)
  await ctx.send(f"<:KEKW:850745103215231036> yOu hAvE bEeN kEkeD by {ctx.author.mention}!")
  await asyncio.sleep(1)
  await ctx.send(f"<:KEKW:850745103215231036> yOu hAvE bEeN kEkeD by {ctx.author.mention}!")
  await asyncio.sleep(1)
  await ctx.send(f"<:KEKW:850745103215231036> yOu hAvE bEeN kEkeD by {ctx.author.mention}!")
  await asyncio.sleep(1)
  await ctx.send(f"<:KEKW:850745103215231036> yOu hAvE bEeN kEkeD by {ctx.author.mention}!")
    
    
bot.run(paste your discord bot token here)

