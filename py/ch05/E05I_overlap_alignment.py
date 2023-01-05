# Overlap Alignment Problem:
# Construct a highest-scoring overlap alignment between two strings.
#   Input: Two strings and a scoring matrix Score
#   Output: A highest-scoring overlap alignment between the two strings as defined by Score

from utils import insert_indel


def OverlapAlignment(v, w):
    S = [[0 for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    backtrack = [[0 for _ in range(len(w)+1)] for _ in range(len(v)+1)]

    max_score = -3*(len(v) + len(w))

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            scores = [S[i-1][j-1] + [-2, 1][v[i-1] == w[j-1]], S[i-1][j] - 2, S[i][j-1] - 2]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

            if i == len(v) or j == len(w):
                if S[i][j] > max_score:
                    max_score = S[i][j]
                    max_indices = (i, j)

    i, j = max_indices
    v_aligned, w_aligned = v[:i], w[:j]

    while i*j != 0:
        if backtrack[i][j] == 1:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 2:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    v_aligned, w_aligned = v_aligned[i:], w_aligned[j:]

    return str(max_score), v_aligned, w_aligned


if __name__ == "__main__":
    _v = input("String 1: ")
    _w = input("String 2: ")

    _result = OverlapAlignment(_v, _w)

    print(_result[0])
    print(_result[1])
    print(_result[2])

