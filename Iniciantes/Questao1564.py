# -*- coding: utf-8 -*-
def main():
	while True:
		try:
			N = int(input())
			if(N > 0):
				print("vai ter duas!")
			else:
				print("vai ter copa!")
		except:
			break;
if __name__ == '__main__':
	main()