import pytest
from ch03.E03D_de_brujin_string import DeBrujinString


@pytest.mark.E03D_de_brujin_string
def test_default():
    assert DeBrujinString('AAGATTCTCTAC', 4) == {'AAG': ['AGA'], 'AGA': ['GAT'], 'ATT': ['TTC'], 'CTA': ['TAC'],
                                                 'CTC': ['TCT'], 'GAT': ['ATT'], 'TCT': ['CTC', 'CTA'], 'TTC': ['TCT']}


@pytest.mark.E03D_de_brujin_string
def test_large():
    f = open('../rosalind/rosalind_ba3d.txt', 'r')
    _k = int(f.readline().strip())
    _genome = f.readline().strip()
    f.readline()

    _temp = f.readline().strip().split('|')
    f.close()

    _result = dict()

    for item in _temp:
        mapping = item.split(' -> ')
        _result[mapping[0]] = mapping[1].split(', ')

    assert DeBrujinString(_genome, _k) == _result
