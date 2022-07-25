from py.utils import text, score, bases
from py.ch02.E02C_profile_most_probable_kmer import MostProbableKmer


def GreedyMotifSearchWithPseudocounts(dna, k, t):
    best_motifs = [string[:k] for string in dna]

    for kmer in [text(dna[0], i, k) for i in range(len(dna[0]) - k + 1)]:
        motifs = [kmer]

        for i in range(1, t):
            _motifs = motifs[:i]
            matrix = []

            for base in bases:
                mat = []
                total = 0

                for j in range(k):
                    mm = [m[j] for m in _motifs]
                    total += mm.count(base) + 1

                    mat.append(mm.count(base) + 1)

                for j in range(k):
                    mat[j] /= total

                matrix.append(mat)

            motifs.append(MostProbableKmer(dna[i], k, matrix=matrix))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs


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

    _t = int(input("t: "))

    for _word in GreedyMotifSearchWithPseudocounts(_dna, _k, _t):
        print(_word)
