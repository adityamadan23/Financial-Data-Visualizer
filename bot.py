import discord
from discord import Game
from alpha_vantage.timeseries import TimeSeries
from discord.ext import commands
import matplotlib.pyplot as plt

ts = TimeSeries(key='X', output_format='pandas') #Hid Token
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user.name))
    # await bot.change_presence(game=Game(name="With the market"))


@bot.command(pass_context=True)
async def stock(ctx, a: str):
    data, meta_data = ts.get_intraday(symbol=a, interval='1min', outputsize='full')
    data['4. close'].plot()
    plt.title('Intraday Times Series for the {} stock (1 min)'.format(a))
    plt.savefig('graph.png')
    file = discord.File('graph.png', filename='graph.png')
    embed = discord.Embed()
    embed.set_image(url="attachment://graph.png")
    await ctx.send(file=file, embed=embed)


@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send('Hello there!')


bot.run("X") #Hid Token
