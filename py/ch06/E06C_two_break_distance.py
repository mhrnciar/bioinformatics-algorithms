# 2-Break Distance Problem:
# Find the 2-break distance between two genomes.
#   Input: Two genomes with circular chromosomes on the same synteny blocks
#   Output: The 2-break distance between these genomes

from utils import parse_permutation


def TwoBreakDistance(p, q):
    edges = {}

    for block in p + q:
        L = len(block)

        for i in range(len(block)):
            if block[i] in edges:
                edges[block[i]].append(-1 * block[(i+1) % L])
            else:
                edges[block[i]] = [-1 * block[(i+1) % L]]

            if -1 * block[(i+1) % L] in edges:
                edges[-1 * block[(i+1) % L]].append(block[i])
            else:
                edges[-1 * block[(i+1) % L]] = [block[i]]

    cycles = 0

    while len(edges) > 0:
        cycles += 1
        current = list(edges.keys())[0]

        while current in edges:
            temp = edges[current][0]
            if len(edges[current]) == 1:
                del edges[current]
            else:
                edges[current] = edges[current][1:]

            if edges[temp] == [current]:
                del edges[temp]
            else:
                edges[temp].remove(current)

            current = temp

    # Theorem: d(P,Q) = blocks(P,W) - cycles(P,Q)
    return sum([len(block) for block in p]) - cycles


if __name__ == "__main__":
    _p = input("Permutation 1: ")
    _p = parse_permutation(_p)

    _q = input("Permutation 2: ")
    _q = parse_permutation(_q)

    _result = TwoBreakDistance(_p, _q)

    print(_result)
