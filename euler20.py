from math import factorial 
# convert to string every number in factorial of 100 
# and save them as integers and print the sum of all 
print(sum([int(x) for x in str(factorial(100))]))