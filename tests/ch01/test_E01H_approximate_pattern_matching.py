import pytest
from ch01.E01H_approximate_pattern_matching import ApproximatePatternMatch


@pytest.mark.E01H_approximate_pattern_matching
def test_default():
    _genome = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
    _pattern = 'ATTCTGGA'
    assert ApproximatePatternMatch(_genome, _pattern, 3)[1] == [6, 7, 26, 27, 78]


@pytest.mark.E01H_approximate_pattern_matching
def test_large():
    f = open('../rosalind/rosalind_ba1h.txt', 'r')
    _pattern = f.readline().strip()
    _genome = f.readline().strip()
    _t = int(f.readline().strip())
    f.readline()

    _result = [int(x) for x in f.readline().strip().split()]
    f.close()

    assert ApproximatePatternMatch(_genome, _pattern, _t)[1] == _result
