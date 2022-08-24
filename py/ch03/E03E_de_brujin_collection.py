# De Bruijn Graph from k-mers Problem:
# Construct the de Bruijn graph of a collection of k-mers
#   Input: A collection of k-mers Patterns
#   Output: The de Bruijn graph DEBRUIJ_N(Patterns)

from utils import text, read_lines, prefix, suffix


def DeBrujinCollection(patterns, head=prefix, tail=suffix):
    graph = {}

    for pattern in patterns:
        if head(pattern) not in graph:
            graph[head(pattern)] = [tail(pattern)]
        else:
            graph[head(pattern)].append(tail(pattern))

    return graph


if __name__ == "__main__":
    _patterns = read_lines(end_with=' ')

    for _key, _word in sorted(DeBrujinCollection(_patterns).items()):
        print(_key + ' -> ' + ', '.join(sorted(_word)))
