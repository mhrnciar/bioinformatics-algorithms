# Peptide Encoding Problem:
# Find substrings of a genome encoding a given amino acid sequence
#   Input: A DNA string Text and an amino acid string Peptide
#   Output: All substrings of Text encoding Peptide (if any such substrings exist)

from ch01.E01C_reverse_complement import ReverseComplement
from ch04.E04A_protein_translation import TranslateProtein
from utils import text, dna_to_rna, rna_to_dna


def encodes(rna, peptide):
    try:
        return TranslateProtein(rna) == peptide
    except KeyError:
        return False


def FindEncodingPeptides(pattern, peptide):
    pattern = dna_to_rna(pattern)
    candidates = [text(pattern, i, 3 * len(peptide)) for i in range(len(pattern) - 3)]

    return [rna_to_dna(rna) for rna in candidates if encodes(rna, peptide) or encodes(ReverseComplement(rna, rna=True)[1], peptide)]


if __name__ == "__main__":
    _pattern = input("Pattern: ")
    _peptide = input("Peptide: ")

    for word in FindEncodingPeptides(_pattern, _peptide):
        print(word)
