from random import randint

from utils import text, read_lines, bases, symbol_key
from ch01.E01G_hamming_distance import HammingDistance
from ch02.E02F_randomized_motif_search import ProfileMostProbableKmer, ProfileWithPseudocounts, Score


def GibbsSampler(dna, k, t, n):
    rand_ints = [randint(0, len(dna[0]) - k) for _ in range(t)]
    motifs = [text(dna[i], r, k) for i, r in enumerate(rand_ints)]

    best_motifs = motifs

    for j in range(1, n):
        i = randint(0, t - 1)

        current_profile = ProfileWithPseudocounts([motif for index, motif in enumerate(motifs) if index != i])
        motifs = [ProfileMostProbableKmer(dna[index], k, current_profile) if index == i else motif for index, motif
                  in enumerate(motifs)]

        current_score = Score(motifs)
        if current_score < Score(best_motifs):
            best_motifs = motifs

        return best_motifs


if __name__ == "__main__":
    _dna, _k = read_lines(end_with='int')
    _t = int(input("t: "))
    _n = int(input("N: "))

    _col = {}

    for _ in range(1000):
        _motifs = GibbsSampler(_dna, _k, _t, _n)

        for _word in _motifs:
            if _word in _col:
                _col[_word] += 1
            else:
                _col[_word] = 1

    _res = sorted(_col.items(), key=lambda x: x[1], reverse=True)[:_t]
    for _word in _res:
        print(_word[0])
