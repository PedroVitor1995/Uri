def main():
	salario = float(input(''))
	reajuste = 0
	novo_salario = 0

	if salario <= 400.00:
		reajuste = salario * 0.15
		novo_salario = salario + reajuste
		print('Novo salario: %.2f') % novo_salario
		print('Reajuste ganho: %.2f') % reajuste
		print('Em percentual: 15 %')
	elif salario > 400.00 and salario <= 800.00:
		reajuste = salario * 0.12
		novo_salario = salario + reajuste
		print('Novo salario: %.2f') % novo_salario
		print('Reajuste ganho: %.2f') % reajuste
		print('Em percentual: 12 %')
	elif salario > 800.00 and salario <= 1200.00:
		reajuste = salario * 0.10
		novo_salario = salario + reajuste
		print('Novo salario: %.2f') % novo_salario
		print('Reajuste ganho: %.2f') % reajuste
		print('Em percentual: 10 %')
	elif salario > 1200.00 and salario <= 2000.00:
		reajuste = salario * 0.07
		novo_salario = salario + reajuste
		print('Novo salario: %.2f') % novo_salario
		print('Reajuste ganho: %.2f') % reajuste
		print('Em percentual: 7 %')	
	else:
		reajuste = salario * 0.04
		novo_salario = salario + reajuste
		print('Novo salario: %.2f') % novo_salario
		print('Reajuste ganho: %.2f') % reajuste
		print('Em percentual: 4 %')
if __name__ == '__main__':
	main()