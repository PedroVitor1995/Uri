# -*- coding: utf-8 -*-
def main():
	while True:
		try:
			linha = input().split(" ")
			A = int(linha[0])
			B = int(linha[1])
			C = int(linha[2])

			if(A != B and A != C):
				print("A")
			elif(B != C and B != A):
				print("B")
			elif(C != A and C != B):
				print("C")
			else:
				print("*")
		except:
			break;
if __name__ == '__main__':
	main()