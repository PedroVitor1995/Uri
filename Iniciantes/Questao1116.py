def main():
	divisao = 0
	teste = input('')
	for i in range(teste):
		numero = (raw_input('').split(' '))
		numero1 = int(numero[0])
		numero2 = int(numero[1])
		if numero2 == 0:
			print('divisao impossivel')
		else:
			divisao = numero1 / float(numero2)
			print('%.1f')% divisao
if __name__ == '__main__':
	main()