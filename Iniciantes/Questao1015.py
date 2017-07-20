from math import sqrt as raiz
def main():
	x1 = float(input(''))
	y1 = float(input(''))
	x2 = float(input(''))
	y2 = float(input(''))

	distancia = raiz ((x2 - x1) ** 2.0  +  (y2 - y1) ** 2.0)

	print('%.4f') % distancia
if __name__ == '__main__':
	main()