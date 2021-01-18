n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())

graph = [[0] * (m - 7) for _ in range(n - 7)]

answer = 2147483647
for i in range(n - 7):
    for j in range(m - 7):
        count1 = 0
        count2 = 0
        for y in range(8):
            for x in range(8):
                hap = i + y + j + x
                if hap % 2 == 1 and board[i + y][j + x] == 'B':
                    count1 += 1
                elif hap % 2 == 0 and board[i + y][j + x] == 'W':
                    count1 += 1
                if hap % 2 == 1 and board[i + y][j + x] == 'W':
                    count2 += 1
                elif hap % 2 == 0 and board[i + y][j + x] == 'B':
                    count2 += 1
        graph[i][j] = min(count1, count2)
    answer = min(min(graph[i]), answer)

print(answer)