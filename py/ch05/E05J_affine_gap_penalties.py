# Alignment with Affine Gap Penalties Problem:
# Construct a highest-scoring global alignment of two strings (with affine gap penalties).
#   Input: Two strings, a scoring matrix Score, and numbers sigma and epsilon
#   Output: A highest scoring global alignment between these strings, as defined by Score and by the gap opening
#   and extension penalties sigma and epsilon

import numpy as np

from dictionaries import BLOSUM62
from utils import insert_indel


def GlobalAlignmentAffineGapPenalty(v, w, scoring_matrix, sigma, epsilon):
    S_lower = np.zeros((len(v)+1, len(w)+1), dtype=int)
    S_middle = np.zeros((len(v)+1, len(w)+1), dtype=int)
    S_upper = np.zeros((len(v)+1, len(w)+1), dtype=int)
    backtrack = np.zeros((len(v)+1, len(w)+1), dtype=int)

    for i in range(1, len(v)+1):
        S_lower[i][0] = -sigma - (i-1) * epsilon
        S_middle[i][0] = -sigma - (i-1) * epsilon
        S_upper[i][0] = -10 * sigma

    for j in range(1, len(w)+1):
        S_upper[0][j] = -sigma - (j-1) * epsilon
        S_middle[0][j] = -sigma - (j-1) * epsilon
        S_lower[0][j] = -10 * sigma

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            S_lower[i][j] = max([S_lower[i-1][j] - epsilon, S_middle[i-1][j] - sigma])
            S_upper[i][j] = max([S_upper[i][j-1] - epsilon, S_middle[i][j-1] - sigma])

            middle_scores = [S_lower[i][j], S_middle[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], S_upper[i][j]]
            S_middle[i][j] = max(middle_scores)

            backtrack[i][j] = middle_scores.index(S_middle[i][j]) + 1

    i, j = len(v), len(w)
    max_score = S_middle[i][j]
    v_aligned, w_aligned = v, w

    while i*j != 0:
        if backtrack[i][j] == 1:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 3:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    for _ in range(i):
        w_aligned = insert_indel(w_aligned, 0)
    for _ in range(j):
        v_aligned = insert_indel(v_aligned, 0)

    return max_score, v_aligned, w_aligned


if __name__ == "__main__":
    _v = input("String 1: ")
    _w = input("String 2: ")

    _result = GlobalAlignmentAffineGapPenalty(_v, _w, BLOSUM62(), 11, 1)

    print(_result[0])
    print(_result[1])
    print(_result[2])

