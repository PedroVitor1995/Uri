# -*- coding: utf-8 -*-
def main():
	S = 0
	aux = 1
	temp = 1
	while(aux <= 39):
		c = aux / temp
		S += c;
		aux += 2
		temp *= 2
	print("%.2f"%S)
if __name__ == '__main__':
	main()