'''
Considere o problema de busca:
Entrada: Uma sequência de n números A = 〈a1, a2, ..., an〉 e um valor v.
Saída: Um índice i tal que v = A[i] ou o valor especial NIL, se v não aparecer em A.
Escreva o pseudocódigo para busca linear, que faça a varredura da sequência, procurando por v.
 Usando um invariante de laço, prove que seu algoritmo é correto. Certifique-se de que seu invariante
 de laço satisfazas três propriedades necessárias.

'''
#Escrevi em python mesmo, porque é muito parecido com um pseudocódigo


lista = input()
lista = lista.split()
elem = int(input())


def busca_linear(l,e):
    for c in range(len(l)):
        if l[c] == e:
            return c
    return NotImplemented
busca_linear(lista,elem)

'''

*NÃO SEI SE ESTA RESPOSTA ESTÁ TOTALMENTE CORRETA*

Inicialização: Antes do primeiro laço, o subarranjo dos elementos invariantes do laço é vazio, logo o subarranjo
 não contém nenhum elemento igual ao elemento e, logo o invariante de laço é verdadeiro antes do primeiro laço.

Manuntenção: Note que se o elemento c está no subconjunto invariante de laço, então l[c] != e, logo 
incrementar c para a próxima iteração do laço for preserva o invariantede laço.

Término: Se o subconjunto da invariante de laço for igual ao conjunto l, então podemos afirmar que o 
elemento e não está no conjunto l, caso contrário, temos que o elemento e está no conjunto. Portanto
 o algoritmo está correto

 '''