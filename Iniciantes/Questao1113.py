def main():
	while True:
		numero = (raw_input('').split(' '))
		numero1 = int(numero[0])
		numero2 = int(numero[1])
		if numero1 == numero2:
			break
		else:
			if numero1 < numero2:
				print('Crescente')
			else:
				print('Decrescente')
if __name__ == '__main__':
	main()