from functools import lru_cache

@lru_cache(5000)
def fib(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

n = 1
while True:
	if len(str(fib(n)))==1000:
		print(n)
		break
	else:
		n+=1

