T = int(input())
for _ in range(0, T):
    string = input()
    result = 0
    former = 0
    for i in range(len(string)):
        if string[i] == "X":
            former = 0
        else:
            former += 1
            result += former
    print(result)
