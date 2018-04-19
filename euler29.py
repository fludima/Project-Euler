lista = []

alim = 100
blim = 100
for i in range(2, alim+1):
	for j in range(2, blim+1):
		lista.append(pow(i,j))

print(len(set(lista)))