from collections import deque

dx = [-2, -1, 1, 2, -2, -1, 1 ,2]
dy = [-1, -2, -2, -1,1, 2, 2, 1]

def bfs(start, end, board):
    queue = deque()
    queue.append((start[0], start[1]))
    board[start[0]][start[1]] = 1
    while queue:
        x, y = queue.popleft()
        if x == end[0] and y == end[1]:
          break;
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= I or ny >= I:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
    return (board[end[0]][end[1]])

K = int(input())
for _ in range(K):
    I = int(input())
    ARRAY = [[0] * I] * I
    X, Y = map(int, input().split())
    X2, Y2 = map(int, input().split())
    if X == X2 and Y == Y2:
      print(0)
    else:
      print(bfs((X, Y), (X2, Y2), ARRAY) - 1)
