def main():
	N = input()
	for i in range(N+1):
		if i > 0:
			if N % i == 0 :
				print i
if __name__ == '__main__':
	main()