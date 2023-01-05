# Middle Edge in Linear Space Problem:
# Find a middle edge in the alignment graph in linear space.
#   Input: Two strings and a scoring matrix Score
#   Output: A middle edge in the alignment graph of these strings (where the edge lengths are defined by Score)

import numpy as np

from dictionaries import BLOSUM62


def MiddleColumnScore(v, w, scoring_matrix, sigma):
    S = [[i*j*sigma for j in range(-1, 1)] for i in range(len(v)+1)]
    S[0][1] = -sigma
    backtrack = [0] * (len(v)+1)

    for j in range(1, len(w)//2+1):
        for i in range(0, len(v)+1):
            if i == 0:
                S[i][1] = -j*sigma
            else:
                scores = [S[i-1][0] + scoring_matrix[v[i-1], w[j-1]], S[i][0] - sigma, S[i-1][1] - sigma]
                S[i][1] = max(scores)
                backtrack[i] = scores.index(S[i][1])

        if j != len(w)/2:
            S = [[row[1]]*2 for row in S]

    return [row[1] for row in S], backtrack


def MiddleEdge(v, w, scoring_matrix, sigma):
    source_to_middle = MiddleColumnScore(v, w, scoring_matrix, sigma)[0]
    middle_to_sink, backtrack = map(lambda l: l[::-1], MiddleColumnScore(v[::-1], w[::-1]+['', '$'][len(w) % 2 == 1 and len(w) > 1], scoring_matrix, sigma))

    scores = list(map(sum, zip(source_to_middle, middle_to_sink)))
    max_middle = max(range(len(scores)), key=lambda i: scores[i])

    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(w)//2 + 1)
    else:
        next_node = [(max_middle + 1, len(w)//2 + 1), (max_middle, len(w)//2 + 1), (max_middle + 1, len(w)//2), ][backtrack[max_middle]]

    return (max_middle, len(w)//2), next_node


if __name__ == "__main__":
    _v = input("String 1: ")
    _w = input("String 2: ")

    _result = MiddleEdge(_v, _w, BLOSUM62(), 5)

    print(_result)

