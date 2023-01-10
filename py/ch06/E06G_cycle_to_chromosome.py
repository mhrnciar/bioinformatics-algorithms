from utils import parse_permutation, format_permutation


def CycleToChromosome(nodes):
    chromosome = []

    it = iter(nodes)
    for i in it:
        first, second = i, next(it)
        if first < second:
            chromosome.append(second//2)
        else:
            chromosome.append(-first//2)

    return chromosome


if __name__ == "__main__":
    _nodes = input("Chromosome: ")
    _nodes = parse_permutation(_nodes)

    _result = CycleToChromosome(_nodes[0])

    print('(' + ' '.join(map(format_permutation, _result)) + ')')
