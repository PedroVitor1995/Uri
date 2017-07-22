# -*- coding: utf-8 -*-
def main():
    quantidade_linhas = int(input())
    numeros = []
    impares = []
    pares = []
    for i in range(quantidade_linhas):
        numero = int(input())
        numeros.append(numero)
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            pares.append(numeros[i])
        else:
            impares.append(numeros[i])
    pares.sort()
    impares.sort(reverse=True)
    for i in range(len(pares)):
        print(pares[i])
    for i in range(len(impares)):
        print(impares[i])
if __name__ == '__main__':
	main()
