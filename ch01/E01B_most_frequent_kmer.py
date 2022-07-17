# Frequent Words Problem:
# Find the most frequent k-mers in a string
#   Input: A string Text and an integer k
#   Output: All most frequent k-mers in Text

from ch01.E01A_pattern_count import Text, PatternCount


# Complexity:
# - Each iteration of first cycle: (n - k + 1) * k, because of PatternCount
# - First cycle: n - k + 1
# - Second cycle: n - k + 1
# O(n - k + 1) * O(k) * O(n - k + 1) + O(n - k + 1) ~ O(n^2 * k)
def FrequentWords(text, k, limit=None):
    frequent_patterns = set()
    count = [0] * len(text)

    # For every index, get pattern of length k and count how many times the pattern appears in the string
    for i in range(len(text) - k):
        pattern = Text(text, i, k)
        count[i], _ = PatternCount(text, pattern)

    if limit is None:
        # Find the maximum pattern count
        max_count = max(count)

        # Cycle through the list and append to set of frequent patterns the ones whose count equals the maximum count
        for i in range(len(text) - k):
            if count[i] == max_count:
                frequent_patterns.add(Text(text, i, k))

    else:
        # Cycle through the list and append to set of frequent patterns the ones whose count is more than the limit
        for i in range(len(text) - k):
            if count[i] >= limit:
                frequent_patterns.add(Text(text, i, k))

    return frequent_patterns


if __name__ == "__main__":
    gene = input("Gene: ").upper()
    size = int(input("k: "))

    for word in FrequentWords(gene, size):
        print(word)
