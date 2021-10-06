i = 1
while True:
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break

    result = (v // p) * l
    result += min((v % p), l)
    
    print('Case %d: %d'%(i, result))
    i += 1
