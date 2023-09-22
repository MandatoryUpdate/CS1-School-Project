import random
#create a list

#method 1: Create manually the list
myList = [3,6,8,23,78,90]
print(myList)

#Method 2 : Using for loop
randList=[0]*10
print(randList)
for i in range(len(randList)):
    randList[i] = random.randint(0,20)
    print(randList[i], end=" ")
print(randList)

#method 3: using append
randList=[]
for i in range(10):
    randList.append(random.randint(0,20))
print(randList)

#if in , Special if
fruits = ["animal", "banana", "orange"]
word = "mango"
if word in fruits:
    print("word is there")
else:
    print("word is not there lol get wrekt")
