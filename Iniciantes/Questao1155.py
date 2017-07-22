def main():
	S = 0
	aux = 1
	for i in range(1,100+1):
		c = 1/i
		S += c
	print("%.2f"%S)
if __name__ == '__main__':
	main()