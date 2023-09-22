def findValue(listNum, num):
    sum = 0
    for x in range(0, len(listNum)-1, 1):
        if num == listNum[x]:
            sum+=1
    return sum
            



bob = [3,5,6,33,111,7,7,15,-5,9,1,6,6,7,8,9,5,6,6,6,7,2,7,99,11,8]
print ( findValue( bob, 6 ) )
print ( findValue( bob, 7 ) )
print ( findValue( bob, 5 ) )
