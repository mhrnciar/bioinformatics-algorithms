import pytest
from ch01.E01C_reverse_complement import ReverseComplement


@pytest.mark.E01C_reverse_complement
def test_default():
    assert ReverseComplement('AAAACCCGGT')[1] == 'ACCGGGTTTT'


@pytest.mark.E01C_reverse_complement
def test_large():
    f = open('../rosalind/rosalind_ba1c.txt', 'r')
    _pattern = f.readline().strip()
    f.readline()

    _result = f.readline().strip()
    f.close()

    assert ReverseComplement(_pattern)[1] == _result
