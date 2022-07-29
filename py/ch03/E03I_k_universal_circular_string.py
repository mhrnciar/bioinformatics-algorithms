# k-Universal Circular String Problem:
# Find a k-universal circular string
#   Input: An integer k
#   Output: A k-universal circular string

from utils import generate_binary_patterns, suffix
from ch03.E03E_de_brujin_collection import DeBrujinCollection
from ch03.E03F_euler_cycle import EulerCycle


def kUniversalCircularString(k):
    patterns = generate_binary_patterns(k)
    graph = DeBrujinCollection(patterns)
    path = EulerCycle(graph)

    result = path[0]

    for i in range(1, len(path) - k + 1):
        result += suffix(path[i], k - 2)

    return result


if __name__ == "__main__":
    _k = int(input("k: "))

    print(kUniversalCircularString(_k))

