def main():
	while True:
		N = input('')
		if N > 0 and N < 13:
			break
	fatorial = 0 
	for i in range(N):
		if i > 0:
			fatorial += (N * (N - i))
	print fatorial
if __name__ == '__main__':
	main()