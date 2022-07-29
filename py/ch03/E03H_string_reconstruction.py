from utils import read_lines, parse_adj_list, suffix
from ch03.E03E_de_brujin_collection import DeBrujinCollection
from ch03.E03G_euler_path import EulerPath


def ReconstructString(patterns, k):
    graph = DeBrujinCollection(patterns)
    path = EulerPath(graph)

    result = path[0]

    for i in range(1, len(path)):
        result += suffix(path[i], k-2)

    return result


if __name__ == "__main__":
    _k = int(input("k: "))
    _patterns = read_lines(end_with=' ')

    print(ReconstructString(_patterns, _k))
