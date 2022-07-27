import pytest
from ch01.E01N_d_neighborhood import ImmediateNeighbors, Neighbors


@pytest.mark.E01N_d_neighborhood
def test_default_immediate():
    assert ImmediateNeighbors('ACG') == {'CCG', 'TCG', 'GCG', 'AAG', 'ATG', 'AGG', 'ACA', 'ACC', 'ACT', 'ACG'}


@pytest.mark.E01N_d_neighborhood
def test_default():
    assert Neighbors('ACG', 1) == {'CCG', 'TCG', 'GCG', 'AAG', 'ATG', 'AGG', 'ACA', 'ACC', 'ACT', 'ACG'}


@pytest.mark.E01N_d_neighborhood
def test_large():
    f = open('../rosalind/rosalind_ba1n.txt', 'r')
    _pattern = f.readline().strip()
    _k = int(f.readline().strip())
    f.readline()

    _result = set(f.readline().strip().split())
    f.close()

    assert Neighbors(_pattern, _k) == _result
