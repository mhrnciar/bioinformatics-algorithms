from ch04.E04G_leaderboard_cyclopeptide_sequencing import LeaderboardCyclopeptideSequencing
from ch04.E04H_spectral_convolution import SpectralConvolution
from utils import cyclo_spectrum


def ConvolutionCyclopeptideSequencing(m, n, spectrum, low_mass=57, high_mass=200):
    def get_masses_from_spectrum(_spectrum):
        masses = []
        last_count = 0

        for mass, count in SpectralConvolution(_spectrum):
            if low_mass <= mass <= high_mass:
                if len(masses) < m:
                    masses.append(mass)
                    last_count = count
                else:
                    if count == last_count:
                        masses.append(mass)
                    else:
                        return masses

        return masses

    return LeaderboardCyclopeptideSequencing(spectrum, n, spect1=get_masses_from_spectrum, spect2=cyclo_spectrum)


if __name__ == '__main__':
    _m = int(input("M: "))
    _n = int(input("N: "))
    _spectrum = [int(x) for x in input('Spectrum: ').split()]

    _leader = ConvolutionCyclopeptideSequencing(_m, _n, _spectrum)[::-1]

    print('-'.join(map(str, _leader)))
