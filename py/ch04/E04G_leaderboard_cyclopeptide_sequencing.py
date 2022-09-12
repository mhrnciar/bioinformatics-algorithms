from ch04.E04F_cyclopeptide_scoring import CyclopeptideScore
from ch04.E04L_leaderboard_trimming import Trim
from utils import parent_mass, expand, mass, linear_spectrum
from dictionaries import amino_mass_dict


def LeaderboardCyclopeptideSequencing(spectrum, n, spect1=linear_spectrum, spect2=linear_spectrum):
    masses = list(set(amino_mass_dict.values()))
    leader_peptide = []
    leaderboard = [[]]

    while len(leaderboard) > 0:
        new_board = []

        for peptide in expand(leaderboard, masses):
            if mass(peptide) == parent_mass(spectrum):
                if CyclopeptideScore(peptide, spectrum, spect2) > CyclopeptideScore(leader_peptide, spectrum, spect2):
                    leader_peptide = peptide
                new_board.append(peptide)

            elif mass(peptide) > parent_mass(spectrum):
                pass  # peptide will be dropped from leader board
            else:
                new_board.append(peptide)

        leaderboard = Trim(new_board, spectrum, n, spect1)

    return leader_peptide


if __name__ == '__main__':
    _n = int(input("n: "))
    _spectrum = [int(x) for x in input('Spectrum: ').split()]

    _leader = LeaderboardCyclopeptideSequencing(_spectrum, _n)[::-1]

    print('-'.join(map(str, _leader)))
