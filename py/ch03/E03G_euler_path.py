import networkx as nx

from utils import read_lines, parse_adj_list
from ch03.E03F_euler_cycle import EulerCycle


def EulerPath(graph):
    deg_diff = {}
    for node, edges in graph.items():
        if node in deg_diff:
            deg_diff[node] += len(edges)
        else:
            deg_diff[node] = len(edges)

        for edge in edges:
            if edge in deg_diff:
                deg_diff[edge] -= 1
            else:
                deg_diff[edge] = -1

    starting_node = ending_node = 0

    for node, diff in deg_diff.items():
        if diff == -1:
            ending_node = node

    for node, diff in deg_diff.items():
        if diff == 1:
            starting_node = node

    if ending_node in graph:
        graph[ending_node].append(starting_node)
    else:
        graph[ending_node] = [starting_node]

    euler_cycle = EulerCycle(graph)

    idx = 0
    while True:
        if euler_cycle[idx] == ending_node and euler_cycle[idx + 1] == starting_node:
            break
        idx += 1

    euler_path = euler_cycle[idx + 1:] + euler_cycle[1:idx + 1]

    return euler_path


def EulerPathVar(graph):
    edges = [line.strip().split(' -> ') for line in graph]

    G = nx.DiGraph()
    for edge in edges:
        for node in edge[1].split(','):
            G.add_edge(edge[0], node)

    path = [str(e[0]) for e in nx.eulerian_path(G)]

    return path


if __name__ == "__main__":
    _graph = read_lines('Adjacency list, end with ', end_with=' ')
    _graph = parse_adj_list(_graph)

    _path = EulerPath(_graph)

    print('->'.join(map(str, _path)))
