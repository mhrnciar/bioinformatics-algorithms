//
// Created by Matej Hrnčiar on 21/07/2022.
//

#include "E01H_approximate_pattern_matching.h"

tuple<int, list<int> > ApproximatePatternMatch(const string &genome, const string &pattern,
                                               int threshold, bool complement) {
    auto [count, indices] = ApproximatePatternCount(genome, pattern, threshold);

    int total = count;
    list<int> result;

    for (int i = 0; i < indices.size(); i++) {
        if (indices[i] == '^') {
            result.push_back(i);
        }
    }

    if (complement) {
        string rev_pattern = ReverseComplement(pattern);
        auto [rev_count, rev_indices] = ApproximatePatternCount(genome, rev_pattern, threshold);

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
    int _threshold;

    cout << "Genome: ";
    cin >> _genome;
    cout << "Pattern: ";
    cin >> _pattern;
    cout << "t: ";
    cin >> _threshold;

    auto [_total, _indices] = ApproximatePatternMatch(_genome, _pattern, _threshold);

    for (auto num : _indices) {
        cout << num << " ";
    }
}
 */
