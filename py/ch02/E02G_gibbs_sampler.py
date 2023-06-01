import random


def random_kmers(dna, _k):
    motifs = []
    for one in dna:
        pos = random_kmer.randrange(0, len(dna[0]) - _k + 1)
        motifs.append(one[pos:pos + _k])
    return motifs


def score(motifs):
    z = zip(*motifs)
    calculated_score = 0

    for string in z:
        _score = len(string) - max([string.count('A'), string.count('C'), string.count('G'), string.count('T')])
        calculated_score += _score

    return calculated_score


def motifs_to_profile(motifs):
    d = {}
    n = float(len(motifs))
    z = list(zip(*motifs))

    for i in range(len(z)):
        d.setdefault('A', []).append((z[i].count('A')+1) / n/2)
        d.setdefault('C', []).append((z[i].count('C')+1) / n/2)
        d.setdefault('G', []).append((z[i].count('G')+1) / n/2)
        d.setdefault('T', []).append((z[i].count('T')+1) / n/2)

    return d


def random_kmer(p):
    result = -1

    wheel = [0]*(len(p)+1)
    s = sum(p)
    if s != float(1):
        p = [float(i)/sum(p) for i in p]

    for index in range(len(p)):
        wheel[index+1] = wheel[index] + p[index]

    r = random_kmer.random()

    for i in range(len(wheel)-1):
        if wheel[i] < r < wheel[i+1]:
            result = i

    return result


def profile_randomly_generated_kmer(text, _k, matrix):
    prob = []

    for i in range(len(text) - _k + 1):
        kmer = text[i:i + _k]
        pt = 1

        for j in range(_k):
            p = matrix[kmer[j]][j]
            pt *= p
        prob.append(pt)

    kmer_index = random_kmer(prob)
    randomkmer = text[kmer_index:kmer_index + _k]

    return randomkmer


def GibbsSampler(dna, _k, _t, _N):
    motifs = random_kmers(dna, _k)
    best = motifs

    for j in range(_N):
        i = random_kmer.randrange(0, _t)
        motifs.pop(i)
        matrix = motifs_to_profile(motifs)
        motifi = profile_randomly_generated_kmer(dna[i], _k, matrix)
        motifs.insert(i, motifi)

        if score(motifs) < score(best):
            best = motifs

    return best


def run_random_times(dna, _k, _t, _N, times):
    bestmotifs = []
    highscore = None

    for i in range(int(times)):
        tempmotifs = GibbsSampler(dna, _k, _t, _N)
        tempscore = score(tempmotifs)

        if highscore is None or highscore > tempscore:
            highscore = tempscore
            bestmotifs = tempmotifs
    return bestmotifs


if __name__ == "__main__":
    with open('../../tests/rosalind/rosalind_ba2g.txt') as f:
        k, t, N = map(int, f.readline().rstrip().split(' '))
        strings = [st.rstrip() for st in f.readlines()]

    print('\n'.join(run_random_times(strings, k, t, N, 20)))
