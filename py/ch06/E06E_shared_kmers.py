# Shared k-mers Problem:
# Given two strings, find all their shared k-mers.
#   Input: An integer k and two strings
#   Output: All k-mers shared by these strings, in the form of ordered pairs (x, y) corresponding to starting
#   positions of these k-mers in the respective strings

from ch01.E01C_reverse_complement import ReverseComplement


def create_frequency_table(string, k):
    freqs = {}

    for kmer in [string[i:i+k] for i in range(len(string)-k+1)]:
        if kmer in freqs:
            freqs[kmer] += 1
        else:
            freqs[kmer] = 1

    return freqs


def subs(s, t):
    matches = []
    start = 0

    while start > -1:
        start = s.find(t, start)
        if start > -1:
            start += 1
            matches.append(start)

    return matches


def SharedKmers(s1, s2, k):
    def create_matches():
        freq1 = create_frequency_table(s1, k)
        freq2 = create_frequency_table(s2, k)
        matches = []

        for kmer in freq1:
            if kmer in freq2:
                matches.append((kmer, kmer))

            remk = ReverseComplement(kmer)

            if remk in freq2:
                matches.append((kmer, remk))
        return matches

    index_pairs = []

    for k1, k2 in create_matches():
        for i1 in subs(s1, k1):
            for i2 in subs(s2, k2):
                index_pairs.append((i1-1, i2-1))

    return sorted(index_pairs)


if __name__ == "__main__":
    _k = int(input("k: "))
    _p = input("First DNA: ")
    _q = input("Second DNA: ")

    _result = SharedKmers(_p, _q, _k)

    for _res in sorted(_result):
        print(_res)
