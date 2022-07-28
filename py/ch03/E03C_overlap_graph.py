# Overlap Graph Problem:
# Construct the overlap graph of a collection of k-mers
#   Input: A collection Patterns of k-mers
#   Output: The overlap graph OVERLAP(Patterns)

from utils import prefix, suffix, read_lines


class Overlap:
    def __init__(self, pattern, neighbor):
        self.pattern = pattern
        self.neighbor = neighbor

    def __str__(self):
        return self.pattern + ' -> ' + self.neighbor


def OverlapGraph(patterns):
    overlaps = []

    for pattern in patterns:
        for neighbor in [motif for motif in patterns if motif != pattern]:
            if prefix(pattern) == suffix(neighbor):
                overlaps.append(Overlap(neighbor, pattern))

    return overlaps


if __name__ == "__main__":
    _patterns = read_lines(end_with=' ')

    for _word in OverlapGraph(_patterns):
        print(_word)
