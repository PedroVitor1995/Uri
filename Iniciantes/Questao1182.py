def main():
	M = []
	soma = 0
	media = 0
	while True:
		coluna_matriz = input('Digite um numero da coluna de uma matriz: ')
		if coluna_matriz >= 0 and coluna_matriz <= 11:
			break
	caractere  = raw_input('Digite S - Soma ou M -  Media: ')
	for i in range(3):
		linha = []
		for j in range(3):
			linha.append(input('Digite um numero: '))
		M.append(linha)
	for i in range(3):
			soma = soma + M[i][coluna_matriz]
	media = soma / float(3)
	if caractere == 'S':
		print('%.1f')%soma
	elif caractere == 'M':
		print('%.1f')%media
if __name__ == '__main__':
	main()