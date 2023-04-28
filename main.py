import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import discord_webhook
from discord_webhook import DiscordWebhook
import colorama
from colorama import Fore
colorama.init(autoreset=True)


your_webhook = "https://discord.com/api/webhooks/1101504342240014417/PyTumBJNIMLRn0LIyNtr2515jPqIX5UhcylQrg3VXPGgN5PZ68BtHBFXYoXSWfPrqd8y"


intents = discord.Intents.default()
intents.message_content = True

#await message.author.send(msg)

bot = Bot("!", intents=intents)



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=":)", url="https://twitch.tv/:)"))
    os.system("cls")
    print(f"""{Fore.RED}

                                                          $$\     $$\                      $$\                     $$\ 
                                                          $$ |    \__|                     $$ |                    $$ |
 $$$$$$$\  $$$$$$\  $$\   $$\        $$$$$$\   $$$$$$$\ $$$$$$\   $$\ $$\    $$\ $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$$ |
$$  _____|$$  __$$\ $$ |  $$ |       \____$$\ $$  _____|\_$$  _|  $$ |\$$\  $$  |\____$$\.\_$$  _|  $$  __$$\ $$  __$$ |
\$$$$$$\  $$ /  $$ |$$ |  $$ |       $$$$$$$ |$$ /        $$ |    $$ | \$$\$$  / $$$$$$$ | $$ |    $$$$$$$$ |$$ /  $$ |
 \____$$\ $$ |  $$ |$$ |  $$ |      $$  __$$ |$$ |        $$ |$$\ $$ |  \$$$  / $$  __$$ | $$ |$$\ $$   ____|$$ |  $$ |
$$$$$$$  |$$$$$$$  |\$$$$$$$ |      \$$$$$$$ |\$$$$$$$\   \$$$$  |$$ |   \$  /  \$$$$$$$ | \$$$$  |\$$$$$$$\ \$$$$$$$ |
\_______/ $$  ____/  \____$$ |       \_______| \_______|   \____/ \__|    \_/    \_______|  \____/  \_______| \_______|
          $$ |      $$\   $$ |                                                                                         
          $$ |      \$$$$$$  |                                                                                         
          \__|       \______/                                                                                          
""")




@bot.event
async def on_message(message):
    with open('./logs/loggedmsg.txt', 'a', encoding="utf-8") as add:
        add.write(f"""{message.content} > {message}
""")
    tt = f"{Fore.RED}[{Fore.MAGENTA}+{Fore.RED}] New message detected > {message.content} | Author: {message.author}"
    tt2 = f"{Fore.RED}[{Fore.MAGENTA}*{Fore.RED}] You can check the logs in ./logs/loggedmsg.txt"
    print(tt)
    print(tt2)
    result = f"""
**New message detected!**
*message* **{message.content}**
*user:* **{message.author}**"""
    webhook = DiscordWebhook(url=your_webhook, content=result, username="natIVE")
    webhook.execute()









bot.run("MTEwMTQ5ODk3NzYwMzU2MzYzMQ.GCI8B0.XIl895jpmXVYnsaeXnwDKq9wa7IeoCxKG7qkus")