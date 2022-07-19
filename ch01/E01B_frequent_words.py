# Frequent Words Problem:
# Find the most frequent k-mers in a string
#   Input: A string Text and an integer k
#   Output: All most frequent k-mers in Text

from utils import Text
from ch01.E01A_pattern_count import PatternCount


# Complexity:
# - Each iteration of first cycle: (n - k + 1) * k, because of PatternCount
# - First cycle: n - k + 1
# - Second cycle: n - k + 1
# O(n - k + 1) * O(k) * O(n - k + 1) + O(n - k + 1) ~ O(n^2 * k)
def FrequentWords(genome, k, limit=None):
    frequent_patterns = set()
    count = [0] * len(genome)

    # For every index, get pattern of length k and count how many times the pattern appears in the string
    for i in range(len(genome) - k):
        pattern = Text(genome, i, k)
        count[i], _ = PatternCount(genome, pattern)

    if limit is None:
        # Find the maximum pattern count
        max_count = max(count)

        # Cycle through the list and append to set of frequent patterns the ones whose count equals the maximum count
        for i in range(len(genome) - k):
            if count[i] == max_count:
                frequent_patterns.add(Text(genome, i, k))

    else:
        # Cycle through the list and append to set of frequent patterns the ones whose count is more than the limit
        for i in range(len(genome) - k):
            if count[i] >= limit:
                frequent_patterns.add(Text(genome, i, k))

    return frequent_patterns


def FastFrequentWords(genome, k):
    freq_patterns = set()
    freq_arr = ComputeFrequencies(genome, k)
    max_count = max(freq_arr)

    for i in range(pow(4, k)):
        if freq_arr[i] == max_count:
            pattern = NumberToPattern(i, k)
            freq_patterns.add(pattern)

    return freq_patterns


def FastFrequentWordsBySorting(genome, k):
    freq_patterns = set()
    index = [0] * (len(genome) - k)
    count = [0] * (len(genome) - k)

    for i in range(len(genome) - k):
        pattern = Text(genome, i, k)
        index[i] = PatternToNumber(pattern)
        count[i] = 1

    index = sorted(index)

    for i in range(1, len(genome) - k):
        if index[i] == index[i-1]:
            count[i] = count[i-1] + 1

    max_count = max(count)

    for i in range(len(genome) - k):
        if count[i] == max_count:
            pattern = NumberToPattern(index[i], k)
            freq_patterns.add(pattern)

    return freq_patterns


if __name__ == "__main__":
    _genome = input("Genome: ").upper()
    _k = int(input("k: "))

    for word in FrequentWords(_genome, _k):
        print(word)
