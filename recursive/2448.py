N = int(input())

def get_tree(k):
    if k == 0:
        tree = []
        tree.append("  *   ")
        tree.append(" * *  ")
        tree.append("***** ")
        return tree
    ret = get_tree(k - 1)
    height = len(ret)
    for i in range(height):
        ret.append(ret[i] + ret[i])
    for i in range(height):
        ret[i] = " " * (3 * 2 ** (k - 1)) + ret[i] + " " * (3 * 2 ** (k - 1))
    return (ret)

K = 0
N = N / 3
while N > 1:
    N = N // 2
    K += 1

answer = get_tree(K)
for line in answer:
    print(line)