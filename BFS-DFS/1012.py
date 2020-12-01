import sys
sys.setrecursionlimit(100000)

t = int(input())

def dfs(y, x):
    global ARRAY, M, N
    if (y < 0 or x < 0 or x >= M or y >= N):
        return False
    if ARRAY[y][x] == 1:
        ARRAY[y][x] = 0
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)
        return True
    return False

for _ in range(t):
    result = 0
    M, N, K = map(int, input().split())
    ARRAY = [[0] * M for row in range(N)]
    for i in range(K):
         x, y = map(int, input().split())
         ARRAY[y][x] = 1
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result += 1
    print(result)
