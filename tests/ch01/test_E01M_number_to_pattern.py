import pytest
from ch01.E01M_number_to_pattern import NumberToPattern


@pytest.mark.E01M_number_to_pattern
def test_default():
    assert NumberToPattern(45, 4) == 'AGTC'


@pytest.mark.E01M_number_to_pattern
def test_large():
    f = open('../rosalind/rosalind_ba1m.txt', 'r')
    _num = int(f.readline().strip())
    _k = int(f.readline().strip())
    f.readline()

    _result = f.readline().strip()
    f.close()

    assert NumberToPattern(_num, _k) == _result
