from time import sleep

text = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'

text = text.strip().split()

value_dict = {}
encountered = 0

for i in text:
	value_dict[i] = 0

for word in text:
	if word in value_dict.keys():
		value_dict[word] = value_dict[word] + 1
	
for k,v in sorted(value_dict.items()):
		print(k,v)
