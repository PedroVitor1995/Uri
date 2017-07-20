# -*- coding: utf-8 -*-
def main():
	while True:
		numeros = input().split(' ')
		numero1 = numeros[0]
		numero2 = numeros[1]
		soma = ''
		if int(numero1) == int(numero2) and int(numero2) == 0:
			break
		soma = int(numero1) + int(numero2)
		soma = str(soma)
		soma = soma.replace('0', '')
		print(soma)
if __name__ == '__main__':
	main()