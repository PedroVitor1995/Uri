def main():
	while True:
		try:
			linha = input().split(" ")
			n = int(linha[0])
			m = linha[1]
			soma = 0
			for numero in m:
				soma += int(numero)
			if(soma % 3 == 0):
				print("%d sim"%soma)
			else:
				print("%d nao"%soma)
		except:
			break;
if __name__ == '__main__':
	main()