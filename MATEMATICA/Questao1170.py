# -*- coding: utf-8 -*-
def main():
	N = int(input())
	for i in range(N):
		dias = 1
		valor = float(input())
		while True:
			div = valor / 2
			if(div <= 1):
				break;
			else:
				valor = div
				dias += 1
		print("%d dias"%dias)
if __name__ == '__main__':
	main()