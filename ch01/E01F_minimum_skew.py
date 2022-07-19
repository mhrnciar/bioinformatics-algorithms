# Minimum Skew Problem:
# Find a position in a genome where the skew diagram attains a minimum
#   Input: A DNA string Genome
#   Output: All integer(s) i minimizing SKEWi(Genome) among all values of i (from 0 to |Genome|)

import plotly.graph_objects as go
from utils import read_txt


# Complexity: O(n)
def MinSkew(genome, show_plot=False):
    graph = [0] * len(genome)
    skew_value, min_skew, min_ind = 0, 1, []

    for index, base in enumerate(genome):
        if base == 'C':
            skew_value -= 1
        elif base == 'G':
            skew_value += 1

        graph[index] = skew_value

        # Check if it matches the current minimum, or is a new minimum.
        if skew_value == min_skew:
            min_ind.append(index + 1)
        elif skew_value < min_skew:
            min_skew = skew_value
            min_ind = [index + 1]

    if show_plot:
        fig = go.Figure(data=go.Scatter(y=graph))
        fig.show()

    return min_skew, min_ind


if __name__ == "__main__":
    _genome = input("Genome: ").upper()
    # gene = read_txt("../data/GCF_000813165.1_ASM81316v1_genomic_Escherichia_coli.fna", 1)

    print(MinSkew(_genome, show_plot=True))
