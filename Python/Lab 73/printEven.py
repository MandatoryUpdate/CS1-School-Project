def printEvens(listNum):
    for x in range(0, len(listNum)-1, 1):
        if listNum[x]%2 == 0:
            print(listNum[x])
    print("\n")




bob = [3,5,6,33,1,10,12,17,20,5]
printEvens( bob ) 

bob = [32,52,62,33,12,10,12,17,20,52]
printEvens( bob ) 
