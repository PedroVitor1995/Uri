def main():
	while True:
		numero = input('')
		if numero > 0 and numero < 1000000:
			break
	nota1 = numero / 100
	nota2 = (numero % 100)/ 50
	nota3 = ((numero % 100) % 50) / 20
	nota4 = (((numero % 100) % 50) % 20) / 10
	nota5 = ((((numero % 100) % 50) % 20) % 10) / 5
	nota6 = (((((numero % 100) % 50) % 20) % 10) % 5) / 2
	nota7 = ((((((numero % 100) % 50) % 20) % 10) % 5) % 2) / 1
	print('%d') % numero
	print('%d nota(s) de R$ 100,00') % nota1
	print('%d nota(s) de R$ 50,00') % nota2
	print('%d nota(s) de R$ 20,00') % nota3
	print('%d nota(s) de R$ 10,00') % nota4
	print('%d nota(s) de R$ 5,00') % nota5
	print('%d nota(s) de R$ 2,00') % nota6
	print('%d nota(s) de R$ 1,00') % nota7
if __name__ == '__main__':
	main()