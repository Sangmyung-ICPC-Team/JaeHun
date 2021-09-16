import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().strip()))

stack = []
num = k
for i in range(n):
    while num > 0 and stack:
        if stack[len(stack)-1] < arr[i]:
            stack.pop()
            num -= 1
        else:
            break
    stack.append(arr[i])

for i in range(n-k):
    print(stack[i], end="")
