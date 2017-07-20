def main():
	while True:
		notas = []
		soma = 0
		for i in range(2):
			while True:
				nota = float(input())
				if(nota > 0 and nota <= 10):
					notas.append(nota)
					break;
				else:
					print("nota invalida")
		for j in range(len(notas)):
			soma += notas[j]

		media = soma / 2
		print("media = %.2f"%media)

		resposta = 0
		while True:
			print("novo calculo (1-sim 2-nao)")
			opcao = int(input())
			if(opcao == 1 or opcao == 2):
				resposta = opcao
				break;

		if(resposta == 2):
			break;
if __name__ == '__main__':
	main()