def main():
	tempo = input('')
	velocidade = input('')

	litros = tempo * velocidade / 12.0
	print('%.3f') % litros
if __name__ == '__main__':
	main()