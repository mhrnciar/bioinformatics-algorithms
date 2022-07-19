# Approximate Pattern Matching Problem:
# Find all approximate occurrences of a pattern in a string
#   Input: Strings Pattern and Text along with an integer d
#   Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches

from ch01.E01C_reverse_complement import ReverseComplement
from ch01.E01G_hamming_distance import ApproximatePatternCount
from utils import read_txt


# Complexity:
# - If complement = False: nk from ApproximatePatternCount
# - If complement = True: 2 * nk from ApproximatePatternCount + n from ReverseComplement
# O(2 * nk) + O(n) ~ O(nk)
def ApproximatePatternMatch(text, pattern, threshold, complement=False):
    cnt, indexes = ApproximatePatternCount(text, pattern, threshold)

    total = cnt
    result = []

    for i in range(len(indexes)):
        if indexes[i] == '^':
            result.append(i)

    if complement:
        _, rev_pattern = ReverseComplement(pattern)
        rev_cnt, rev_indexes = ApproximatePatternCount(text, rev_pattern, threshold)

        total += rev_cnt

        for i in range(len(rev_indexes)):
            if rev_indexes[i] == '^':
                result.append(i)

    return total, result


if __name__ == "__main__":
    gene = input("Gene: ").upper()
    # gene = read_txt("../data/GCF_000006745.1_ASM674v1_genomic_Vibrio_cholerae.fna", 1)
    substr = input("Pattern: ").upper()
    d = int(input("Threshold: "))

    tot, ind = ApproximatePatternMatch(gene, substr, d, False)

    for item in ind:
        print(item, end=" ")
