import discord
import requests
import os
import random
from discord.ext import commands

choices = (".","wahaha","no se")
choices2 = ("1 = Cara","2 = Sello")

memelist = []

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', help_command = commands.DefaultHelpCommand(
    no_category = "Comandos"

), intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    """Solo es el bot que saluda."""
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    """Suena como si fuera Sans hablando."""
    await ctx.send("he" * count_heh)

@bot.command()
async def repite_lo_que_digo(ctx, content='YAAAAAAAAAAAAAAAAHOYAAAAAAA'):
    for i in range(5):
        """Ya es muy obvio. ._."""
        await ctx.send(content)

@bot.command(description="Para decidir de otra manera quien tiene suerte.")
async def escoger(ctx, choices =(choices)):
    """Un dado, escoge un carácter puesto del código."""
    await ctx.send(random.choice(choices))

@bot.command(description= "Para decidir de otra manera quien tiene suerte... n°2")
async def escoger2(ctx, choices2 = (choices2)):
    """Otro dado, escoge un carácter puesto del código."""
    await ctx.send("Mi decisión es...")
    await ctx.send("...")
    await ctx.send("...")
    await ctx.send("...")
    await ctx.send("...")
    await ctx.send("...")
    await ctx.send(random.choice(choices2))


@bot.command()
async def mem(ctx):
    """Un meme ya programado. Supongo que podré añadir más."""
    with open('M2L1\images\mem1.jpg','rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    memelist.append = ["mem1.jpg"]

@bot.command()
async def mem2(ctx):
    """Un meme ya programado. Supongo que podré añadir más."""
    with open('M2L1\images\mem2.jpg','rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    memelist.append = ["mem2.jpg"]

@bot.command()
async def mem3(ctx):
    """Un meme ya programado. Supongo que podré añadir más."""
    with open('M2L1\images\mem3.jpg','rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    memelist.append = ["mem3.jpg"]

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    ''' Imagen aleatorio de patos.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

descomposicion={
    "botella":500,
    "lata":50,
    "bolsa":150,
    "vidrio":4000
}
@bot.command()
async def impacto(ctx,objeto:str):
    objeto=objeto.lower()
    if objeto in descomposicion:
        tiempo=descomposicion[objeto]
        await ctx.send(f"El objeto {objeto} dura aproximadamente {tiempo} en descomponerse.")
        if tiempo>=100:
            await ctx.send(f"Vayase preocupando. Por favor.")
        elif tiempo>=50:
            await ctx.send(f"Ok, algo preocupante.")

    else: 
        await ctx.send("No registro este objeto.")

bot.run("Aquí va el token.")