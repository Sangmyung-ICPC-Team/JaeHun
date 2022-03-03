n = int(input())

dictionary = {}
for _ in range(n):
    book = input()

    if book in dictionary.keys():
        dictionary[book] += 1
    else:
        dictionary[book] = 1    

result = []
for i in dictionary.keys():
    if dictionary[i] == max(dictionary.values()):
        result.append(i)
result.sort()

print(result[0])
