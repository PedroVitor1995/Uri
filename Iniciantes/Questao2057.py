def main():
	linha = input().split(" ")
	S = int(linha[0])
	T = int(linha[1])
	F = int(linha[2])

	horario = S + T + F
	if(horario > 24):
		horario -= 24
	if(horario < 0):
		horario += 24
	print(horario)
if __name__ == '__main__':
	main()