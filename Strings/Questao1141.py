# -*- coding: utf-8 -*-
def main():
	while True:
		teste = int(input())
		if teste == 0:
			break
		texto = []
		for i in range(teste):
			texto.append(input())
		tamanho_total = len(texto)
		menor_string = min(texto)
		tamanho_menor_string = len(menor_string)
		qtd_igual = 0
		qtd_diferente = 0
		for i in range(tamanho_total-1):
			for j in range(i+1,tamanho_total):
				if (texto[i][:tamanho_menor_string:]) == (texto[j][:tamanho_menor_string:]):
					qtd_igual += 1
				else:
					qtd_diferente += 1
		if qtd_diferente == 0:
			print('1')
		else:
			if qtd_diferente > qtd_igual:
				print(tamanho_total - qtd_igual)
			else:
				print((tamanho_total - qtd_diferente) + 1)
if __name__ == '__main__':
	main()