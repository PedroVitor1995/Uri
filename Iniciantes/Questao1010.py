def main():	
	linha1 = (raw_input().split(" "))
	linha2 = (raw_input().split(" "))
	qtd1 = int(linha1[1])
	valor1 = float(linha1[2])
	qtd2 = int(linha2[1])
	valor2 = float(linha2[2])
	total1 = qtd1 * valor1
	total2 = qtd2 * valor2
	total = total1 + total2
	print('VALOR A PAGAR: R$ %.2f') % total
if __name__ == '__main__':
	main()