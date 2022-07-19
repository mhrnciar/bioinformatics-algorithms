from utils import Text
from ch01.E01L_pattern_to_number import PatternToNumber
from ch01.E01M_number_to_pattern import NumberToPattern


def ComputeFrequencies(genome, k):
    freq_arr = [0] * pow(4, k)

    for i in range(len(genome) - k + 1):
        pattern = Text(genome, i, k)
        j = PatternToNumber(pattern)
        freq_arr[j] += 1

    return freq_arr


if __name__ == "__main__":
    _genome = input("Genome: ").upper()
    _k = int(input("k: "))

    arr = ComputeFrequencies(_genome, _k)

    for ind in arr:
        print(ind, end=" ")