def main():
	fib = []
	anterior1 = 0
	anterior2 = 1
	fib = [anterior1,anterior2]
	for i in range(60):
		atual = anterior1 + anterior2
		fib.append(atual)
		anterior1 = anterior2
		anterior2 = atual
	numero_teste = input('Digite quantas vezes quer testar: ')
	for i in range(numero_teste):
		posicao = input('Digite a posicao: ')
		print('Fib(%d) = %d') % (posicao,fib[posicao])
if __name__ == '__main__':
	main()