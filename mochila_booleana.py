def mochila_booleana(n,c,p,v):
    ma = []
    for i in range(n + 1):
        linha = []
        for j in range(c + 1):
            linha.append(0)
        ma.append(linha)
        
    for j in range(1,c + 1):
        for i in range(1,n + 1):
            if p[i] > j:
                ma[i][j] = ma[i-1][j]
            else:
                ma[i][j] = max(ma[i-1][j], ma[i-1][j - p[i]] + v[i])
    return ma[n][c]
7
if __name__ == '__main__':
    n = int(input())
    c = int(input())
    p = [0] * (n + 1)
    v = [0] * (n + 1)
    for d in range(1, n + 1):
        p[d] = int(input())
        v[d] = int(input())
    a = mochila_booleana(n,c,p,v)
    print(a)