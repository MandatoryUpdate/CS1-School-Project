def pythonGreat():
    print("에야디야")

def myMethod(num):
    return num + 100;
'''
#Example input and if - else

name = input("What's your name? ")
age = int(input("How old are you? "))
print("\nYour name is: ", name)
if age >= 65:
    print("You are a senior")
elif age >= 21 and age < 65: #Else if in Java
    print("You are an adult")
else:
    print("You are probably in highschool")
'''

#Calling methods main program
pythonGreat()
print(myMethod(7))
print(myMethod(50))
