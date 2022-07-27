import pytest
from ch01.E01D_pattern_matching import PatternMatch


@pytest.mark.E01A_pattern_count
def test_default():
    assert PatternMatch('GATATATGCATATACTT', 'ATAT')[1] == [1, 3, 9]


@pytest.mark.E01A_pattern_count
def test_large():
    f = open('../rosalind/rosalind_ba1d.txt', 'r')
    _pattern = f.readline().strip()
    _genome = f.readline().strip()
    f.readline()

    _result = [int(x) for x in f.readline().strip().split()]
    f.close()

    assert PatternMatch(_genome, _pattern)[1] == _result
