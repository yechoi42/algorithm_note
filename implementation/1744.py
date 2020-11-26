num = int(input())
nums = []
pnum = []
mnum = []
zero = []
one = []
for _ in range(0,num):
    nums.append(int(input()))

nums.sort()
for i in range(0, len(nums)):
    if nums[i] < 0:
        mnum.append(nums[i])
    elif nums[i] == 0:
        zero.append(nums[i])
    elif nums[i] == 1:
        one.append(nums[i])
    else:
        pnum.append(nums[i])
pnum.sort(reverse=True)

result = 0
i = 0
while i < len(mnum) - 1:
    result += mnum[i] * mnum[i + 1]
    i += 2
if (len(mnum) % 2) and len(zero) == 0:
    result += mnum[len(mnum) - 1]

i = 0
while i < (len(pnum) - 1):
    result += pnum[i] * pnum[i + 1]
    i += 2
if len(pnum) % 2:
    result += pnum[len(pnum) - 1]
result += len(one)
print(result)