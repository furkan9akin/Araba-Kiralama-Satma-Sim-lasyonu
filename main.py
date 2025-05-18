import discord
from discord.ext import commands
import man 
intents = discord. Intents.default ()
intents.message_content = True
bot = commands.Bot (command_prefix='/', intents=intents)

x = man.DB_Manager("Car_Sales.db")

@bot.event
async def on_ready():
    print(f'{bot.user} olarak online durumdayım yardım için /help')

@bot.command()
async def araba_bulucu(ctx):
    liste = ["Price", "Company", "Color"]
    await ctx.send("Hangi parametre ile filitrelemek istersiniz?")
    await ctx.send(liste)
    tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    parametre = tahmin_mesaji.content
    await ctx.send(f"{parametre} değeri ne olsun? ör: Black/Toyota/199000")
    mesaj = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    değer = mesaj.content
    y = x.tek_par(parametre, değer)
    for i in y:
        await ctx.send(i)
    

bot.run("")