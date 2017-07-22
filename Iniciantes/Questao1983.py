def main():
	qtd = int(input())
	notas = []
	mats = []
	max = 0.0
	indice = 0
	for i in range(qtd):
		linha = input().split(" ")
		mat = int(linha[0])
		nota = float(linha[1])
		mats.append(mat)
		notas.append(nota)
	for j in range(qtd):
		if(notas[j] > max):
			max = notas[j]
			indice = j
	if(max < 8):
		print("Minimum note not reached")
	else:
		print(mats[indice])
if __name__ == '__main__':
	main()