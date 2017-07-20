def main():
	vetor_x = []
	for i in range(10):
		vetor_x.append(input('Digite um numero: '))
	for i in range(len(vetor_x)):
		if vetor_x[i] <= 0:
			vetor_x[i] = 1
	for i in range(len(vetor_x)):
		print('X[%d] = %d') % (i,vetor_x[i])
if __name__ == '__main__':
	main()