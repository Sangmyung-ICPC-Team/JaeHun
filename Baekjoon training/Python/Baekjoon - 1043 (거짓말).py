def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x in a:
        parent[y] =x
    elif y in a:
        parent[x] = y
    else:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
a = list(map(int, input().split()))[1:]
    
party = []
num_arr = []
for _ in range(m):
    party = list(map(int, input().split()))
    num = party[1:]
    for i in range(party[0] - 1):
        union(parent, num[i] , num[i+1])
    num_arr.append(num)

result = 0
for i in num_arr:
    for j in range(len(i)):
        if find(parent, i[j]) in a:
            break
    else:
        result += 1
print(result)