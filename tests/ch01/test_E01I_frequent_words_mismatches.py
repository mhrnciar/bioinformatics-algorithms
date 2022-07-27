import pytest
from ch01.E01I_frequent_words_mismatches import MismatchFrequentWords, MismatchFrequentWordsBySorting


f = open('../rosalind/rosalind_ba1i.txt', 'r')
_genome = f.readline().strip()
_k, _t = [int(x) for x in f.readline().strip().split()]
f.readline()

_result = set(f.readline().strip().split())
f.close()


@pytest.mark.E01I_frequent_words_mismatches
def test_default():
    assert MismatchFrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1) == {'GATG', 'ATGC', 'ATGT'}


@pytest.mark.E01I_frequent_words_mismatches
def test_large():
    assert MismatchFrequentWords(_genome, _k, _t) == _result


@pytest.mark.E01I_frequent_words_mismatches
def test_sorting():
    assert MismatchFrequentWordsBySorting(_genome, _k, _t) == _result
