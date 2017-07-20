def main():
	qtd1 = 0
	qtd2 = 0
	qtd3 = 0
	while True:
		numero = int(input())
		if numero == 4:
			break
		else:
			if numero == 1:
				qtd1 += 1
			elif numero == 2:
				qtd2 += 1
			elif numero == 3:
				qtd3 += 1
	print('MUITO OBRIGADO')
	print('Alcool: {}'.format(qtd1))
	print('Gasolina: {}'.format(qtd2))
	print('Diesel: {}'.format(qtd3))
if __name__ == '__main__':
	main()