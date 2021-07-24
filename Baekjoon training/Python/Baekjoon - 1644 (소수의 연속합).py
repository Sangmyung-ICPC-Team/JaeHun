import sys
input = sys.stdin.readline
n = int(input())

primes = []
def prime(n):
    a = [False, False] + [True] * (n-1)
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n+1, i):
                a[j] = False
prime(n)

result, start, end = 0, 0, 0
while end <= len(primes):
    temp = sum(primes[start:end])
    if temp == n:
        result += 1
        end += 1
    elif temp < n:
        end += 1
    else:
        start += 1      
print(result)
