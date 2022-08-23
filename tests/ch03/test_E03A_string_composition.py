import pytest
from ch03.E03A_string_composition import StringComposition


@pytest.mark.E03A_string_composition
def test_default():
    assert StringComposition('CAATCCAAC', 5) == ['AATCC', 'ATCCA', 'CAATC', 'CCAAC', 'TCCAA']


@pytest.mark.E03A_string_composition
def test_large():
    f = open('../rosalind/rosalind_ba3a.txt', 'r')
    _k = int(f.readline().strip())
    _genome = f.readline().strip()
    f.readline()

    _result = f.readline().strip().split()
    f.close()

    assert StringComposition(_genome, _k) == _result
