# -*- coding: utf-8 -*-
def main():
	X = int(input())
	soma = 0
	while True:
		Z = int(input())
		if(Z > X):
			cont = 0
			while(soma <= Z):
				soma += X
				X += 1
				cont += 1
			print(cont)
			break;
if __name__ == '__main__':
	main()