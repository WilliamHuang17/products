import random
import os

if os.path.isfile('product.csv'):
	print('file product.csv exists')
else:
	print('file product.csv not exists \n')
	print('teminated \n')
	quit()
# check if file exists
product_list = []
with open('product.csv', 'r') as f:
	for p in f:
		if 'a,1' in p:
			continue
		name, price =  p.strip().split(',')
		product_list.append([name, price])		
while True:
	name = input('product name ? ')
	if name == 'q':
		break
	price = input('product price ? ')
	product_list.append([name, price])
with open('product.csv', 'w')	as f:
	for p in product_list:
		f.write(p[0] + ',' + p[1] + '\n')

