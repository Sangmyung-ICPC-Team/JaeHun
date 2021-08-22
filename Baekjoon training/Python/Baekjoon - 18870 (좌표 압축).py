import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))

dictionary = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dictionary[i], end = ' ')
