def main():
	M = []
	soma = 0
	media = 0
	while True:
		linha_matriz = input('Digite um numero da linha de uma matriz: ')
		if linha_matriz >= 0 and linha_matriz <= 11:
			break
	caractere  = raw_input('Digite S - Soma ou M -  Media: ')
	for i in range(2):
		linha = []
		for j in range(2):
			linha.append(input('Digite um numero: '))
		M.append(linha)
	for i in range(2):
		soma = soma + M[linha_matriz][i]
	media = soma / float(2)
	if caractere == 'S':
		print('%.1f')%soma
	elif caractere == 'M':
		print('%.1f')%media
if __name__ == '__main__':
	main()