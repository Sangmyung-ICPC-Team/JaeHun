import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    deadline, score = map(int, input().split())
    arr.append((deadline, score)) #tuple (d, s)
arr.sort() #deadline sort if same : score sort (asc)

able = []
date = arr[-1][0] # date -> dsc (6 ~> 1)

result = 0
while True:
    if date == 0:
        break
    while arr and arr[-1][0] >= date: #able to do assignment in that date
        able.append(arr.pop()[1])
    date -= 1
    if not able:
        continue
    able.sort()
    result += able.pop()
print(result)
