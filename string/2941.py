alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
string = input()
length = len(string)
while string:
    flag = [0,0,0,0,0,0,0,0]
    for i in range(0, 8):
        index = string.find(alphabets[i])
        if index != -1:
            flag[i] = 1
            alpha_len = len(alphabets[i])
            length -= alpha_len - 1
            string = string[: index] + ' ' + string[index + alpha_len:]
            break
    if flag == [0,0,0,0,0,0,0,0]:
        break
print(length)
