n = int(input())
arr = list(map(int, input().split()))
for i in sorted(set(arr)):
    print(i, end = ' ')
