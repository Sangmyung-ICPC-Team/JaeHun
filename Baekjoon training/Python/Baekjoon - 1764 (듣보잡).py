n, m = map(int, input().split())

a_set = set()
for _ in range(n):
    a_set.add(input())

b_set = set()
for _ in range(m):
    b_set.add(input())

result = sorted(list(a_set & b_set))

print(len(result))
for i in range(len(result)):
    print(result[i])
