# 주어진 수 N이 1이될 때까지
# 1. 1을 빼거나
# 2. K로 나눌 수 있다(N을 K로 나누는 것은 나누어 떨어질 때만 가능)
# N과 K가 주어질 때, 1번 또는 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하라


n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)