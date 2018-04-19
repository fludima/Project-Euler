from decimal import *
from time import sleep


best_bet = 0
d = 2
a = float(1)
current_best = 0
the_d = d
while d < 1000:
	a = Decimal(1 / d)
	a = str(a)
	pattern = ''
	seen_once = 0
	for i in a[2:]:
		pattern = pattern + i 
	for j in pattern:
		if i == j:
			seen_once+=1
			if seen_once == 2:
				if current_best < len(pattern):
						current_best = len(pattern)
						the_d = d

						


	d+=1

print(current_best)
print(the_d)