def main():
	while True:
		N = input()
		if N > 2 and N < 1000:
			break
	for i in range(11):
		if i > 0:
			valor = i * N
			print('%d x %d = %d') % (i,N,valor)
if __name__ == '__main__':
	main()