import pytest
from ch01.E01J_frequent_words_mismatches_reverse_complements import MismatchFrequentWordsWithRevComps


@pytest.mark.E01J_frequent_words_mismatches_reverse_complements
def test_default():
    assert MismatchFrequentWordsWithRevComps('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1) == {'ATGT', 'ACAT'}


@pytest.mark.E01J_frequent_words_mismatches_reverse_complements
def test_large():
    f = open('../rosalind/rosalind_ba1j.txt', 'r')
    _genome = f.readline().strip()
    _k, _t = [int(x) for x in f.readline().strip().split()]
    f.readline()

    _result = set(f.readline().strip().split())
    f.close()

    assert MismatchFrequentWordsWithRevComps(_genome, _k, _t) == _result
