import random

def makeValues():
    values =[1,2,3,4,5,6,7,8,9,0,0,0,0]
    deckValues = []
#Code that generates 52 values on deckValues list [1,1,1,1,2,2,2,2,3,3,3,3......]
    num = 0
    for x in range(13):
        for y in range(4):
            deckValues.append(values[num])
        num+=1
    return deckValues

def makeNames():
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deckNames = []
    num = 0
    num2 = 0
    deckSuites = ["Spades", "Clubs", "Hearts", "Clubs"]
    
#Code that generates 52 names on deckNames list ["A Spades","A Diamonds","A Hearts", "A Clubs",...    
    for x in range(13):
        for y in range(4):
            deckNames.append(cards[num] + " " + deckSuites[num2])
            num2+=1
        num+=1
        num2 = 0
    return deckNames

#Method dealNames that extracts and returns card name
def dealNames(num, deckName):
    name = deckName.pop(num)
    return name

#Method dealValues  that extracts and returns card value
def dealValues(num,deckValue):
    value = deckValue.pop(num)
    return value

#Method handTotal that calculates and returns the hand total,
#if total is >9 returns just the last digit 
def handTotal(values):
    sum = 0
    for x in range(0, len(values)):
        sum+=values[x]
    if(sum > 9):
        sum = sum%10
    
    return sum
    
#main program

money = 100

while money > 0:
    #Completely cleans deck so that refilled deck is always 52, instead of appending 52 new cards into cards not used
    nameDeck = []
    valueDeck = []

    #Intializes/Refills deck to 52 cards so program can work
    nameDeck = makeNames()
    valueDeck = makeValues()

    AHandNames = [] #List that saves  2 or 3 hand cards names for player A
    AHandValues = [] #List that saves 2 or 3 hand cards values for player A
    BHandNames = []   #List that saves  2 or 3 hand cards values for player B
    BHandValues = [] #List that saves  2 or 3 hand cards values for player B
    
    bet = input ("Choose either Player A or Player B to win: ")

    #Method that generates cards for Player A and B
    for x in range(0, 2):
        #A Values
        num = random.randint(0,len(nameDeck)-1)
        AHandNames.append(dealNames(num, nameDeck))
        AHandValues.append(dealValues(num, valueDeck))

        #B values
        num2 = random.randint(0,len(nameDeck)-1)
        BHandNames.append(dealNames(num2, nameDeck))
        BHandValues.append(dealValues(num2, valueDeck))

    #Commands to print Player A Cards
    print("Player A cards: ", AHandNames)
    print("Initial hand value: ", handTotal(AHandValues))
    if(handTotal(AHandValues) <= 7):
        num = random.randint(0,len(nameDeck)-1)
        AHandNames.append(dealNames(num, nameDeck))
        AHandValues.append(dealValues(num, valueDeck))
        print("Player A draws: ", AHandNames[len(AHandNames)-1])
    else:
        print("Player A is done")
    print("Player A final total is: ",handTotal(AHandValues))
    print()

    #Commands to print Player B Cards
    print("Player B cards: ", BHandNames)
    print("Initial hand value: ", handTotal(BHandValues))
    if(handTotal(BHandValues) <= 7):
        num = random.randint(0,len(nameDeck)-1)
        BHandNames.append(dealNames(num, nameDeck))
        BHandValues.append(dealValues(num, valueDeck))
        print("Player B draws: ", BHandNames[len(BHandNames)-1])
    else:
        print("Player A is done")
    print("Player B final total is: ",handTotal(BHandValues))
    print()

    #Calculations for winning
    if(handTotal(AHandValues) > handTotal(BHandValues)):
        print("Player A wins")
    elif (handTotal(AHandValues) < handTotal(BHandValues)):
        print("Player B wins")
    elif (handTotal(AHandValues) == handTotal(BHandValues)):
        print("It's a tie")

    if(handTotal(AHandValues) > handTotal(BHandValues) and bet == "A" or handTotal(AHandValues) < handTotal(BHandValues) and bet == "B"):
        print("You win!")
        money+=10
    elif(handTotal(AHandValues) == handTotal(BHandValues)):
        print("NO winner")
    else:
        print("You lose!")
        money -=10
    print("money is: ",money, "\n")    
    
