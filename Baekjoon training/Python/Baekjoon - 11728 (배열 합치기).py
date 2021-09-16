import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
answer_list = a_list + b_list
answer = ' '.join(map(str, sorted(answer_list)))
print(answer)
