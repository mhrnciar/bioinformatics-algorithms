# Frequent Words Problem:
# Find the most frequent k-mers in a string
#   Input: A string Text and an integer k
#   Output: All most frequent k-mers in Text

from ch01.E01A_pattern_count import Text, PatternCount


def FrequentWords(text, k):
    frequent_patterns = []
    count = [0] * len(text)

    for i in range(len(text) - k):
        pattern = Text(text, i, k)
        count[i], _ = PatternCount(text, pattern)

    max_count = max(count)

    for i in range(len(text) - k):
        if count[i] == max_count:
            frequent_patterns.append(Text(text, i, k))

    return set(frequent_patterns)


if __name__ == "__main__":
    gene = input("Gene: ").upper()
    size = int(input("k: "))

    for word in FrequentWords(gene, size):
        print(word)
