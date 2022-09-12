bases = ['A', 'C', 'G', 'T']

complement_key = {
    'C': 'G',
    'G': 'C',
    'A': 'T',
    'T': 'A'
}

rna_complement_key = {
    'C': 'G',
    'G': 'C',
    'A': 'U',
    'U': 'A'
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


skew_step = {
    'A': 0,
    'C': -1,
    'G': +1,
    'T': 0
}


codon_dict = {
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
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


amino_mass_dict = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
    'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
    'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
}


class AminoAcid:
    def __init__(self, name, short, abbrev, mon_mass, average_mass):
        self.name = name
        self.short = short
        self.abbrev = abbrev
        self.mon_mass = mon_mass
        self.average_mass = average_mass

    def __str__(self):
        return '%(name)s %(short)s %(abbrev)s %(int_mass)d %(mon_mass)f %(average_mass)f' % \
               {
                   'name': self.name,
                   'short': self.short,
                   'abbrev': self.abbrev,
                   'mon_mass': self.mon_mass,
                   'average_mass': self.average_mass,
                   'int_mass': self.asInteger()
               }

    def asInteger(self):
        return int(self.mon_mass)


amino_acids = {
    'A': AminoAcid('Alanine', 'A', 'Ala', 71.03711, 71.0788),
    'C': AminoAcid('Cysteine', 'C', 'Cys', 103.00919, 103.1388),
    'D': AminoAcid('Aspartic acid', 'D', 'Asp', 115.02694, 115.0886),
    'E': AminoAcid('Glutamic acid', 'E', 'Glu', 129.04259, 129.1155),
    'F': AminoAcid('Phenylalanine', 'F', 'Phe', 147.06841, 147.1766),
    'G': AminoAcid('Glycine', 'G', 'Gly', 57.02146, 57.0519),
    'H': AminoAcid('Histidine', 'H', 'His', 137.05891, 137.1411),
    'I': AminoAcid('Isoleucine', 'I', 'Ile', 113.08406, 113.1594),
    'K': AminoAcid('Lysine', 'K', 'Lys', 128.09496, 128.1741),
    'L': AminoAcid('Leucine', 'L', 'Leu', 113.08406, 113.1594),
    'M': AminoAcid('Methionine', 'M', 'Met', 131.04049, 131.1986),
    'N': AminoAcid('Asparagine', 'N', 'Asn', 114.04293, 114.1039),
    'O': AminoAcid('Pyrrolysine', 'O', 'Pyl', 255.15829, 255.3172),
    'P': AminoAcid('Proline', 'P', 'Pro', 97.05276, 97.1167),
    'Q': AminoAcid('Glutamine', 'Q', 'Gln', 128.05858, 128.1307),
    'R': AminoAcid('Arginine', 'R', 'Arg', 156.10111, 156.1875),
    'S': AminoAcid('Serine', 'S', 'Ser', 87.03203, 87.0782),
    'T': AminoAcid('Threonine', 'T', 'Thr', 101.04768, 101.1051),
    'U': AminoAcid('Selenocysteine', 'U', 'Sec', 150.95364, 150.0388),
    'V': AminoAcid('Valine', 'V', 'Val', 99.06841, 99.1326),
    'W': AminoAcid('Tryptophan', 'W', 'Trp', 186.07931, 186.2132),
    'Y': AminoAcid('Tyrosine', 'Y', 'Tyr', 163.06333, 163.1760)
}


class BLOSUM62:
    def __init__(self):
        import os

        with open(os.path.join(os.path.dirname(__file__), '../data/BLOSUM62.txt')) as input_data:
            items = [line.strip().split() for line in input_data.readlines()]
            self.scoring_matrix = {(item[0], item[1]): int(item[2]) for item in items}

    def __getitem__(self, pair):
        return self.scoring_matrix[pair[0], pair[1]]