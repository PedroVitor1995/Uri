# -*- coding: utf-8 -*-
def main():
	teste = int(input())
	for i in range(teste):
		numero = 0
		palavra = input()
		if len(palavra) == 5:
			numero = 3
		else:
			p0 = palavra[0]
			p1 = palavra[1]
			p2 = palavra[2]
			if ((p0 == 'o' and p1 == 'n') or (p0 == 'o' and p2 == 'e') or\
			(p1 == 'n' and p2 == 'e')):
				numero = 1
			else:
				numero = 2
		print(numero)
if __name__ == '__main__':
	main()