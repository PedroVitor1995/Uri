def main():
	linha = input().split(" ")
	X = int(linha[0])
	Y = int(linha[1])
	aux = 0
	for i in range(1,Y+1):
		aux += 1
		if(aux == X):
			print("%d"%i,end="")
			aux = 0
			print("\t")
		else:
			print("%d"%i,end=" ")
if __name__ == '__main__':
	main()