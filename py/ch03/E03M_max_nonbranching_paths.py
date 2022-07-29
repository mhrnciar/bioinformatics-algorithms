from utils import read_lines, parse_adj_list


def add_counts(graph):
    counts = {}

    for node, outs in graph.items():
        counts[node] = (0, len(outs))

    for node, outs in graph.items():
        for out in outs:
            if out not in counts:
                counts[out] = (0, 0)
            x, y = counts[out]
            counts[out] = x + 1, y

    return counts


def standardize(cycle):
    mm = min(cycle)
    ii = cycle.index(mm)
    return cycle[ii:] + cycle[:ii] + [mm]


def make_cycle(start, graph):
    cycle = [start]
    node = start

    while node in graph and len(graph[node]) == 1:
        succ = graph[node][0]

        if succ == start:
            return standardize(cycle)
        else:
            cycle.append(succ)
            node = succ

    return []


def isolated_cycles(graph):
    cycles = []

    for node in graph.keys():
        cycle = make_cycle(node, graph)

        if len(cycle) > 0 and cycle not in cycles:
            cycles.append(cycle)

    return cycles


def MaxNonbranchingPaths(graph):
    paths = []
    nodes = add_counts(graph)

    for v in nodes:
        (ins, outs) = nodes[v]
        if ins != 1 or outs != 1:
            if outs > 0:
                for w in graph[v]:
                    nbp = [v, w]
                    w_in, w_out = nodes[w]
                    while w_in == 1 and w_out == 1:
                        u = graph[w][0]
                        nbp.append(u)
                        w = u
                        w_in, w_out = nodes[w]
                    paths.append(nbp)

    return isolated_cycles(graph) + paths


if __name__ == "__main__":
    _patterns = read_lines(end_with=' ')
    _graph = parse_adj_list(_patterns)

    _paths = MaxNonbranchingPaths(_graph)

    for _path in sorted(_paths):
        print(' -> '.join(map(str, _path)))
