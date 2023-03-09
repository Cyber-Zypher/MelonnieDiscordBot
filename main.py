import discord
import random
import requests
import bs4

BOT_TOKEN = 'MTA2OTk2MzYwMzczMTU0NjExMg.GYJJvI.lC4okGBohJqP1ojt0r-FHcbFmRUuLwA3dNn8L8'
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'bot-commands':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'reveal your source code':
            sourcelink = "https://pastebin.com/bnVDWHEx"
            await message.channel.send(f'Here is my source code:' + sourcelink)
            return
        elif user_message.lower() == 'hi':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}')
            return
        elif user_message.lower() == 'random':
            response = f'This is your random number: {random.randrange(10000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'who are you' or user_message.lower() == 'what are you' or user_message.lower() == "who's this" or user_message.lower() == 'who is this':
            await message.channel.send("I am Melonnie! A Multipurpose Discord Bot Created by Sidharth Everett")
            return
        elif user_message.lower() == 'who created you':
            await message.channel.send("I was created by Sidharth Everett.")
            return
        elif user_message.lower() == 'who is your father':
            await message.channel.send("Sidharth Everett is my father!")
            return
        elif user_message.lower() == 'i love you':
            await message.channel.send("Thanks for the complement!")
            return
        elif user_message.lower() == 'i hate you':
            await message.channel.send("Sorry for disappointing you...")
            return
        elif "mellonie" in user_message.lower():
            await message.channel.send("Yes that's me!!!")
        else:
            try:
                googlesearch = user_message.lower()
                url = f"https://www.google.com/search?q={googlesearch}"
                urllink = url.replace(" ", "+")
                request_results = requests.get(url)
                soup = bs4.BeautifulSoup(request_results.text, "html.parser")
                result = soup.find("div", class_="BNeawe").text
                print(result)
                await message.channel.send(f'{result}')
                await message.channel.send("Click this link to get more results " + urllink)
                return
            except Exception as a:
                print(a)
                await message.channel.send("Sorry I can't help you with that because I am still learning..")
                return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere!')
        return


client.run(BOT_TOKEN)
