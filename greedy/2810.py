num = int(input())
seats = input()

ret = seats.replace("LL", "C")
if seats.find("LL") != -1:
    print(len(ret) + 1)
else:
    print(num)


# import sys

# num = int(input())
# sits = sys.stdin.readline()
# L = 0
# count = 0
# for i in range(0, num):
#     if sits[i] == 'L':
#         L += 1
#     elif sits[i] == 'S':
#         count += 1
# if L == 0:
#     print(count)
# else:
#     print(count + L/2 + 1)

# for i in range(0, num):
#     if sits[i] == 'S':
#         count += 1
#     if sits[i] == 'L':
#         L += 1
# count += L / 2
# if num > 2 and (sits[num - 1] == 'L' or (sits[num - 1] == 'S' and sits[num - 2] == 'L')):
#     count += 1
# if num == 2 and (sits[0] == 'L'):
#     count += 1