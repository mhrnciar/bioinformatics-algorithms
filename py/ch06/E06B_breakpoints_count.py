# Number of Breakpoints Problem:
# Find the number of breakpoints in a permutation.
#   Input: A permutation
#   Output: The number of breakpoints in this permutation

from utils import parse_permutation


def BreakpointCount(p):
    cnt = 0 if p[0] == 1 else 1
    prev = p[0]

    for i in range(1, len(p)):
        if p[i] < 0:
            if p[i] == prev + 1:
                prev = p[i]
                continue
            else:
                prev = p[i]
                cnt += 1
        elif p[i] > 0:
            if p[i] == prev + 1:
                prev = p[i]
                continue
            else:
                prev = p[i]
                cnt += 1

    return cnt


if __name__ == "__main__":
    _p = input("Permutation: ")
    _p = parse_permutation(_p)

    _result = BreakpointCount(_p)

    print(_result)
