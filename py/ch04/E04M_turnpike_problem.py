import math
import numpy as np


def Turnpike(D, check=False):
    def find_remaining_points(X, D, first, last):
        def get_set_diffs(diffs):
            diffs.sort()
            set_diffs = []
            i = 0

            for diff in diffs:
                found = False

                while i < len(D):
                    if D[i] < diff:
                        set_diffs.append(D[i])
                    elif D[i] == diff:
                        found = True
                        i += 1
                        break

                    i += 1

                if not found:
                    return None

            while i < len(D):
                set_diffs.append(D[i])
                i += 1

            return set_diffs

        def explore(candidate, X, first, last):
            diffs = [abs(candidate-x) for x in X if not np.isnan(x) and x != candidate]
            set_diffs = get_set_diffs(diffs)

            if set_diffs == None:
                return None
            elif len(set_diffs) == 0:
                return X
            else:
                return find_remaining_points(X, set_diffs, first, last)

        x_max = D[-1]
        XX = X[:]
        XX[last-1] = x_max
        trial_solution = explore(x_max, XX, first, last-1)

        if trial_solution == None:
            XX = X[:]
            XX[first+1] = X[-1] - x_max
            return explore(X[-1]-x_max, XX, first+1, last)
        else:
            return trial_solution

    def check_diffs(reconstruction):
        diffs = [a-b for a in reconstruction for b in reconstruction]
        diffs.sort()
        if len(diffs) != len(D):
            print('Length of reconstructed diffs ({0}) does not match length of D ({1}) '.format(len(diffs), len(D)))
        mismatches = 0
        for a, b in zip(D, diffs):
            if a != b:
                mismatches += 1
                print(a, b)

        if mismatches > 0:
            print('Found {0} mismatches'.format(mismatches))
        return diffs

    len_D = len(D)
    len_X = int(np.sqrt(len_D))
    X = [float('nan')] * len_X
    X[0] = 0
    X[-1] = D[-1]
    reconstruction = find_remaining_points(X, [d for d in D[:-1] if d > 0], 0, -1)
    if check:
        check_diffs(reconstruction)
    return reconstruction


if __name__ == '__main__':
    with open('../../tests/rosalind/rosalind_ba4m.txt') as f:
        strings = [int(n) for n in f.read().split()]
        for i in Turnpike(strings, check=True):
            print(i, end=' ')
