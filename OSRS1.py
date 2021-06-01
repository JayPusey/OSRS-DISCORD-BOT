#################################################################################
#               OSRS PRICE CHECKING BOT ON DISCORD                              #
#                                                                               #
#               CREATED BY SOCKS#1988                                           #
#                                                                               #
#               PURPOSE: A BOT THAT CALLS THE OSRS WIKI FOR ITEM PRICE          #
#                        LEARNING HOW TO INTERACT WITH THE API                  #
#                                                                               #
#################################################################################
import os
import requests
import json
import discord
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

itemnames = []
itemid = []
with open('itemids.txt') as itemids:
    content = itemids.read().splitlines()
for line in content:
    fields = line.lower().split(",")
    itemnames.append(fields[0].lower())
    itemid.append(fields[1])
zipbObj = zip(itemid,itemnames)
itemDictionary = dict(zipbObj)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content[:1] == TRIGGERCHAR:           
        if message.content.lower()[1:6] == 'value':
            item = message.content[7:].lower()
            itemID = findItemID(itemDictionary, item)
            if itemID == 'ERROR':
                await message.channel.send("Cannot find item: " + item)
            else:
                values = GetValueData(itemID)
                if item[0] in Vouels:
                    refferal = 'an'
                else: refferal = 'a'
                await message.channel.send("The price of " + refferal+ " "+
                                           item[:1].upper()+item[1:] + " is as follows:" 
                                           "\nHigh Value:\t" + str("{:,}".format(values[0]))+ " GP per item" +
                                           "\nLow Value :\t" + str("{:,}".format(values[1])) + " GP per item" +
                                           "\nInformation Taken from https://oldschool.runescape.wiki/w/" +
                                           item.replace(" ", "_"))

def GetValueData(item):
    value_url = (WIKI_BASE_URL + item)
    values = json.loads(requests.get(value_url, headers=headers).text)
    print(values)
    H_value = values['data'][item]['high']
    L_value = values['data'][item]['low']
    value_list = [H_value, L_value]
    return value_list

def findItemID(itemIDs, item):
    try:
        itemID = itemIDs[item]
    except KeyError: itemID = 'ERROR'
        
    return itemID
    
client.run(TOKEN)
