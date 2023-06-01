import numpy as np
from E06D_two_break_sorting import two_break_on_genome, format_sequence


if __name__ == '__main__':
    with open('../../tests/rosalind/rosalind_ba6k.txt') as f:
        genome = [list(map(int, f.readline().strip()[1:-1].split(' ')))]
        [i, j, k, l] = list(map(int, f.readline().strip().split(', ')))
    genome = two_break_on_genome(genome, i, j, k, l)
    print(''.join(format_sequence(genome)))
