def solution(n, words):
    said = [words[0]]
    answer = []
    for i in range(1, len(words)):
        if words[i] in said or words[i][0] != words[i - 1][len(words[i-1]) - 1]:
            return [i % n + 1, i // n + 1]
        said.append(words[i])
    return [0, 0]