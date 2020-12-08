N = int(input())
words_list = []
for _ in range(N):
  words_list.append(input())
words = set(words_list)
words_list = list(words)
words_list.sort()
words_list.sort(key=lambda x:len(x))
for word in words_list:
  print(word)