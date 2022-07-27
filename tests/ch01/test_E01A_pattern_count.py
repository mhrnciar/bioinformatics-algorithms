import pytest
from ch01.E01A_pattern_count import PatternCount


@pytest.mark.E01A_pattern_count
def test_default():
    assert PatternCount('GCGCG', 'GCG')[0] == 2


@pytest.mark.E01A_pattern_count
def test_large():
    f = open('../rosalind/rosalind_ba1a.txt', 'r')
    _genome = f.readline().strip()
    _pattern = f.readline().strip()
    f.readline()

    _result = int(f.readline().strip())
    f.close()

    assert PatternCount(_genome, _pattern)[0] == _result
