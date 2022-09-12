# Longest Common Subsequence Problem:
#   Input: Two strings
#   Output: The longest common subsequence of these strings

import numpy as np


def LCS(v, w):
    s = np.zeros((len(v) + 1, len(w) + 1), dtype=int)

    for i in range(len(v)):
        for j in range(len(w)):
            if v[i] == w[j]:
                s[i + 1, j + 1] = s[i, j] + 1
            else:
                s[i + 1, j + 1] = max(s[i + 1, j], s[i, j + 1])

    lcs = ''
    i, j = len(v), len(w)

    while i*j != 0:
        if s[i, j] == s[i - 1, j]:
            i -= 1
        elif s[i, j] == s[i, j - 1]:
            j -= 1
        else:
            lcs = v[i - 1] + lcs
            i -= 1
            j -= 1

    return lcs


if __name__ == "__main__":
    _str1 = input("String 1: ")
    _str2 = input("String 2: ")

    print(LCS(_str1, _str2))
