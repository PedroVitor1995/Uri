def main():
	N = int(input())
	for i in range(N):
		linha = input().split(" ")
		nome = linha[0]
		numero = linha[1]
		if(nome == "Thor"):
			print("Y")
		else:
			print("N")
if __name__ == '__main__':
	main()