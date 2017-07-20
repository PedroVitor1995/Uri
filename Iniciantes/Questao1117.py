def main():
	qtd = 0
	soma = 0
	media = 0
	while True:
		nota = input('')
		if nota > 0 and nota <= 10:
			soma += nota
			qtd += 1
		else:
			print('nota invalida')
		media = soma / 2.0
		if qtd == 2:
				print('media = %.2f') % media
				break
if __name__ == '__main__':
	main()