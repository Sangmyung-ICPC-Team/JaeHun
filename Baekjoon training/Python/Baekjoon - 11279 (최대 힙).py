import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, (-x, x)) #(-val, val) -> tuple, value가 클수록 -value값이 가장 작게 되서 루트가 됨
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
