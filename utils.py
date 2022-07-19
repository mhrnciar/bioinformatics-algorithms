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
