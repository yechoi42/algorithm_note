s = input()

dic = []
for i in range(len(s)):
    dic.append(s[i:])

dic.sort()
for word in dic:
    print(word)