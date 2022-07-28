# String Spelled by a Genome Path Problem:
# Reconstruct a string from its genome path
#   Input: A sequence of k-mers Pattern_1, ... , Pattern_n such that the last k - 1 symbols of Pattern_i are equal to
#   the first k - 1 symbols of Pattern_i+1 for 1 <= n - 1
#   Output: A string Text of length k + n - 1 such that the i-th k-mer in Text is equal to Pattern_i (for 1 <= i <= n)

from utils import read_lines


def ReconstructString(substrings):
    result = substrings[0]

    for string in substrings[1:]:
        result += string[-1]

    return result


if __name__ == "__main__":
    _dna = read_lines(end_with=' ')

    print(ReconstructString(_dna))
