def main():
	x = int(input())
	y = int(input())
	if x > y:
		maior = x
		menor = y
	else:
		maior = y
		menor = x
	soma = 0
	for i in range(menor,maior+1):
		if i % 13 != 0:
			soma += i
	print(soma)
if __name__ == '__main__':
	main()