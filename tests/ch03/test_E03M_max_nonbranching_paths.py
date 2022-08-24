import pytest
from ch03.E03M_max_nonbranching_paths import MaxNonbranchingPaths
from utils import parse_adj_list


# More possible results, the test might fail
@pytest.mark.E03M_max_nonbranching_paths
def test_default():
    _graph = parse_adj_list(['1 -> 2', '2 -> 3', '3 -> 4,5', '6 -> 7', '7 -> 6'])
    _res = MaxNonbranchingPaths(_graph)

    _list = []

    for _path in _res:
        _list.append(' -> '.join(map(str, _path)))

    assert sorted(_list) == ['1 -> 2 -> 3', '3 -> 4', '3 -> 5', '7 -> 6 -> 7']


# More possible results, the test might fail
@pytest.mark.E03M_max_nonbranching_paths
def test_large():
    f = open('../rosalind/rosalind_ba3m.txt', 'r')
    _graph = parse_adj_list(f.readline().strip().split('|'))
    f.readline()

    _result = f.readline().strip().split('|')
    f.close()

    _res = MaxNonbranchingPaths(_graph)

    _list = []

    for _path in _res:
        _list.append(' -> '.join(map(str, _path)))

    assert sorted(_list) == _result
