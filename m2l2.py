import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$sol1'):
        await message.channel.send(f'Melalukan penyaringan terhadap asap atau limbah asap yang akan dibuang ke udara bebas agar tidak terlalu membahayakan kesehatan Bumi')
    if message.content.startswith('$sol2'):
        await message.channel.send(f'coba browsing dan terapkan, saya malas')
    if message.content.startswith('$sol3'):
        await message.channel.send(f'ngotak')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
        
client.run("MTEwMzk4MzA3NTE4MTk5ODE0MQ.GZSf52.pOunrvryY6kmtJXodOm4ljDBhYWWTqN8tBb_V0")