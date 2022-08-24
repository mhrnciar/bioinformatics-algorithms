import pytest
from ch03.E03K_generate_contigs import GenerateContigs


@pytest.mark.E03K_generate_contigs
def test_default():
    _patterns = ['ATG', 'ATG', 'TGT', 'TGG', 'CAT', 'GGA', 'GAT', 'AGA']
    assert sorted(GenerateContigs(_patterns)) == ['AGA', 'ATG', 'ATG', 'CAT', 'GAT', 'TGGA', 'TGT']


@pytest.mark.E03K_generate_contigs
def test_large():
    f = open('../rosalind/rosalind_ba3k.txt', 'r')
    _patterns = f.readline().strip().split()
    f.readline()

    _result = f.readline().strip().split()
    f.close()

    assert sorted(GenerateContigs(_patterns)) == _result
