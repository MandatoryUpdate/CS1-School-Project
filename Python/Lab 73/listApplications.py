#App 1:Sum all elements of the list using a method
def sumElements(numbers):
    sum =0;
    for x in numbers:
        sum += x
    return sum

myList = [2,6,8,3,5,8]
print(myList)
print("The sum of all elements is = ",sumElements(myList))#calling the method

#App 2: Find a number in the list
myList = [2,6,8,3,5,8]
number =6
if number in myList:
    print("I found the number")
else:
    print("No number")
#App3: number of times
myList =[4,7,8,8,4,6,7,0,7]
number =7
counter =0
for x in myList:
    if x==number:
        counter+=1
print(counter)

#App 4: Create a sublist of 2 random elements from the original list
import random
def getFruit(myFruits,randFruit):
    theFruit =myFruits.pop(randFruit)
    return theFruit


fruits = ["apple", "banana", "orange", "papaya", "mango"]
print("The original list is: ", fruits)
subFruits  =[] # sublist to save two fruits
#First fruit
rand=random.randint(0,len(fruits)-1)
subFruits.append(getFruit(fruits,rand))# calling a method
#Second fruit
rand=random.randint(0,len(fruits)-1)
subFruits.append(getFruit(fruits,rand))
print("The new fruit sublist is: ", subFruits)
print("The new original list is: ", fruits)
