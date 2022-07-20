from utils import symbol_key


def PatternToNumber(pattern):
    if pattern == "":
        return 0

    symbol = pattern[-1]
    prefix = pattern[:-1]

    return 4 * PatternToNumber(prefix) + symbol_key.get(symbol, 0)


if __name__ == "__main__":
    _pattern = input("Pattern: ").upper()

    print(PatternToNumber(_pattern))
