import os
import requests
import json
import discord
import Items
from dotenv import load_dotenv

##INITIALISING BOT##

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

DISCORD_NAME = 'Discord Name'

Vouels = ['a','e','i','o','u']

##CONSTANTS/STRINGS##
TRIGGERCHAR = '!'
JSON = '.json'

##OSRS SOURCE##

OSRS_BASE_URL = 'http://services.runescape.com/m=itemdb_oldschool'
OSRS_GRAPH = '/api/graph/'
OSRS_VALUE = '/api/catalogue/detail.json?item='

##WIKI SOURCE##
WIKI_BASE_URL = 'https://prices.runescape.wiki/api/v1/osrs/latest?id='



headers = {
    'User-Agent': 'Personal Discord bot for price checking',
    'From': DISCORD_NAME
    }

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content[:1] == TRIGGERCHAR:
        user_message = message.content.lower()
        BotMessage = Triggered(user_message)
        await message.channel.send(BotMessage)
                

def GetValueData(item):
    value_url = (WIKI_BASE_URL + item)
    values = json.loads(requests.get(value_url, headers=headers).text)
    print(values)
    H_value = values['data'][item]['high']
    L_value = values['data'][item]['low']
    value_list = [H_value, L_value]
    return value_list


def Triggered(user_message):
    if user_message[1:6] == 'value':
            item = user_message[7:].lower()
            itemID = Items.findItemID(item)
            if itemID == 'ERROR':
                botMessage = str("Cannot find item: " + item)
            else:
                values = GetValueData(itemID)
                if item[0] in Vouels:
                    refferal = 'an'
                else: refferal = 'a'
                botMessage = str("The price of " + refferal+ " "+
                                           item[:1].upper()+item[1:] + " is as follows:" 
                                           "\nHigh Value:\t" + str("{:,}".format(values[0]))+ " GP per item" +
                                           "\nLow Value :\t" + str("{:,}".format(values[1])) + " GP per item" +
                                           "\nInformation Taken from https://oldschool.runescape.wiki/w/" +
                                           item.replace(" ", "_"))
    if user_message.lower()[1:8]== 'highalc':
            item = user_message[9:].lower()
            itemID = Items.findItemID(item)
            if itemID != 'ERROR':
                HighAlc = Items.HighAlc(itemID)
                botMessage = str("You will get " + HighAlc + " GP by casting High level Alchemy on " + item[:1].upper()+item[1:])

    if user_message.lower()[1:7]== 'lowalc':
            item = user_message[8:].lower()
            itemID = Items.findItemID(item)
            if itemID != 'ERROR':
                LowAlc = Items.LowAlc(itemID)
                botMessage = str("You will get " + LowAlc + " GP by casting Low level Alchemy on " + item[:1].upper()+item[1:])

    if user_message.lower()[1:8] == 'examine':
            item = user_message[9:].lower()
            itemID = Items.findItemID(item)
            if itemID != 'ERROR':
                Examine = Items.Examine(itemID)
                botMessage = str(Examine)
                
    if itemID == 'ERROR':
        botMessage = str("Cannot find item: " + item[:1].upper()+item[1:])
    return botMessage

client.run(TOKEN)
