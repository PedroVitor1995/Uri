def main():
	teste = input('')
	comeco = 0
	fim = 0
	contador = 1
	soma = 0
	valor = 0
	for i in range(teste):
		numero = (raw_input('').split(' '))
		numero1 = int(numero[0])
		numero2 = int(numero[1])
		if numero1 % 2 == 0:
			valor = numero1 + 1
		else:
			valor = numero1
		while contador <= numero2: 
			if valor % 2 != 0:
				soma += valor
			valor += 2
			contador += 1
		contador = 1
		print soma
		soma = 0
if __name__ == '__main__':
	main()