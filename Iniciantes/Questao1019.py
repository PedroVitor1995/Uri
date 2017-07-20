def main():
	tempo = input()
	segundos = tempo % 60
	minutos  = (tempo / 60) % 60
	horas = (tempo / 60) / 60
	print('%d:%d:%d')%(horas,minutos,segundos)
if __name__ == '__main__':
	main()