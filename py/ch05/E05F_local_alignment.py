# Local Alignment Problem:
# Find the highest-scoring local alignment between two strings.
#   Input: Strings v and w as well as a scoring matrix Score
#   Output: Substrings of v and w whose global alignment score (as defined by Score) is maximized among all
#   substrings of v and w

import numpy as np

from dictionaries import PAM250
from utils import insert_indel


def LocalAlignment(v, w, scoring_matrix, sigma):
    S = np.zeros((len(v)+1, len(w)+1), dtype=int)
    backtrack = np.zeros((len(v)+1, len(w)+1), dtype=int)

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], 0]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    i, j = np.unravel_index(S.argmax(), S.shape)
    max_score = str(S[i][j])
    v_aligned, w_aligned = v[:i], w[:j]

    while backtrack[i][j] != 3 and i*j != 0:
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
    w_aligned = w_aligned[j:]

    return max_score, v_aligned, w_aligned


if __name__ == "__main__":
    _v = input("String 1: ")
    _w = input("String 2: ")

    _result = LocalAlignment(_v, _w, PAM250(), 5)

    print(_result[0])
    print(_result[1])
    print(_result[2])

