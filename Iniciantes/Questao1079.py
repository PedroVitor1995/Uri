def main():
	media = 0
	teste = input('')
	for i in range(teste):
		numero = (raw_input('').split(' '))
		numero1 = float(numero[0])
		numero2 = float(numero[1])
		numero3 = float(numero[2])
		media = ((numero1 * 2) + (numero2 * 3) + (numero3 * 5)) / float(2 + 3 + 5)
		print('%.1f') % media
if __name__ == '__main__':
	main()