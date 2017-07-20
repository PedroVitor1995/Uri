def main():
	soma = 0
	qtd = 0
	while True:
		idade = input('Digite a idade de uma pessoa: ')
		if idade < 0:
			break
		else:
			soma += idade
			qtd += 1
	media = soma / float(qtd)
	print('%.2f')% media
if __name__ == '__main__':
	main()