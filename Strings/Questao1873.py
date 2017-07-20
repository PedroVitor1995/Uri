# -*- coding: utf-8 -*-
def main():
	teste = int(input())
	for i in range(teste):
		palavras = input().split(' ')
		palavra1 = palavras[0]
		palavra2 = palavras[1]

		if palavra1 == palavra2:
			print('empate')
		elif palavra1 == 'tesoura' and palavra2 == 'papel':
			print('rajesh')
		elif palavra1 == 'papel' and palavra2 == 'pedra':
			print('rajesh')
		elif palavra1 == 'pedra' and palavra2 == 'lagarto':
			print('rajesh')
		elif palavra1 == 'lagarto' and palavra2 == 'spock':
			print('rajesh')
		elif palavra1 == 'spock' and palavra2 == 'tesoura':
			print('rajesh')
		elif palavra1 == 'tesoura' and palavra2 == 'lagarto':
			print('rajesh')
		elif palavra1 == 'lagarto' and palavra2 == 'papel':
			print('rajesh')
		elif palavra1 == 'papel' and palavra2 == 'spock':
			print('rajesh')
		elif palavra1 == 'spock' and palavra2 == 'pedra':
			print('rajesh')
		elif palavra1 == 'pedra' and palavra2 == 'tesoura':
			print('rajesh')
		else:
			print('sheldon')
if __name__ == '__main__':
	main()