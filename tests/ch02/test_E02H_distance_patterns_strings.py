import pytest
from ch02.E02H_distance_patterns_strings import DistanceBetweenPatternsStrings


@pytest.mark.E02H_distance_patterns_strings
def test_default():
    _dna = ['TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']

    assert DistanceBetweenPatternsStrings(_dna, 'AAA') == 5


@pytest.mark.E02H_distance_patterns_strings
def test_large():
    f = open('../rosalind/rosalind_ba2h.txt', 'r')
    _pattern = f.readline().strip()
    _genome = f.readline().strip().split()
    f.readline()

    _result = int(f.readline().strip())
    f.close()

    assert DistanceBetweenPatternsStrings(_genome, _pattern) == _result
