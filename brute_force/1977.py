M = int(input())
N = int(input())
min_num = 0
whole_sum = 0
for i in range(1, 101):
    i_square = i * i
    if M <= i_square <= N:
        if min_num == 0:
            min_num = i_square
        whole_sum = whole_sum + i_square
    elif i_square > N:
        break
if whole_sum == 0:
    print(-1)
else:
    print(whole_sum)
    print(min_num)