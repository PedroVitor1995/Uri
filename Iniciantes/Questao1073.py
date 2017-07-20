def main():
	while True:
		numero = input()
		if numero > 5 and numero <  2000:
			break
	for i in range(1,numero+1):
		if i > 0:
			if i % 2 == 0:
				raiz = i ** 2
				print('%d^2 = %d')%(i,raiz)
if __name__ == '__main__':
	main()