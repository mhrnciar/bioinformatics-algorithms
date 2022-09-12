# Manhattan Tourist Problem:
# Find the longest path in a rectangular city
#   Input: A weighted n x m rectangular grid with n + 1 rows and m + 1 columns
#   Output: The longest path from source (0, 0) to sink (n, m) in the grid

import numpy as np


def ManhattanTourist(n, m, down, right):
    s = np.zeros((n + 1, m + 1))

    for i in range(1, n + 1):
        s[i, 0] = s[i-1, 0] + down[i-1][0]

    for i in range(1, m + 1):
        s[0][i] = s[0, i-1] + right[0][i-1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i, j] = max(s[i-1, j] + down[i-1][j], s[i, j-1] + right[i][j-1])

    return int(s[n, m])


if __name__ == "__main__":
    _n = int(input("n: "))
    _m = int(input("m: "))
    _down = []
    _right = []

    for _ in range(_n):
        _down.append([int(x) for x in input().split(' ')])

    for _ in range(_n + 1):
        _right.append([int(x) for x in input().split(' ')])

    print(ManhattanTourist(_n, _m, _down, _right))
