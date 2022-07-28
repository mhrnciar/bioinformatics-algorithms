from utils import text, read_lines


def EulerCycle(graph):
    edges = {}

    for edge in graph:
        node_out, node_in = edge.split(' -> ')
        node_out = int(node_out)
        node_in = [int(x) for x in node_in.split(',')]

        if node_out not in edges:
            edges[node_out] = []

        for node in node_in:
            edges[node_out].append(node)

    current_node = list(edges.keys())[0]
    path = [current_node]

    # Get the initial cycle.
    while True:
        path.append(edges[current_node][0])

        if len(edges[current_node]) == 1:
            del edges[current_node]
        else:
            edges[current_node] = edges[current_node][1:]

        if path[-1] in edges:
            current_node = path[-1]
        else:
            break

    while len(edges) > 0:
        for i in range(len(path)):
            if path[i] in edges:
                current_node = path[i]
                cycle = [current_node]

                while True:
                    cycle.append(edges[current_node][0])

                    if len(edges[current_node]) == 1:
                        del edges[current_node]
                    else:
                        edges[current_node] = edges[current_node][1:]

                    if cycle[-1] in edges:
                        current_node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i + 1:]
                break

    return path


if __name__ == "__main__":
    _graph = read_lines('Adjacency list, end with', end_with=' ')

    _path = EulerCycle(_graph)

    print('->'.join(map(str, _path)))
