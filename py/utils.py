import fileinput

import logomaker
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
plt.ion()

bases = ['A', 'C', 'G', 'T']

complement_key = {
    'C': 'G',
    'G': 'C',
    'A': 'T',
    'T': 'A'
}

symbol_key = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

number_key = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
}


amino_acid_dict = {
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
    'ACA': 'U', 'ACC': 'U', 'ACG': 'U', 'ACU': 'U',
    'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
    'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
    'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W',
}


def text(genome: str, i: int, pattern_len: int) -> str:
    return genome[i:i+pattern_len]


def generate_patterns(k: int, arr: [str] = None, prefix: str = "") -> [str]:
    if arr is None:
        arr = list()
    if k == 0:
        arr.append(prefix)
        return arr

    for base in bases:
        new_prefix = prefix + base
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
            total += prob*np.log2(prob)

    return -total


def score(motifs: [str]) -> int:
    total = 0

    for i in range(len(motifs[0])):
        j = [motif[i] for motif in motifs]
        total += (len(j) - max(j.count("A"), j.count("C"), j.count("T"), j.count("G")))

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

    logo = logomaker.Logo(df, font_name='Arial Rounded MT Bold')

    if save:
        if fig_path[-1] != '/':
            fig_path += '/'
        plt.savefig('{}{}.pdf'.format(fig_path, fig_name))

    plt.show()


if __name__ == "__main__":
    # read_txt("/Users/mhrnciar/Downloads/GCF_000006745.1_ASM674v1_genomic_Vibrio_cholerae.fna")
    # print(entropy([0.0, 0.6, 0.0, 0.4]))

    _genome = input("Genome: ")
    _n = int(input("n: "))

    print(profile_probability(_genome, _n))
