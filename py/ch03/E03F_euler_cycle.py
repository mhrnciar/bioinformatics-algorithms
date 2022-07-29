from random import choice
import networkx as nx

from utils import read_lines, parse_adj_list, remove_edge


def EulerCycle(graph):
    start_node, edges = choice(list(graph.items()))
    target_node = choice(edges)

    graph = remove_edge(graph, start_node, target_node)

    cycle = [start_node, target_node]
    current_node = target_node

    while current_node != start_node:
        edges = graph[current_node]
        target_node = choice(edges)

        graph = remove_edge(graph, current_node, target_node)

        current_node = target_node
        cycle.append(current_node)

    while graph:
        potential_starts = [(idx, node) for idx, node in enumerate(cycle) if node in graph]
        idx, new_start = choice(potential_starts)

        new_cycle = cycle[idx:] + cycle[1:idx + 1]
        edges = graph[new_start]
        target_node = choice(edges)

        graph = remove_edge(graph, new_start, target_node)

        current_node = target_node
        new_cycle.append(current_node)

        while current_node != new_start:
            edges = graph[current_node]
            target_node = choice(edges)

            graph = remove_edge(graph, current_node, target_node)

            current_node = target_node
            new_cycle.append(current_node)

        cycle = new_cycle

    return cycle


def EulerCycleVar(graph):
    edges = [line.strip().split(' -> ') for line in graph]

    G = nx.DiGraph()
    for edge in edges:
        for node in edge[1].split(','):
            G.add_edge(edge[0], node)

    path = [str(e[0]) for e in nx.eulerian_circuit(G)]
    path.append(path[0])

    return path


if __name__ == "__main__":
    _graph = read_lines('Adjacency list, end with ', end_with=' ')
    _graph = parse_adj_list(_graph)

    _path = EulerCycle(_graph)

    print('->'.join(map(str, _path)))
