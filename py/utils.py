bases = ['A', 'T', 'C', 'G']

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


def Text(text, i, pattern_len):
    return text[i:i+pattern_len]


def read_txt(path, skip_num=1):
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


if __name__ == "__main__":
    read_txt("/Users/mhrnciar/Downloads/GCF_000006745.1_ASM674v1_genomic_Vibrio_cholerae.fna")
