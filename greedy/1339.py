n = int(input())
words =[]
alpha = [0 for _ in range(26)]
for _ in range(n):
    words.append(input())

words.sort(key=lambda x:len(x), reverse=True)

dic = dict()
for word in words:
    k = len(word) - 1
    for w in word:
        if w in dic:
            dic[w] += pow(10, k)
        else:
            dic[w] = pow(10, k)
        k -= 1
    
nums = []
for value in dic.values():
    nums.append(value)

nums.sort(reverse=True)

result = 0
k = 9
for i in range(len(nums)):
    result += nums[i] * k
    k -= 1

print(result)