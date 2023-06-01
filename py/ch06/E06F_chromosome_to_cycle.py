from utils import parse_permutation
from E06D_two_break_sorting import chromosome_to_cycle


if __name__ == "__main__":
    _chromosome = input("Chromosome: ")
    _chromosome = parse_permutation(_chromosome)

    _result = chromosome_to_cycle(_chromosome[0])

    print('(' + ' '.join(map(str, _result)) + ')')
