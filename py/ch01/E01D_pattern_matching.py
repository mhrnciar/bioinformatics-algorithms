# Pattern Matching Problem:
# Find all occurrences of a pattern in a string
#   Input: Strings Pattern and Genome
#   Output: All starting positions in Genome where Pattern appears as a substring

from ch01.E01A_pattern_count import PatternCount
from ch01.E01C_reverse_complement import ReverseComplement


# Complexity:
# - If complement = False: (n - k + 1) * k from PatternCount
# - If complement = True: 2 * (n - k + 1) * k from PatternCount + n from ReverseComplement
# O(2 * (n - k + 1)) * O(k) + O(n) ~ O(nk)
def PatternMatch(genome, pattern, complement=False):
    count, indices = PatternCount(genome, pattern)

    total = count
    result = []

    for i in range(len(indices)):
        if indices[i] == '^':
            result.append(i)

    if complement:
        _, rev_pattern = ReverseComplement(pattern)
        rev_cnt, rev_indices = PatternCount(genome, rev_pattern)

        total += rev_cnt

        for i in range(len(rev_indices)):
            if rev_indices[i] == '^':
                result.append(i)

    return total, result


if __name__ == "__main__":
    _genome = input("Genome: ").upper()
    # _genome = read_txt("../data/GCF_000006745.1_ASM674v1_genomic_Vibrio_cholerae.fna", 1)
    _pattern = input("Pattern: ").upper()

    _total, _indices = PatternMatch(_genome, _pattern, False)

    for index in _indices:
        print(index, end=" ")
