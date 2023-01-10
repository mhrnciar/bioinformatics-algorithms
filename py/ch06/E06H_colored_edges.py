from utils import parse_permutation
from ch06.E06F_chromosome_to_cycle import ChromosomeToCycle


def ColoredEdges(p):
    edges = set()

    for block in p:
        nodes = ChromosomeToCycle(block)
        it = iter(nodes[1:] + [nodes[0]])

        for i in it:
            edges.add((i, next(it)))

    return sorted(edges)


if __name__ == "__main__":
    _p = input("Chromosome: ")
    _p = parse_permutation(_p)

    _result = ColoredEdges(_p)

    print(_result)
