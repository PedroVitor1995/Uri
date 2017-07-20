def main():
	numeros = (raw_input('').split(' '))
	numero = int(numeros[0])
	valor = int(numeros[1])
	primeiro = 0
	segundo = 0
	if numero < valor:
		primeiro = numero
		segundo = valor
	else:
		primeiro = valor
		segundo = numero
	if segundo % primeiro == 0:
		print('Sao Multiplos')
	else:
		print('Nao sao Multiplos')
if __name__ == '__main__':
	main()