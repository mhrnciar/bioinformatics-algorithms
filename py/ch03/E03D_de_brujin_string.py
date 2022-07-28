# De Bruijn Graph from a String Problem:
# Construct the de Bruijn graph of a string
#   Input: A string Text and an integer k
#   Output: DEBRUIJN_k(Text)

from utils import text, prefix, suffix


def DeBrujinString(genome, k):
    graph = {}
    kmers = []

    for i in range(len(genome) - k + 1):
        kmers.append(text(genome, i, k))

    for pattern in kmers:
        if prefix(pattern) not in graph:
            graph[prefix(pattern)] = [suffix(pattern)]
        else:
            graph[prefix(pattern)].append(suffix(pattern))

    return graph


if __name__ == "__main__":
    _genome = input("Genome: ")
    _k = int(input("k: "))

    for _key, _word in sorted(DeBrujinString(_genome, _k).items()):
        print(_key + ' -> ' + ', '.join(_word))
