string = input()
length = len(string)
count = 0
if string == " ":
    print(0)
else:
    for i in range(length):
        if string[i] == ' ' and i != 0 and i != length - 1:
            count += 1
    if length != 0:
        count += 1
    print(count)