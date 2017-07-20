from math import sqrt as raiz
def main():
	while True:
		numero_vezes = input('Digite um numero inteiro: ')
		if numero_vezes >= 1 and numero_vezes <= 100:
			break
	for i in range(numero_vezes):
		numero = input('Digite um numero: ')
		raiz_quadrada = raiz (numero)
		raiz_quadrada = int (raiz_quadrada)
		quadrado_numero = raiz_quadrada ** 2
		if numero != 1 and quadrado_numero != numero :
			if numero == 2 or numero % 2 != 0 :
				if numero == 2 or numero % 3 != 0 or numero == 3 :
					if numero == 2 or numero % 5 != 0 or numero == 5 :
						if numero == 2 or numero % 7 != 0 or numero == 7 :
							if numero == 2 or numero % 9 != 0 :
								print ('%d eh primo ') % (numero)
							else :
								print ('%d nao eh primo ') % (numero)
						else :
							print ('%d nao eh primo ') % (numero)
					else :
						print ('%d nao eh primo ') % (numero)
				else :
					print ('%d nao eh primo ') % (numero)
			else :
				print ('%d nao eh primo ') % (numero)
		else :
			print ('%d nao eh primo ') % (numero)

if __name__ == '__main__':
	main()

