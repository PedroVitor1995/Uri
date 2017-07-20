def main():
	vetor_X = []
	posicao = 0
	while True:
		valor = input()
		if valor > 1 and valor < 1000:
			break
	vetor_X = [int(i) for i in raw_input().split()]
	menor = vetor_X[0]

	for i in range(valor):
		if vetor_X[i] < menor:
			menor = vetor_X[i]
			posicao = i
	print('Menor valor: %d') % menor
	print('Posicao: %d') % posicao
if __name__ == '__main__':
	main()