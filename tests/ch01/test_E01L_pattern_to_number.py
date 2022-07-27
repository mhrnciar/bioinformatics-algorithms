import pytest
from ch01.E01L_pattern_to_number import PatternToNumber


@pytest.mark.E01L_pattern_to_number
def test_default():
    assert PatternToNumber('AGT') == 11


@pytest.mark.E01L_pattern_to_number
def test_large():
    f = open('../rosalind/rosalind_ba1l.txt', 'r')
    _pattern = f.readline().strip()
    f.readline()

    _result = int(f.readline().strip())
    f.close()

    assert PatternToNumber(_pattern) == _result
