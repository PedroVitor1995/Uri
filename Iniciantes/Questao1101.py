def main():
	while True:
		numero = (raw_input('').split(' '))
		numero1 = int(numero[0])
		numero2 = int(numero[1])
		if numero1 <= 0 or numero2 <= 0:
			break
		else:
			comeco = 0
			fim = 0
			soma = 0
			if numero1 < numero2:
				comeco = numero1
				fim = numero2
			else:
				comeco = numero2
				fim = numero1
			for i in range(comeco,fim+1):
				soma += i
				print('%d') % i,
			print('Sum=%d')%soma
if __name__ == '__main__':
	main()