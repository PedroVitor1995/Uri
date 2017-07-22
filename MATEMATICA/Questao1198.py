# -*- coding: utf-8 -*-
def main():
	while True:
		try:
			linha = input().split(" ")
			exercito1 = int(linha[0])
			exercito2 = int(linha[1])
			diferenca = 0
			if(exercito1 > exercito2):
				diferenca = exercito1 - exercito2
			else:
				diferenca = exercito2 - exercito1
			print(diferenca)
		except:
			break;
if __name__ == '__main__':
	main()