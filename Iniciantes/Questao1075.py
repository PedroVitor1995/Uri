def main():
	while True:
		N = input()
		if N < 50:
			break
	for i in range(1,50):
		if i % N == 2:
			print i
if __name__ == '__main__':
	main()