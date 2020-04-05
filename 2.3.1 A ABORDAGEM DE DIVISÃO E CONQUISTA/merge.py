from math import inf
lista = input()
lista = lista.split()

def Merge(A,p,q,r):
    n1 = q - p + 1 #Calculando o comprimento n1 do subarranjo A[p...q]
    n2 = r - q  # Calculando o comprimento n2 do subarranjo A[q + 1 ... r]
    R = [] #R de 'right'
    L = [] #L de 'left'
    for i in range(n1 + 1): #copia o arranjo A[p...q] em L[0...n1]
        L.append(A[p + i - 1])
    for j in range(n2 + 1): #copia o arranjo A[q + 1 ... r] em R[0 ... n2]
        R.append(A[q + j])
    L[n1] = inf
    L[n2] = inf
    i = 1
    j = 1
    for k in range(p,r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
print(Merge(lista,2,5,7))