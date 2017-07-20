def main():
	maior = 0
	posicao = 1
	vetor = []
	for i in range(5):
		vetor.append(input(''))
	for i in range(5):
		maior = vetor[0]
	for i in range(5):
		if vetor[i] > maior:
			maior = vetor[i]
			posicao = i + 1
	print maior
	print posicao
if __name__ == '__main__':
	main()