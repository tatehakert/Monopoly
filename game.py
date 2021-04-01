#monopoly
import random

players = {
    "1": {
        "position": 0,
        "balance": 1500,
        "in-jail": False,
        "hasGetOutOfJailCard": False
    },
    "2": {
        "position": 0,
        "balance": 1500,
        "in-jail": False,
        "hasGetOutOfJailCard": False
    }
}

boardPositions = {
    0: {
        "name": "Start",
        "role": None,
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    1: {
        "name": "Mediterranean Avenue",
        "role": "property",
        "propertySet": "purple",
        "canPurchase": True,
        "purchasePrice": 60,
        "hitCount": 0
    },
    2: {
        "name": "Community Chest",
        "role": "community chest",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    3: {
        "name": "Baltic Avenue",
        "role": "property",
        "propertySet": "purple",
        "canPurchase": True,
        "purchasePrice": 60,
        "hitCount": 0
    },
    4: {
        "name": "Income Tax",
        "role": "tax",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    5: {
        "name": "Reading Railroad",
        "role": None,
        "propertySet": None,
        "canPurchase": 200,
        "purchasePrice": None,
        "hitCount": 0
    },
    6: {
        "name": "Oriental Avenue",
        "role": "property",
        "propertySet": 'sky',
        "canPurchase": True,
        "purchasePrice": 100,
        "hitCount": 0
    },
    7: {
        "name": "Chance",
        "role": "chance",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    8: {
        "name": "Vermont Avenue",
        "role": "property",
        "propertySet": 'sky',
        "canPurchase": True,
        "purchasePrice": 100,
        "hitCount": 0
    },
    9: {
        "name": "Connecticut Avenue",
        "role": "property",
        "propertySet": 'sky',
        "canPurchase": True,
        "purchasePrice": 120,
        "hitCount": 0
    },
    10: {
        "name": "Jail/Just Visiting",
        "role": "jail",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    11: {
        "name": "St. Charles Place",
        "role": "property",
        "propertySet": "pink",
        "canPurchase": True,
        "purchasePrice": 140,
        "hitCount": 0
    },
    12: {
        "name": "Electric Company",
        "role": "utility",
        "propertySet": "utilities",
        "canPurchase": True,
        "purchasePrice": 150,
        "hitCount": 0
    },
    13: {
        "name": "States Avenue",
        "role": "property",
        "propertySet": "pink",
        "canPurchase": True,
        "purchasePrice": 140,
        "hitCount": 0
    },
    14: {
        "name": "Virginia Avenue",
        "role": "property",
        "propertySet": "pink",
        "canPurchase": True,
        "purchasePrice": 160,
        "hitCount": 0
    },
    15: {
        "name": "Pennsylvania Railroad",
        "role": "railroad",
        "propertySet": "railroads",
        "canPurchase": True,
        "purchasePrice": 200,
        "hitCount": 0
    },
    16: {
        "name": "St. James Place",
        "role": "property",
        "propertySet": "orange",
        "canPurchase": True,
        "purchasePrice": 180,
        "hitCount": 0
    },
    17: {
        "name": "Community Chest",
        "role": "community chest",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    18: {
        "name": "Tennessee Avenue",
        "role": "property",
        "propertySet": "orange",
        "canPurchase": True,
        "purchasePrice": 180,
        "hitCount": 0
    },
    19: {
        "name": "New York Avenue",
        "role": "property",
        "propertySet": "orange",
        "canPurchase": True,
        "purchasePrice": 200,
        "hitCount": 0
    },
    20: {
        "name": "Free Parking",
        "role": None,
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    21: {
        "name": "Kentucky Avenue",
        "role": "property",
        "propertySet": "red",
        "canPurchase": True,
        "purchasePrice": 220,
        "hitCount": 0
    },
    22: {
        "name": "Chance",
        "role": "chance",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    23: {
        "name": "Indiana Avenue",
        "role": "property",
        "propertySet": "red",
        "canPurchase": True,
        "purchasePrice": 220,
        "hitCount": 0
    },
    24: {
        "name": "Illinois Avenue",
        "role": "property",
        "propertySet": "red",
        "canPurchase": True,
        "purchasePrice": 240,
        "hitCount": 0
    },
    25: {
        "name": "B & O Railroad",
        "role": "railroad",
        "propertySet": "railroads",
        "canPurchase": True,
        "purchasePrice": 200,
        "hitCount": 0
    },
    26: {
        "name": "Atlantic Avenue",
        "role": "property",
        "propertySet": "yellow",
        "canPurchase": True,
        "purchasePrice": 260,
        "hitCount": 0
    },
    27: {
        "name": "Ventnor Avenue",
        "role": "propery",
        "propertySet": "yellow",
        "canPurchase": True,
        "purchasePrice": 260,
        "hitCount": 0
    },
    28: {
        "name": "Water Works",
        "role": "utility",
        "propertySet": "utilities",
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    29: {
        "name": "Marvin Gardens",
        "role": None,
        "propertySet": "yellow",
        "canPurchase": True,
        "purchasePrice": 280,
        "hitCount": 0
    },
    30: {
        "name": "Go To Jail!",
        "role": "send to jail",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    31: {
        "name": "Pacific Avenue",
        "role": "property",
        "propertySet": "green",
        "canPurchase": True,
        "purchasePrice": 300,
        "hitCount": 0
    },
    32: {
        "name": "North Carolina Avenue",
        "role": "property",
        "propertySet": "green",
        "canPurchase": True,
        "purchasePrice": 300,
        "hitCount": 0
    },
    33: {
        "name": "Community Chest",
        "role": None,
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    34: {
        "name": "Penisylvania Avenue",
        "role": "property",
        "propertySet": "green",
        "canPurchase": True,
        "purchasePrice": 320,
        "hitCount": 0
    },
    35: {
        "name": "Short Line",
        "role": "railroad",
        "propertySet": "railroads",
        "canPurchase": True,
        "purchasePrice": 200,
        "hitCount": 0
    },
    36: {
        "name": "Chance",
        "role": "chance",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    37: {
        "name": "Park Place",
        "role": "propery",
        "propertySet": "blue",
        "canPurchase": True,
        "purchasePrice": 350,
        "hitCount": 0
    },
    38: {
        "name": "Luxury Tax",
        "role": "tax",
        "propertySet": None,
        "canPurchase": False,
        "purchasePrice": None,
        "hitCount": 0
    },
    39: {
        "name": "Boardwalk",
        "role": "property",
        "propertySet": "blue",
        "canPurchase": True,
        "purchasePrice": 400,
        "hitCount": 0
    }
}
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

while running and turns < 1000000:
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
                    print("Player", playerId, " rolled doubles! You have been released from jail!")
                    players[playerId]["in-jail"] = False
                    players[playerId]["position"] = (players[playerId]["position"] + total) % 40
                    boardPositions[players[playerId]["position"]]["hitCount"] += 1
                    rollAgain = False
                else:
                    print("sorry! you must roll doubles to be released from jail")
            else:
                currentPosition = players[playerId]["position"]
                newPosition = (currentPosition + total) % 40
                boardPositions[newPosition]["hitCount"] += 1 

                if newPosition < currentPosition:
                    # print("Player", playerId, " passed start --> collect $200")
                    players[playerId]["balance"] = players[playerId]["balance"] + 200
                    
                players[playerId]["position"] = newPosition
                # print("Player", playerId, " landed at ", boardPositions[newPosition]["name"])

                if boardPositions[newPosition]["role"] == "tax":
                    # print("Player", playerId, " owes taxes --> pay $100")
                    players[playerId]["balance"] = players[playerId]["balance"] - 100
                elif boardPositions[newPosition]["role"] == "property":
                    if boardPositions[newPosition]["canPurchase"]:
                        if players[playerId]["balance"] > (4 * boardPositions[newPosition]["purchasePrice"]):
                            # print("Player", playerId, " is purchasing this property --> pay ", boardPositions[newPosition]["purchasePrice"])
                            players[playerId]["balance"] -= boardPositions[newPosition]["purchasePrice"]
                            boardPositions[newPosition]["canPurchase"] = False
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

for pos in boardPositions:
    print(pos, "\tcount: ", boardPositions[pos]["hitCount"], "\tpercentage: ", boardPositions[pos]["hitCount"]/1000000,"\tname: ", boardPositions[pos]["name"])