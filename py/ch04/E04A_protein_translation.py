# Protein Translation Problem:
# Translate an RNA string into an amino acid string
#   Input: An RNA string Pattern and the array GENETICCODE
#   Output: The translation of Pattern into an amino acid string Peptide

from utils import codon_dict, text, dna_to_rna


def TranslateProtein(pattern, translate=False):
    result = ""

    if translate:
        pattern = dna_to_rna(pattern)

    for i in range(0, len(pattern), 3):
        protein = codon_dict.get(text(pattern, i, 3))

        if protein != '_' and protein is not None:
            result += protein

    return result


if __name__ == "__main__":
    _pattern = input("Pattern: ")

    print(TranslateProtein(_pattern))
