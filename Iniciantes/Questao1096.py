def main():
	i = 1
	j = 7
	while True:

		if i > 9:
			break
		else:
			print('I=%d J=%d') % (i,j)
			print('I=%d J=%d') % (i,j-1)
			print('I=%d J=%d') % (i,j-2)
		i += 2
if __name__ == '__main__':
	main()