# -*- coding: utf-8 -*-
def main():
	while True:
		numero = float(input())
		if numero >= 0.00 and numero <= 1000000.00:
			break
	aux1 = numero * 100

	nota1 = numero / 100
	aux = numero % 100
	nota2 = aux / 50
	aux = aux % 50
	nota3 = aux / 20
	aux = aux % 20
	nota4 = aux / 10
	aux = aux % 10
	nota5 = aux / 5
	aux = aux % 5
	nota6 = aux / 2
	aux = aux % 2
	moeda1 = aux / 1
	aux1 = aux1 % 100
	moeda2 = aux1 / 50
	aux1 = aux1 % 50
	moeda3 = aux1 / 25
	aux1 = aux1 % 25
	moeda4 = aux1 / 10
	aux1 = aux1 % 10
	moeda5 = aux1 / 5
	aux1 = aux1 % 5
	moeda6 = aux1 / 1


	print('NOTAS:')
	print('%d nota(s) de R$ 100.00') % nota1
	print('%d nota(s) de R$ 50.00') % nota2
	print('%d nota(s) de R$ 20.00') % nota3
	print('%d nota(s) de R$ 10.00') % nota4
	print('%d nota(s) de R$ 5.00') % nota5
	print('%d nota(s) de R$ 2.00') % nota6

	print('MOEDAS:')
	print('%d moeda(s) de R$ 1.00') % moeda1
	print('%d moeda(s) de R$ 0.50') % moeda2
	print('%d moeda(s) de R$ 0.25') % moeda3
	print('%d moeda(s) de R$ 0.10') % moeda4
	print('%d moeda(s) de R$ 0.05') % moeda5
	print('%d moeda(s) de R$ 0.01') % moeda6
if __name__ == '__main__':
	main()