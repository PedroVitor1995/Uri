# -*- coding: utf-8 -*-
def main():
	soma = 0.0
	M = []
	O = input()
	for i in range(12):
		linha = []
		for j in range(12):
			numero = float(input())
			linha.append(numero)
		M.append(linha)
	for i in range(12):
		for j in range(12):
			if(j < (11 - i)):
				soma += M[i][j]
			aux -= 1
	if(O == "S"):
		print("%.1f"%soma)
	elif(O == "M"):
		media = soma / 66.0
		print("%.1f"%media)
if __name__ == '__main__':
	main()