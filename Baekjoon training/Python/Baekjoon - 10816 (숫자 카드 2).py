import sys
input = sys.stdin.readline

def binary_search(i, start, end, b):
    while(start < end):
        m = (start + end) // 2
        if b == 0:
            if arr_n[m] < i:
                start = m + 1
            else:
                end = m
        else:
            if arr_n[m] <= i:
                start = m + 1
            else:
                end = m
    return end

if __name__ == "__main__":
    n = int(input())
    arr_n = list(map(int, input().split()))
    arr_n.sort()
    m = int(input())
    arr_m = list(map(int, input().split()))

    result = []
    for i in arr_m:
        start = 0
        end = n
        result.append(binary_search(i, start, end, 1) - binary_search(i, start, end, 0))
    print(*result)
