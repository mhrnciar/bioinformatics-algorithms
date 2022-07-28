import pytest
from ch02.E02A_motif_enumeration import MotifEnumeration


@pytest.mark.E02A_motif_enumeration
def test_default():
    assert MotifEnumeration(['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT'], 3, 1) == {'ATA', 'ATT', 'GTT', 'TTT'}


@pytest.mark.E02A_motif_enumeration
def test_large():
    f = open('../rosalind/rosalind_ba2a.txt', 'r')
    _k, _d = [int(x) for x in f.readline().strip().split()]

    _lines = f.readlines()
    _lines = [line.rstrip() for line in _lines]
    f.readline()

    _result = set(f.readline().strip().split())
    f.close()

    assert MotifEnumeration(_lines, _k, _d) == _result
