rep = int(input())

books = []
for i in range(0, rep):
    books.append(str(input()))

books.sort()

count = 0
while len(books) != 0:
    idx = 0
    idx2 = 0
    end = books[0][2]
    for i in range(1, len(books)):
        if books[i][2] < end:
            end = books[i][2]
            idx = i
            continue
        if books[idx][0] == books[i][0]:
            idx = i
    if idx < len(books)
        books = books[idx + 1 : ]
    else:
        books = []
    count += 1
print(count)