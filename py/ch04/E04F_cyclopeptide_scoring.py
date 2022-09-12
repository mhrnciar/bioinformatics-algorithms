# Cyclopeptide Scoring Problem:
# Compute the score of a cyclic peptide against a spectrum
#   Input: An amino acid string Peptide and a collection of integers Spectrum
#   Output: The score of Peptide against Spectrum, SCORE(Peptide, Spectrum)

from utils import count_matches_in_spectra, cyclo_spectrum
from dictionaries import amino_mass_dict


def CyclopeptideScore(peptide, spectrum, spect_from_peptide=cyclo_spectrum):
    if len(peptide) > 0 and isinstance(peptide[0], str):
        peptide = [amino_mass_dict.get(x) for x in peptide]
    return count_matches_in_spectra(spect_from_peptide(peptide), spectrum)


if __name__ == '__main__':
    _peptide = input("Peptide: ")
    _spectrum = [int(x) for x in input('Spectrum: ').split()]

    print(CyclopeptideScore(_peptide, _spectrum))

