#monopoly
import random

players = {
    "1": {
        "position": 0,
        "balance": 1500,
        "in-jail": False,
        "hasGetOutOfJailCard": False,
        "properties": {
            "utilities": [],
            "railroads": [],
            "purple": [],
            "sky": [],
            "pink": [],
            "orange": [],
            "red": [],
            "yellow": [],
            "green": [],
            "blue": []
        }
    },
    "2": {
        "position": 0,
        "balance": 1500,
        "in-jail": False,
        "hasGetOutOfJailCard": False,
        "properties": {
            "utilities": [],
            "railroads": [],
            "purple": [],
            "sky": [],
            "pink": [],
            "orange": [],
            "red": [],
            "yellow": [],
            "green": [],
            "blue": []
        }
    }
}



boardPositions = {
    0: {
        "name": "Start",
        "role": None,
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
    },
    1: {
        "name": "Mediterranean Avenue",
        "role": "property",
        "propertySet": "purple",
        "canPurchase": True,
        "purchasePrice": 60,
        "houseCost": 50,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 2,
        "propertiesInSet": [1, 3],
        "rentMultiplier": [1, 5, 15, 45, 80, 125],
    },
    2: {
        "name": "Community Chest",
        "role": "community chest",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
    },
    3: {
        "name": "Baltic Avenue",
        "role": "property",
        "propertySet": "purple",
        "canPurchase": True,
        "purchasePrice": 60,
        "houseCost": 50,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 4,
        "propertiesInSet": [1, 3],
        "rentMultiplier": [1, 5, 15, 45, 80, 125]
    },
    4: {
        "name": "Income Tax",
        "role": "tax",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
        "ownedBy": None,
    },
    5: {
        "name": "Reading Railroad",
        "role": None,
        "propertySet": None,
        "canPurchase": True,
        "purchasePrice": 200,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 25,
        "propertiesInSet": [5, 15, 25, 35],
        "rentMultiplier": [0, 1, 2, 4, 8]
    },
    6: {
        "name": "Oriental Avenue",
        "role": "property",
        "propertySet": 'sky',
        "canPurchase": True,
        "purchasePrice": 100,
        "houseCost": 50,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 6,
        "propertiesInSet": [6, 8, 9],
        "rentMultiplier": [1, 5, 15, 45, 66.66666667, 91.66666667]
    },
    7: {
        "name": "Chance",
        "role": "chance",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
        "ownedBy": None,
    },
    8: {
        "name": "Vermont Avenue",
        "role": "property",
        "propertySet": 'sky',
        "canPurchase": True,
        "purchasePrice": 100,
        "houseCost": 50,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 6,
        "propertiesInSet": [6, 8, 9],
        "rentMultiplier": [1, 5, 15, 45, 66.66666667, 91.66666667]
    },
    9: {
        "name": "Connecticut Avenue",
        "role": "property",
        "propertySet": 'sky',
        "canPurchase": True,
        "purchasePrice": 120,
        "houseCost": 50,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 8,
        "propertiesInSet": [6, 8, 9],
        "rentMultiplier": [1, 5, 12.5, 37.5, 56.25, 75]
    },
    10: {
        "name": "Jail/Just Visiting",
        "role": "jail",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
        "ownedBy": None,
    },
    11: {
        "name": "St. Charles Place",
        "role": "property",
        "propertySet": "pink",
        "canPurchase": True,
        "purchasePrice": 140,
        "houseCost": 100,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 10,
        "propertiesInSet": [11, 13, 14],
        "rentMultiplier": [1,5,15,45,62.5,75]
    },
    12: {
        "name": "Electric Company",
        "role": "utility",
        "propertySet": "utilities",
        "canPurchase": True,
        "purchasePrice": 150,
        "hitCount": 0,
        "ownedBy": None,
        "propertiesInSet": [12, 28],
        "rentMultiplier": [0, 4, 10]
    },
    13: {
        "name": "States Avenue",
        "role": "property",
        "propertySet": "pink",
        "canPurchase": True,
        "purchasePrice": 140,
        "houseCost": 100,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 10,
        "propertiesInSet": [11, 13, 14],
        "rentMultiplier": [1,5,15,45,62.5,75]
    },
    14: {
        "name": "Virginia Avenue",
        "role": "property",
        "propertySet": "pink",
        "canPurchase": True,
        "purchasePrice": 160,
        "houseCost": 100,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 12,
        "propertiesInSet": [11, 13, 14],
        "rentMultiplier": [1,5,15,41.66666667,58.33333333,75]
    },
    15: {
        "name": "Pennsylvania Railroad",
        "role": "railroad",
        "propertySet": "railroads",
        "canPurchase": True,
        "purchasePrice": 200,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 25,
        "propertiesInSet": [5, 15, 25, 35],
        "rentMultiplier": [0, 1, 2, 4, 8]
    },
    16: {
        "name": "St. James Place",
        "role": "property",
        "propertySet": "orange",
        "canPurchase": True,
        "purchasePrice": 180,
        "houseCost": 100,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 14,
        "propertiesInSet": [16, 18, 19],
        "rentMultiplier": [1, 5, 14.28571429, 39.28571429, 53.57142857, 67.85714286]
    },
    17: {
        "name": "Community Chest",
        "role": "community chest",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
        "ownedBy": None,
    },
    18: {
        "name": "Tennessee Avenue",
        "role": "property",
        "propertySet": "orange",
        "canPurchase": True,
        "purchasePrice": 180,
        "houseCost": 100,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 14,
        "propertiesInSet": [16, 18, 19],
        "rentMultiplier": [1, 5, 14.28571429, 39.28571429, 53.57142857, 67.85714286]
    },
    19: {
        "name": "New York Avenue",
        "role": "property",
        "propertySet": "orange",
        "canPurchase": True,
        "purchasePrice": 200,
        "houseCost": 100,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 16,
        "propertiesInSet": [16, 18, 19],
        "rentMultiplier": [1, 5, 13.75, 37.5, 50, 62.5]
    },
    20: {
        "name": "Free Parking",
        "role": None,
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
        "ownedBy": None,
    },
    21: {
        "name": "Kentucky Avenue",
        "role": "property",
        "propertySet": "red",
        "canPurchase": True,
        "purchasePrice": 220,
        "houseCost": 150,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 18,
        "propertiesInSet": [21, 23, 24],
        "rentMultiplier": [1, 5, 13.88888889, 38.88888889, 48.61111111, 58.33333333]
    },
    22: {
        "name": "Chance",
        "role": "chance",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
        "ownedBy": None,
    },
    23: {
        "name": "Indiana Avenue",
        "role": "property",
        "propertySet": "red",
        "canPurchase": True,
        "purchasePrice": 220,
        "houseCost": 150,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 18,
        "propertiesInSet": [21, 23, 24],
        "rentMultiplier": [1, 5, 13.88888889, 38.88888889, 48.61111111, 58.33333333]
    },
    24: {
        "name": "Illinois Avenue",
        "role": "property",
        "propertySet": "red",
        "canPurchase": True,
        "purchasePrice": 240,
        "houseCost": 150,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 20,
        "propertiesInSet": [21, 23, 24],
        "rentMultiplier": [1, 5	, 15, 37.5, 46.25, 55]
    },
    25: {
        "name": "B & O Railroad",
        "role": "railroad",
        "propertySet": "railroads",
        "canPurchase": True,
        "purchasePrice": 200,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 25,
        "propertiesInSet": [5, 15, 25, 35],
        "rentMultiplier": [0, 1, 2, 4, 8]
    },
    26: {
        "name": "Atlantic Avenue",
        "role": "property",
        "propertySet": "yellow",
        "canPurchase": True,
        "purchasePrice": 260,
        "houseCost": 150,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 22,
        "propertiesInSet": [26, 27, 29],
        "rentMultiplier": [1, 5, 15, 36.36363636, 44.31818182, 52.27272727]
    },
    27: {
        "name": "Ventnor Avenue",
        "role": "propery",
        "propertySet": "yellow",
        "canPurchase": True,
        "purchasePrice": 260,
        "houseCost": 150,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 22,
        "propertiesInSet": [26, 27, 29],
        "rentMultiplier": [1, 5, 15, 36.36363636, 44.31818182, 52.27272727]
    },
    28: {
        "name": "Water Works",
        "role": "utility",
        "propertySet": "utilities",
        "canPurchase": True,
        "purchasePrice": 150,
        "hitCount": 0,
        "ownedBy": None,
        "propertiesInSet": [12, 28],
        "rentMultiplier": [0, 4, 10]
    },
    29: {
        "name": "Marvin Gardens",
        "role": None,
        "propertySet": "yellow",
        "canPurchase": True,
        "purchasePrice": 280,
        "houseCost": 150,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 24,
        "propertiesInSet": [26, 27, 29],
        "rentMultiplier": [1, 5, 15, 35.41666667, 42.70833333, 50]
    },
    30: {
        "name": "Go To Jail!",
        "role": "send to jail",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
        "ownedBy": None,
    },
    31: {
        "name": "Pacific Avenue",
        "role": "property",
        "propertySet": "green",
        "canPurchase": True,
        "purchasePrice": 300,
        "houseCost": 200,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 26,
        "propertiesInSet": [31, 32, 34],
        "rentMultiplier": [1, 5, 15, 34.61538462, 42.30769231, 49.03846154]
    },
    32: {
        "name": "North Carolina Avenue",
        "role": "property",
        "propertySet": "green",
        "canPurchase": True,
        "purchasePrice": 300,
        "houseCost": 200,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 26,
        "propertiesInSet": [31, 32, 34],
        "rentMultiplier": [1, 5, 15, 34.61538462, 42.30769231, 49.03846154]
    },
    33: {
        "name": "Community Chest",
        "role": None,
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
        "ownedBy": None,
    },
    34: {
        "name": "Penisylvania Avenue",
        "role": "property",
        "propertySet": "green",
        "canPurchase": True,
        "purchasePrice": 320,
        "houseCost": 200,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 28,
        "propertiesInSet": [31, 32, 34],
        "rentMultiplier": [1, 5.357142857, 16.07142857, 35.71428571, 42.85714286, 50]
    },
    35: {
        "name": "Short Line",
        "role": "railroad",
        "propertySet": "railroads",
        "canPurchase": True,
        "purchasePrice": 200,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 25,
        "propertiesInSet": [5, 15, 25, 35],
        "rentMultiplier": [0, 1, 2, 4, 8]
    },
    36: {
        "name": "Chance",
        "role": "chance",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
        "ownedBy": None,
    },
    37: {
        "name": "Park Place",
        "role": "propery",
        "propertySet": "blue",
        "canPurchase": True,
        "purchasePrice": 350,
        "houseCost": 200,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 35,
        "propertiesInSet": [37, 39],
        "rentMultiplier": [1, 5, 14.28571429, 31.42857143, 37.14285714, 42.85714286]
    },
    38: {
        "name": "Luxury Tax",
        "role": "tax",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0,
        "ownedBy": None,
    },
    39: {
        "name": "Boardwalk",
        "role": "property",
        "propertySet": "blue",
        "canPurchase": True,
        "purchasePrice": 400,
        "houseCost": 200,
        "numHouses": 0,
        "hitCount": 0,
        "ownedBy": None,
        "baseRent": 50,
        "propertiesInSet": [37, 39],
        "rentMultiplier": [1, 3.5, 10, 22, 26, 30]
    }
}

def getRentPrice(position, diceTotal):
    owner = boardPositions[position]["ownedBy"]
    propertiesInSet = boardPositions[position]["propertiesInSet"]
    numOwned = 0
    rentOwed = 0

    for prop in propertiesInSet:
        if boardPositions[prop]["ownedBy"] == owner:
            numOwned+=1

    if position == 12 or position == 28: #utilities
        rentOwed = diceTotal * boardPositions[position]["rentMultiplier"][numOwned]

    elif position == 5 or position == 15 or position == 25 or position == 35: #railroads
        rentOwed = boardPositions[position]["baseRent"] * boardPositions[position]["rentMultiplier"][numOwned]

    elif numOwned == len(propertiesInSet): # if all properties in the set are owned
        if boardPositions[position]["numHouses"] > 0:
            rentOwed = boardPositions[position]["baseRent"] * boardPositions[position]["rentMultiplier"][numOwned]
        else:
            rentOwed = boardPositions[position]["baseRent"] * 2

    else:
        rentOwed = boardPositions[position]["baseRent"] 

    return round(rentOwed)

usedChanceCards = []
chanceCards = [
    {
      "title": "Advance to Go (Collect $200)",
      "action": "move",
      "tileid": 0
    },
    {
      "title": "Advance to Illinois Avenue - If you pass Go, collect $200",
      "action": "move",
      "tileid": 24
    },
    {
      "title": "Advance to St. Charles Place - If you pass Go, collect $200",
      "action": "move",
      "tileid": 11
    },
    {
      "title": "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.",
      "action": "movenearest",
      "propertySet": "utilities",
      "rentmultiplier": 10
    },
    {
      "title": "Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.",
      "action": "movenearest",
      "propertySet": "railroads",
      "rentmultiplier": 2
    },
    {
      "title": "Bank pays you dividend of $50",
      "action": "credit",
      "amount": 50
    },
    {
      "title": "Get out of Jail Free - This card may be kept until needed, or traded/sold",
      "action": "jail",
      "subaction": "getout"
    },
    {
      "title": "Go Back 3 Spaces",
      "action": "move",
      "count": -3
    },
    {
      "title": "Go to Jail - Go directly to Jail - Do not pass Go, do not collect $200",
      "action": "jail",
      "subaction": "goto"
    },
    {
      "title": "Make general repairs on all your property - For each house pay $25 - For each hotel $100",
      "action": "propertyCharges",
      "buildings": 25,
      "hotels": 100
    },
    {
      "title": "Pay poor tax of $15",
      "action": "debit",
      "amount": 15
    },
    {
      "title": "Take a trip to Reading Railroad - If you pass Go, collect $200",
      "action": "move",
      "tileid": 5
    },
    {
      "title": "Take a walk on the Boardwalk - Advance token to Boardwalk",
      "action": "move",
      "tileid": 39
    },
    {
      "title": "You have been elected Chairman of the Board - Pay each player $50",
      "action": "payOtherPlayers",
      "amount": 50
    },
    {
      "title": "Your building loan matures - Collect $150",
      "action": "credit",
      "amount": 50
    }
  ]



running = True
turns = 0

while running and turns < 1000:
    for playerId in players:
        consecutiveTurns = 0
        turns += 1
        rollAgain = True

        while rollAgain == True and consecutiveTurns < 3:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice1 + dice2
            consecutiveTurns += 1
            rollAgain = dice1 == dice2
            # print("dice1: ", dice1, " dice2: ", dice2, " total", total)

            if players[playerId]["in-jail"]:
                if dice1 == dice2:
                    # print("Player", playerId, " rolled doubles! You have been released from jail!")
                    players[playerId]["in-jail"] = False
                    players[playerId]["position"] = (players[playerId]["position"] + total) % 40
                    boardPositions[players[playerId]["position"]]["hitCount"] += 1
                    rollAgain = False
                else:
                    # print("sorry! you must roll doubles to be released from jail")
                    rollAgain = False
            else:
                currentPosition = players[playerId]["position"]
                newPosition = (currentPosition + total) % 40
                boardPositions[newPosition]["hitCount"] += 1 

                if newPosition < currentPosition:
                    print("Player", playerId, " passed start --> collect $200")
                    players[playerId]["balance"] = players[playerId]["balance"] + 200
                    
                players[playerId]["position"] = newPosition
                print("Player", playerId, " landed at ", boardPositions[newPosition]["name"])

                if boardPositions[newPosition]["role"] == "tax":
                    print("Player", playerId, " owes taxes --> pay $100")
                    players[playerId]["balance"] = players[playerId]["balance"] - 100

                elif newPosition == 30:  #pos 30 is go to jail
                    print("Player", playerId, " go to jail!")
                    players[playerId]["position"] = 10
                    boardPositions[10]["hitCount"] += 1
                    players[playerId]["in-jail"] = True
                    rollAgain = False

                elif newPosition == 7 or newPosition == 22 or newPosition == 26: #chance card
                    if len(chanceCards) > 0:
                        chanceCard = chanceCards.pop()
                    else:
                        random.shuffle(usedChanceCards)
                        chanceCards = usedChanceCards
                        usedChanceCards = []
                        chanceCard = chanceCards.pop()
                    
                    if chanceCard["action"] == "move":
                        # print("move")
                        oldPos = players[playerId]["position"]

                        if "count" in chanceCard: 
                            newPos = oldPos + chanceCard["count"]
                            if newPos < 0:
                                newPos += 40
                            else:
                                newPos = newPos % 40
                            players[playerId]["position"] = newPos
                            if chanceCard["count"] > 0 and newPos < oldPos: #player passed go
                                players[playerId]["balance"] += 200
                        else:
                            newPos = chanceCard["tileid"]
                            players[playerId]["position"] = newPos
                            if newPos < oldPos: #player passed go
                                players[playerId]["balance"] += 200

                    elif chanceCard["action"] == "movenearest":
                        #print("movenearest")
                        newPos = None
                        temp = players[playerId]["position"]
                        while not newPos:
                            temp+=1
                            if boardPositions[(temp)%40]["propertySet"] == chanceCard["propertySet"]:
                                newPos = temp
                        players[playerId]["position"] = newPos
                    elif chanceCard["action"] == "credit":
                        #print("credit")
                        players[playerId]["balance"] += chanceCard["amount"]
                    elif chanceCard["action"] == "jail":
                        if chanceCard["subaction"] == "goto":
                            #print("goto jail")
                            players[playerId]["position"] = 10
                            players[playerId]["in-jail"] = True
                            boardPositions[10]["hitCount"] += 1
                        else:
                            #print("getout of jail")
                            players[playerId]["hasGetOutOfJailCard"] = True
                    elif chanceCard["action"] == "propertyCharges":
                        players[playerId]["balance"] -= 100
                    elif chanceCard["action"] == "debit":
                        players[playerId]["balance"] -= chanceCard["amount"]
                    elif chanceCard["action"] == "payOtherPlayers":
                        for player in players:
                            if not player == playerId: 
                                players[playerId]["balance"] -= chanceCard["amount"]
                                players[player]["balance"] += chanceCard["amount"]
                    else:
                        print("could not find chance card")
                    
                    if not (chanceCard["action"] == "jail" and chanceCard["subaction"] == "getout"):
                        usedChanceCards.append(chanceCard)

                elif boardPositions[newPosition]["role"] == "property":
                    if boardPositions[newPosition]["ownedBy"]:
                        if not boardPositions[newPosition]["ownedBy"] == playerId: #if someone else owns the property --> pay rent
                            rentPrice = getRentPrice(newPosition, total)
                            print("Player", playerId, " pays $", rentPrice," in rent at ", boardPositions[newPosition]["name"])
                            players[playerId]["balance"] -= rentPrice
                            players[boardPositions[newPosition]["ownedBy"]]["balance"] += rentPrice
                            for player in players:
                                print(players[player])
                    elif boardPositions[newPosition]["canPurchase"]:
                        if players[playerId]["balance"] > (4 * boardPositions[newPosition]["purchasePrice"]):
                            print("Player", playerId, " is purchasing ", boardPositions[newPosition]["name"]," --> pay ", boardPositions[newPosition]["purchasePrice"])
                            players[playerId]["balance"] -= boardPositions[newPosition]["purchasePrice"]
                            boardPositions[newPosition]["canPurchase"] = False
                            boardPositions[newPosition]["ownedBy"] = playerId
                            players[playerId]["properties"][boardPositions[newPosition]["propertySet"]].append(newPosition)
                            for player in players:
                                print(players[player])
            
            if players[playerId]["balance"] < 0:
                rollAgain = False
                running = False
                print("***Player #", playerId, " is out of money!")
        

        #check which properties are currently owned and decide to purchase houses:
        ownedProperties = players[playerId]["properties"]
        fullSets = []
        for propertySet in ownedProperties:
            if not (propertySet == "utilities" or propertySet == "railroads") and len(ownedProperties[propertySet]) > 0:
                if len(ownedProperties[propertySet]) == len(boardPositions[ownedProperties[propertySet][0]]["propertiesInSet"]): #owns all properties in set
                    fullSets.append(boardPositions[ownedProperties[propertySet][0]]["propertiesInSet"])

        for s in fullSets:
            for pos in s:
                if boardPositions[pos]["numHouses"] < 5 and players[playerId]["balance"] > (2.5 * boardPositions[pos]["houseCost"]): #buy a house
                    print("Player #", playerId, " bought a house for: ", boardPositions[pos]["name"])
                    players[playerId]["balance"] -= boardPositions[pos]["houseCost"]
                    boardPositions[pos]["numHouses"] += 1
                    


for pos in boardPositions:
    print(pos, "\tcount: ", boardPositions[pos]["hitCount"], "\tprobability: ", boardPositions[pos]["hitCount"]/1000,"\tname: ", boardPositions[pos]["name"])

for player in players:
    print(players[player])