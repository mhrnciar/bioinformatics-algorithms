//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01D_pattern_matching.h"

tuple<int, list<int> > PatternMatch(const string &genome, const string &pattern, bool complement) {
    auto [count, indices] = PatternCount(genome, pattern);

    int total = count;
    list<int> result;

    for (int i = 0; i < indices.size(); i++) {
        if (indices[i] == '^') {
            result.push_back(i);
        }
    }

    if (complement) {
        string rev_pattern = ReverseComplement(pattern);
        auto [rev_count, rev_indices] = PatternCount(genome, rev_pattern);

        total += rev_count;

        for (int i = 0; i < rev_indices.size(); i++) {
            if (rev_indices[i] == '^') {
                result.push_back(i);
            }
        }
    }

    return {total, result};
}

/*
int main() {
    string _genome, _pattern;

    cout << "Genome: ";
    cin >> _genome;
    cout << "Pattern: ";
    cin >> _pattern;

    auto [_total, _indices] = PatternMatch(_genome, _pattern);

    for (const auto &num : _indices) {
        cout << num << " ";
    }
}
 */
