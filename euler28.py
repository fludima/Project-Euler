n = 1001 
def getnum(n):
	if n==1:
		return 1
	if n%2==0:
		n+=1
	n_x = n**2
	size = n - 1
	uvek = 9 + 7 + 5 + 3 + 1
	suma = 0
	while size>3:
		for i in range(4):
			print(n_x)
			suma = suma + n_x
			n_x = n_x - size
		size = size - 2

	return suma+uvek


print(getnum(2))