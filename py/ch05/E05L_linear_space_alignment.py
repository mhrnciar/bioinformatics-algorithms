# Space efficient global alignment

import numpy as np

from ch05.E05E_global_alignment import GlobalAlignment
from ch05.E05K_middle_edge_linear_space import MiddleEdge
from dictionaries import BLOSUM62


def SpaceEfficientGlobalAlignment(v, w, scoring_matrix, sigma):
    def LinearSpaceAlignment(top, bottom, left, right):
        if left == right:
            return [v[top:bottom], '-'*(bottom - top)]

        elif top == bottom:
            return ['-'*(right - left), w[left:right]]

        elif bottom - top == 1 or right - left == 1:
            return GlobalAlignment(v[top:bottom], w[left:right], scoring_matrix, sigma)[1:]

        else:
            mid_node, next_node = MiddleEdge(v[top:bottom], w[left:right], scoring_matrix, sigma)

            mid_node = tuple(map(sum, zip(mid_node, [top, left])))
            next_node = tuple(map(sum, zip(next_node, [top, left])))

            current = [['-', v[mid_node[0] % len(v)]][next_node[0] - mid_node[0]], ['-', w[mid_node[1] % len(w)]][next_node[1] - mid_node[1]]]

            A = LinearSpaceAlignment(top, mid_node[0], left, mid_node[1])
            B = LinearSpaceAlignment(next_node[0], bottom, next_node[1], right)
            return [A[i] + current[i] + B[i] for i in range(2)]

    v_aligned, w_aligned = LinearSpaceAlignment(0, len(v), 0, len(w))
    score = sum([-sigma if '-' in pair else scoring_matrix[pair] for pair in zip(v_aligned, w_aligned)])

    return str(score), v_aligned, w_aligned


if __name__ == "__main__":
    _v = input("String 1: ")
    _w = input("String 2: ")

    _result = SpaceEfficientGlobalAlignment(_v, _w, BLOSUM62(), 5)

    print(_result[0])
    print(_result[1])
    print(_result[2])

