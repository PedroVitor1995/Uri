# -*- coding: utf-8 -*-
def main():
	N = int(input())
	for i in range(N):
		linha = input().split(" ")
		x = int(linha[0])
		y = int(linha[1])
		area = (x * y) / 2
		print("%d cm2"%area)
if __name__ == '__main__':
	main()