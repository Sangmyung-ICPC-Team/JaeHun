import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    z = 1
    o = 0
    temp = 0
    for _ in range(n):
        temp = o
        o += z
        z = temp
    print(z, o)
