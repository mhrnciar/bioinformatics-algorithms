from utils import linear_spectrum
from dictionaries import amino_mass_dict


def LinearSpectrumFromString(peptide):
    return linear_spectrum([amino_mass_dict.get(x) for x in peptide])


if __name__ == '__main__':
    _peptide = input('Peptide: ')

    print(' '.join(map(str, LinearSpectrumFromString(_peptide))))
