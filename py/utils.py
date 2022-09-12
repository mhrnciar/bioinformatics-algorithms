import fileinput
import logomaker
import numpy as np
import pandas as pd

from dictionaries import bases, symbol_key, number_key, amino_acids

import matplotlib.pyplot as plt
plt.ion()


def text(genome: str, i: int, pattern_len: int) -> str:
    return genome[i:i + pattern_len]


def dna_to_rna(dna: str) -> str:
    return dna.replace('T', 'U')


def rna_to_dna(rna: str) -> str:
    return rna.replace('U', 'T')


def generate_combinations(string: str) -> [str]:
    substrings = set()
    substrings.add(string)

    string += string

    for i in range(len(string)):
        for j in range(1, len(string) // 2):
            substrings.add(text(string, i, j))

    return list(substrings)


def generate_patterns(k: int, arr: [str] = None, _prefix: str = "") -> [str]:
    if arr is None:
        arr = list()
    if k == 0:
        arr.append(_prefix)
        return arr

    for base in bases:
        new_prefix = _prefix + base
        generate_patterns(k - 1, arr, new_prefix)

    return arr


def generate_binary_patterns(k: int):
    result = []

    def generate(string, n):
        if n == 0:
            result.append(string)

            if len(result) == 2:
                return result
        else:
            generate((string + '0'), n - 1)
            generate((string + '1'), n - 1)

    generate('', k)
    return result


def read_txt(path: str, skip_num: int = 1) -> str:
    with open(path, 'r') as f:
        seq = ""

        # Skip first lines and read remaining lines to list
        for i in range(skip_num):
            next(f)

        lines = f.readlines()

        # Assemble genome from list with removed newlines
        for line in lines:
            seq += line.replace('\n', '')

        return seq


def read_lines(prompt: str = 'DNA strings separated with newlines, end with ', end_with: str = 'int'):
    result = []
    val = 0

    if end_with == ' ':
        print(prompt + 'space: ')

        while True:
            inp = input('')

            if inp != ' ':
                result.append(inp)
            else:
                break
    elif end_with == 'float':
        print(prompt + 'float: ')

        while True:
            inp = input('')

            try:
                val = float(inp)
                break
            except ValueError:
                result.append(inp)
    else:
        print(prompt + 'int: ')

        while True:
            inp = input('')

            try:
                val = int(inp)
                break
            except ValueError:
                result.append(inp)

    if end_with == ' ':
        return result
    else:
        return result, val


def parse_adj_list(graph: [str]) -> {int: [int]}:
    edges = {}

    for edge in graph:
        node_out, node_in = edge.split(' -> ')
        node_out = int(node_out)
        node_in = [int(x) for x in node_in.split(',')]

        if node_out not in edges:
            edges[node_out] = []

        for node in node_in:
            edges[node_out].append(node)

    return edges


def remove_edge(graph: {int: [int]}, start_node: int, target_node: int) -> {int: [int]}:
    graph[start_node].remove(target_node)

    if not graph[start_node]:
        del graph[start_node]

    return graph


def prefix(pattern: str, back: int = 1) -> str:
    return pattern[0:-back]


def suffix(pattern: str, front: int = 1) -> str:
    return pattern[front:]


def pair_prefix(pair: (str, str), back: int = 1) -> (str, str):
    a, b = pair
    return a[0:-back], b[0:-back]


def pair_suffix(pair: (str, str), front: int = 1) -> (str, str):
    a, b = pair
    return a[front:], b[front:]


def create_pair(string: str, delim: str = '|') -> (str, str):
    a, b = string.split(delim)
    return a, b


def entropy(dist: [float]) -> float:
    total = 0

    for prob in dist:
        if prob == 0:
            total += 0
        else:
            total += prob * np.log2(prob)

    return -total


def score(motifs: [str]) -> int:
    total = 0

    for i in range(len(motifs[0])):
        j = [motif[i] for motif in motifs]
        total += (len(j) - max(j.count('A'), j.count('C'), j.count('T'), j.count('G')))

    return total


def motif_score(dna: [str], score_type: str = 'counts') -> pd.DataFrame:
    genome_len = len(dna[0])
    counts = np.zeros((4, genome_len), dtype=int)

    for genome in dna:
        for i in range(len(genome)):
            symbol = symbol_key.get(genome[i])
            counts[symbol][i] += 1

    df = pd.DataFrame(counts).T
    df.columns = list(symbol_key.keys())

    if score_type == 'counts':
        return df
    elif score_type == 'profile':
        return df / len(dna)


def generate_probs(n: int) -> pd.DataFrame:
    arr = np.zeros((4, n), dtype=float)
    i = 0

    for line in fileinput.input():
        line = line.strip().split(' ')

        for j in range(len(line)):
            arr[i][j] = line[j]

        i += 1
        if i == 4:
            break

    df = pd.DataFrame(arr).T
    df.columns = list(symbol_key.keys())

    return df


def display_logo(dna: [str], save: bool = False, fig_path: str = '', fig_name: str = 'logo'):
    df = motif_score(dna, score_type='profile')

    _ = logomaker.Logo(df, font_name='Arial Rounded MT Bold')

    if save:
        if fig_path[-1] != '/':
            fig_path += '/'
        plt.savefig('{}{}.pdf'.format(fig_path, fig_name))

    plt.show()


def get_weight(peptide):
    return sum(amino_acids[amino_acid].mon_mass for amino_acid in peptide)


def expand(peptides, masses):
    return [peptide + [_mass] for peptide in peptides for _mass in masses]


def mass(peptide):
    return sum([weight for weight in peptide])


def parent_mass(spectrum):
    return max(spectrum)


def is_consistent(_peptide, spectrum):
    def count(_element, spect):
        return len([s for s in spect if s == _element])

    peptide_spectrum = linear_spectrum(_peptide)

    for element in peptide_spectrum:
        if count(element, peptide_spectrum) > count(element, spectrum):
            return False
    return True


def linear_spectrum(_peptide):
    def get_pairs():
        return [(i, j) for i in range(len(_peptide)) for j in range(len(_peptide) + 1) if i < j]

    result = [sum(_peptide[i:j]) for (i, j) in get_pairs()]
    result.append(0)
    result.sort()

    return result


def cyclo_spectrum(_peptide):
    def get_pairs(index_range):
        return [(i, j) for i in index_range for j in range(i, i + len(index_range)) if j != i]

    augmented_peptide = _peptide + _peptide
    result = [sum(augmented_peptide[a:b]) for a, b in get_pairs(range(len(_peptide)))]

    result.append(0)
    result.append(sum(_peptide))
    result.sort()

    return result


def count_matches_in_spectra(spect1, spect2):
    i1 = 0
    i2 = 0
    count = 0

    while i1 < len(spect1) and i2 < len(spect2):
        diff = spect1[i1] - spect2[i2]

        if diff == 0:
            count += 1
            i1 += 1
            i2 += 1

        elif diff < 0:
            i1 += 1

        else:
            i2 += 1

    return count


def topological_ordering(graph):
    graph = set(graph)
    ordering = []
    candidates = list({edge[0] for edge in graph} - {edge[1] for edge in graph})

    while len(candidates) != 0:
        ordering.append(candidates[0])

        temp_nodes = []
        for edge in list(filter(lambda e: e[0] == candidates[0], graph)):
            graph.remove(edge)
            temp_nodes.append(edge[1])

        for node in temp_nodes:
            if node not in {edge[1] for edge in graph}:
                candidates.append(node)

        candidates = candidates[1:]

    return ordering
