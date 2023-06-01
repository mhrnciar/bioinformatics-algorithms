from random import randint

from utils import text, read_lines
from dictionaries import bases, symbol_key
from ch01.E01G_hamming_distance import HammingDistance

import numpy as np


def create_profile(_motifs):
    motif_len = len(_motifs[0])
    motifs_num = len(_motifs)
    profile = {'A': [1 for _ in range(motif_len)],
               'C': [1 for _ in range(motif_len)],
               'G': [1 for _ in range(motif_len)],
               'T': [1 for _ in range(motif_len)]}

    for i in range(motifs_num):
        for j in range(motif_len):
            profile[_motifs[i][j]][j] += 1

    return profile


def create_motifs(profile, dna):
    return [get_best_match(profile, s) for s in dna]


def get_best_match(profile, string):
    motif_len = len(profile['A'])
    scores = calc_prob_for_all(profile, string)
    start = scores.index(max(scores))

    return string[start:start + motif_len]


def calc_prob_for_all(profile, string):
    return [calc_prob(profile, string, pos) for pos in range(len(string)-len(profile['A']))]


def calc_prob(profile, string, pos):
    result = 1
    for i in range(len(profile['A'])):
        result *= profile[string[pos+i]][i]

    return result


def score(_motifs):
    consensus = get_consensus(_motifs)
    _score = 0
    for motif in _motifs:
        _score += HammingDistance(consensus, motif)

    return _score


def get_consensus(_motifs):
    length = len(_motifs[0])
    profile = {'A': [0 for _ in range(length)],
               'C': [0 for _ in range(length)],
               'G': [0 for _ in range(length)],
               'T': [0 for _ in range(length)]}

    for i in range(len(_motifs)):
        for j in range(length):
            profile[_motifs[i][j]][j] += 1

    consensus = []
    for j in range(length):
        max_elem = max(profile['A'][j],
                       profile['C'][j],
                       profile['G'][j],
                       profile['T'][j])

        if max_elem == profile['A'][j]:
            consensus.append("A")
        elif max_elem == profile['C'][j]:
            consensus.append("C")
        elif max_elem == profile['G'][j]:
            consensus.append("G")
        else:
            consensus.append("T")

    return ''.join(consensus)


def RandomMotifSearch(_dna, _k, _t):
    last_ind = len(_dna[0]) - _k + 1
    idxs = [np.random.randint(0, last_ind) for _ in range(_t)]
    _best_motifs = [s[start:(start + _k)] for s, start in zip(_dna, idxs)]

    while True:
        profile = create_profile(_best_motifs)
        _motifs = create_motifs(profile, _dna)
        if score(_motifs) < score(_best_motifs):
            _best_motifs = _motifs
        else:
            return _best_motifs


if __name__ == '__main__':
    ITER_NUM = 10000
    with open('../../tests/rosalind/rosalind_ba2f.txt', 'r') as file:
        k, t = (int(element) for element in (file.readline().strip()).split())
        strings = [motif.strip() for motif in file]

    best_motifs = RandomMotifSearch(strings, k, t)

    for index in range(ITER_NUM):
        motifs = RandomMotifSearch(strings, k, t)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    for motif in best_motifs:
        print(motif)
