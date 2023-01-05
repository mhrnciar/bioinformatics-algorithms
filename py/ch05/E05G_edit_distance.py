# Edit Distance Problem:
# Find the edit distance between two strings.
#   Input: Two strings
#   Output: The edit distance between these strings

import numpy as np


def EditDistance(v, w):
    M = np.zeros((len(v)+1, len(w)+1), dtype=int)
    for i in range(1, len(v)+1):
        M[i][0] = i
    for j in range(1, len(w)+1):
        M[0][j] = j

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            if v[i-1] == w[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j]+1, M[i][j-1]+1, M[i-1][j-1]+1)

    # Print and save the desired edit distance.
    return M[len(v)][len(w)]


if __name__ == "__main__":
    _v = input("String 1: ")
    _w = input("String 2: ")

    _result = EditDistance(_v, _w)

    print(_result)

