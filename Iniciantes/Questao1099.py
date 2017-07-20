def main():
	teste = input('')
	comeco = 0
	fim = 0
	soma = 0
	for i in range(teste):
		numero = (raw_input('').split(' '))
		numero1 = int(numero[0])
		numero2 = int(numero[1])
		if numero1 < numero2:
			comeco = numero1
			fim = numero2
		else:
			comeco = numero2
			fim = numero1
		for i in range(comeco+1,fim):
			if i % 2 != 0:
				soma += i
		print soma
		soma = 0
if __name__ == '__main__':
	main()