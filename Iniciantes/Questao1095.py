def main():
	i = 1
	j = 60
	while True:

		if j < 0:
			break
		else:
			print('I=%d J=%d') % (i,j)
		i += 3
		j -= 5
if __name__ == '__main__':
	main()