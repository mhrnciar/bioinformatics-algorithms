import pytest
from ch02.E02C_profile_most_probable_kmer import MostProbableKmer


@pytest.mark.E02C_profile_most_probable_kmer
def test_default():
    _arr = [[0.2, 0.2, 0.3, 0.2, 0.3],
            [0.4, 0.3, 0.1, 0.5, 0.1],
            [0.3, 0.3, 0.5, 0.2, 0.4],
            [0.1, 0.2, 0.1, 0.1, 0.2]]

    assert MostProbableKmer('ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT', 5, _arr) == 'CCGAG'


@pytest.mark.E02C_profile_most_probable_kmer
def test_large():
    f = open('../rosalind/rosalind_ba2c.txt', 'r')
    _genome = f.readline().strip()
    _k = int(f.readline().strip())
    f.readline()

    _result = f.readline().strip()

    _lines = f.readlines()
    _arr = [[float(x) for x in line.rstrip().split()] for line in _lines]
    f.close()

    assert MostProbableKmer(_genome, _k, _arr) == _result
