# Frequent Words with Mismatches Problem:
# Find the most frequent k-mers with mismatches in a string
#   Input: A string Text as well as integers k and d
#   Output: All most frequent k-mers with up to d mismatches in Text


from utils import Text
from ch01.E01G_hamming_distance import HammingDistance
from collections import defaultdict


def _neighbour(pattern, mismatch, words):
    if mismatch == 0:
        words.add(pattern)
    else:
        bases = ['A', 'T', 'C', 'G']

        for i in range(len(pattern)):
            for base in bases:
                new_pattern = pattern[:i] + base + pattern[i + 1:]

                if mismatch <= 1:
                    words.add(new_pattern)
                else:
                    _neighbour(new_pattern, mismatch - 1, words)


def MismatchFrequentWords(text, k, threshold):
    all_freq_words = defaultdict(int)
    result = set()

    for i in range(len(text) - k + 1):
        freq_words = set()

        _neighbour(Text(text, i, k), threshold, freq_words)

        for words in freq_words:
            all_freq_words[words] += 1

    max_count = max(all_freq_words.values())

    for i in all_freq_words.keys():
        if all_freq_words[i] == max_count:
            result.add(i)

    return result


if __name__ == "__main__":
    gene = input("Gene: ").upper()
    size = int(input("k: "))
    d = int(input("Threshold: "))

    for word in MismatchFrequentWords(gene, size, d):
        print(word)
