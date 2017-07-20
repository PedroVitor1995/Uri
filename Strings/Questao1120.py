def funcao(linha):
    if linha[0] in linha[1] :
        r = linha[0]
        l = linha[1].replace(r, '')
        if l == '':
            print 0
        else:
            print int(l)
    
    else:
        print linha[1]

def teste():
    
    
    linha = raw_input()
    linha = linha.split()
    
    if linha[0] != '0' and linha[1] != '0':
        funcao(linha)
        return True
    else:
        return False
    
def main():
    flag = True
    
    while flag:
        flag = input('')

if __name__ == '__main__':
    main()