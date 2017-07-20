def main():
	numero = input('')
	valor = input('')
	comeco = 0
	fim = 0
	if numero > valor:
		fim = numero
		comeco = valor
	else:
		comeco = numero
		fim = valor
	soma = 0

	for i in range(comeco+1,fim):
		if i % 2 != 0:
			soma += i
	print soma
if __name__ == '__main__':
	main()
