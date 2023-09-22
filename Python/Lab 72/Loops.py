"""
#for loop
for x in range(0,5,1):
    print(x,end=" ")
for x in range(7):
    print(x,end=" ")
for x in range(9,0,-1):
    print(x,end=" ")
#each for loop
    for x in "hola":
        print(x,end = " ");
"""
#print all letters until finds the letter s

word = "Computer Science"
for letter in word:
    if letter == "S":
        break
    print(letter,end=" ")
"""
#count how many letters are on the string
counter = 0
word = "catsss and dogsss"
for letter in word:
    if letter == "s":
        counter+=1
print(counter)
"""
