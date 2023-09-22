def flip_em( s ):
    reverseNum = s.find(" ")
    reversedWord1 = s[0:reverseNum]
    reversedWord2 = s[reverseNum:len(s)]
    reversedWord3 = reversedWord2 + ", " + reversedWord1
    return reversedWord3

print ( flip_em("aplus comp") )
print ( flip_em("comp aplus") )
print ( flip_em("ben sam") )
print ( flip_em("sally sue") )
print ( flip_em("big man") )
print ( flip_em("fat head") )
