from time import sleep


with open('euler22.txt','r') as some_txt:
	some_txt = some_txt.read()
	some_txt = list(eval(some_txt))
	some_txt = sorted(some_txt)

	suma = 0
	for i in some_txt:
		abstract = 0
		for char in i:
			abstract= abstract + (ord(char.lower())-96)

		suma = suma + (abstract * (some_txt.index(i)+1))
		
	

print(suma)



