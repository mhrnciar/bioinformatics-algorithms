import ast

from utils import parse_permutation, format_permutation
from ch06.E06G_cycle_to_chromosome import CycleToChromosome


def GraphToGenome(graph):
    def diff(a, b):
        _, x = a
        y, _ = b

        return abs(x - y)

    def build_cycle(pair, dcycles):
        result = [pair]

        while pair in dcycles:
            pair = dcycles[pair]
            result.append(pair)

        return result

    def black_edges(cycle):
        result = []

        for i in range(len(cycle)):
            a, _ = cycle[i]
            _, b = cycle[i - 1]
            result.append((b, a))

        return result

    extract = [(a, b, diff(a, b)) for (a, b) in zip([graph[-1]] + graph[0:], graph)]
    gaps = [(a, b) for (a, b, diff) in extract if diff > 1]
    cycles = [(a, b) for (a, b, diff) in extract if diff == 1]

    dcycles = {}
    for (a, b) in cycles:
        dcycles[a] = b

    P = [build_cycle(pair, dcycles) for _, pair in gaps]
    Q = [black_edges(p) for p in P]

    next_node = 1
    R = []

    for q in Q:
        r = []

        for a, b in q:
            r.append(next_node if a < b else -next_node)
            next_node += 1

        R.append(r)

    return R


if __name__ == "__main__":
    _graph = input("Graph: ")
    _graph = list(ast.literal_eval(_graph))

    _result = GraphToGenome(_graph)

    for _res in _result:
        print('(' + ' '.join(map(format_permutation, _res)) + ')', end='')
