import fileinput

from utils import text
from py.ch01.E01G_hamming_distance import HammingDistance


def DistanceBetweenPatternsStrings(dna, pattern):
    k = len(pattern)
    distance = 0

    for string in dna:
        h_distance = 10_000_000

        for i in range(len(string) - k):
            n_pattern = text(string, i, k)
            n_distance = HammingDistance(pattern, n_pattern)

            if h_distance > n_distance:
                h_distance = n_distance

        distance += h_distance

    return distance


if __name__ == "__main__":
    _pattern = input("Pattern: ")
    _dna = []

    print("DNA strings separated with spaces: ")
    for line in fileinput.input():
        _dna = line.strip().split(' ')
        break

    print(DistanceBetweenPatternsStrings(_dna, _pattern))
