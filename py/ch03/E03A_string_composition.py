# String Composition Problem:
# Generate the k-mer composition of a string
#   Input: A string Text and an integer k
#   Output: COMPOSITIONk(Text), where the k-mers are arranged in lexicographic order

from utils import text


def StringComposition(genome, k):
    result = []

    for i in range(len(genome) - k + 1):
        result.append(text(genome, i, k))

    return sorted(result)


if __name__ == "__main__":
    _genome = input("Genome: ")
    _k = int(input("k: "))

    for word in StringComposition(_genome, _k):
        print(word)
