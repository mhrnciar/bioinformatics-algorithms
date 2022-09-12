# Frequent Words with Mismatches and Reverse Complements Problem:
# Find the most frequent k-mers (with mismatches and reverse complements) in a string
#   Input: A DNA string Text as well as integers k and d
#   Output: All k-mers Pattern that maximize the sum COUNT_d(Text, Pattern) + COUNT_d(Text, Pattern)
#   over all possible k-mers

from collections import defaultdict

from utils import text
from dictionaries import bases
from ch01.E01C_reverse_complement import ReverseComplement
from ch01.E01G_hamming_distance import HammingDistance


def _neighbour(pattern, mismatch, words):
    if mismatch == 0:
        words.add(pattern)
    else:
        for i in range(len(pattern)):
            for base in bases:
                new_pattern = pattern[:i] + base + pattern[i + 1:]

                if mismatch <= 1:
                    words.add(new_pattern)
                else:
                    _neighbour(new_pattern, mismatch - 1, words)


def MismatchFrequentWordsWithRevComps(genome, k, threshold):
    all_frequent_words = defaultdict(int)

    for i in range(len(genome) - k + 1):
        frequent_words = set()
        _neighbour(text(genome, i, k), threshold, frequent_words)

        for words in frequent_words:
            all_frequent_words[words] += 1

    for t in all_frequent_words.keys():
        _, reverse_k = ReverseComplement(t)

        for i in range(len(genome) - k + 1):
            if HammingDistance(text(genome, i, k), reverse_k) <= threshold:
                all_frequent_words[t] += 1

    result = set()

    for t in all_frequent_words.keys():
        if all_frequent_words[t] == max(all_frequent_words.values()):
            result.add(t)
            result.add(ReverseComplement(t)[1])

    return result


if __name__ == "__main__":
    _genome = input("Genome: ").upper()
    _k = int(input("k: "))
    _threshold = int(input("Threshold: "))

    _patterns = MismatchFrequentWordsWithRevComps(_genome, _k, _threshold)

    for _pattern in _patterns:
        print(_pattern)

