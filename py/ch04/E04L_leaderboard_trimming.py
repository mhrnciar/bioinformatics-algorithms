from ch04.E04F_cyclopeptide_scoring import CyclopeptideScore
from utils import linear_spectrum


def Trim(leaderboard, spectrum, n, spectrum_generator=linear_spectrum):
    if len(leaderboard) < n:
        return leaderboard

    peptides_with_scores = [(CyclopeptideScore(peptide, spectrum, spectrum_generator), peptide)
                            for peptide in leaderboard]
    peptides_with_scores.sort(reverse=True)

    (cutoff, _) = peptides_with_scores[n-1]
    return [peptide for (score, peptide) in peptides_with_scores if score >= cutoff]


if __name__ == '__main__':
    _leaderboard = input("Leaderboard: ").split()
    _spectrum = [int(x) for x in input('Spectrum: ').split()]
    _n = int(input("n: "))

    print(' '.join(Trim(_leaderboard, _spectrum, _n)))
