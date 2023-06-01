import numpy as np


def two_break_on_genome(_genome, i1, i2, j1, j2):
    g = colored_edges(_genome)
    g = two_break_on_genome_graph(g, i1, i2, j1, j2)
    _genome = graph_to_genome(g)

    return _genome


def two_break_on_genome_graph(_g, i1, i2, j1, j2):
    rem = ((i1, i2), (i2, i1), (j1, j2), (j2, j1))
    bg = [t for t in _g if t not in rem]
    bg.append((i1, j1))
    bg.append((i2, j2))

    return bg


def two_break_distance(_P, _Q):
    blue = colored_edges(_P)
    red = colored_edges(_Q)
    size = len(blue) + len(red)
    _l = colored_edges_cycles(blue, red)
    return size // 2 - len(_l)


def permutation_list_to_str(_p):
    ps = []
    for i in _p:
        if i > 0:
            ps.append('+' + str(i))
        elif i == 0:
            ps.append('0')
        elif i < 0:
            ps.append(str(i))
    return '(' + ' '.join(ps) + ')'


def permutation_str_to_list(str_p):
    _p = list(map(int, str_p.strip()[1:-1].split(' ')))
    return _p


def format_sequence(_s):
    fs = []

    for i in _s:
        str_p = permutation_list_to_str(i)
        fs.append(str_p)

    return fs


def chromosome_to_cycle(_p):
    nodes = []

    for i in _p:
        if i > 0:
            nodes.append(2 * i - 1)
            nodes.append(2 * i)
        else:
            nodes.append(-2 * i)
            nodes.append(-2 * i - 1)

    return nodes


def cycle_to_chromosome(nodes):
    _p = []
    for j in range(0, len(nodes) // 2):
        if nodes[2 * j] < nodes[2 * j + 1]:
            s = j + 1
        else:
            s = -(j + 1)
        _p.append(s)
    return p


def genome_str_to_list(genome):
    lp = []
    for _p in genome.split('(')[1:]:
        _p = permutation_str_to_list('(' + _p)
        lp.append(_p)
    return lp


def colored_edges(genome):
    g = []
    for _p in genome:
        s = chromosome_to_cycle(_p)

        for j in range(len(s) // 2):
            head = 1 + 2 * j
            tail = (2 + 2 * j) % len(s)
            e = (s[head], s[tail])
            g.append(e)

    return g


def graph_to_genome(_g):
    genome = []
    visited = []
    adj = np.zeros(len(_g) * 2, dtype=int)
    for t in _g:
        adj[t[0] - 1] = t[1] - 1
        adj[t[1] - 1] = t[0] - 1

    for t in _g:
        orig = t[0]
        if orig in visited:
            continue

        visited.append(orig)

        if orig % 2 == 0:
            closing = orig - 1
        else:
            closing = orig + 1
        _p = []
        i = 0

        while True:
            if orig % 2 == 0:
                _p.append(orig // 2)
            else:
                _p.append(-(orig + 1) // 2)

            dest = adj[orig - 1] + 1
            i = i + 1

            if i > 100:
                return

            visited.append(dest)

            if dest == closing:
                genome.append(_p)
                break

            if dest % 2 == 0:
                orig = dest - 1
            else:
                orig = dest + 1

            assert orig > 0

            visited.append(orig)

    return genome


def colored_edges_cycles(blue, red):
    cycles = []
    size = len(blue) + len(red)
    adj = np.zeros(shape=(size, 2), dtype=int)
    visiteded = np.zeros(shape=size, dtype=bool)

    for e in blue:
        adj[e[0] - 1, 0] = e[1] - 1
        adj[e[1] - 1, 0] = e[0] - 1
    for e in red:
        adj[e[0] - 1, 1] = e[1] - 1
        adj[e[1] - 1, 1] = e[0] - 1

    for node in range(size):
        if not visiteded[node]:
            visiteded[node] = True
            head = node
            cycle = [head + 1]
            color = 0

            while True:
                node = adj[node, color]

                if node == head:
                    cycles.append(cycle)
                    break

                cycle.append(node + 1)
                visiteded[node] = True
                color = (color + 1) % 2

    return cycles


def TwoBreakSorting(_P, _Q):
    red = colored_edges(_Q)
    _path = [_P]

    while two_break_distance(_P, _Q) > 0:
        cycles = colored_edges_cycles(colored_edges(_P), red)
        for i in cycles:
            if len(i) >= 4:
                _P = two_break_on_genome(_P, i[0], i[1], i[3], i[2])
                _path.append(_P)
                break

    return _path


if __name__ == '__main__':
    with open('../../tests/rosalind/rosalind_ba6d.txt') as f:
        P = [list(map(int, f.readline().strip()[1:-1].split(' ')))]
        Q = [list(map(int, f.readline().strip()[1:-1].split(' ')))]

    path = TwoBreakSorting(P, Q)

    for p in path:
        print(''.join(format_sequence(p)))
