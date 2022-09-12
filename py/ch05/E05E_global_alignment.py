# Global Alignment Problem:
# Find a highest-scoring alignment of two strings as defined by a scoring matrix
#   Input: Two strings and a scoring matrix Score
#   Output: An alignment of the strings whose alignment score (as defined by Score) is maximized among all possible
#   alignments of the strings

import numpy as np

from dictionaries import BLOSUM62


def GlobalAlignment(v, w, scoring_matrix, sigma):
    def insert_indel(word, index):
        return word[:index] + '-' + word[index:]

    s = np.zeros((len(v) + 1, len(w) + 1), dtype=int)
    backtrack = np.zeros((len(v) + 1, len(w) + 1), dtype=int)

    for i in range(1, len(v) + 1):
        s[i, 0] = -i * sigma

    for j in range(1, len(w) + 1):
        s[0, j] = -j * sigma

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            scores = [s[i - 1, j] - sigma, s[i, j - 1] - sigma, s[i - 1, j - 1] + scoring_matrix[v[i - 1], w[j - 1]]]
            s[i, j] = max(scores)
            backtrack[i, j] = scores.index(s[i, j])

    v_aligned, w_aligned = v, w
    i, j = len(v), len(w)
    max_score = str(s[i, j])

    while i * j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
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

    _result = GlobalAlignment(_v, _w, BLOSUM62(), 5)

    print(_result[0])
    print(_result[1])
    print(_result[2])

