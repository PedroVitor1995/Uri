def main():
	anterior1 = 0
	anterior2 = 1
	numero_vezes = input('Digite quantas vezes quer testar: ')
	print anterior1, anterior2,
	for i in range(numero_vezes):
		if i >= 2:
			atual = anterior1 + anterior2
			print atual,
			anterior1 = anterior2
			anterior2 = atual
if __name__ == '__main__':
	main()