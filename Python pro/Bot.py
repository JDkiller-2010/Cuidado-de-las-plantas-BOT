import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def inicio(ctx):
    await ctx.send('Holi')

@bot.command()
async def Lanzamiento(ctx):
    moneda = random.randint(1,2)
    if moneda == 1:
        resultado = 'cara'
    if moneda == 2:
        resultado = 'cruz'
    await ctx.send(f'El resultado es {resultado}')

@bot.command()
async def Platinos(ctx,*,genero:str):
    listaPLA = {'Metroidvania': ['Hollow Knight'],
                'shooter': ['CS2'],
                'RPG': ['Undertale y Deltarune']
                }
    if genero in listaPLA:
        lista = listaPLA[genero]
        respuesta = f"Los juegos del genero {genero} son:"
        for i in range(len(listaPLA)):
            respuesta += f"{listaPLa[i]}"
    else:
        respuesta = "No tenemos ese genero"
    await ctx.send(respuesta)


@bot.command()
async def meme2(CTX):
    with open("Imagenes/meme2.jpg", "rb") as f:
        picture = discord.File(f)
    await CTX.send(file=picture)

@bot.command()
async def memes(CTX):
    lista_imagenes = os.listdir("Imagenes")
    with open(f"Imagenes/{random.choice(lista_imagenes)}", "rb") as f:
        picture = discord.File(f)
    await CTX.send(file=picture)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def Cuidado_de_las_plantas(CTX):
    await CTX.send("La tala desmedida de arboles es un gran problema ambiental el cual hace que la eliminacion de gases de invernaderos sea mas laboriosa, y hace que el paisaje se vea asi")
    await CTX.send("Esto pasa ya que la madera es un material extremadamente arraigado en la sociedad para diversas funciones sea construccion, decoraciones, combustible, liberar areas para ganado/cultivos y desastres como incendios forestales y tornados causan una disminucion en la cantidad de flora en la tierra lo que causan que se vean asi")
    lista_plantas = os.listdir("Plantas")
    with open(f"Plantas/{random.choice(lista_plantas)}", "rb") as f:
        picture = discord.File(f)
    await CTX.send(file=picture)
    await CTX.send("Cuidemos, plantemos y seamos conscientes con los arboles que si no no tendremos planeta donde lamentar no haberlo hecho")