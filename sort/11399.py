T = int(input())
times = list(map(int, input().split()))
times.sort()
length = len(times)
sum = 0
for i in range(0, length):
    sum += times[i] * (length - i)
print(sum)