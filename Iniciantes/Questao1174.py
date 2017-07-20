def main():
	vetor_A = []
	for i in range(5):
		vetor_A.append(input('Digite um numero: '))
	for i in range(5):
		if vetor_A[i] <= 10:
			print('A[%d] = %.1f') % (i,vetor_A[i])
if __name__ == '__main__':
	main()