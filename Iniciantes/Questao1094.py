def main():
	teste = input()
	qtd_cobaias = 0
	qtd_coelho = 0
	qtd_rato = 0
	qtd_sapo = 0
	for i in range(teste):
		linha = (raw_input().split(' '))
		quantia = int(linha[0])
		tipo = linha[1]
		qtd_cobaias += quantia
		if tipo == 'C':
			qtd_coelho += quantia
		elif tipo == 'R':
			qtd_rato += quantia
		elif tipo == 'S':
			qtd_sapo += quantia
	percentual_coelho = (qtd_coelho * 100) / float(qtd_cobaias)
	percentual_rato = (qtd_rato * 100) / float(qtd_cobaias)
	percentual_sapo = (qtd_sapo * 100) / float(qtd_cobaias)

	print('Total: %d cobaias')%qtd_cobaias
	print('Total de coelhos: %d')%qtd_coelho
	print('Total de ratos: %d')%qtd_rato
	print('Total de sapos: %d')%qtd_sapo
	print('Percentual de coelhos: %.2f %%')%percentual_coelho
	print('Percentual de ratos: %.2f %%')%percentual_rato
	print('Percentual de sapos: %.2f %%')%percentual_sapo
if __name__ == '__main__':
	main()