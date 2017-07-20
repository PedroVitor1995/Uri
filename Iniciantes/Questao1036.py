from math import sqrt
def main():
	numeros = input().split(' ')
	A = float(numeros[0])
	B = float(numeros[1])
	C = float(numeros[2])
	if A == 0 or B == 0 or C == 0:
		print('Impossivel calcular')
	else:
		delta =  (B ** 2) - (4 * A * C)
		if delta > 0:
			x1 = (- B + sqrt(delta)) / (2 * A)
			x2 = (- B - sqrt(delta)) / (2 * A)
			print('R1 = %.5f'%x1)
			print('R2 = %.5f'%x2)
		else:
			print('Impossivel calcular')

if __name__ == '__main__':
	main()