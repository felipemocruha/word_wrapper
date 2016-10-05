#coding: utf-8
import sys

def word_wrap(palavras, l, tam_l, max_linha):
    resto = [[0]* tam_l for i in range(tam_l)]
    for i in range(tam_l):
        resto[i][i] = max_linha - l[i]#
        for j in range(i+1, tam_l):
            resto[i][j] = resto[i][j-1] - l[j] - 1

    m = [0] + [float('inf')]*tam_l
    b = [0]*tam_l
    for j in range(tam_l):
        i = j
        while i >= 0:
            if resto[i][j] < 0:
                custo = float('inf')
            else:
                custo = m[i] + resto[i][j]**2
            if m[j+1] > custo:
                m[j+1] = custo
                b[j] = i
            i -= 1
    
    linhas = []
    j = tam_l
    while j > 0:
        i = b[j-1]
        linhas.append(' '.join(palavras[i:j]))
        j = i
    linhas.reverse()
    return linhas

if __name__ == "__main__":
    #lendo e tratando as palavras
    raw = sys.stdin.readlines()
    raw_str = ''.join(raw)
    L = int(raw_str[0:2])
    raw_str = raw_str[2:]
    palavras = raw_str.split()
    l = [len(i) for i in palavras]
    
    caminho = word_wrap(palavras,l, len(l), L)
    for i in caminho:
        print i
