def main():
	linha = input().split(" ")
	A = int(linha[0])
	B = int(linha[1])
	soma = (A + B) * (B - A + 1) // 2
	print(soma)
if __name__ == '__main__':
	main()