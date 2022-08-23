import pytest
from ch03.E03C_overlap_graph import OverlapGraph


@pytest.mark.E03C_overlap_graph
def test_default():
    _result = {'AGGCA -> GGCAT', 'CATGC -> ATGCG', 'GCATG -> CATGC', 'GGCAT -> GCATG'}
    assert set(map(str, OverlapGraph(['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT']))) == _result


@pytest.mark.E03C_overlap_graph
def test_large():
    f = open('../rosalind/rosalind_ba3c.txt', 'r')
    _patterns = f.readline().strip().split()
    f.readline()

    _result = f.readline().strip().split('|')
    f.close()

    assert set(map(str, OverlapGraph(_patterns))) == set(_result)
