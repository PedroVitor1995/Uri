def main():
	qtd = 0
	for i in range(6):
		numero = input('')
		if numero > 0:
			qtd += 1
	print('%d valores positivos') % qtd
if __name__ == '__main__':
	main()