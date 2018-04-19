from math import factorial
from time import sleep
import operator


brojevi = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 
		   6: 'six', 7:'seven', 8:'eight', 9:'nine'}

brojevi_10 = {10:'ten', 11:'eleven', 12:'twelve',13:'thirteen', 14:'fourteen', 15:'fifteen',
		   16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}

brojevi_20 = {20:'twenty', 30:'thirty', 40:'forty', 
			 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}


brojevi_1000 = {}

for k,v in brojevi.items():
	brojevi_1000[int(str(k)+'00')] = v+' '+'hundred'
	if k==10:
		break

brojevi_1000[1000] = 'one thousand'


dict_1_99 = {}
for k,v in brojevi.items():
	dict_1_99[k] = v

for k,v in brojevi_10.items():
	dict_1_99[k] = v

for k,v in brojevi_20.items():
	dict_1_99[k] = v
	for m,j in brojevi.items():
		dict_1_99[k+m] = v + ' ' + j	

dict_1_1000 = {}
for k,v in brojevi_1000.items():
	dict_1_1000[k] = v
	for i,o in dict_1_99.items():
		dict_1_1000[k+i] = v + ' and ' + o

for k,v in dict_1_99.items():
	dict_1_1000[k] = v


suma = 0
replaced_dict = {}

for k,v in dict_1_1000.items():
	replaced_dict[k] = v.replace(' ', '')

# print(suma)
# for values in replaced_dict.values():
# 	suma = suma + len(values)

for i in range(1,1001):
	suma = suma + len(replaced_dict[i])

print(suma)