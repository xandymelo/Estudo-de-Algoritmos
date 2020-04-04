lista = input()
lista = lista.split()
def insertion_sort(l):
    for j in range(1,len(l)):
        chave = l[j]
        i = j - 1
        while i >= 0 and l[i] > chave:
            l[i + 1] = l [i]
            i -= 1
        l[i + 1] = chave
insertion_sort(lista)
print(lista)

"""
Essa função pega o segundo elemento, olha se o primeiro é maior que ele, se sim, troca o lugar dos elementos 1
 e 2, agora o subconjunto da lista que possue os elementos l[0] e l[1] estão ordenados, agora ele pega o 
elemento l[2], e vai ordenar o subconjunto da lista q possuem os elementos l[0],l[1] e l[2].
"""
    