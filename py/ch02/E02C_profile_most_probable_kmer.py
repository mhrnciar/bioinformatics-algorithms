# Profile-most Probable k-mer Problem:
# Find a Profile-most probable k-mer in a string
#   Input: A string Text, an integer k, and a 4 x k matrix Profile
#   Output: A Profile-most probable k-mer in Text

import pandas as pd

from utils import text, generate_probs, bases


def MostProbableKmer(genome, k, matrix=None):
    if matrix is None:
        matrix = generate_probs(k)
    else:
        matrix = pd.DataFrame(matrix).T
        matrix.columns = bases

    probs = []
    max_prob = -1
    max_kmer = ""

    for i in range(len(genome) - k):
        substr = text(genome, i, k)
        total = 1

        for j in range(len(substr)):
            total *= matrix.loc[j, substr[j]]

        probs.append(total)

        if total > max_prob:
            max_prob = total
            max_kmer = substr

    return max_kmer


if __name__ == "__main__":
    _genome = input("Genome: ").upper()
    _k = int(input("k: "))

    print(MostProbableKmer(_genome, _k))
