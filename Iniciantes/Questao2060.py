def main():
	teste = int(input())
	numeros = input().split(' ')
	qtd2 = 0
	qtd3 = 0
	qtd4 = 0
	qtd5 = 0
	for i in range(teste):
		if int(numeros[i]) % 2 == 0:
			qtd2 += 1
		
		if int(numeros[i]) % 3 == 0:
			qtd3 += 1
		
		if int(numeros[i]) % 4 == 0:
			qtd4 += 1
		
		if int(numeros[i]) % 5 == 0:
			qtd5 += 1
	print('{} Multiplo(s) de 2'.format(qtd2))
	print('{} Multiplo(s) de 3'.format(qtd3))
	print('{} Multiplo(s) de 4'.format(qtd4))
	print('{} Multiplo(s) de 5'.format(qtd5))
if __name__ == '__main__':
	main()