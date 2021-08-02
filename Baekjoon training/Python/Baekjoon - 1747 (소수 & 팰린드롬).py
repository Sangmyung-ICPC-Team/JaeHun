import math
import sys
input = sys.stdin.readline

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())

result = 0
for i in range(n, 1000001):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if is_prime(i) == True:
            result = i
            break
if result == 0:
    result = 1003001
print(result)
