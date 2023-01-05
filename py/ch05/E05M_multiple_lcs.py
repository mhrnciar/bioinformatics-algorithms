# Multiple Alignment Problem:
# Find the highest-scoring alignment between multiple strings under a given scoring matrix.
#   Input: A collection of t strings and a t-dimensional matrix Score
#   Output: A multiple alignment of these strings whose score (as defined by the matrix Score) is maximized among all
#   possible alignments of these strings

from utils import insert_indel


def MultipleLCS(v, w, x):
    S = [[[0 for _ in range(len(x) + 1)] for _ in range(len(w) + 1)] for _ in range(len(v) + 1)]
    backtrack = [[[0 for _ in range(len(x) + 1)] for _ in range(len(w) + 1)] for _ in range(len(v) + 1)]

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            for k in range(1, len(x) + 1):
                scores = [S[i-1][j-1][k-1] + int(v[i-1] == w[j-1] == x[k - 1]), S[i - 1][j][k], S[i][j - 1][k], S[i][j][k - 1], S[i - 1][j][k - 1], S[i][j - 1][k - 1]]
                backtrack[i][j][k], S[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

    v_aligned, w_aligned, x_aligned = v, w, x
    i, j, k = len(v), len(w), len(x)
    max_score = S[i][j][k]

    while i*j*k != 0:
        if backtrack[i][j][k] == 1:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
            x_aligned = insert_indel(x_aligned, k)
        elif backtrack[i][j][k] == 2:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
            x_aligned = insert_indel(x_aligned, k)
        elif backtrack[i][j][k] == 3:
            k -= 1
            v_aligned = insert_indel(v_aligned, i)
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j][k] == 4:
            i -= 1
            j -= 1
            x_aligned = insert_indel(x_aligned, k)
        elif backtrack[i][j][k] == 5:
            i -= 1
            k -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1
            k -= 1

    while len(v_aligned) != max(len(v_aligned), len(w_aligned), len(x_aligned)):
        v_aligned = insert_indel(v_aligned, 0)
    while len(w_aligned) != max(len(v_aligned), len(w_aligned), len(x_aligned)):
        w_aligned = insert_indel(w_aligned, 0)
    while len(x_aligned) != max(len(v_aligned), len(w_aligned), len(x_aligned)):
        x_aligned = insert_indel(x_aligned, 0)

    return str(max_score), v_aligned, w_aligned, x_aligned


if __name__ == "__main__":
    _v = input("String 1: ")
    _w = input("String 2: ")
    _x = input("String 3: ")

    _result = MultipleLCS(_v, _w, _x)

    print(_result[0])
    print(_result[1])
    print(_result[2])
    print(_result[3])

