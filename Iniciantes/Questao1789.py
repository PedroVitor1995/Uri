def main():
	while True:
		try:
			qtd_lesma = input()

			velocidade = (raw_input().split(' '))
			mais_veloz = int(velocidade[0])

			for i in range(qtd_lesma):
				if mais_veloz < int(velocidade[i]):
					mais_veloz = int(velocidade[i])
			if mais_veloz < 10:
				print('1')
			elif mais_veloz >= 10 and mais_veloz < 20:
				print('2')
			else:
				print('3')
		except EOFError:
			break

if __name__ == '__main__':
	main()