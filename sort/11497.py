T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    minimum = nums[0] - nums[1]
    for i in range(2, len(nums)):
        temp = nums[i - 2] - nums[i]
        if temp > minimum:
            minimum = temp
    print(minimum)
