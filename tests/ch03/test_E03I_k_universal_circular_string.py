import pytest
from ch03.E03I_k_universal_circular_string import kUniversalCircularString


# Many possible results, the test might fail
@pytest.mark.E03I_k_universal_circular_string
def test_default():
    assert kUniversalCircularString(4) in ['0000110010111101', '1110100110000101', '1011110010000110',
                                           '0111100101000011', '0001011110011010', '1110101100001001',
                                           '1011110000100110', '1110110000101001', '0111101001011000',
                                           '0001011001111010', '0010000110101111', '1111001010000110']


# Many possible results, the test might fail
@pytest.mark.E03I_k_universal_circular_string
def test_large():
    f = open('../rosalind/rosalind_ba3i.txt', 'r')
    _k = int(f.readline().strip())
    f.readline()

    _result = f.readline().strip()
    f.close()

    assert kUniversalCircularString(_k) == _result
