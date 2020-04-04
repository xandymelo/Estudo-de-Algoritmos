'''
Reescreva  o  procedimento Insertion-Sort para  ordenar  em  ordem  não  crescente,
  em  vez  da  ordem  não decrescente.
'''

lista = input()
lista = lista.split()
def insertion_sort(l):
    for j in range(1,len(l)):
        chave = l[j]
        i = j - 1
        while i >= 0 and l[i] < chave:
            l[i + 1] = l [i]
            i -= 1
        l[i + 1] = chave
insertion_sort(lista)
print(lista)

#Apenas trocar o sinal de Maior para menor, na condição do while, linha 12#