from itertools import permutations

a = permutations('0123456789',10)
a = list(a)
some = [''.join(x) for x in a]
 #creates a list where numbers are joined 123456789 instead of '1','2'..
print(some[1000000-1]) 
#We need the milionth minus 1 because the indexing starts at 0 instead of 1