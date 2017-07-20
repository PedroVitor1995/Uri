def main():
	while True:
		valor = int(input())
		soma = 0
		qtd = 5
		if valor == 0:
			break
		else:
			if valor % 2 == 0:
				valor = valor
			else:
				valor = valor + 1
			while qtd > 0:
				soma += valor
				valor += 2
				qtd -= 1
			print(soma)
			soma = 0

if __name__ == '__main__':
	main()