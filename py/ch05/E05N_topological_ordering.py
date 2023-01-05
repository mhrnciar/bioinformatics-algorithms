# Topological ordering problem

from utils import read_lines, parse_adj_list


def TopologicalOrdering(graph):
    def number_incoming(node):
        n = 0
        for out in graph.values():
            if node in out:
                n += 1
        return n

    ordering = []
    candidates = [node for node in graph.keys() if number_incoming(node) == 0]
    while len(candidates) > 0:
        a = candidates.pop()
        ordering.append(a)

        if a in graph:
            bs = [b for b in graph[a]]
            del graph[a]

            for b in bs:
                if number_incoming(b) == 0:
                    candidates.append(b)

    if len(graph) > 0:
        return None

    return ordering


if __name__ == "__main__":
    _graph = read_lines('Adjacency list, end with ', end_with=' ')
    _graph = parse_adj_list(_graph)

    _result = TopologicalOrdering(_graph)

    print(_result)

