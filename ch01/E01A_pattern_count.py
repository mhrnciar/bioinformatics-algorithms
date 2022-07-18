# Count the number of occurrences of Pattern in Text
#   Input: A string Text and a string Pattern
#   Output: A number of Pattern occurrences in Text

from numba import jit


@jit(nopython=True)
def Text(text, i, pattern_len):
    return text[i:i+pattern_len]


# Complexity:
# - Cycle: n - k + 1
# - Comparison: k
# O(n - k + 1) * k
@jit(nopython=True)
def PatternCount(text, pattern):
    cnt = 0
    indexes = []

    # Cycle through the string and compare each substring with passed pattern
    for i in range(len(text) - len(pattern)):
        if Text(text, i, len(pattern)) == pattern:
            cnt += 1
            indexes.append("^")
        else:
            indexes.append("-")

    return cnt, indexes


if __name__ == "__main__":
    gene = input("Gene: ").upper()
    substr = input("Pattern: ").upper()

    count, matches = PatternCount(gene, substr)

    print(count)
    print(gene)

    for index in matches:
        print(index, end="")
