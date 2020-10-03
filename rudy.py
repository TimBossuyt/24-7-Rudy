import discord
import requests
import os
from googletrans import Translator, constants
translator = Translator()

def get_fact():
    fact = requests.get('https://uselessfacts.jsph.pl/random.json').json()['text']
    translation = translator.translate(fact, dest='nl')
    return translation.text

client = discord.Client()

@client.event
async def on_message(message):
    print(message.content)
    if message.content == '!weetje':
        msg = get_fact()
        await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='Vroeger was alles beter'))

client.run(os.environ['token'])