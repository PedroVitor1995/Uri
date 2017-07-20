def main():
	teste = int(input('teste: '))
	letra_ascii = ''
	letra_normal = ''
	for i in range(teste):
		caractere = input('Caractere: ')
		for letra in caractere:
			letra_ascii = ord(letra)
			if letra_ascii >= 65 and letra_ascii <= 90:
				letra_ascii = ord(letra) + 2
				letra_normal += chr(letra_ascii)
			elif letra_ascii >= 97 and letra_ascii <= 122:
				letra_ascii = ord(letra) + 2
				letra_normal += chr(letra_ascii)
			else:
				letra_normal += chr(letra_ascii)
		print(letra_normal[::-1])
		letra_normal = ''
		letra_ascii = ''
if __name__ == '__main__':
	main()