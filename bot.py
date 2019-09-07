import discord

client = discord.Client()


@client.event
async def on_read():
    print("Lets Get That Bread")
    await client.change_presence(game=discord.Game(name="Ivey Street Bets"))
