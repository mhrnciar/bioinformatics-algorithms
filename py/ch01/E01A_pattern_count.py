# Count the number of occurrences of Pattern in Text
#   Input: A string Text and a string Pattern
#   Output: A number of Pattern occurrences in Text


from utils import text


# Complexity:
# - Cycle: n - k + 1
# - Comparison: k
# O(n - k + 1) * k
def PatternCount(genome, pattern):
    count = 0
    indices = []

    # Cycle through the string and compare each substring with passed pattern
    for i in range(len(genome) - len(pattern) + 1):
        if text(genome, i, len(pattern)) == pattern:
            count += 1
            indices.append("^")
        else:
            indices.append("-")

    return count, indices


if __name__ == "__main__":
    _genome = input("Genome: ").upper()
    _pattern = input("Pattern: ").upper()

    _count, _indices = PatternCount(_genome, _pattern)

    print(_count)
    print(_genome)

    for index in _indices:
        print(index, end="")
