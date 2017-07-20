def main():
	hora = (raw_input('').split(' '))

	comeco = int(hora[0])
	fim = int(hora[1])
	tempo = 0

	if comeco >= fim:
		tempo = 24 - comeco + fim
	elif comeco < fim:
		tempo = fim - comeco

	print('O JOGO DUROU %d HORA(S)') % tempo

if __name__ == '__main__':
	main()
