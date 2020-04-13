

def mergesort(lista, inicio = 0, fim = None):       #mergesort(lista, inicio, fim)
    if fim is None:                                     
        fim = len(lista)
    if (fim - inicio > 1):                              #1 if fim - inicio > 1
        meio = (fim + inicio) // 2                          #2 meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio)                      #3 mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)                         #4 mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)                     #5 merge(lista, inicio, meio, fim)



def merge(lista, inicio, meio, fim):               #merge(lisa, inicio, meio, fim)
    left = lista[inicio:meio]                           #1 dividir a lista em dois subarranjos, lista[0,1, ..., meio -1]
    right = lista[meio:fim]                             # e lista[meio, ..., fim]   
    top_left = 0                                        #2 top_left = 0 (COMO SE OS SUBARRANJOS FOSSEM BARALHOS
    top_right = 0                                       # E O TOPO DO BARALHO FOSSE O PRIMEIRO ELEMENTO)
    for k in range(inicio, fim):                        #3 top_right = 0
        if top_left >= len(left):                       #4 for k=inicio to fim
            lista[k] = right[top_right]                     #a partir daqui o algoritmo é igual ao código
            top_right += 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_right]
            top_left += 1
        else:
            lista[k] = right[top_right]
            top_right += 1


n = input()
n = n.split()
mergesort(n)
print(n)