def main():	
	distancia = int(input())
	combustivel = float(input())

	consumo = distancia / combustivel

	print("%0.3f km/l" %consumo)
if __name__ == '__main__':
	main()