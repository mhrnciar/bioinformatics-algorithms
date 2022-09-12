# Reverse Complement Problem:
# Find the reverse complement of a DNA string
#   Input: A DNA string Pattern
#   Output: Pattern, the reverse complement of Pattern

from dictionaries import complement_key, rna_complement_key


# Complexity: O(n)
def ReverseComplement(pattern, rna=False):
    result = ""

    for i in range(len(pattern) - 1, -1, -1):
        if rna:
            result += rna_complement_key.get(pattern[i])
        else:
            result += complement_key.get(pattern[i])

    return pattern, result


if __name__ == "__main__":
    _pattern = input("Pattern: ").upper()

    print(ReverseComplement(_pattern))

