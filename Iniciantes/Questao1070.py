def main():
	numero = input('')
	for i in range(6+1):
		if numero % 2 != 0:
			print numero
			numero += 2
		else:
			numero += 1
if __name__ == '__main__':
	main()