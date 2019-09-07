import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("with the market")
    await client.change_presence(status=discord.Status, activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run("NjE5OTYxNjUyNTg2MjE3NDky.XXQGTg.jdJsJXE7RrHbM5U1PpBWfbaDago")
