def ehpar(pares):
    for i in range(5):
        print("par[%d] = %d" %(i,pares[i]))

def ehimpar(impares):
    for j in range(5):
        print("impar[%d] = %d" %(j,impares[j]))
def main():
    par = []
    impar = []

    for i in range(15):
        numero = input('Digite um numero: ')
        if numero % 2 == 0:
            par.append(numero)
            if len(par) >= 5:
                ehpar(par)
                par = []
        else:
            impar.append(numero)
            if len(impar) >= 5:
                ehimpar(impar)
                impar = []
    for i in range(len(impar)):
        print("impar[%d] = %d" %(i,impar[i]))
    for j in range(len(par)):
        print("par[%d] = %d" %(j,par[j]))
if __name__ == '__main__':
    main()