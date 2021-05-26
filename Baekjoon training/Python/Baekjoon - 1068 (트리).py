import sys
input = sys.stdin.readline

def dfs(node, arr):
    arr[node] = -2 #지울 노드
    for i in range(len(arr)):
        if node == arr[i]: #삭제할 인덱스 (-2가 된) 가 부모인 노드이면
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
parent = int(input())

dfs(parent, arr)
cnt = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr: #삭제된 노드 아니고 부모인 노드가 없을 때 (리프일때)
        cnt += 1
print(cnt)
