def solution(word):
    result = [0, 0, 0]
    i = 0
    j = -1
    while i < len(word):
        if word[i].isdigit() == True:
            j += 1
            result[j] = int(word[i])
            if i < len(word) - 1 and word[i + 1].isdigit()==True:
                i += 1
                result[j] = 10
        elif word[i] == '*':
            result[j] *= 2
            if j > 0:
                result[j - 1] *= 2
        elif word[i] == '#':
            result[j] *= -1
        elif word[i] == 'D':
            result[j] *= result[j]
        elif word[i] == 'T':
            result[j] *= result[j] * result[j]
        i += 1
    # print(result)
    answer = result[0] + result[1] + result[2]
    return answer
            