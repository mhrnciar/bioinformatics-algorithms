import pytest
from ch03.E03E_de_brujin_collection import DeBrujinCollection


@pytest.mark.E03E_de_brujin_collection
def test_default():
    _genome = ['GAGG', 'CAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']
    assert DeBrujinCollection(_genome) == {'AGG': {'GGG'}, 'CAG': {'AGG', 'AGG'}, 'GAG': {'AGG'},
                                           'GGA': {'GAG'}, 'GGG': {'GGG', 'GGA'}}


@pytest.mark.E03E_de_brujin_collection
def test_large():
    f = open('../rosalind/rosalind_ba3e.txt', 'r')
    _genome = f.readline().strip().split()
    f.readline()

    _temp = f.readline().strip().split('|')
    f.close()

    _result = dict()

    for item in _temp:
        mapping = item.split(' -> ')
        _result[mapping[0]] = set(mapping[1].split(', '))

    assert DeBrujinCollection(_genome) == _result
