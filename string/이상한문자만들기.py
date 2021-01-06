def solution(s):
    words = s.split(" ")
    answer = ""
    idx = 0
    for word in words:
        for i in range(0, len(word)):
            if i % 2 == 0 and word[i] <= 'z' and word[i] >= 'a':
                answer += word[i].upper()
            elif i % 2 and word[i] <= 'Z' and word[i] >= 'A':
                answer += word[i].lower()
            else:
                answer += word[i]
        if idx != len(words) - 1:
            answer += " "
        idx += 1
    return answer

print(solution("try hello world"))