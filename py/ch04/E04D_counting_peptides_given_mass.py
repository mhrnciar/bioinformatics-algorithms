# Counting Peptides with Given Mass Problem:
# Compute the number of peptides of given mass
#   Input: An integer m
#   Output: The number of linear peptides having integer mass m

from dictionaries import amino_mass_dict


def CountPeptides(total_mass):
    cache = []
    total = 0

    masses = list(set(amino_mass_dict.values()))

    for target_mass in range(total_mass + 1):
        total = 0

        for amino_acid_mass in masses:
            residual_mass = target_mass - amino_acid_mass

            if residual_mass == 0:
                total += 1
            elif residual_mass > 0:
                total += cache[residual_mass]

        cache.append(total)

    return total


if __name__ == "__main__":
    _mass = int(input("Total mass: "))

    print(CountPeptides(_mass))
