def main():
	qtd1 = 0
	qtd2 = 0
	while True:
		numero = input()
		if numero < 10000:
			break
	for i in range(numero):
		numeros = input()
		if numeros >= 10 and numeros <= 20:
			qtd1 += 1
		else:
			qtd2 += 1
	print('%d in')% qtd1
	print('%d out')% qtd2

if __name__ == '__main__':
	main()