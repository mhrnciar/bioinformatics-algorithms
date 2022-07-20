from utils import bases
from py.ch01.E01G_hamming_distance import HammingDistance


def ImmediateNeighbors(pattern):
    neighborhood = set()

    for i in range(len(pattern)):
        for base in bases:
            temp = list(pattern)
            temp[i] = base

            neighborhood.add("".join(temp))

    return neighborhood


def Neighbors(pattern, d):
    if d == 0:
        return [pattern]

    if len(pattern) == 1:
        return bases

    neighborhood = set()
    suffix_neighbors = Neighbors(pattern[1:], d)

    for text in suffix_neighbors:
        if HammingDistance(pattern[1:], text) < d:
            for base in bases:
                neighborhood.add(base + text)
        else:
            neighborhood.add(pattern[0] + text)

    return neighborhood


if __name__ == "__main__":
    _pattern = input("Pattern: ").upper()
    _d = int(input("d: "))

    for word in Neighbors(_pattern, _d):
        print(word)
