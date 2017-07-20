def main():
	tipo = int(input())
	resposta = input().split(' ')
	qtd = 0
	for i in range(5):
		if int(resposta[i]) == tipo:
			qtd += 1
	print(qtd)
if __name__ == '__main__':
	main()