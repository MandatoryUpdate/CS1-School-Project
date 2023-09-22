# slicing - substring
word = "watermelon"
print(word[0:5])
print(word[2:6])
print(word[:4])
print(word[3:-2])
print(word[:-3])
print(word[-2:])
print(word[1:1])

#find scan from left to right
word = "Computer Science"
print(word.find("p"))
print(word.find("x"))
space=(word.find(" "))
print(word[space+1:])
#rfind scan string from right to left
word = "Computer Science"
print(word.rfind("e"))
print(word.rfind("c"))
#len size of the string
print(len(word))
#Add String
word1 = "water"
word2 = "melon"
word3 = word1 + " " + word2
print(word3)
chars = len(word3)
print(word1 + " " + word2 + ", the number of characters is " + str(chars))
