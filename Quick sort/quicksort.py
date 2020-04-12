#rever o video de quicksort e escrever o algoritmo de outro algoritmo de ordenação

l = input()
l  = l.split()


def quicksort(lista, inicio = 0, fim = None):#quisort(lista, inicio, fim)#
    if fim is None:
        fim = len(lista) - 1                  #0 colocar o fim - 1 para já usar essa variavel como pivot
    if inicio < fim:                          #1  if inicio < fim 
        p = partition(lista, inicio, fim)       #2 p = parition(lista, inicio, fim)
        quicksort(lista, inicio, p - 1)         #3 quicksort(lista, inicio, p - 1)
        quicksort(lista, p + 1, fim)            #4 quicksort(lista, p + 1, fim)



def partition(lista, inicio, fim):                      #partition(lista, inicio, fim)
    pivot = lista[fim]                                      #1 pivot = lista[fim]
    i = inicio                                              #2 i = inicio
    for j in range(inicio, fim):                            #3 for j = inicio to fim:
        if lista[j] <= pivot:                                   #4  if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]                 #5 trocar lista[i] com lista[j]
            i += 1                                                  #6 i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]             #7 trocar lista[i] com lista[fim]
    return i                                                #8 retornar i
quicksort(l)
print(l)