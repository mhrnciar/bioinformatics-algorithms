# Median String Problem:
# Find a median string
#   Input: A collection of strings Dna and an integer k
#   Output: A k-mer Pattern minimizing d(Pattern, Dna) among all k-mers Pattern

from utils import text, read_lines, generate_patterns, bases
from py.ch01.E01G_hamming_distance import HammingDistance
from py.ch01.E01L_pattern_to_number import PatternToNumber
from py.ch01.E01M_number_to_pattern import NumberToPattern
from py.ch02.E02H_distance_patterns_strings import DistanceBetweenPatternsStrings


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


def MedianStringVar(dna, k):
    distance = 10_000_000
    median = ""

    for i in range(pow(4, k) - 1):
        pattern = NumberToPattern(i, k)
        n_distance = DistanceBetweenPatternsStrings(dna, pattern)

        if distance > n_distance:
            distance = n_distance
            median = pattern

    return median


if __name__ == "__main__":
    _dna, _k = read_lines(end_with='int')

    for word in MedianString(_dna, _k):
        print(word)
