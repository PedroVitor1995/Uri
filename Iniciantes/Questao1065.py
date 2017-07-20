def main():
	qtd = 0
	for i in range(5):
		numero = input('Digite um numero: ')
		if numero % 2 == 0:
			qtd += 1
	print('%d valores pares')% qtd
if __name__ == '__main__':
	main()