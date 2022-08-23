import pytest
from ch03.E03F_euler_cycle import EulerCycle, EulerCycleVar
from utils import parse_adj_list


@pytest.mark.E03F_euler_cycle
def test_default():
    _graph = parse_adj_list(['0 -> 3', '1 -> 0', '2 -> 1,6', '3 -> 2', '4 -> 2',
                             '5 -> 4', '6 -> 5,8', '7 -> 9', '8 -> 7', '9 -> 6'])
    assert '->'.join(map(str, EulerCycle(_graph))) == '6->8->7->9->6->5->4->2->1->0->3->2->6'


@pytest.mark.E03F_euler_cycle
def test_large():
    f = open('../rosalind/rosalind_ba3f.txt', 'r')
    _graph = parse_adj_list(f.readline().strip().split('|'))
    f.readline()

    _result = f.readline().strip().split()
    f.close()

    assert '->'.join(map(str, EulerCycle(_graph))) == _result
