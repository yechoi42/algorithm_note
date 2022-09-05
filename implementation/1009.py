T = int(input())

# for _ in range(T):
#     a, b = map(int, input().split())
#     if a % 10 != 0:
#         a = a % 10
#     pattern = []
#     num = 1
#     if b == 1:
#         length = 1
#     for i in range(1, b + 1):
#             num = num * a
#             remainder = num % 10
#             if remainder == 0 and a >= 10:
#                 remainder = 10
#             if remainder not in pattern:
#                 pattern.append(remainder)
#             else :
#                 length = len(pattern)
#                 break
#     print(pattern[b % length - 1])

for _ in range(T):
    a, b = map(int, input().split())
    if a % 10 == 0:
        a = 10
    else: 
        a = a % 10 
    if a in [5, 6, 10]:
        length = 1
    elif a in [4, 9]:
        length = 2
    else:
        length = 4
    num = 1
    pattern = []
    if a == 10:
        pattern = [10]
    else: 
        for i in range(1, length + 1):
            num = num * a
            pattern.append(num % 10)
    print(pattern[b % length -1])