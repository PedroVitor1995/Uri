# -*- coding: utf-8 -*-
def main():
	M = []
	soma = 0
	media = 0
	caractere  = input()
	for i in range(12):
		linha = []
		for j in range(12):
			linha.append(float(input()))
		M.append(linha)
	for i in range(12):
		i += 1
		for j in range(12):
			soma += (M[i][j])

	media = soma / float(12)
	if caractere == 'S':
		print('%.1f')%soma
	elif caractere == 'M':
		print('%.1f')%media
if __name__ == '__main__':
	main()