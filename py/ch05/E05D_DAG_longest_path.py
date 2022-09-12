# Longest Path in a DAG Problem:
# Find the longest path between two nodes in an edge-weighted DAG
#   Input: An integer representing the source node of a graph, followed by an integer representing the sink node of the
#   graph, followed by an edge-weighted graph. The graph is represented by a modified adjacency list in which the
#   notation "0->1:7" indicates that an edge connects node 0 to node 1 with weight 7
#   Output: The length of the longest path in the graph, followed by the longest path. (If multiple longest paths exist,
#   you may return any one)

from utils import topological_ordering, read_lines


def DAGLongestPath(graph, source, sink):
    top_order = topological_ordering(graph.keys())
    top_order = top_order[top_order.index(source)+1:top_order.index(sink)+1]

    S = {node: -100 for node in {edge[0] for edge in graph.keys()} | {edge[1] for edge in graph.keys()}}
    S[source] = 0
    backtrack = {node: None for node in top_order}

    for node in top_order:
        try:
            S[node], backtrack[node] = max(map(lambda e: [S[e[0]] + graph[e], e[0]],
                                               filter(lambda e: e[1] == node, graph.keys())), key=lambda p: p[0])
        except ValueError:
            pass

    path = [sink]

    while path[0] != source:
        path = [backtrack[path[0]]] + path

    return S[sink], path


if __name__ == "__main__":
    _source = int(input("Source: "))
    _sink = int(input("Sink: "))
    _input = read_lines(prompt='Adjacency list, end with ', end_with=' ')

    _edges, _graph = {}, {}
    for _pair in [_line.strip().split('->') for _line in _input]:
        if int(_pair[0]) not in _edges:
            _edges[int(_pair[0])] = [int(_pair[1].split(':')[0])]
        else:
            _edges[int(_pair[0])].append(int(_pair[1].split(':')[0]))

        _graph[int(_pair[0]), int(_pair[1].split(':')[0])] = int(_pair[1].split(':')[1])

    _result = DAGLongestPath(_graph, _source, _sink)

    print(_result[0])
    print('->'.join(map(str, _result[1])))

