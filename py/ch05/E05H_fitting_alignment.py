# Fitting Alignment Problem:
# Construct a highest-scoring fitting alignment between two strings.
#   Input: Strings v and w as well as a scoring matrix Score
#   Output: A highest-scoring fitting alignment of v and w as defined by Score

import numpy as np

from utils import insert_indel


def FittingAlignment(v, w):
    S = np.zeros((len(v)+1, len(w)+1), dtype=int)
    backtrack = np.zeros((len(v)+1, len(w)+1), dtype=int)

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            scores = [S[i-1][j] - 1, S[i][j-1] - 1, S[i-1][j-1] + [-1, 1][v[i-1] == w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    j = len(w)
    i = max(enumerate([S[row][j] for row in range(len(w), len(v))]), key=lambda x: x[1])[0] + len(w)
    max_score = str(S[i][j])

    v_aligned, w_aligned = v[:i], w[:j]

    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    v_aligned = v_aligned[i:]

    return max_score, v_aligned, w_aligned


if __name__ == "__main__":
    _v = input("String 1: ")
    _w = input("String 2: ")

    _result = FittingAlignment(_v, _w)

    print(_result[0])
    print(_result[1])
    print(_result[2])

