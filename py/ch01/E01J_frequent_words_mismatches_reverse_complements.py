# Frequent Words with Mismatches and Reverse Complements Problem:
# Find the most frequent k-mers (with mismatches and reverse complements) in a string
#   Input: A DNA string Text as well as integers k and d
#   Output: All k-mers Pattern that maximize the sum COUNT_d(Text, Pattern) + COUNT_d(Text, Pattern)
#   over all possible k-mers

from collections import defaultdict
from utils import Text
from py.ch01.E01C_reverse_complement import ReverseComplement
from py.ch01.E01G_hamming_distance import HammingDistance
from py.ch01.E01I_frequent_words_with_mismatches import _neighbour


def MismatchFrequentPatterns(text, k, threshold):
    all_frequent_words = defaultdict(int)

    for i in range(len(text) - k + 1):
        frequent_words = set()
        _neighbour(Text(text, i, k), threshold, frequent_words)

        for words in frequent_words:
            all_frequent_words[words] += 1

    for t in all_frequent_words.keys():
        _, reverse_k = ReverseComplement(t)

        for i in range(len(text) - k + 1):
            if HammingDistance(Text(text, i, k), reverse_k) <= threshold:
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

    _patterns = MismatchFrequentPatterns(_genome, _k, _threshold)

    for pattern in _patterns:
        print(pattern)

