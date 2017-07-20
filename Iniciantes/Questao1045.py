def main():
	lados = input().split(' ')
	lado1 = float(lados[0])
	lado2 = float(lados[1])
	lado3 = float(lados[2])
	A = 0
	B = 0
	C = 0
	if lado1 >= lado2 and lado1 >= lado3:
		A = lado1
		if lado2 >= lado3:
			B = lado2
			C = lado3
		else:
			B = lado3
			C = lado2
	elif lado2 >= lado1 and lado2 >= lado3:
		A = lado2
		if lado1 >= lado3:
			B = lado1
			C = lado3
		else:
			B = lado3
			C = lado1
	elif lado3 >= lado1 and lado3 >= lado2:
		A = lado3
		if lado1 >= lado2:
			B = lado1
			C = lado2
		else:
			B = lado2
			C = lado1

	if A >= B + C:
		print('NAO FORMA TRIANGULO')
	else:
		if (A ** 2) == (B ** 2) + (C ** 2):
			print('TRIANGULO RETANGULO')

		if (A ** 2) > (B ** 2) + (C ** 2):
			print('TRIANGULO OBTUSANGULO')

		if (A ** 2) < (B ** 2) + (C ** 2):
			print('TRIANGULO ACUTANGULO')

		if A == B and A == C and B == C:
			print('TRIANGULO EQUILATERO')
		elif A == B or A == C or B == C:
			print('TRIANGULO ISOSCELES')
if __name__ == '__main__':
	main()