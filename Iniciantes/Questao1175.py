def main():
	vetor_N = []
	for i in range(5):
		vetor_N.append(input('Digite um numero: '))
	vetor_N = vetor_N[::-1]
	for i in range(5):
		print('N[%d] = %d') % (i,vetor_N[i])
if __name__ == '__main__':
	main()