def main():	
	valor = (raw_input().split(" "))

	a = int(valor[0])
	b = int(valor[1])
	c = int(valor[2])

	maiorAB = (a + b + abs(a - b)) / 2
	maior = (maiorAB + c + abs(maiorAB - c)) / 2
	print('%d eh o maior') % maior
if __name__ == '__main__':
	main()