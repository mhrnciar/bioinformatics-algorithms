# Hamming Distance Problem:
# Compute the Hamming distance between two strings
#   Input: Two strings of equal length
#   Output: The Hamming distance between these strings

from utils import Text


# Complexity: O(n)
def HammingDistance(str1, str2):
    distance = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1

    return distance


# Complexity:
# - For cycle: n - k
# - Calculating distance: k
# O(n - k) * O(k) = O(nk - k^2) ~ O(nk), because n >> k
def ApproximatePatternCount(text, pattern, threshold):
    count = 0
    indices = []

    for i in range(len(text) - len(pattern)):
        n_pattern = Text(text, i, len(pattern))

        if HammingDistance(pattern, n_pattern) <= threshold:
            count += 1
            indices.append("^")
        else:
            indices.append("-")

    return count, indices


if __name__ == "__main__":
    _genome = input("Genome: ").upper()
    # _genome = read_txt("../data/GCF_000813165.1_ASM81316v1_genomic_Escherichia_coli.fna", 1)

    _pattern = input("Pattern: ").upper()
    _threshold = int(input("Threshold: "))

    _count, _matches = ApproximatePatternCount(_genome, _pattern, _threshold)

    print(_count)
    print(_genome)

    for index in _matches:
        print(index, end="")
