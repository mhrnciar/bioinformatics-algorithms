# Frequent Words with Mismatches Problem:
# Find the most frequent k-mers with mismatches in a string
#   Input: A string Text as well as integers k and d
#   Output: All most frequent k-mers with up to d mismatches in Text

from collections import defaultdict
from utils import Text, bases
from ch01.E01G_hamming_distance import HammingDistance, ApproximatePatternCount
from ch01.E01L_pattern_to_number import PatternToNumber
from ch01.E01M_number_to_pattern import NumberToPattern
from ch01.E01N_d_neighborhood import Neighbors


def MismatchFrequentWords(genome, k, threshold):
    freq_patterns = set()
    freq_arr = [0] * pow(4, k)
    close = [0] * pow(4, k)

    for i in range(len(genome) - k):
        neighborhood = Neighbors(Text(genome, i, k), threshold)

        for pattern in neighborhood:
            index = PatternToNumber(pattern)
            close[index] = 1

    for i in range(pow(4, k)):
        if close[i] == 1:
            pattern = NumberToPattern(i, k)
            freq_arr[i], _ = ApproximatePatternCount(genome, pattern, threshold)

    max_count = max(freq_arr)

    for i in range(pow(4, k)):
        if freq_arr[i] == max_count:
            pattern = NumberToPattern(i, k)
            freq_patterns.add(pattern)

    return freq_patterns


def MismatchFrequentWordsBySorting(genome, k, threshold):
    freq_patterns = set()
    temp_neighborhoods = list()

    for i in range(len(genome) - k):
        temp_neighborhoods.append(Neighbors(Text(genome, i, k), threshold))

    neighborhoods = [x for xs in temp_neighborhoods for x in xs]
    index = [0] * len(temp_neighborhoods)
    count = [0] * len(temp_neighborhoods)

    for i in range(len(temp_neighborhoods)):
        pattern = neighborhoods[i]
        index[i] = PatternToNumber(pattern)
        count[i] = 1

    index = sorted(index)

    for i in range(len(temp_neighborhoods) - 1):
        if index[i] == index[i+1]:
            count[i+1] = count[i] + 1

    max_count = max(count)

    for i in range(len(temp_neighborhoods)):
        if count[i] == max_count:
            pattern = NumberToPattern(index[i], k)
            freq_patterns.add(pattern)

    return freq_patterns


if __name__ == "__main__":
    _genome = input("Genome: ").upper()
    _k = int(input("k: "))
    _threshold = int(input("Threshold: "))

    for word in MismatchFrequentWordsBySorting(_genome, _k, _threshold):
        print(word)
