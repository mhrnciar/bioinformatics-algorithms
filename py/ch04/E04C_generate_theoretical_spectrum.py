# Generating Theoretical Spectrum Problem:
# Generate the theoretical spectrum of a cyclic peptide
#   Input: An amino acid string Peptide
#   Output: CYCLOSPECTRUM(Peptide)

from utils import generate_combinations, amino_mass_dict


def GenerateCyclospectrum(peptide, return_type=int):
    cyclospec = [0, sum([amino_mass_dict[protein] for protein in peptide])]

    cyclospec += [sum([amino_mass_dict[protein] for protein in (peptide * 2)[j:j + i]])
                  for i in range(1, len(peptide))
                  for j in range(len(peptide))]

    return list(map(return_type, sorted(cyclospec)))


if __name__ == "__main__":
    _peptide = input("Peptide: ")

    print(' '.join(GenerateCyclospectrum(_peptide, return_type=str)))
