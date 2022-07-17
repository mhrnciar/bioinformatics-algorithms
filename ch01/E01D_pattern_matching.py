# Pattern Matching Problem:
# Find all occurrences of a pattern in a string
#   Input: Strings Pattern and Genome
#   Output: All starting positions in Genome where Pattern appears as a substring

from ch01.E01C_reverse_complement import ReverseComplement
from ch01.E01A_pattern_count import PatternCount
from utils import read_txt


# Complexity:
# - If complement = False: (n - k + 1) * k from PatternCount
# - If complement = True: 2 * (n - k + 1) * k from PatternCount + n from ReverseComplement
# O(2 * (n - k + 1)) * O(k) + O(n) ~ O(nk)
def PatternMatch(text, pattern, complement=False):
    cnt, indexes = PatternCount(text, pattern)

    total = cnt
    result = []

    for i in range(len(indexes)):
        if indexes[i] == '^':
            result.append(i)

    if complement:
        _, rev_pattern = ReverseComplement(pattern)
        rev_cnt, rev_indexes = PatternCount(text, rev_pattern)

        total += rev_cnt

        for i in range(len(rev_indexes)):
            if rev_indexes[i] == '^':
                result.append(i)

    return total, result


if __name__ == "__main__":
    # gene = input("Gene: ").upper()
    gene = read_txt("../data/GCF_000006745.1_ASM674v1_genomic_Vibrio_cholerae.fna", 1)
    substr = input("Pattern: ").upper()

    print(PatternMatch(gene, substr, False))
