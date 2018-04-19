from time import sleep
limit_n = 28123 


# for i in range(1, n):
# 	values = 0
# 	for j in range(1, i):
def is_abd(num):
	num = int(num)
	lista = []
	suma = 0
	for i in range(1, num):
		if num%i==0:
			suma = suma+ i
	if suma>num:
		return True
	else: 
		return False
	
	
