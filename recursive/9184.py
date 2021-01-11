graph = [[[-1] * 21 for _ in range(21)] for _ in range(21)]

def w(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x > 20 or y > 20 or z > 20:
        return w(20, 20, 20)

    if graph[x][y][z] != -1:
        return graph[x][y][z]
    elif x < y and y < z:
        graph[x][y][z] = w(x, y, z - 1) + w(x, y - 1, z - 1) - w(x, y - 1, z)
    else:
        graph[x][y][z] = w(x - 1, y, z) + w(x - 1, y - 1, z) + w(x - 1, y, z -1) - w(x - 1, y - 1, z - 1)
    return (graph[x][y][z])

a = 1
b = 1
c = 1
while (1):
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) =".format(a, b, c), w(a, b, c))