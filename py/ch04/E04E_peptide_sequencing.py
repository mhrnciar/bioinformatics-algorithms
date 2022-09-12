# Cyclopeptide Sequencing Problem:
# Find a cyclic peptide having maximum score against an experimental spectrum
#   Input: A collection of integers Spectrum
#   Output: A cyclic peptide Peptide maximizing SCORE(Peptide, Spectrum) over all peptides
#   Peptide with mass equal to PARENTMASS(Spectrum)

from utils import cyclo_spectrum, mass, parent_mass, expand, is_consistent
from dictionaries import amino_mass_dict


def CyclopeptideSequencing(spectrum):
    peptides = [[]]
    output = []
    masses = list(set(amino_mass_dict.values()))

    while len(peptides) > 0:
        next_peptides = []

        for peptide in expand(peptides, masses):
            if mass(peptide) == parent_mass(spectrum):
                if cyclo_spectrum(peptide) == spectrum:
                    output.append(peptide)

            else:
                if is_consistent(peptide, spectrum):
                    next_peptides.append(peptide)

        peptides = next_peptides

    return output


if __name__ == '__main__':
    _spectrum = [int(x) for x in input('Spectrum: ').split()]

    _result = CyclopeptideSequencing(_spectrum)

    for _item in sorted(_result, reverse=True):
        print('-'.join(map(str, _item)), end=' ')
