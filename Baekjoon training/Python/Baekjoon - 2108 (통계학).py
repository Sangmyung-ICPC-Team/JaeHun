import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

def mid(arrs):
    arrs.sort()
    result = arrs[n//2]
    return result

sum = 0
for i in range(n):
    sum += arr[i]

print('%.f' %(sum/n))
print(mid(arr))

num = Counter(arr).most_common()
if len(num) > 1 and num[0][1] == num[1][1]:
    print(num[1][0])
else:
    print(num[0][0])

print(max(arr) - min(arr))
