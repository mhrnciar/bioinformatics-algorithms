# Median String Problem:
# Find a median string
#   Input: A collection of strings Dna and an integer k
#   Output: A k-mer Pattern minimizing d(Pattern, Dna) among all k-mers Pattern

from utils import text, generate_patterns, bases
from py.ch01.E01G_hamming_distance import HammingDistance


def MinHammingDistance(genome, pattern, k):
    min_distance = k

    for i in range(len(genome) - k + 1):
        distance = HammingDistance(text(genome, i, k), pattern)
        if distance < min_distance:
            min_distance = distance

    return min_distance


def MedianString(dna, k):
    patterns = generate_patterns(k)
    distance_of_pattern_dna = dict()
    min_string = 10_000_000
    medians = set()

    for pattern in patterns:
        sum_distance = 0

        for string in dna:
            sum_distance += MinHammingDistance(string, pattern, k)

        distance_of_pattern_dna[pattern] = sum_distance

        if sum_distance < min_string:
            min_string = sum_distance

    for i in distance_of_pattern_dna.keys():
        if distance_of_pattern_dna[i] == min_string:
            medians.add(i)

    return medians


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

    for word in MedianString(_dna, _k):
        print(word)
