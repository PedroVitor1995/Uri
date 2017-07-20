def main():
	dias = input('')
	ano = dias / 365
	meses = (dias % 365) / 30
	dias = (dias % 365) % 30
	print('%d ano(s)') % ano
	print('%d mes(es)') % meses
	print('%d dia(s)') % dias
if __name__ == '__main__':
	main()