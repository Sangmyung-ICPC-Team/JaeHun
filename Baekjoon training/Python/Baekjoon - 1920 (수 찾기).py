import sys
input = sys.stdin.readline

#binary search algorithm (if sorted)
def binary_search(i, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if i == arr_n[m]:
        return 1
    elif i > arr_n[m]:
        return binary_search(i, m+1, end)
    else:
        return binary_search(i, start, m-1)

if __name__ == "__main__":
    n = int(input())
    arr_n = list(map(int, input().split()))
    arr_n.sort()
    m = int(input())
    arr_m = list(map(int, input().split()))

    for i in arr_m:
        start = 0
        end = n - 1
        print(binary_search(i, start, end))
