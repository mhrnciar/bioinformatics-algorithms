# String Reconstruction from Read-Pairs Problem:
# Reconstruct a string from its paired composition
#   Input: A collection of paired k-mers PairedReads and an integer d
#   Output: A string Text with (k, d)-mer composition equal to PairedReads (if such a string exists)

from utils import read_lines, create_pair, pair_prefix, pair_suffix
from ch03.E03E_de_brujin_collection import DeBrujinCollection
from ch03.E03G_euler_path import EulerPath


def extract_func(pairs, i):
    (a, _) = pairs[i]
    return a


def reconstruct_as_list(k, n, fragments, extract=lambda fragments, i: fragments[i]):
    result = []

    for i in range(0, n, k):
        result.append(extract(fragments, i))

    target_len = n + k - 1
    actual_len = len(result) * k
    overlap = target_len - actual_len

    if overlap > 0:
        result.append(fragments[-1][k - overlap:k])

    return result


def ReconstructStringPairs(patterns, k, d):
    pairs = [create_pair(string) for string in patterns]
    graph = DeBrujinCollection(pairs, head=pair_prefix, tail=pair_suffix)
    path = EulerPath(graph)

    head_reconstruction = ''.join(reconstruct_as_list(k - 1, len(path), path, extract_func)[:-1])
    expected_length = len(patterns) + 2 * k + d - 1
    deficit = expected_length - len(head_reconstruction)

    _, tail_reconstruction = path[-1]
    i = -2

    while len(tail_reconstruction) < deficit:
        _, tail = path[i]
        tail_reconstruction = tail[0] + tail_reconstruction
        i -= 1

    return head_reconstruction + tail_reconstruction


if __name__ == "__main__":
    _k = int(input("k: "))
    _d = int(input("d: "))
    _patterns = read_lines(end_with=' ')

    print(ReconstructStringPairs(_patterns, _k, _d))
