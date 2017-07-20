def main():
	valor = 0
	vetor_N = []
	while  True:
		valor = input('Digite um valor: ')
		if valor <= 50:
			break
	for i in range(10):
		if i == 0:
			Numero = valor
		else:
			Numero = Numero * 2
		vetor_N.append(Numero)
	for i in range(10):
		print('N[%d] = %d') % (i,vetor_N[i])
if __name__ == '__main__':
	main()