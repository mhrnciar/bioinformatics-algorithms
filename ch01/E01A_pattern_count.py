# Count the number of occurrences of Pattern in Text
#   Input: A string Text and a string Pattern
#   Output: A number of Pattern occurrences in Text

def Text(text, i, pattern_len):
    return text[i:(i+pattern_len)]


def PatternCount(text, pattern):
    cnt = 0
    indexes = []
    for i in range(len(text) - len(pattern)):
        if Text(text, i, len(pattern)) == pattern:
            cnt += 1
            indexes.append(True)
        else:
            indexes.append(False)

    return cnt, indexes


if __name__ == "__main__":
    gene = input("Gene: ").upper()
    substr = input("Pattern: ").upper()

    count, matches = PatternCount(gene, substr)

    print(count)
    print(gene)

    for index in matches:
        print("^" if index else "-", end="")
