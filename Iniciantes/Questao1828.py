def main():
	T = int(input())
	for i in range(T):
		linha = input().split(" ")
		n1 = linha[0]
		n2 = linha[1]
		i = i + 1
		if(n1 == n2):
			print("Caso #%d: De novo!"%i)
		elif(n1 == "tesoura" and n2 == "papel"):
			print("Caso #%d: Bazinga!"%i)
		elif(n1 == "papel" and n2 == "pedra"):
			print("Caso #%d: Bazinga!"%i)
		elif(n1 == "pedra" and n2 == "lagarto"):
			print("Caso #%d: Bazinga!"%i)
		elif(n1 == "lagarto"and n2 == "Spock"):
			print("Caso #%d: Bazinga!"%i)
		elif(n1 == "Spock" and n2 == "tesoura"):
			print("Caso #%d: Bazinga!"%i)
		elif(n1 == "tesoura" and n2 == "lagarto"):
			print("Caso #%d: Bazinga!"%i)
		elif(n1 == "lagarto" and n2 == "papel"):
			print("Caso #%d: Bazinga!"%i)
		elif(n1 == "papel" and n2 == "Spock"):
			print("Caso #%d: Bazinga!"%i)
		elif(n1 == "Spock" and n2 == "pedra"):
			print("Caso #%d: Bazinga!"%i)
		elif(n1 == "pedra" and n2 == "tesoura"):
			print("Caso #%d: Bazinga!"%i)
		else:
			print("Caso #%d: Raj trapaceou!"%i)
if __name__ == '__main__':
	main()