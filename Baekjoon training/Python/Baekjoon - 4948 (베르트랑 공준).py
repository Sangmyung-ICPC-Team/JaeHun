import sys
input = sys.stdin.readline
n = 123456 * 2 + 1
arr = [True] * n
for i in range(2, int(n ** 0.5)+1):
    if arr[i]:
        for j in range(2*i, n, i):
            arr[j] = False
def prime(num):
    cnt = 0
    for i in range(num + 1, num*2 + 1):
        if arr[i]:
            cnt += 1
    print(cnt)
while True:
    test = int(input())
    if test == 0:
        break
    prime(test)
