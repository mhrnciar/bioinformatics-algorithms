import pytest
from ch03.E03L_gapped_genome_path import GappedGenomePath


@pytest.mark.E03L_gapped_genome_path
def test_default():
    assert GappedGenomePath(['GACC|GCGC', 'ACCG|CGCC', 'CCGA|GCCG', 'CGAG|CCGG', 'GAGC|CGGA'], 4, 2) == 'GACCGAGCGCCGGA'


@pytest.mark.E03L_gapped_genome_path
def test_large():
    f = open('../rosalind/rosalind_ba3l.txt', 'r')
    _k, _t = [int(x) for x in f.readline().strip().split()]
    _patterns = f.readline().strip().split()
    f.readline()

    _result = f.readline().strip()
    f.close()

    assert GappedGenomePath(_patterns, _k, _t) == _result
