import sys

rep = int(input())
books = []
for i in range(0, rep):
    start, end = map(int, sys.stdin.readline().split())
    books.append((start, end))

books = sorted(books, key=lambda x: (x[1], x[0]))
count = 1
end = books[0][1]
i = 1
while i < len(books):
    if end <= books[i][0]:
        end = books[i][1]
        count+= 1
    i += 1
print(count)