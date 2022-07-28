from utils import text, read_lines, score, bases
from ch02.E02C_profile_most_probable_kmer import MostProbableKmer


def GreedyMotifSearchWithPseudocounts(dna, k, t):
    best_motifs = [string[:k] for string in dna]

    for kmer in [text(dna[0], i, k) for i in range(len(dna[0]) - k + 1)]:
        motifs = [kmer]

        for i in range(1, t):
            _motifs = motifs[:i]
            matrix = []

            for base in bases:
                mat = []

                for j in range(k):
                    mm = [m[j] for m in _motifs]
                    mat.append((mm.count(base) + 1) / (len(mm) + 4))

                matrix.append(mat)

            motifs.append(MostProbableKmer(dna[i], k, matrix=matrix))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs


if __name__ == "__main__":
    _dna, _k = read_lines(end_with='int')
    _t = int(input("t: "))

    for _word in GreedyMotifSearchWithPseudocounts(_dna, _k, _t):
        print(_word)
