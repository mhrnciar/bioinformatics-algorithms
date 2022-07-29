# Contig Generation Problem:
# Generate the contigs from a collection of reads (with imperfect coverage)
#   Input: A collection of k-mers Patterns
#   Output: All contigs in DEBRUIJN(Patterns)

from utils import read_lines
from ch03.E03E_de_brujin_collection import DeBrujinCollection
from ch03.E03M_max_nonbranching_paths import MaxNonbranchingPaths


def GenerateContigs(patterns):
    contigs = []
    graph = DeBrujinCollection(patterns)

    for path in MaxNonbranchingPaths(graph):
        contig = path[0]

        for p in path[1:]:
            contig = contig + p[-1]

        contigs.append(contig)

    return contigs


if __name__ == "__main__":
    _patterns = read_lines(end_with=' ')

    _contigs = GenerateContigs(_patterns)

    for _contig in sorted(_contigs):
        print(_contig, end=' ')
