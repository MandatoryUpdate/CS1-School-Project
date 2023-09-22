#Importing Songs into Runner
from Songs import *


song1 = Songs("Joe Biscuit", "African Wildflower", 285)
song2 = Songs("Stock Holm", "I'm Locked Up", 194)
song3 = Songs("Miss Take", "Oops", 212)
song4 = Songs("Roe Bout", "Beep Boop", 222)
print(song1)
print(song2)
print(song3)
print(song4)
song1.setArtist("A-Pun")
song1.setArtist("It's A Joke")
print(song1)
print(song4.getArtist())
