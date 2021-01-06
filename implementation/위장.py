def solution(clothes):
    clothes = sorted(clothes, key = lambda x : x[1])
    type = []
    newlst = []
    nums = []
    for cloth in clothes:
        if cloth[1] not in type:
            type.append(cloth[1])
            newlst.append([])
        newlst[type.index(cloth[1])].append(cloth[0])
    for lst in newlst:
        nums.append(len(lst))
    answer = 1
    for num in nums:
        answer *= (num + 1)
    return answer -1