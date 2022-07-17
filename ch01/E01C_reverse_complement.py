# Reverse Complement Problem:
# Find the reverse complement of a DNA string
#   Input: A DNA string Pattern
#   Output: Pattern, the reverse complement of Pattern

# Complexity: O(n)
def ReverseComplement(pattern):
    result = ""
    complement_key = {"C": "G", "G": "C", "A": "T", "T": "A"}

    for i in range(len(pattern) - 1, -1, -1):
        result += complement_key.get(pattern[i])

    return pattern, result


if __name__ == "__main__":
    text = input("Pattern: ").upper()

    print(ReverseComplement(text))

