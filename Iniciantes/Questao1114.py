def main():
	while True:
		senha = input('')
		if senha == 2002:
			print('Acesso Permitido')
			break
		else:
			print('Senha Invalida')
if __name__ == '__main__':
	main()