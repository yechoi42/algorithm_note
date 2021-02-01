n, s = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

count = 0
def search(prev_sum, start_idx):
    if start_idx >= n:
        return
    if (prev_sum + arr[start_idx]) == s:
        global count
        count += 1
    search(prev_sum, start_idx + 1)
    search(prev_sum + arr[start_idx], start_idx + 1)

search(0, 0)
print(count)