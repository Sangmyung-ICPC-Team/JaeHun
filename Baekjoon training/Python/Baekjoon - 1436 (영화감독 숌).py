import sys
input = sys.stdin.readline

n = int(input())
end = 666
cnt = 0
while True:
    if '666' in str(end):
        cnt += 1
    if n == cnt:
        print(end)
        break
    end += 1
