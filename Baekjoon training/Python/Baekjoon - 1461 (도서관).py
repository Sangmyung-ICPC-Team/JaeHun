n, m = map(int, input().split())
book_dist = list(map(int, input().split()))

positive = []
negative = []
max_dist = 0

for i in book_dist:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)

    if abs(max_dist) < abs(i):
        max_dist = i

positive = sorted(positive, reverse=True)
negative.sort() # 음수는 오름차순으로 해야 result에 들어갈 때 짝이 맞음

result = []
for i in range(0, len(positive), m):
    if positive[i] != max_dist:
        result.append(positive[i])
for i in range(0, len(negative), m):
    if negative[i] != max_dist:
        result.append(negative[i])

result_dist = abs(max_dist)
for i in result:
    result_dist += abs(i * 2)
print(result_dist)
