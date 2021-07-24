import sys
input = sys.stdin.readline
arr = [0 for i in range(10001)]
arr[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        arr[j] = 1
t = int(input())
for i in range(t):
    num = int(input())
    for j in range(num // 2, 1, -1):
        if arr[num - j] == 0 and arr[j] == 0:
            print(j, num-j)
            break
