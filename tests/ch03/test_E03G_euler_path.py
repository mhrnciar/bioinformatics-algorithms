import pytest
from ch03.E03G_euler_path import EulerPath
from utils import parse_adj_list


@pytest.mark.E03G_euler_path
def test_default():
    _graph = parse_adj_list(['0 -> 2', '1 -> 3', '2 -> 1', '3 -> 0,4',
                             '6 -> 3,7', '7 -> 8', '8 -> 9', '9 -> 6'])
    assert '->'.join(map(str, EulerPath(_graph))) == '6->7->8->9->6->3->0->2->1->3->4'


# Many possible paths, the test might fail
@pytest.mark.E03G_euler_path
def test_large():
    f = open('../rosalind/rosalind_ba3g.txt', 'r')
    _graph = parse_adj_list(f.readline().strip().split('|'))
    f.readline()

    _result = f.readline().strip().split()
    f.close()

    assert '->'.join(map(str, EulerPath(_graph))) == _result[0]
