# -*- coding: utf-8 -*-
def main():
	numeros = input().split(' ')
	x = float(numeros[0])
	y = float(numeros[1])
	if x == 0 and y == 0:
		print('Origem')
	elif x == 0 and y != 0:
		print('Eixo Y')
	elif x != 0 and y == 0:
		print('Eixo X')
	else:
		if x > 0 and y > 0:
			print('Q1')
		elif x < 0 and y > 0:
			print('Q2')
		elif x < 0 and y < 0:
			print('Q3')
		elif x > 0 and y < 0:
			print('Q4')
if __name__ == '__main__':
	main()