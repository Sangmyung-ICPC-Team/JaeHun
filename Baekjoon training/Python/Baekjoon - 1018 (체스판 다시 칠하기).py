import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
result = []
for _ in range(n):
    arr.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        index_1 = 0
        index_2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if(k + l) % 2 == 0:
                    if arr[k][l] != 'B':
                        index_1 += 1
                    if arr[k][l] != 'W':
                        index_2 += 1
                else:
                    if arr[k][l] != 'W':
                        index_1 += 1
                    if arr[k][l] != 'B':
                        index_2 += 1
        result.append(index_1)
        result.append(index_2)
print(min(result))
