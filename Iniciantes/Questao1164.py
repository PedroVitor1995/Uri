# -*- coding: utf-8 -*-
def main():
	N = int(input())
	for i in range(N):
		X = int(input())
		perf = 0
		for j in range(1,X):
			if(X % j == 0):
				perf += j
				if(perf > X):
					break;
		if(perf == X):
			print("%d eh perfeito"%X)
		else:
			print("%d nao eh perfeito"%X)
if __name__ == '__main__':
	main()