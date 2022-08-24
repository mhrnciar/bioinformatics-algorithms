import pytest
from ch03.E03J_read_pairs_string_reconstruction import ReconstructStringPairs


@pytest.mark.E03J_read_pairs_string_reconstruction
def test_default():
    _patterns = ['GAGA|TTGA', 'TCGT|GATG', 'CGTG|ATGT', 'TGGT|TGAG', 'GTGA|TGTT',
                 'GTGG|GTGA', 'TGAG|GTTG', 'GGTC|GAGA', 'GTCG|AGAT']
    assert ReconstructStringPairs(_patterns, 4, 2) == 'GTGGTCGTGAGATGTTGA'


@pytest.mark.E03J_read_pairs_string_reconstruction
def test_large():
    f = open('../rosalind/rosalind_ba3j.txt', 'r')
    _k, _t = [int(x) for x in f.readline().strip().split()]
    _patterns = f.readline().strip().split()
    f.readline()

    _result = f.readline().strip()
    f.close()

    assert ReconstructStringPairs(_patterns, _k, _t) == _result
