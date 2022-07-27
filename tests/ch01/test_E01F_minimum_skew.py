import pytest
from ch01.E01F_minimum_skew import MinSkew


@pytest.mark.E01F_minimum_skew
def test_default():
    _genome = 'CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG'
    assert MinSkew(_genome, show_plot=False)[1] == [53, 97]


@pytest.mark.E01F_minimum_skew
def test_large():
    f = open('../rosalind/rosalind_ba1f.txt', 'r')
    _genome = f.readline().strip()
    f.readline()

    _result = [int(x) for x in f.readline().strip().split()]
    f.close()

    assert MinSkew(_genome, show_plot=False)[1] == _result
