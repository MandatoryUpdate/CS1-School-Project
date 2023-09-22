def count_pairs( s ):
  #add in code to count
    pairs = 0
    for x in range(0, len(s)-2, 1):
        if(s[x] == s[x+1]):
            pairs+=1
    
  #how many pairs of letters exist
  #return the number of letter pairs in each string
  #aadogbbcatcc would return 3
  #aadogcatcc would return 2
    return pairs

print ( count_pairs("ddogccatppig") )
print ( count_pairs("dogcatpig") )
print ( count_pairs("xxyyzz") )
print ( count_pairs("a") )
print ( count_pairs("abc") )
print ( count_pairs("aabb") )
print ( count_pairs("dogcatpigaabbcc") )
print ( count_pairs("aabbccdogcatpig") )
print ( count_pairs("dogabbcccatpig") )
print ( count_pairs("aaaa") )
print ( count_pairs("AAAAAAAAA") )
