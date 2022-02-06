import discord

bot = discord.Bot()
token = input("Token: ")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[924643051039785020])
async def clone(ctx, msgid):
    if not msgid.isdecimal():
        await ctx.respond("int入力しろ")
        return
    await ctx.respond("Loading embeds, please wait...", ephemeral=True)
    for ch in ctx.guild.threads + ctx.guild.text_channels: #ctx.guild.text_channels:
        try:
            msg = await ch.fetch_message(msgid)
            print("Found -> "+str(ch.name))
            break
        except:
            print("Not Found -> "+str(ch.name))
    await ctx.respond(embed=msg.embeds[0], ephemeral=True)

bot.run(token)
