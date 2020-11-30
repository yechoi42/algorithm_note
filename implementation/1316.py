rep = int(input())

count = 0
for i in range(0, rep):
    alpha = [0 for i in range (26)]
    word = str(input())
    j = 1
    while j < len(word):
        if word[j] != word[j - 1]:
            if alpha[ord(word[j-1]) - 97] == 1:
                break
            else:
                alpha[ord(word[j-1]) - 97] = 1
        j += 1
    if j == len(word) and alpha[ord(word[j-1]) - 97] == 0:
        count += 1
print(count)