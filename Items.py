class Items:

    global Armory
    global itemDictionary
    Armory = {}
    Item_Ref = {}
    itemnames = []
    itemid = []
    
    with open('itemids.txt') as itemids:
        content = itemids.read().splitlines()
    for line in content:
        fields = line.lower().split(",")
        item_info = dict(Item_Members = fields[2],Item_HAlc = fields[3], Item_LAlc = fields[4],Item_Examine = fields[5])
        Armory[fields[0]] = item_info
        itemnames.append(fields[0].replace('"', ''))
        itemid.append(fields[1])
        
    itemDictionary = dict(zip(itemid, itemnames))
    print(list(itemDictionary)[-1] + ":\t" + str(itemDictionary[list(itemDictionary)[-1]]))
    print(list(Armory)[-1] + ":\t" + str(Armory[list(Armory)[-1]]))


def findItemID(item_to_check):
    
        try:
            itemID = itemDictionary[str('"'+item_to_check+'"')]
        except KeyError:
            itemID = 'ERROR'
        return itemID

def HighAlc(itemID):

    HighAlc = Armory[itemID]['Item_HAlc']
    return HighAlc

def LowAlc(itemID):
    LowAlc = Armory[itemID]['Item_LAlc']
    return LowAlc    

def Examine(itemID):
    Examine = Armory[itemID]['Item_Examine']
    return Examine
