INT = int(1e9)

n = int(input())
m = int(input())

# 2차원 배열
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신을 향하는 비용은 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = cost

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] = INF:
            print("X", end=" ")
        else:
            print(graph[a][b], end=" "
    print() 