# getFactorial method here
def getFactorial(n):
    num = 1
    n2 = n
    for x in range(n,1,-1):
        num = num*x
    print("Factorial of " + str(n2) + " is " + str(num))



#main method

getFactorial(5)
getFactorial(4)
getFactorial(8)
getFactorial(15)
getFactorial(6)
getFactorial(9)
getFactorial(3)

