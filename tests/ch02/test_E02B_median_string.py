import pytest
from ch02.E02B_median_string import MedianString, MedianStringVar


f = open('../rosalind/rosalind_ba2b.txt', 'r')
_k = int(f.readline().strip())

_lines = f.readlines()
_lines = [line.rstrip() for line in _lines]
f.readline()

_result = set(f.readline().strip().split())
f.close()


@pytest.mark.E02B_median_string
def test_default():
    _input = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
    assert {'GAC'}.issubset(MedianString(_input, 3))


@pytest.mark.E02B_median_string
def test_large():
    assert _result.issubset(MedianString(_lines, _k))


@pytest.mark.E02B_median_string
def test_var():
    assert _result.issubset(MedianStringVar(_lines, _k))
