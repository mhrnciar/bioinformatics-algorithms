import pytest
from ch03.E03B_string_reconstruction import ReconstructString


@pytest.mark.E03B_string_reconstruction
def test_default():
    assert ReconstructString(['ACCGA', 'CCGAA', 'CGAAG', 'GAAGC', 'AAGCT']) == 'ACCGAAGCT'


@pytest.mark.E03B_string_reconstruction
def test_large():
    f = open('../rosalind/rosalind_ba3b.txt', 'r')
    _genome = f.readline().strip().split()
    f.readline()

    _result = f.readline().strip()

    assert ReconstructString(_genome) == _result
