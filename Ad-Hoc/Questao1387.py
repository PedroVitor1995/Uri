# -*- coding: utf-8 -*-
def main():
	while True:
		linha = input().split(" ")
		L = int(linha[0])
		R = int(linha[1])
		soma = L + R
		if(L == R and R == 0):
			break;
		else:
			print(soma)
if __name__ == '__main__':
	main()