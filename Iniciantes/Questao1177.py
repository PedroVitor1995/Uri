def main():
	vetor_N = []
	while True:
		valor = input('Digite um valor: ')
		if valor >= 2 and valor <= 50:
			break
	for i in range(10):
		for j in range(valor):
			vetor_N.append(j)
	for i in range(10):
		print('N[%d] = %d') % (i,vetor_N[i])
if __name__ == '__main__':
	main()