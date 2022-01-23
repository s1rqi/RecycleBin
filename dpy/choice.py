import discord, random
client = discord.Client()
token = input("Token: ")

@client.event
async def on_ready():
	print("on ready")
	
@client.event
async def on_message(message):
	if message.author.bot: return
	
	if message.content.startswith("!choice"):
		args = message.content.split(" ")
		
		a = random.choice(args[1:])
		await message.channel.send(a)
		
client.run(token)