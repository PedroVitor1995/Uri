# -*- coding: utf-8 -*-
def main():
	N = int(input())
	for i in range(N):
		K = int(input())
		for j in range(K):
			feedback = int(input())
			if(feedback == 1):
				print("Rolien")
			elif(feedback == 2):
				print("Naej")
			elif(feedback == 3):
				print("Elehcim")
			elif(feedback == 4):
				print("Odranoel")
if __name__ == '__main__':
	main()