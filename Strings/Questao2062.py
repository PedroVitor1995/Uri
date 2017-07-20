# -*- coding: utf-8 -*-
def main():
	teste = int(input())
	palavras = input().split()
	texto = ''
	for i in range(teste):
		if len(palavras[i]) == 3:
			if palavras[i][0] == 'U' and palavras[i][1] == 'R':
				texto += 'URI'
			elif palavras[i][0] == 'O' and palavras[i][1] == 'B':
				texto += 'OBI'
			else:
				texto += palavras[i]
		else:
			texto += palavras[i]

		if i != (teste - 1):
			texto += ' '
	print(texto)
if __name__ == '__main__':
	main()