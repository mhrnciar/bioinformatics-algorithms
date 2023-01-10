from utils import parse_permutation


def ChromosomeToCycle(chromosome):
    nodes = []

    for i in chromosome:
        if i > 0:
            nodes.append(2 * i - 1)
            nodes.append(2 * i)
        else:
            nodes.append(-2 * i)
            nodes.append(-2 * i - 1)

    return nodes


if __name__ == "__main__":
    _chromosome = input("Chromosome: ")
    _chromosome = parse_permutation(_chromosome)

    _result = ChromosomeToCycle(_chromosome[0])

    print('(' + ' '.join(map(str, _result)) + ')')
