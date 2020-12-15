N = int(input())
budgets = list(map(int, input().split(' ')))
M = int(input())

start = 0
end = max(budgets)

previous_mid = 0
while start <= end :
    mid = (start + end) // 2
    sum_total = 0
    for budget in budgets:
        if budget < mid:
            sum_total += budget
        else:
            sum_total += mid
    if sum_total == M:
        previous_mid = mid
        break
    elif sum_total < M:
        start = mid + 1
        previous_mid = mid
    else:
        end = mid - 1

print(previous_mid)
        