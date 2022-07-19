# Clump Finding Problem:
# Find patterns forming clumps in a string
#   Input: A string Genome, and integers k, L, and t
#   Output: All distinct k-mers forming (L, t)-clumps in Genome


# Complexity:
# - Inner cycle: (i + l - k) - i = l - k
# k is small number which can be ignored in generalisation
# - Outer cycle: n - l + 1
# O(n - l + 1) * O(l - k) ~ O(n * l)
def FindClumps(string, k, window_len, threshold):
    res = set()

    for i in range(len(string) - window_len + 1):
        for j in range(i, i + window_len - k):
            if string[i:i + window_len].count(string[j:j + k]) == threshold:
                res.add(string[j:j + k])

    return res


if __name__ == "__main__":
    gene = input("Gene: ").upper()
    size = int(input("k: "))
    L = int(input("L: "))
    t = int(input("t: "))

    for word in FindClumps(gene, size, L, t):
        print(word)
