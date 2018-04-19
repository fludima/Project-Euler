import requests
from bs4 import BeautifulSoup
from time import sleep


basic_req = requests.get('https://projecteuler.net/problem=18').text

soup = BeautifulSoup(basic_req, 'lxml')


p_finder = soup.find('p',{"style":"text-align:center;font-family:'courier new';"})

p_finder = p_finder.text

spliter = p_finder.splitlines()


lista = []
suma = 0

start_pont = 0
for path in range(len(spliter)):
	somepath = spliter[path].split()
	print(somepath)




