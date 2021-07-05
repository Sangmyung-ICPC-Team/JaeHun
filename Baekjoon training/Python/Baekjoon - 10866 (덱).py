from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dq = deque()

def empty():
    if len(dq) == 0:
        return 1
    else:
        return 0

for i in range(n):
    order = list(input().split())

    if order[0] == 'push_front':
        dq.appendleft(order[1])
    elif order[0] == 'push_back':
        dq.append(order[1])
    elif order[0] == 'pop_front':
        if empty() == 1:
            print('-1')
        else:
            print(dq.popleft())
    elif order[0] == 'pop_back':
        if empty() == 1:
            print('-1')
        else:
            print(dq.pop())
    elif order[0] == 'front':
        if empty() == 1:
            print('-1')
        else:
            print(dq[0])
    elif order[0] == 'back':
        if empty() == 1:
            print('-1')
        else:
            print(dq[len(dq) - 1])
    elif order[0] == 'size':
        print(len(dq))
    elif order[0] == 'empty':
        print(empty())
