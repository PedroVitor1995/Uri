# -*- coding: utf-8 -*-
def main():
	T = int(input())
	for i in range(T):
		raios = input().split(" ")
		R1 = int(raios[0])
		R2 = int(raios[1])

		menor_raio = R1 + R2

		print(menor_raio)
if __name__ == '__main__':
	main()