# -*- coding: utf-8 -*-
def main():
	while True:
		N = int(input())
		qtd1 = 0
		qtd2 = 0
		for i in range(N):
			linha = input().split(" ")
			A = int(linha[0])
			B = int(linha[1])
			if(A > B):
				qtd1 += 1
			elif(B > A):
				qtd2 += 1
		if(N == 0):
			break;
		else:
			print("%d %d"%(qtd1,qtd2))
if __name__ == '__main__':
	main()