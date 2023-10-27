import discord
import time

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('éçevre nedir'):
        await message.channel.send(f'yeşilliğe çevre denir zvzvzv')
    elif  message.content.startswith('é'):
        await message.channel.send(f'bu olmadan benimle konuşamassın.Bunsuz benimle konuşmayı denersen...')
        time.sleep(2)
        await message.channel.send(f'özürdilerim annem çağırdıda.Ama anladın yani değilmi')

        
client.run("")
