import sys
input = sys.stdin.readline
N = int(input())
nums = []
result = [0 for _ in range(10001)]

for i in range(N):
    num = int(input())
    result[num] += 1
    
for i in range(len(result)):
    for j in range(result[i]):
        print(i)
