def main():
	numero1 = input('')
	numero2 = input('')
	comeco = 0
	fim = 0
	if numero1 < numero2:
		comeco = numero1
		fim = numero2
	else:
		comeco = numero2
		fim = numero1
	for i in range(comeco+1,fim):
		if i % 5 == 2 or i % 5 == 3:
			print i
if __name__ == '__main__':
	main()