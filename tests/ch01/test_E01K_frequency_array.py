import pytest
from ch01.E01K_frequency_array import ComputeFrequencies


@pytest.mark.E01K_frequency_array
def test_default():
    assert ComputeFrequencies('ACGCGGCTCTGAAA', 2) == [2, 1, 0, 0, 0, 0, 2, 2, 1, 2, 1, 0, 0, 1, 1, 0]


@pytest.mark.E01K_frequency_array
def test_large():
    f = open('../rosalind/rosalind_ba1k.txt', 'r')
    _genome = f.readline().strip()
    _k = int(f.readline().strip())
    f.readline()

    _result = [int(x) for x in f.readline().strip().split()]
    f.close()

    assert ComputeFrequencies(_genome, _k) == _result
