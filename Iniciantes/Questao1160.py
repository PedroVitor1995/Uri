# -*- coding: utf-8 -*-
def main():
	T = int(input())
	for i in range(T):
		linha = input().split(" ")
		PA = int(linha[0])
		PB = int(linha[1])
		G1 = float(linha[2])
		G2 = float(linha[3])

		qtd_anos = 0
		seculo = 0

		while(PA <= PB):
			PA += ((PA*G1)//100)
			PB += ((PB*G2)//100)

			qtd_anos += 1

		if(qtd_anos > 100):
			seculo = 1
		if(seculo == 0):
			print("%d anos."%qtd_anos)
		else:
			print("Mais de 1 seculo.")
if __name__ == '__main__':
	main()