import sys
input = sys.stdin.readline
n = int(input())
arr = map(int, input().split())
height_sum = 0
two_sum = 0
for i in arr:
    height_sum += i
    two_sum += i // 2  # 2 up 물뿌리개 횟수
if height_sum % 3 == 0:
    if two_sum >= (height_sum // 3):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
