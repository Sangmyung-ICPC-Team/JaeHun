def hbb():
    max_h = 0
    for i in range(n-2, 0, -1):
        temp = (total[-1] - honey[n-1] - honey[i]) + (total[i] - honey[i])
        max_h = max(max_h, temp)
    return max_h

def bhb():
    max_h = 0
    for i in range(1, n-1):
        temp = (total[i] - honey[0]) + (total[-1] - total[i-1] - honey[-1])
        max_h = max(max_h, temp)
    return max_h

def bbh():
    max_h = 0
    for i in range(1, n-1):
        temp = (total[-1] - honey[0] - honey[i]) + (total[-1] - total[i])
        max_h = max(max_h, temp)
    return max_h

n = int(input())
honey = list(map(int, input().split()))
total = []
total.append(honey[0])
for i in range(1, n):
    total.append(total[i-1] + honey[i])

result = max(hbb(), bhb(), bbh())
print(result)