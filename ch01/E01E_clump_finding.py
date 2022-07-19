# Clump Finding Problem:
# Find patterns forming clumps in a string
#   Input: A string Genome, and integers k, L, and t
#   Output: All distinct k-mers forming (L, t)-clumps in Genome

from utils import Text
from ch01.E01K_frequency_array import ComputeFrequencies
from ch01.E01L_pattern_to_number import PatternToNumber
from ch01.E01M_number_to_pattern import NumberToPattern


# Complexity:
# - Inner cycle: (i + l - k) - i = l - k
# k is small number which can be ignored in generalisation
# - Outer cycle: n - l + 1
# O(n - l + 1) * O(l - k) ~ O(n * l)
def FindClumps(genome, k, window_len, threshold):
    res = set()

    for i in range(len(genome) - window_len + 1):
        for j in range(i, i + window_len - k):
            pattern = Text(genome, j, k)

            if Text(genome, i, window_len).count(pattern) == threshold:
                res.add(pattern)

    return res


# Algorithm using frequency array
def FindClumpsWithFrequencies(genome, k, window_len, threshold):
    freq_patterns = set()
    clumps = [0] * pow(4, k)

    for i in range(len(genome) - window_len):
        substr = Text(genome, i, window_len)
        freq_arr = ComputeFrequencies(substr, k)

        for j in range(pow(4, k)):
            if freq_arr[j] >= threshold:
                clumps[j] = 1

    for i in range(pow(4, k)):
        if clumps[i] == 1:
            pattern = NumberToPattern(i, k)
            freq_patterns.add(pattern)

    return freq_patterns


def FastFindClumps(genome, k, window_len, threshold):
    freq_patterns = set()
    clumps = [0] * pow(4, k)

    substr = Text(genome, 0, window_len)
    freq_arr = ComputeFrequencies(substr, k)

    for i in range(pow(4, k)):
        if freq_arr[i] >= threshold:
            clumps[i] = 1

    # Frequency array is generated only once and with moving window, we only recalculate the first and the last
    # patterns, which are the only ones that change
    for i in range(1, len(genome) - window_len):
        first_pattern = Text(genome, i - 1, k)
        index = PatternToNumber(first_pattern)
        freq_arr[index] -= 1

        last_pattern = Text(genome, i + window_len - k, k)
        index = PatternToNumber(last_pattern)
        freq_arr[index] += 1

        if freq_arr[index] >= threshold:
            clumps[index] = 1

    for i in range(pow(4, k)):
        if clumps[i] == 1:
            pattern = NumberToPattern(i, k)
            freq_patterns.add(pattern)

    return freq_patterns


if __name__ == "__main__":
    _genome = input("Genome: ").upper()
    _k = int(input("k: "))
    _window_len = int(input("L: "))
    _threshold = int(input("t: "))

    for word in FastFindClumps(_genome, _k, _window_len, _threshold):
        print(word)
