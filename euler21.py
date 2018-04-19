from time import sleep
from functools import lru_cache

@lru_cache(1280)
def d(n):
	lista = []
	for i in range(1,n):
		if n%i==0:
			lista.append(i)

	return lista


def ofc(limit):
	my_lista = []
	i = 0 
	while i<limit:
		for j in range(1, limit):
			if sum(d(i))==j and sum(d(j))==i and i != j:
				print(i)
				print(j)
				my_lista.append(i)
				my_lista.append(j)
				i = j + 1 

		i = i+1
	return my_lista

a = ofc(10000)
print(sum(a))
print(a)