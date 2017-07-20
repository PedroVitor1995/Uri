def main():
	while True:
		teste = input('')
		if teste > 1 and teste < 1000:
			break
	for i in range(teste+1):
		if i > 0:
			if i == 1:
				print i,i*i,i*i
			else:
				print i,i*i,i*(i*i)
if __name__ == '__main__':
	main()