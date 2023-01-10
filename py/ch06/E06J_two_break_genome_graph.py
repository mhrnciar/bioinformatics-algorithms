import ast

from utils import parse_permutation, format_permutation


def TwoBreakOnGenomeGraph(graph, i0, i1, j0, j1):
    def eq(x, y):
        u, v = x
        w, z = y
        return (u == w and v == z) or (w == v and u == z)

    removed = [x for x in graph if not eq(x, (i0, i1)) and not eq(x, (j0, j1))]

    return sorted(removed + [(i0, j0)] + [(i1, j1)])


if __name__ == "__main__":
    _graph = input("Graph: ")
    _graph = list(ast.literal_eval(_graph))

    _i0 = int(input("i0: "))
    _i1 = int(input("i1: "))
    _j0 = int(input("j0: "))
    _j1 = int(input("j1: "))

    _result = TwoBreakOnGenomeGraph(_graph, _i0, _i1, _j0, _j1)

    print(_result)
