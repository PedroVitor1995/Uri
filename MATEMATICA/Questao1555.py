# -*- coding: utf-8 -*-

def main():
	N = int(input())
	for i in range(N):
		linha = input().split(" ")
		x = int(linha[0])
		y = int(linha[1])
		rafa = ((3 * x) ** 2) + (y ** 2)
		beto = (2 * (x ** 2)) + ((5 * y) ** 2)
		carlos = -100 * x + (y ** 3)
		if(rafa > beto and rafa > carlos):
			print("Rafael ganhou")
		elif(beto > rafa and beto > carlos):
			print("Beto ganhou")
		elif(carlos > rafa and carlos > beto):
			print("Carlos ganhou")
if __name__ == '__main__':
	main()