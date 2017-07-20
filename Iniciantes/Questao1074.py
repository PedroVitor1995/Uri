def main():
	while True:
		N = input()
		if N < 10000:
			break
	for i in range(N):
		numero = input()
		if numero == 0:
			print('NULL')
		elif numero % 2 == 0:
			if numero < 0:
				print('EVEN NEGATIVE')
			else:
				print('EVEN POSITIVE')
		elif numero % 2 != 0:
			if numero < 0:
				print('ODD NEGATIVE')
			else:
				print('ODD POSITIVE')
if __name__ == '__main__':
	main()