import pytest
from ch03.E03H_string_reconstruction import ReconstructString


@pytest.mark.E03H_string_reconstruction
def test_default():
    assert ReconstructString(['CTTA', 'ACCA', 'TACC', 'GGCT', 'GCTT', 'TTAC'], 4) == 'GGCTTACCA'


@pytest.mark.E03H_string_reconstruction
def test_large():
    f = open('../rosalind/rosalind_ba3h.txt', 'r')
    _k = int(f.readline().strip())
    _patterns = f.readline().strip().split()
    f.readline()

    _result = f.readline().strip()
    f.close()

    assert ReconstructString(_patterns, _k) == _result
