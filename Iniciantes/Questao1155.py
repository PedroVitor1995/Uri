def main():
	S = 0
	for i in range(101):
		if i > 0:
			S +=  (1 + (1 / float(i)))
	print('%.2f')%S
if __name__ == '__main__':
	main()