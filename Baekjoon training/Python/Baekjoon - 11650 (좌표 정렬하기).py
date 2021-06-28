n = int(input())
c = []

for i in range(n):
    c.append(list(map(int, input().split())))
    
c = sorted(c, key = lambda x: (x[0], x[1]))

for i in c:
    print(*i)
