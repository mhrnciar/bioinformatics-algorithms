# Spectral Convolution Problem:
# Generate the convolution of a spectrum
#   Input: A collection of integers Spectrum
#   Output: The list of elements in the convolution of Spectrum in decreasing order of their multiplicities


def SpectralConvolution(spectrum):
    def create_counts(_diffs):
        counts = {}

        for diff in _diffs:
            if diff not in counts:
                counts[diff] = 0

            counts[diff] += 1

        return counts

    diffs = [abs(spectrum[i] - spectrum[j])
             for i in range(len(spectrum))
             for j in range(i + 1, len(spectrum)) if spectrum[i] != spectrum[j]]

    return sorted([(diff, count) for diff, count in create_counts(diffs).items()], key=lambda x: (-x[1], x[0]))


if __name__ == '__main__':
    _spectrum = [int(x) for x in input('Spectrum: ').split()]

    _result = SpectralConvolution(_spectrum)

    for _item in _result:
        print(' '.join([str(_item[0])] * _item[1]), end=' ')
