def main():
	qtd_produtos = int(input())
	soma = 0
	for i in range(qtd_produtos):
		compras = input().split()
		tipo = int(compras[0])
		quantidade = int(compras[1])
		if tipo == 1001:
			soma += (quantidade * 1.5)
		elif tipo == 1002:
			soma += (quantidade * 2.5)
		elif tipo == 1003:
			soma += (quantidade * 3.5)
		elif tipo == 1004:
			soma += (quantidade * 4.5)
		elif tipo == 1005:
			soma += (quantidade * 5.5)
	print('%.2f'%soma)
if __name__ == '__main__':
	main()