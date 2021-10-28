import sys
input = sys.stdin.readline

n = int(input())
dictionary = {} #key:번호 #value:개수

for i in range(n):
    card = int(input())
    if card in dictionary:
        dictionary[card] += 1
    else:
        dictionary[card] = 1

result = sorted(dictionary.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])
