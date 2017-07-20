# -*- coding: utf-8 -*-
def main():
	entrada = raw_input().split()
	nota1 = float(entrada[0])
	nota2 = float(entrada[1])
	nota3 = float(entrada[2])
	nota4 = float(entrada[3])
	media1 = 0
	media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1)) / (2.0 + 3.0 + 4.0 + 1.0)
	print('Media: %.1f') % media

	if media >= 7.0:
		print('Aluno aprovado.')
	elif media < 5.0:
		print('Aluno reprovado.')
	elif media >= 5.0 and media < 7.0:
		print('Aluno em exame.')
		exame = float(input())
		print('Nota do exame: %.1f') % exame
		media1 = (exame + media) / 2
		if media1 >= 5.0:
			print('Aluno aprovado.')
			print('Media final: %.1f') % media1
		else:
			print('Aluno reprovado.')
			print('Media final: %.1f') % media1

if __name__ == '__main__':
	main()