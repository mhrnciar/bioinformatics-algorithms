# Implementation of a greedy sorting algorithm

from utils import parse_permutation, format_permutation
from operator import neg


def k_index(perm, k):
    return list(map(abs, perm)).index(k)


def k_sort (perm, i, j):
    return perm[:i] + list(map(neg, perm[i:j + 1][::-1])) + perm[j + 1:]


def GreedySorting(p):
    transformations = []

    i = 0
    while i < len(p):
        if p[i] == i+1:
            i += 1
        elif p[i] == -(i+1):
            p = k_sort(p, i, i)
            transformations.append(p)
        else:
            p = k_sort(p, i, k_index(p, i+1))
            transformations.append(p)

    return transformations


if __name__ == "__main__":
    _p = input("Permutation: ")
    _p = parse_permutation(_p)

    _result = GreedySorting(_p)

    for _res in _result:
        print('(' + ' '.join(map(format_permutation, _res)) + ')')
