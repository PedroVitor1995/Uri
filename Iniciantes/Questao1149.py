# -*- coding: utf-8 -*-
def main():
	while True:
		numero = (raw_input('').split(' '))
		A = int(numero[0])
		N = int(numero[1])
		if N <= 0:
			while True:
				N = input('')
				if N > 0:
					break
			break
		else:
			break
	contador = 1
	soma = 0
	while contador <= N: 
			soma += A
			A += 1
			contador += 1
	print soma

if __name__ == '__main__':
	main()