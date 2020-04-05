lista = input()
lista = lista.split()
def Partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            #trocar A[i] por A[j]
            troca = A[i]
            troca2 = A[j]
            A[i] = troca2
            A[j] = troca
    #trocar A[i + 1] por A[r]
    troca3 = A[i + 1]
    troca4 = A[r]
    A[i + 1] = troca4
    A[r] = troca3
    return i + 1
print(Partition(lista,2,3))