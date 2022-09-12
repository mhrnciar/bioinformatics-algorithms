from random import randint

from utils import text, read_lines
from dictionaries import bases, symbol_key
from ch01.E01G_hamming_distance import HammingDistance


def Score(motifs):
    total = 0

    for i in range(len(motifs[0])):
        motif = ''.join([motifs[j][i] for j in range(len(motifs))])
        total += min([HammingDistance(motif, base * len(motif)) for base in bases])

    return total


def Profile(motifs):
    prof = []

    for i in range(len(motifs[0])):
        col = ''.join([motifs[j][i] for j in range(len(motifs))])
        prof.append([float(col.count(nuc)) / float(len(col)) for nuc in 'ACGT'])

    return prof


def ProfileMostProbableKmer(genome, k, prof):
    # Initialize the maximum probability.
    max_prob = [-1, None]

    # Compute the probability of each k-mer, store it if it's currently a maximum.
    for i in range(len(genome) - k + 1):
        current_prob = 1
        for j, nucleotide in enumerate(text(genome, i, k)):
            current_prob *= prof[j][symbol_key[nucleotide]]

        if current_prob > max_prob[0]:
            max_prob = [current_prob, text(genome, i, k)]

    return max_prob[1]


def ProfileWithPseudocounts(motifs):
    prof = []

    for i in range(len(motifs[0])):
        col = ''.join([motifs[j][i] for j in range(len(motifs))])
        prof.append([(col.count(base) + 1) / (len(col) + 4) for base in bases])

    return prof


def MotifsFromProfile(profile, dna, k):
    return [ProfileMostProbableKmer(seq, k, profile) for seq in dna]


def RandomizedMotifSearch(dna, k, t):
    # Randomly generate k-mers from each sequence in the dna list.
    rand_ints = [randint(0, len(dna[0]) - k) for _ in range(t)]
    motifs = [text(dna[i], r, k) for i, r in enumerate(rand_ints)]

    # Initialize the best score as a score higher than the highest possible score.
    best_motifs = motifs

    # Iterate motifs.
    while True:
        current_profile = ProfileWithPseudocounts(motifs)
        motifs = MotifsFromProfile(current_profile, dna, k)
        current_score = Score(motifs)

        if current_score < Score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


if __name__ == "__main__":
    _dna, _k = read_lines(end_with='int')
    _t = int(input("t: "))

    _col = {}

    for _ in range(1000):
        _motifs = RandomizedMotifSearch(_dna, _k, _t)

        for _word in _motifs:
            if _word in _col:
                _col[_word] += 1
            else:
                _col[_word] = 1

    _res = sorted(_col.items(), key=lambda x: x[1], reverse=True)[:_t]
    for _word in _res:
        print(_word[0])
