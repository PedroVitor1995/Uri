def main():
	valor_x = input('Digite um valor: ')
	vetor_N = []
	for i in range(100):
		if i == 0:
			Numero = valor_x
		else:
			Numero = Numero / 2
		vetor_N.append(Numero)
	for i in range(len(vetor_N)):
		print('N[%d] = %.4f') % (i,vetor_N[i])
if __name__ == '__main__':
	main()