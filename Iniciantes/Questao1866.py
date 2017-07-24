def main():
	N = int(input())
	for i in range(N):
		C = int(input())
		if(C % 2 == 0):
			print(0)
		else:
			print(1)
if __name__ == '__main__':
	main()