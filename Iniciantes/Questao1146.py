# -*- coding: utf-8 -*-
def main():
	while True:
		numero = input('')
		if numero == 0:
			break
		else:
			for i in range(numero+1):
				if i > 0:
					print('%d')%(i),
		print('\n')
if __name__ == '__main__':
	main()