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
    cnt = 0
    indexes = []

    for i in range(len(text) - len(pattern)):
        n_pattern = Text(text, i, len(pattern))
        if HammingDistance(pattern, n_pattern) <= threshold:
            cnt += 1
            indexes.append("^")
        else:
            indexes.append("-")

    return cnt, indexes


if __name__ == "__main__":
    gene = input("Gene: ").upper()
    # gene = read_txt("../data/GCF_000813165.1_ASM81316v1_genomic_Escherichia_coli.fna", 1)

    substr = input("Pattern: ").upper()
    d = int(input("Threshold: "))

    count, matches = ApproximatePatternCount(gene, substr, d)

    print(count)
    print(gene)

    for index in matches:
        print(index, end="")
