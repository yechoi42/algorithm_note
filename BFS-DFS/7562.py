
dx = [-2, -1, 1, 2, -2, -1, 1 ,2]
dy = [-1, -2, -2, -1,1, 2, 2, 1]

def bfs(start, end):
    queue = [start]
    while queue:
        x, y = map(int, queue.pop(0))
        if x == end[0] and y == end[1]:
          return board[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= I or ny >= I:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

T = int(input())
for _ in range(T):
    I = int(input())
    board = [[0] * I for _ in range(I)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if sx == ex and sy == ey:
      print(0)
    else:
      print(bfs((sx, sy), (ex, ey)))
