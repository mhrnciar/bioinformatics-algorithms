# Implanted Motif Problem:
# Find all (k, d)-motifs in a collection of strings
#   Input: A collection of strings Dna, and integers k and d
#   Output: All (k, d)-motifs in Dna

from utils import text
from py.ch01.E01N_d_neighborhood import Neighbors


def MotifEnumeration(dna, k, d):
    motifs = []

    for pattern in dna:
        temp = set()

        for i in range(len(pattern) - k + 1):
            neighbors = Neighbors(text(pattern, i, k), d)

            for word in neighbors:
                temp.add(word)

        for motif in temp:
            motifs.append(motif)

    motif_pattern = set()

    for element in motifs:
        if motifs.count(element) == len(dna):
            motif_pattern.add(element)

    return motif_pattern


if __name__ == "__main__":
    _dna = []

    print("DNA strings separated with spaces and k: ")
    while True:
        inp = input("")
        try:
            val = int(inp)
            _k = val
            break
        except ValueError:
            _dna.append(inp)

    _d = int(input("d: "))

    for _word in MotifEnumeration(_dna, _k, _d):
        print(_word)
