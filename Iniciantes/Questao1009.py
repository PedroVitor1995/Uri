def main():	
	nome = raw_input('')
	salario_fixo = float(input(''))
	qtd_de_evendas = float(input(''))

	total = salario_fixo + float(15*qtd_de_evendas/100)

	print('TOTAL = R$ %.2f') % total
if __name__ == '__main__':
	main()