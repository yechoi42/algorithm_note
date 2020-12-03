n = int(input())
check = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
previous = 0
def dfs(X): 
  global previous
  if check[X] != 0:
    return
  check[X] = previous + 1
  print("graph[",X,"]", graph[X])
  print("check[",X,"]", check[X])
  for i in graph[X]: 
    if check[i] == 0:
      previous = check[X]
      dfs(i)

a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
dfs(a)
print(check)
print(check[b] -1)
