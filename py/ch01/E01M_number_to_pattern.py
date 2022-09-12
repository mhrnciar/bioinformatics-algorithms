from dictionaries import number_key


def NumberToPattern(num, k):
    if k == 1:
        return number_key.get(num, 'A')

    prefix_index = num // 4
    r = num % 4
    symbol = number_key.get(r, 'A')

    prefix_pattern = NumberToPattern(prefix_index, k - 1)

    return prefix_pattern + symbol


if __name__ == "__main__":
    _num = int(input("Number: "))
    _k = int(input("k: "))

    print(NumberToPattern(_num, _k))
