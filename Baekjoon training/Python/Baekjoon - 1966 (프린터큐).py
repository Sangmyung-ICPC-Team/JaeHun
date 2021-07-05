from collections import deque
import sys

num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    cnt = 0
    while queue:
        top = max(queue)
        m -= 1
        pop = queue.popleft()
        if top != pop:
            queue.append(pop)
            if m < 0:
                m = len(queue) - 1
        else:
            cnt += 1
            if m == -1:
                print(cnt)
                break
