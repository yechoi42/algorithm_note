# 시간복잡도 문제로 c++로 풂
n = int(input())

def possible(board, y):
    for i in range(y):
        if board[i] == board[y] or abs(board[y] - board[i]) == y - i:
            return False
    return True

def set_queen(board, row):
    if row == n:
        global result
        result += 1
        return
    for i in range(n):
        board[row] = i
        if possible(board, row) == True:
            set_queen(board, row + 1)

result = 0        
board = [0] * n 
set_queen(board, 0)
print(result)