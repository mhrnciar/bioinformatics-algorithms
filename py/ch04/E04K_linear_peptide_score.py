from ch04.E04J_linear_spectrum_string import LinearSpectrumFromString
from utils import count_matches_in_spectra


def LinearPeptideScore(peptide, spectrum):
    return count_matches_in_spectra(LinearSpectrumFromString(peptide), spectrum)


if __name__ == '__main__':
    _peptide = input('Peptide: ')
    _spectrum = [int(x) for x in input('Spectrum: ').split()]

    print(LinearPeptideScore(_peptide, _spectrum))
