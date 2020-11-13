import discord, asyncio, socket, json, time, sys, requests
from colorama import *
import io, random, threading, requests, os
from discord.ext import commands
from discord.ext.commands import Bot
from colorama import Fore, init
from selenium import webdriver
bot = commands.Bot(description='SERVER SPAMMER!', command_prefix='x')
bot.remove_command('help')

def Clear():
    os.system('cls')

token = input("Enter users token : ")
head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
if src.status_code == 200:
    print(f"{Fore.WHITE} Valid token")
    input("Press any key")
else:
    print(f'{Fore.WHITE} Invalid token')
    input(f"Press any key")
    exit(0)
Clear()

ServerName = input("Enter Message:")

if ServerName == "":
    print("Error Didnt enter a message!")
    input("Press Any key.")
    exit(0)
else:
    print("Press any key to continue")
    input("")
Clear()


print(f'''{Fore.WHITE}Starting...''')

def MassServers():
    print("Spamming servers..")

    @bot.event
    async def on_connect(times: int=95):
        for i in range(times):
            await bot.create_guild(name=ServerName, region=None, icon=None)
            print(f"{Fore.WHITE}Created {i} Servers!")
        else:
            print('\n')
            print('done')
            input()
    bot.run(token, bot=False)


def mainanswer():
    answer = input(f"")
    if answer == 'start':
        MassServers()
    else:
        print("error")
        MassServers()

MassServers()

    