def main():
	n = int(input())
	for i in range(1,n+1):
		primeiro1 = i ** 1
		primeiro2 = i ** 2
		primeiro3 = i ** 3
		segundo1 = i
		segundo2 = (i ** 2) + 1
		segundo3 = (i ** 3) + 1
		print('{} {} {}'.format(primeiro1,primeiro2,primeiro3))
		print('{} {} {}'.format(segundo1,segundo2,segundo3))
if __name__ == '__main__':
	main()