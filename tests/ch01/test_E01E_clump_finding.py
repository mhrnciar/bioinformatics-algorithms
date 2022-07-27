import pytest
from ch01.E01E_clump_finding import FindClumps, FastFindClumps, FindClumpsWithFrequencies


f = open('../rosalind/rosalind_ba1e.txt', 'r')
_genome = f.readline().strip()
_k, _L, _t = [int(x) for x in f.readline().strip().split()]
f.readline()

_result = set(f.readline().strip().split())
f.close()


@pytest.mark.E01E_clump_finding
def test_default():
    _tgenome = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
    assert FindClumps(_tgenome, 5, 75, 4) == {'CGACA', 'GAAGA', 'AATGT'}


@pytest.mark.E01E_clump_finding
def test_large():
    assert FindClumps(_genome, _k, _L, _t) == _result


@pytest.mark.E01E_clump_finding
def test_fast():
    assert FastFindClumps(_genome, _k, _L, _t) == _result


# @pytest.mark.E01E_clump_finding
# def test_frequencies():
#     assert FindClumpsWithFrequencies(_genome, _k, _L, _t) == _result
