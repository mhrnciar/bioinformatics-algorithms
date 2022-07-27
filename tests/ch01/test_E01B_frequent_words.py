import pytest
from ch01.E01B_frequent_words import FrequentWords, FastFrequentWords, FastFrequentWordsBySorting


f = open('../rosalind/rosalind_ba1b.txt', 'r')
_genome = f.readline().strip()
_k = int(f.readline().strip())
f.readline()

_result = set(f.readline().strip().split())
f.close()


@pytest.mark.E01B_frequent_words
def test_default():
    assert FrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4) == {'CATG', 'GCAT'}


@pytest.mark.E01B_frequent_words
def test_large():
    assert FrequentWords(_genome, _k) == _result


@pytest.mark.E01B_frequent_words
def test_fast():
    assert FastFrequentWords(_genome, _k) == _result


@pytest.mark.E01B_frequent_words
def test_sorting():
    assert FastFrequentWordsBySorting(_genome, _k) == _result
