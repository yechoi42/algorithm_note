# 여행가 A는 N x N의 정사각형 공간 위에 서있다
# 이 공간은 1 x 1의 정사각형으로 나눠져 있다
# 가장 왼쪽 위 좌표는 (1,1)이며 가장 오른쪽 아래 좌표는 (N, N)에 해당
# 여행가는 상하좌우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)
# 계획서엔 하나의 줄에 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀있음
# 정사각형의 공간을 벗어나는 움직임은 무시됨
# 계획서대로 이동했을 때 최종적으로 도착하는 좌표는

n = int(input())
x, y = 1, 1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx >n or ny > n:
        continue
    x, y = nx, ny

print(x, y)