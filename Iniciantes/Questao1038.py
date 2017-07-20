def main():
	numeros = (raw_input('').split(' '))
	numero = int(numeros[0])
	qtd = int(numeros[1])
	valor = 0

	if numero == 1:
		valor = qtd * 4.0
	elif numero == 2:
		valor = qtd * 4.5
	elif numero == 3:
		valor = qtd * 5.0
	elif numero == 4:
		valor = qtd * 2.0
	elif numero == 5:
		valor = qtd * 1.5
	print('Total: R$ %.2f') % valor
if __name__ == '__main__':
	main()