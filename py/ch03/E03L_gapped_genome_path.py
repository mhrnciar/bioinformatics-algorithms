# String Spelled by a Gapped Genome Path Problem:
# Reconstruct a sequence of (k, d)-mers corresponding to a path in a paired de Bruijn graph.
#   Input: A sequence of (k, d)-mers (a1|b1), . . . , (an|bn) such that SUFFIX((ai|bi)) = PREFIX((ai+1|bi+1))
#   for 1 <= i <= n - 1
#   Output: A string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer of Text is equal to (ai|bi)
#   for 1 <= i <= n (if such a string exists)

from utils import read_lines, create_pair
from ch03.E03J_read_pairs_string_reconstruction import ReconstructStringPairs


def StringSpelledByPatterns(patterns):
    result = patterns[0]

    for i in range(1, len(patterns)):
        result += patterns[i][-1]

    return result


def GappedGenomePath(patterns, k, d):
    pairs = [create_pair(pattern) for pattern in patterns]

    first_patterns = []
    second_patterns = []

    for i in range(len(pairs)):
        first_patterns.append(pairs[i][0])
        second_patterns.append(pairs[i][1])

    prefix_string = StringSpelledByPatterns(first_patterns)
    suffix_string = StringSpelledByPatterns(second_patterns)

    for i in range(k + d + 1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - k - d]:
            return None

    return prefix_string + suffix_string[-(k + d):]


if __name__ == "__main__":
    _k = int(input("k: "))
    _d = int(input("d: "))
    _patterns = read_lines(end_with=' ')

    print(GappedGenomePath(_patterns, _k, _d))
