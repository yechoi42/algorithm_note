array = [[0]*100 for i in range(100)]
x_max = 0
y_max = 0
answer = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x_max or x2 > x_max:
        x_max = x1 if x1 > x2 else x2
    if y1 > y_max or y2 > y_max:
        y_max = y1 if y1 > y2 else y2 
    for i in range(x1, x2):
        for j in range(y1, y2):
            if array[i][j] == 0:
                array[i][j] = 1
                answer += 1
print(answer)