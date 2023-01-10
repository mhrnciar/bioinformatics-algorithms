import ast

from utils import parse_permutation, format_permutation
from ch06.E06F_chromosome_to_cycle import ChromosomeToCycle
from ch06.E06G_cycle_to_chromosome import CycleToChromosome
from ch06.E06J_two_break_genome_graph import TwoBreakOnGenomeGraph


def edges(it):
    return [(i, next(it)) for i in it]


def black_edges(Nodes):
    return edges(iter(Nodes))


def colored_edges(Nodes):
    return edges(iter(Nodes[1:] + [Nodes[0]]))


def graph_genome_all(graph):
    def build_index():
        def insert(first, second):
            if first not in index:
                index[first] = []
            index[first].append(second)

        index = {}

        for (first, second) in graph:
            insert(first, second)
            insert(second, first)

        return index

    def extract_cycle(index, first, second):
        cycle = [first, second]

        while True:
            nexts = index[second]
            next_link = list(set(nexts) - set(cycle))

            if len(next_link) > 0:
                second = next_link[0]
                cycle.append(second)
            else:
                x, y = nexts

                assert x == cycle[0] or y == cycle[0]

                for c in cycle:
                    del index[c]

                return cycle

    index = build_index()
    graph = graph[:]
    genome = []

    while len(graph) > 0:
        a, b = graph[0]
        cycle = extract_cycle(index, a, b)
        genome.append(cycle)
        graph = [(a, b) for (a, b) in graph if a not in cycle]
    return [CycleToChromosome(g) for g in genome]


def TwoBreakOnGenome(graph, i0, i1, j0, j1):
    nodes = ChromosomeToCycle(graph)

    return graph_genome_all(TwoBreakOnGenomeGraph(black_edges(nodes) + colored_edges(nodes), i0, i1, j0, j1))


if __name__ == "__main__":
    _graph = input("Graph: ")
    _graph = parse_permutation(_graph)[0]

    _i0 = int(input("i0: "))
    _i1 = int(input("i1: "))
    _j0 = int(input("j0: "))
    _j1 = int(input("j1: "))

    _result = TwoBreakOnGenome(_graph, _i0, _i1, _j0, _j1)

    for _res in _result:
        print('(' + ' '.join(map(format_permutation, _res)) + ')', end='')
