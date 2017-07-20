def main():
	qtd = int(input())
	for i in range(qtd):
		if(i <= qtd-2):
			print("Ho ", end="")
		elif(i == qtd-1):
			print("Ho!")
if __name__ == '__main__':
	main()