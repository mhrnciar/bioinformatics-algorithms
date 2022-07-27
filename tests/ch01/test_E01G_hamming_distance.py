import pytest
from ch01.E01G_hamming_distance import HammingDistance


@pytest.mark.E01G_hamming_distance
def test_default():
    assert HammingDistance('GGGCCGTTGGT', 'GGACCGTTGAC') == 3


@pytest.mark.E01G_hamming_distance
def test_large():
    f = open('../rosalind/rosalind_ba1g.txt', 'r')
    _str1 = f.readline().strip()
    _str2 = f.readline().strip()
    f.readline()

    _result = int(f.readline().strip())
    f.close()

    assert HammingDistance(_str1, _str2) == _result
